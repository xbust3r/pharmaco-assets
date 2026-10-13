import re, json, html, sys, collections, os
REPO = '/Users/miguel/servers/pharmaco-assets/.claude/worktrees/task-006-migracion'
PAGES = ['index','nosotros','servicios','servicio-detalle','portafolio','contactanos','campana-cyberwow','campana-iveco','campana-stralis','diseño-de-personajes']

PARAM_ATTRS = {'href','src','srcset','alt','aria-label','title','data-origen-src','data-origen-srcset','data-reveal-delay','data-reveal'}
MAX_PARAMS = 10

class N:
    def __init__(self, raw, level, kind):
        self.raw = raw; self.level = level; self.kind = kind  # kind: comment|text|el
        self.children = []; self.comment = None

def split_head(text):
    m = re.match(r'^([a-zA-Z][\w-]*)', text)
    tag = m.group(1); rest = text[len(tag):]
    attrs = []; inline = None
    if rest.startswith('('):
        i = 1; depth = 0; q = None; start = 1
        while i < len(rest):
            ch = rest[i]
            if q:
                if ch == '\\': i += 2; continue
                if ch == q: q = None
            elif ch in '"\'': q = ch
            elif ch == ')': break
            i += 1
        inner = rest[1:i]; after = rest[i+1:].strip()
        attrs = split_attrs(inner)
        inline = after if after else None
    else:
        inline = rest.strip() or None
    return tag, attrs, inline

def split_attrs(s):
    out = []; i = 0; n = len(s)
    while i < n:
        while i < n and s[i] in ', ': i += 1
        if i >= n: break
        j = i
        while j < n and s[j] not in '=, ': j += 1
        name = s[i:j]
        if j < n and s[j] == '=':
            k = j + 1
            if k < n and s[k] in '"\'':
                q = s[k]; m = k + 1
                while m < n and not (s[m] == q and s[m-1] != '\\'): m += 1
                raw = s[k:m+1]; i = m + 1
            else:
                m = k
                while m < n and s[m] != ',': m += 1
                raw = s[k:m]; i = m
            out.append((name, raw))
        else:
            out.append((name, None)); i = j
    return out

def unq(raw):
    if raw is None: return None
    if raw[0] in '"\'': 
        v = raw[1:-1]
        return v.replace("\\'", "'")
    return raw

def parse_page(path):
    lines = open(path, encoding='utf8').read().split('\n')
    idx = lines.index('block content')
    root = N('', -1, 'root'); stack = [root]; pending = None
    for ln in lines[idx+1:]:
        if not ln.strip(): continue
        level = (len(ln) - len(ln.lstrip(' '))) // 4
        text = ln.strip()
        while stack and stack[-1].level >= level: stack.pop()
        if text.startswith('//-'):
            pending = ln; continue
        if text.startswith('|'):
            node = N(ln, level, 'text')
        else:
            node = N(ln, level, 'el')
        node.comment = pending; pending = None
        stack[-1].children.append(node)
        stack.append(node)
    return root, lines[:idx+1]

def sig_and_params(node):
    """Devuelve (firma, parámetros[(tipo, valor)], cabeza) para un nodo y su subárbol."""
    if node.kind == 'text':
        txt = node.raw.strip()[1:].strip()
        if '#{' in txt or '!{' in txt:
            return ('TEXTC', txt), []
        head = ('TEXT', '| §')
        params = [('text', txt)]
        return head, params
    tag, attrs, inline = split_head(node.raw.strip())
    parts = []; params = []
    for name, raw in attrs:
        if raw is None:
            parts.append(name)
        elif name == 'class':
            parts.append(f'{name}={raw}')
        elif name in PARAM_ATTRS:
            parts.append(f'{name}=§'); params.append(('attr', (name, unq(raw))))
        else:
            parts.append(f'{name}={raw}')
    inline_const = inline is not None and ('#{' in inline or '!{' in inline)
    if inline is not None and not inline_const:
        params.append(('text', inline))
    cm = node.comment.strip() if node.comment else ''
    head = (tag, tuple(parts), (inline if inline_const else (inline is not None)), cm)
    return head, params

def full_sig(node):
    head, params = sig_and_params(node)
    return (head, tuple(full_sig(c) for c in node.children))

def all_params(node):
    out = []
    _, params = sig_and_params(node)
    out.extend(params)
    for c in node.children:
        out.extend(all_params(c))
    return out

def camel(bem):
    b = re.sub(r'^[cso]-', '', bem)
    parts = re.split(r'[-_]+', b)
    parts = [p for p in parts if p]
    return parts[0] + ''.join(p.capitalize() for p in parts[1:]) if parts else 'bloque'

def body_lines(node, pidx, indent):
    """Reconstruye el subárbol con parámetros pN en lugar de valores."""
    out = []
    pad = '    ' * indent
    if node.comment: out.append(pad + node.comment.strip())
    if node.kind == 'text':
        txt = node.raw.strip()[1:].strip()
        if '#{' in txt or '!{' in txt:
            out.append(pad + '| ' + txt); return out, pidx
        out.append(pad + '| !{p%d}' % pidx.pop(0)); return out, pidx
    tag, attrs, inline = split_head(node.raw.strip())
    parts = []
    for name, raw in attrs:
        if raw is None: parts.append(name)
        elif name == 'class': parts.append(f'{name}={raw}')
        elif name in PARAM_ATTRS: parts.append(f'{name}=p{pidx.pop(0)}')
        else: parts.append(f'{name}={raw}')
    head = tag + ('(' + ', '.join(parts) + ')' if parts else '')
    if inline is not None:
        if '#{' in inline or '!{' in inline: head += ' ' + inline
        else: head += ' !{p%d}' % pidx.pop(0)
    out.append(pad + head)
    for c in node.children:
        sub, pidx = body_lines(c, pidx, indent + 1)
        out.extend(sub)
    return out, pidx

def mixin_for(node, name):
    params = all_params(node)
    names = ['p%d' % i for i in range(len(params))]
    body, _ = body_lines(node, list(range(len(params))), 1)
    sigline = f'mixin {name}(' + ', '.join(names) + ')'
    return [sigline] + body, params

def main():
    pages = {}
    counts = collections.Counter()
    def walk_count(n):
        for c in n.children:
            if c.kind != 'comment':
                counts[full_sig(c)] += 1
            walk_count(c)
    trees = {}
    for pg in PAGES:
        root, header = parse_page(f'{REPO}/src/pages/{pg}.pug')
        trees[pg] = (root, header)
        walk_count(root)
    mixins = {}; order = []; used_names = collections.Counter()
    def bem_of(node):
        if node.comment and 'origen:' in node.comment:
            return node.comment.split('origen:')[1].strip()
        return None
    def choose(node, fn):
        for c in node.children:
            sig = full_sig(c)
            if counts[sig] >= 2 and c.children and c.kind == 'el' and len(all_params(c)) <= MAX_PARAMS:
                if sig not in mixins:
                    bem = bem_of(c) or 'bloque'
                    base = 'rep' + camel(bem)[:1].upper() + camel(bem)[1:]
                    used_names[base] += 1
                    name = base if used_names[base] == 1 else f'{base}{used_names[base]}'
                    lines, params = mixin_for(c, name)
                    mixins[sig] = (name, lines, params)
                    order.append(sig)
                c.mixin = mixins[sig][0]
                c.mixin_params = mixins[sig][2]
            else:
                choose(c, fn)
    for pg in PAGES:
        choose(trees[pg][0], None)
    # escribir mixins
    lib = ['//- Mixins de componentes repetidos entre páginas (fase 4). Generados desde el marcado del origen:',
           '//- cada uno sustituye a un bloque que aparece en 2 o más sitios; los textos y atributos son parámetros.', '']
    for sig in order:
        name, lines, params = mixins[sig]
        lib.extend(lines); lib.append('')
    open(f'{REPO}/src/components/repetidos.pug', 'w', encoding='utf8').write('\n'.join(lib) + '\n')
    # reescribir páginas
    def emit(node, indent, out):
        if node.kind == 'root':
            for c in node.children: emit(c, indent, out)
            return
        if node.kind == 'comment': return
        if hasattr(node, 'mixin'):
            if node.comment: out.append(node.comment)
            args = []
            for typ, val in all_params(node):
                if typ == 'attr':
                    args.append(json.dumps(html.unescape(val[1]), ensure_ascii=False))
                else:
                    args.append(json.dumps(val, ensure_ascii=False))
            out.append('    ' * indent + '+' + node.mixin + '(' + ', '.join(args) + ')')
            return
        if node.comment: out.append(node.comment)
        out.append(node.raw)
        for c in node.children: emit(c, indent + 1, out)
    total = 0
    for pg in PAGES:
        root, header = trees[pg]
        out = []
        for c in root.children: emit(c, 1, out)
        hdr = header
        # incluir mixins dentro del bloque content
        content = ['    include ../components/repetidos'] + out
        text = '\n'.join(hdr + content) + '\n'
        open(f'{REPO}/src/pages/{pg}.pug', 'w', encoding='utf8').write(text)
        total += sum(1 for l in out if l.strip().startswith('+'))
    print('mixins', len(order), 'llamadas', total)

if __name__ == '__main__':
    main()
