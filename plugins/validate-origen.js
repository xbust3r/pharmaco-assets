/**
 * Validador «playgrow origen».
 *
 * El clon local del que se migró el marcado era estático: no traía ni uno de
 * los comportamientos del tema. La fuente de la verdad de lo que este sitio
 * tiene que *hacer* es el sitio vivo, catalogado en
 * `docs/migracion/origen-comportamientos.json`.
 *
 * Este comando no visita el sitio: un build no debe depender de que un servidor
 * de terceros esté en pie, y el catálogo ya está escrito. Lo que hace es cruzar
 * ese catálogo contra `src/` y responder dos preguntas distintas:
 *
 *   1. ¿Qué falta?  — informe de cobertura, no falla.
 *   2. ¿Lo que dice estar hecho, sigue estándolo? — eso sí falla.
 *
 * Lo segundo es lo que justifica que sea un validador y no un documento: un
 * `hook` que alguien renombra en el Pug, o un módulo que se cae de `main.js`,
 * dejan el comportamiento muerto sin que ninguna otra comprobación se entere.
 *
 *     node plugins/validate-origen.js            informe completo
 *     node plugins/validate-origen.js --pendientes   sólo lo que falta
 */

import { readFileSync, existsSync } from 'node:fs';
import { resolve } from 'node:path';
import { glob } from 'glob';
import pc from 'picocolors';

const raiz = process.cwd();
const soloPendientes = process.argv.includes('--pendientes');

const manifiesto = JSON.parse(
    readFileSync(resolve(raiz, 'docs/migracion/origen-comportamientos.json'), 'utf8'),
);

// Marcado, scripts y estilos, leídos una vez.
const marcado = (await glob('src/**/*.pug', { cwd: raiz, absolute: true }))
    .map((f) => readFileSync(f, 'utf8'))
    .join('\n');

const entrada = existsSync(resolve(raiz, 'src/scripts/main.js'))
    ? readFileSync(resolve(raiz, 'src/scripts/main.js'), 'utf8')
    : '';

const scripts = (await glob('src/scripts/**/*.js', { cwd: raiz, absolute: true }))
    .map((f) => readFileSync(f, 'utf8'))
    .join('\n');

const estilos = (await glob('src/styles/**/*.css', { cwd: raiz, absolute: true }))
    .map((f) => readFileSync(f, 'utf8'))
    .join('\n');

const IMPLEMENTADOS = new Set(['hecho', 'mejorado']);

const revisar = (c) => {
    const { hook, archivo } = c.destino || {};
    const fallos = [];

    // Un comportamiento sin hook ni archivo es maquetado o CSS: no hay nada
    // mecánico que comprobar, y decir lo contrario sería ruido.
    if (!hook && !archivo) return { fallos, comprobable: false };

    if (hook) {
        if (!marcado.includes(hook)) {
            fallos.push(`el hook \`${hook}\` no aparece en ningún .pug`);
        } else if (IMPLEMENTADOS.has(c.estado) && !scripts.includes(hook) && !estilos.includes(hook)) {
            fallos.push(`el hook \`${hook}\` no tiene consumidor ni en src/scripts/ ni en src/styles/`);
        }
    }

    if (archivo) {
        if (!existsSync(resolve(raiz, archivo))) {
            fallos.push(`falta el módulo \`${archivo}\``);
        } else {
            // Importado desde main.js, con o sin extensión.
            const nombre = archivo.split('/').pop().replace(/\.js$/, '');
            if (!new RegExp(`['"\\./]${nombre}(\\.js)?['"]`).test(entrada)) {
                fallos.push(`\`${archivo}\` existe pero no se importa desde main.js`);
            }
        }
    }

    return { fallos, comprobable: true };
};

const grupos = new Map();
const regresiones = [];

for (const c of manifiesto.comportamientos) {
    if (!grupos.has(c.grupo)) grupos.set(c.grupo, []);

    const { fallos, comprobable } = revisar(c);
    const roto = IMPLEMENTADOS.has(c.estado) && comprobable && fallos.length > 0;

    if (roto) regresiones.push({ c, fallos });

    grupos.get(c.grupo).push({ c, fallos, comprobable, roto });
}

// ── informe ────────────────────────────────────────────────────────────────
const SIMBOLO = {
    hecho: pc.green('✔'),
    mejorado: pc.green('★'),
    pendiente: pc.yellow('○'),
    'requiere-backend': pc.blue('◑'),
    'otra-fase': pc.blue('◑'),
    descartado: pc.dim('–'),
};

console.log(pc.cyan(pc.bold('Validador · playgrow origen')));
console.log(pc.dim(manifiesto.origen + '  ·  catálogo revisado ' + manifiesto.revisado));
console.log(pc.gray('------------------------------------------------'));

for (const [grupo, filas] of grupos) {
    const visibles = soloPendientes ? filas.filter((f) => f.c.estado === 'pendiente') : filas;

    if (!visibles.length) continue;

    console.log('\n' + pc.bold(grupo.toUpperCase()));

    for (const { c, fallos, roto } of visibles) {
        const marca = roto ? pc.red('✘') : SIMBOLO[c.estado] || '?';
        console.log(`  ${marca} ${c.nombre} ${pc.dim('· ' + c.id)}`);

        if (roto) {
            for (const f of fallos) console.log(`      ${pc.red('regresión:')} ${f}`);
        } else if (c.estado === 'pendiente' && c.destino?.hook) {
            console.log(`      ${pc.dim('esperado: ' + c.destino.hook)}`);
        }

        if (c.nota && (c.estado === 'pendiente' || roto)) {
            console.log(`      ${pc.dim(c.nota)}`);
        }
    }
}

// ── resumen ────────────────────────────────────────────────────────────────
const cuenta = (e) => manifiesto.comportamientos.filter((c) => c.estado === e).length;
const total = manifiesto.comportamientos.length;
const listos = cuenta('hecho') + cuenta('mejorado');

console.log('\n' + pc.gray('------------------------------------------------'));
const fuera = cuenta('otra-fase') + cuenta('requiere-backend') + cuenta('descartado');

console.log(
    `${pc.green(listos + ' listos')}  ·  ${pc.yellow(cuenta('pendiente') + ' pendientes')}  ·  `
    + `${pc.blue(cuenta('otra-fase') + cuenta('requiere-backend') + ' en otra fase')}  ·  `
    + `${pc.dim(cuenta('descartado') + ' descartados')}  ·  ${total} en total`,
);

// El porcentaje se mide contra lo que este proyecto sí quiere hacer: contar
// contra el total castigaría por decisiones deliberadas —no queremos sliders—
// y daría una cifra que no significa nada.
const enAlcance = total - fuera;
const porcentaje = Math.round((listos / enAlcance) * 100);
console.log(pc.dim(`Cobertura dentro del alcance actual: ${porcentaje}% (${listos}/${enAlcance})`));

if (regresiones.length) {
    console.log('\n' + pc.red(pc.bold(`${regresiones.length} regresión(es): algo declarado como hecho ya no lo está.`)));
    console.log(pc.dim('Corregirlo, o actualizar su `estado` en el manifiesto si el cambio fue intencionado.'));
    process.exit(1);
}

console.log(pc.green('\nNada declarado como hecho está roto.'));
