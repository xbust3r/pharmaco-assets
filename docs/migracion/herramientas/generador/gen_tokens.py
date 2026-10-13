import re
ORIGIN = '/Users/miguel/servers/pharmaco-assets/.claude/worktrees/task-006-migracion/assets/css/main.css'
OUT = '/Users/miguel/servers/pharmaco-assets/.claude/worktrees/task-006-migracion/src/styles/styles.css'
css = open(ORIGIN, encoding='utf8').read()

# Colores: valor exacto tal como aparece en main.css. Nombre por el papel que tiene en el CSS origen.
COLORS = [
    ('white', '#fff'), ('black', '#000'), ('ink', '#111029'),
    ('purple', '#5956e9'), ('purple-hover', '#433fe6'), ('purple-soft', 'rgba(89,86,233,0.2)'),
    ('purple-original', '#7c56e9'),
    ('deep-purple', '#3a30a0'), ('deep-purple-hover', '#392f9c'),
    ('dark-purple', '#4d30a0'), ('dark-purple-hover', '#442a8c'),
    ('blue', '#4c40f7'), ('blue-hover', '#473bf7'), ('blue-strong', '#2d29e3'),
    ('medium-blue', '#2565b8'), ('orange', '#fa832b'), ('strong-blue', '#0030ff'), ('dark-blue', '#00113b'),
    ('sky-blue', '#b8defa'), ('sky-blue-hover', '#b3dcfa'),
    ('yellow', '#ffd027'), ('red', '#be0000'), ('rust', '#b93d0c'), ('highlight', '#ff0'),
    ('gray-dark', '#2f2f2f'), ('gray-body', '#6b6b6b'), ('gray-text', '#6e7177'),
    ('gray-subtitle', '#787878'), ('gray-soft', '#999fae'), ('gray-muted', '#a7a7a7'),
    ('gray-icon', '#9da4ac'), ('gray-border', '#cfcfcf'), ('gray-button', '#d6dade'),
    ('gray-input', '#f4f4f4'), ('gray-tag-bg', '#eaeaeb'), ('gray-tag-text', '#929292'),
    ('gray-modal', '#afb7bc'), ('gray-666', '#666'), ('gray-555', '#555'),
    ('section-gray', '#f0f5f8'), ('section-contact', '#edf0f3'),
    ('overlay', 'rgba(0,0,0,0.4)'), ('modal-control', 'rgba(0,0,0,0.7)'), ('transparent', 'rgba(0,0,0,0)'),
    ('paleturquoise', '#afe7e9'), ('paleturquoise-text', '#73dcde'),
    ('turquoise-service', '#7ad5f2'), ('service-ads', '#6490ff'), ('service-software', '#8082c0'),
    ('service-pink', '#ff99fb'), ('service-photos', '#b896ff'), ('service-marketing', '#888'),
    ('service-branding', '#7d7afa'), ('service-photo', '#b27afa'), ('service-mktdg', '#bb85e5'),
    ('teaser-yellow', '#ffeddc'), ('teaser-purple', '#bddeff'), ('teaser-blue', '#bdf8ff'),
    ('teaser-pink', '#f3d1ff'), ('teaser-violet', '#d9c7ff'), ('teaser-red', '#ffe2e2'),
]

# Tamaños de fuente y radios: todos los valores px que hay en main.css.
sizes = sorted({int(x) for x in re.findall(r'font-size:(\d+)px', css)})
radii = sorted({int(x) for x in re.findall(r'border-radius:(\d+)px', css)})

# Sombras: valor exacto, nombre por el selector donde se usa (ver inventario, sección 5.5).
SHADOWS = [
    ('soft', '4px 5px 13px rgba(0,0,0,0.08)', '.c-button:focus/hover, .c-project-teaser, .c-contact-options__option:focus/hover'),
    ('wrapper-body', '0 4px 8px rgba(0,0,0,0.08)', '.o-wrapper-body'),
    ('media', '1.58463px 1.58463px 6.33854px rgba(0,0,0,0.15)', '.c-carrousel-format.facebook, .c-featured-ads__pic'),
    ('canvas', '6px 10px 24px rgba(0,0,0,0.1)', '.c-format-canvas__item'),
    ('error', '0 3px 6px 0 rgba(0,0,0,0.16)', '.c-contact-form label.js-form-error'),
    ('focus', '0 0 0 2px var(--color-yellow)', '.c-contact-form-radios__input:focus, .c-contact-form-checkboxes__input:focus'),
    ('section-contact', '0 -48px 0 0 var(--color-dark-blue) inset', '.c-section--contact'),
    ('modal', '0 4px 15px rgba(0,0,0,0.2)', '.modaal-container (Modaal, se sustituye en fase 6)'),
    ('modal-video', '0 0 10px rgba(0,0,0,0.3)', '.modaal-video-container (Modaal)'),
]

def hexcheck(v):
    return v

lines = []
A = lines.append
A('@import "tailwindcss/theme.css" layer(theme);')
A('@import "tailwindcss/utilities.css" layer(utilities);')
A('')
A('/*')
A(' * Fase 2 de TASK-006. Tokens con los valores exactos de assets/css/main.css.')
A(' * No hay preflight: el origen trae su propio reset (normalize e inuitCSS), y')
A(' * importar el de Tailwind cambiaría el render antes de tocar un solo componente.')
A(' */')
A('')
A('@font-face {')
A('    font-family: Poppins;')
A('    src: url(../assets/fonts/Poppins-Regular.woff2) format("woff2"), url(../assets/fonts/Poppins-Regular.woff) format("woff");')
A('    font-weight: 400;')
A('    font-style: normal;')
A('    font-display: swap;')
A('}')
A('@font-face {')
A('    font-family: Poppins;')
A('    src: url(../assets/fonts/Poppins-Medium.woff2) format("woff2"), url(../assets/fonts/Poppins-Medium.woff) format("woff");')
A('    font-weight: 500;')
A('    font-style: normal;')
A('    font-display: swap;')
A('}')
A('@font-face {')
A('    font-family: Poppins;')
A('    src: url(../assets/fonts/Poppins-SemiBold.woff2) format("woff2"), url(../assets/fonts/Poppins-SemiBold.woff) format("woff");')
A('    font-weight: 600;')
A('    font-style: normal;')
A('    font-display: swap;')
A('}')
A('')
A('@theme {')
A('    /* Se borran los valores por defecto de Tailwind: lo que no esté aquí no existe. */')
A('    --color-*: initial;')
A('    --font-*: initial;')
A('    --text-*: initial;')
A('    --breakpoint-*: initial;')
A('    --radius-*: initial;')
A('    --shadow-*: initial;')
A('    --container-*: initial;')
A('')
A('    /* Color (main.css, 57 hex y 4 rgba) */')
for n, v in COLORS:
    A(f'    --color-{n}: {v};')
A('')
A('    /* Tipografía. Poppins es la única familia del origen. */')
A('    --font-sans: Poppins, Arial, Helvetica, sans-serif;')
A('    --font-mono: monospace, monospace;')
A('    /* Pesos como propiedades (no como utilidades): verify-render lee --font-* como familias. */')
A('    --weight-regular: 400;')
A('    --weight-medium: 500;')
A('    --weight-semibold: 600;')
for s in sizes:
    A(f'    --text-{s}: {s}px;')
A('')
A('    /* Breakpoints: los 7 de sass-mq, en em con base 16 px, como en el origen. */')
A('    --breakpoint-mobile-small: 22.5em;')
A('    --breakpoint-mobile-mid: 26.5625em;')
A('    --breakpoint-mobile-wide: 31.25em;')
A('    --breakpoint-tablet: 43.75em;')
A('    --breakpoint-desktop: 61.25em;')
A('    --breakpoint-wide: 75em;')
A('    --breakpoint-ultrawide: 87.5em;')
A('')
A('    /* Contenedor (.o-wrapper): máximo 1302 px, variantes small y large. */')
A('    --container-wrapper: 1302px;')
A('    --container-wrapper-small: 1120px;')
A('    --container-wrapper-large: 1440px;')
A('    --wrapper-padding: 30px;')
A('')
A('    /* Radios (border-radius de main.css). */')
for r in radii:
    A(f'    --radius-{r}: {r}px;')
A('    --radius-circle: 50%;')
A('    --radius-round: 100%;')
A('')
A('    /* Sombras. El nombre dice el uso; ver inventario, sección 5.5. */')
for n, v, where in SHADOWS:
    A(f'    /* {where} */')
    if n == 'media':
        A('    /* stylelint-disable-next-line number-max-precision -- valor exacto de main.css (1.58463px); redondear cambiaría el origen */')
    A(f'    --shadow-{n}: {v};')
A('}')
open(OUT, 'w', encoding='utf8').write('\n'.join(lines) + '\n')
print('written', OUT, 'colors', len(COLORS), 'sizes', sizes, 'radii', radii)
