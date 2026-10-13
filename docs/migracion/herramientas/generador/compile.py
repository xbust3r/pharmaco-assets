import re, math, sys, collections
sys.path.insert(0, '/private/tmp/claude-502/-Users-miguel-servers-pharmaco-assets/628bef5e-2ce6-469e-bb61-14e50d4f299c/scratchpad/comp')
import cssparse, dom

REPO = '/Users/miguel/servers/pharmaco-assets/.claude/worktrees/task-006-migracion'
CSS = open(REPO + '/assets/css/main.css', encoding='utf8').read()
RULES = cssparse.parse_rules(CSS)
STYLES = open(REPO + '/src/styles/styles.css', encoding='utf8').read()

# Tokens de color (hex -> nombre) leídos de @theme para no escribir nombres a mano
COLOR_TOKEN = {}
for name, val in re.findall(r'--color-([\w-]+):\s*(#[0-9a-fA-F]{3,6});', STYLES):
    COLOR_TOKEN.setdefault(val.lower(), name)
SHADOW_TOKEN = {
    '4px 5px 13px rgba(0,0,0,.08)': 'soft',
    '0 4px 8px rgba(0,0,0,.08)': 'wrapper-body',
    '1.58463px 1.58463px 6.33854px rgba(0,0,0,.15)': 'media',
    '6px 10px 24px rgba(0,0,0,.1)': 'canvas',
    '0 3px 6px 0 rgba(0,0,0,.16)': 'error',
    '0 0 0 2px #ffd027': 'focus',
    '0 -48px 0 0 #00113b inset': 'section-contact',
    '0 4px 15px rgba(0,0,0,.2)': 'modal',
    '0 0 10px rgba(0,0,0,.3)': 'modal-video',
}
TEXT_PX = {9,10,12,14,16,17,18,19,20,21,22,24,27,28,30,32,35,37,39,40,42,44,49,63,64,77,84}
RADIUS_PX = {0,3,4,5,6,8,9,10,12,14,15,16,18,20,28,40}
BP_NAME = {360: 'mobile-small', 425: 'mobile-mid', 500: 'mobile-wide', 700: 'tablet', 980: 'desktop', 1200: 'wide', 1400: 'ultrawide'}
STATE_MAP = {'hover': 'hover', 'focus': 'focus', 'active': 'active', 'disabled': 'disabled', 'checked': 'checked',
             'focus-within': 'focus-within', 'focus-visible': 'focus-visible', 'before': 'before', 'after': 'after',
             'placeholder': 'placeholder', 'marker': 'marker', 'selection': 'selection'}
STRUCTURAL = {'first-child', 'last-child', 'only-child'}
# clases del origen que se sustituyen por utilidades ya definidas en styles.css (@utility)
ALIAS = {'o-wrapper': 'wrapper', 'o-icon': 'icon', 'c-button-line': 'link-underline'}
UNSUPPORTED = collections.Counter()
HOOKS_EXTRA = {
    'c-clients__slider': 'flex overflow-x-auto snap-x snap-mandatory [scrollbar-width:none] [-ms-overflow-style:none] js-clients-track',
    'c-clients__slide': 'js-slider-item snap-start shrink-0',
    'c-clients__slider-controls': 'desktop:hidden',  # el origen los oculta desde escritorio; los botones siguen en el DOM para el JS
    'c-contact-form__item--business': 'js-business-item',
    'c-contact-form__item--textarea': 'js-textarea-item',
}
SKIP_SELECTOR_PARTS = ('data-aos', 'no-js', '-webkit-', '-moz-', '-ms-')

_chain_cache = {}
def chain_of(sel):
    if sel not in _chain_cache:
        try:
            _chain_cache[sel] = dom.parse_selector(sel)
        except ValueError:
            _chain_cache[sel] = None
    return _chain_cache[sel]

def specificity(chain):
    b = c = 0
    for _, cp in chain:
        b += len(cp['classes']) + len(cp['attrs']) + len(cp['not'])
        b += sum(1 for s in cp['states'] if s not in ('first-child','last-child') or True)
        c += 1 if cp['tag'] and cp['tag'] != '*' else 0
        c += len(cp['elem'])
    return (b, c)

def expand_shorthand(p, v):
    if p in ('margin', 'padding'):
        parts = v.split()
        if not parts or len(parts) > 4:
            return [(p, v)]
        if len(parts) == 1: t = r = b = l = parts[0]
        elif len(parts) == 2: t = b = parts[0]; r = l = parts[1]
        elif len(parts) == 3: t = parts[0]; r = l = parts[1]; b = parts[2]
        else: t, r, b, l = parts
        return [(p + '-top', t), (p + '-right', r), (p + '-bottom', b), (p + '-left', l)]
    return [(p, v)]

def element_entries(el):
    entries = []
    for r in RULES:
        m = r['media']
        if m == 'skip' or (isinstance(m, tuple) and m[0] == 'maxh'):
            continue
        for sel in r['sel']:
            if any(p in sel for p in SKIP_SELECTOR_PARTS):
                continue
            chain = chain_of(sel)
            if chain is not None and not any(cp['classes'] for _, cp in chain):
                continue  # reglas de elemento: ya están en @layer base
            if chain is None:
                UNSUPPORTED['parse: ' + sel[:60]] += 1
                continue
            last = chain[-1][1]
            # las reglas de alias (o-wrapper, o-icon) se conservan: sus valores son la base de la cascada; coinciden con las utilidades
            res = dom.match(el, chain, len(chain) - 1)
            if res is None:
                continue
            subj, grp = res
            toks = []
            bad = False
            for s in subj:
                if s in STRUCTURAL or s.startswith('nth-child('):
                    continue
                if s in STATE_MAP:
                    toks.append(STATE_MAP[s])
                else:
                    bad = True
            gtoks = []
            for anc, s in grp:
                if s in STRUCTURAL or s.startswith('nth-child('):
                    continue
                if s in STATE_MAP:
                    gtoks.append('group-' + STATE_MAP[s])
                else:
                    bad = True
            if bad:
                UNSUPPORTED[sel[:80]] += 1
                continue
            key = tuple(gtoks + toks)
            spec = specificity(chain)
            for idx, (p, v, imp) in enumerate(r['decls']):
                if p.startswith(('-webkit-', '-ms-', '-moz-')) or v.lower().startswith(('-webkit-', '-ms-', '-moz-')):
                    continue
                for p2, v2 in expand_shorthand(p, v):
                    entries.append({'key': key, 'media': m, 'prop': p2, 'value': v2, 'imp': imp, 'spec': spec, 'order': (r['order'], idx)})
    return entries

def comp_point(media):
    # máximo V (px) -> primer px donde deja de aplicar
    v = media[1]
    return math.floor(v) + 1 if v == int(v) else math.ceil(v)

def applies(media, p):
    if media == 'base':
        return True
    kind, v = media
    if kind == 'min':
        return p >= v
    if kind == 'max':
        return p <= v
    return False

def winner(cands):
    return max(cands, key=lambda e: (e['imp'], e['spec'], e['order']))

def util(prop, value, imp):
    v = value.strip()
    v = re.sub(r"url\((['\"]?)\.\./images/", r'url(\1/src/assets/images/', v)
    v = re.sub(r"url\((['\"]?)\.\./fonts/", r'url(\1/src/assets/fonts/', v)
    lv = v.lower()
    cls = None
    if prop in ('color', 'background-color', 'border-color', 'fill', 'stroke'):
        pre = {'color': 'text', 'background-color': 'bg', 'border-color': 'border', 'fill': 'fill', 'stroke': 'stroke'}[prop]
        if lv in COLOR_TOKEN:
            cls = f'{pre}-{COLOR_TOKEN[lv]}'
        elif lv == 'transparent':
            cls = f'{pre}-transparent'
    elif prop == 'font-size' and re.match(r'^\d+px$', lv) and int(lv[:-2]) in TEXT_PX:
        cls = f'text-{lv[:-2]}'
    elif prop == 'font-weight' and lv in ('400', '500', '600'):
        cls = {'400': 'weight-regular', '500': 'weight-medium', '600': 'weight-semibold'}[lv]
    elif prop == 'border-radius':
        if re.match(r'^\d+px$', lv) and int(lv[:-2]) in RADIUS_PX:
            cls = f'rounded-{lv[:-2]}'
        elif lv == '50%':
            cls = 'rounded-circle'
        elif lv == '100%':
            cls = 'rounded-round'
    elif prop == 'box-shadow' and lv in SHADOW_TOKEN:
        cls = f'shadow-{SHADOW_TOKEN[lv]}'
    elif prop == 'display' and lv in ('flex', 'block', 'inline-flex', 'inline-block', 'none', 'inline', 'grid'):
        cls = {'none': 'hidden'}.get(lv, lv)
    elif prop == 'position' and lv in ('absolute', 'relative', 'fixed', 'static', 'sticky'):
        cls = lv
    elif prop == 'content' and value.strip() in ("''", '""'):
        cls = "content-['']"
    if cls is None:
        if lv == 'initial':
            pass
        val = v.replace(' ', '_')
        if prop == 'content':
            val = val
        cls = f'[{prop}:{val}]'
    return cls + ('!' if imp else '')

def prefix_for(p, key):
    parts = []
    if p != 0:
        r = round(p)
        parts.append(BP_NAME.get(r, f'min-[{r}px]'))
    parts.extend(key)
    return ''.join(t + ':' for t in parts)

HERO_ATTR = {}
# Valor por defecto del navegador para `display` según la etiqueta (no es `initial`, que sería inline).
BLOCK_TAGS = {'div','section','article','aside','header','footer','nav','main','p','h1','h2','h3','h4','h5','h6','ul','ol','dl','figure','figcaption','form','fieldset','blockquote','hr','address','dialog','details','summary'}
NONE_TAGS = {'source','track','script','style','template','link','meta','head','title'}
def default_display(tag):
    if tag == 'li': return 'list-item'
    if tag in NONE_TAGS: return 'none'
    if tag in BLOCK_TAGS: return 'block'
    if tag in ('button','input','select','textarea'): return 'inline-block'
    return 'inline'

def classes_for(el):
    entries = element_entries(el)
    groups = collections.defaultdict(list)
    points = {0.0}
    for e in entries:
        groups[(e['key'], e['prop'])].append(e)
        m = e['media']
        if isinstance(m, tuple):
            if m[0] == 'min':
                points.add(float(m[1]))
            elif m[0] == 'max':
                points.add(float(comp_point(m)))
    points = sorted(points)
    out = []
    for (key, prop), es in groups.items():
        prev = object()
        for p in points:
            cands = [e for e in es if applies(e['media'], p)]
            if cands:
                w = winner(cands)
                val = w['value']
                imp = w['imp']
            else:
                val, imp = None, False
            if val is None:
                if prev is not None and prev is not object() and prev is not None:
                    reset = default_display(el.tag) if prop == 'display' else 'initial'
                    out.append((p, key, util(prop, reset, False)))
                prev = None
                continue
            if val != prev:
                out.append((p, key, util(prop, val, imp)))
            prev = val
    # ordenar: base primero, luego por punto
    out.sort(key=lambda t: t[0])
    cls = []
    for p, key, c in out:
        cls.append(prefix_for(p, key) + c)
    # alias de utilidades de origen
    extra = [ALIAS[c] for c in el.classes if c in ALIAS]
    # clases de apoyo: el origen las pinta con tiny-slider o con reglas que ya no existen
    for origen_cls, util_cls in HOOKS_EXTRA.items():
        if origen_cls in el.classes:
            extra.append(util_cls)
    hero = [c[len('c-hero--'):] for c in el.classes if c.startswith('c-hero--')]
    if hero:
        HERO_ATTR[id(el)] = hero[0]
    keep = [c for c in el.classes if c.startswith('js-') or c.endswith('-js')]
    res = extra + keep + cls
    if el.need_group:
        res.insert(0, 'group')
    return res


# ---------- emisión Pug ----------
SKIP_TAGS = {'script', 'link', 'style', 'meta', 'noscript', 'header', 'footer', 'template'}
DROP_ATTRS = {'class', 'style', 'focusable', 'data-aos-once'}
URL_ATTRS = {'href', 'src', 'srcset', 'poster', 'xlink:href'}
EMPTY_OK = True
import os
BROKEN = []
DROPPED = []
NOTES = []
def _exists_origin(val):
    first = val.split(',')[0].strip().split(' ')[0]
    if not first or first.startswith(('http', 'data:', '#')):
        return True
    return os.path.exists(os.path.join(REPO, 'assets', first.split('?')[0]))

def rewrite_url(v):
    v = re.sub(r'images/icons/icons\.svg#icon-', '/src/assets/images/sprite.svg#icon-', v)
    v = re.sub(r'(^|[\s,(])images/', r'\1/src/assets/images/', v)
    return v

def attr_value(v):
    if '"' in v:
        v = v.replace('"', '&quot;')
    return '"' + v + '"'

SLIDER_LABEL = {'js-clients-slider-prev': 'Anterior slide', 'js-clients-slider-next': 'Siguiente slide'}
def node_is_slider_btn(el, name):
    return False

def el_attrs(el):
    out = []
    style_color = None
    extra = []
    for hook, label in SLIDER_LABEL.items():
        if hook in el.classes and el.tag == 'button' and 'aria-label' not in dict(el.attrs):
            extra.append(f'aria-label={attr_value(label)}')
    for name, val in el.attrs:
        if name == 'style' and val:
            m = re.search(r'color:\s*(#[0-9a-fA-F]{3,6})', val)
            if m and m.group(1).lower() in COLOR_TOKEN:
                style_color = 'text-' + COLOR_TOKEN[m.group(1).lower()]
            continue
        if name in DROP_ATTRS:
            continue
        if node_is_slider_btn(el, name):
            pass
        if name == 'data-aos':
            name = 'data-reveal'
        elif name == 'data-aos-delay':
            name = 'data-reveal-delay'
        if val is None:
            out.append(name)
            continue
        if name in ('height', 'width') and val is not None and not re.match(r'^\d+$', val):
            DROPPED.append(f'{name}="{val}"')
            continue
        if name == 'media':
            val = re.sub(r'(\d+(?:\.\d+)?)px', lambda m: ('%g' % (float(m.group(1)) / 16)) + 'rem', val)
        if name in URL_ATTRS:
            if name in ('src', 'srcset') and not _exists_origin(val):
                # referencia rota en el origen: se conserva como dato, sin petición
                BROKEN.append(val)
                NOTES.append('src roto en el origen, sin archivo: ' + re.sub(r'^images/', '', val).replace('.webp', ' (webp)'))
                continue
            val = rewrite_url(val)
        out.append(f'{name}={attr_value(val)}')
    return out + extra, style_color

def safe_text(t):
    return t.replace('#{', '\\#{').replace('#[', '\\#[').replace('!{', '\\!{')

def text_of(children):
    return ''.join(c if isinstance(c, str) else '' for c in children)

node_prev = [None]
def node_lines(node, depth):
    lines = node_lines_inner(node, depth)
    if isinstance(node, dom.El) and node.tag not in SKIP_TAGS and node.tag not in ('legend', 'fieldset') and lines:
        bem = [c for c in node.classes if re.match(r'^[cso]-', c) and not c.startswith('o-wrapper')]
        if bem:
            lines.insert(0, '    ' * depth + '//- origen: ' + bem[0])
    return lines

def node_lines_inner(node, depth):
    pad = '    ' * depth
    if isinstance(node, str):
        t = re.sub(r'\s+', ' ', node)
        core = t.strip()
        if core == '':
            prev_el = node_prev[0]
            if os.environ.get('DROP_WS'):
                return []
            return [pad + "| #{' '}"] if t else []
        lead = t.startswith(' ')
        trail = t.endswith(' ')
        return [pad + '| ' + ("#{' '}" if lead else '') + safe_text(core) + ("#{' '}" if trail else '')]
    if node.tag in SKIP_TAGS:
        return []
    cls = classes_for(node)
    broken_img = node.tag == 'img' and any(n == 'src' and not _exists_origin(v or '') for n, v in node.attrs)
    fallback_src = None
    if broken_img:
        alt = dict(node.attrs).get('alt') or ''
        srcs = [dict(k.attrs).get('srcset') for k in (node.parent.children if node.parent else []) if isinstance(k, dom.El) and k.tag == 'source' and dict(k.attrs).get('srcset')]
        if srcs and node.parent is not None and node.parent.tag == 'picture':
            first = re.split(r'[,\s]+', srcs[0].strip())[0]
            fallback_src = first
            NOTES.append('img de respaldo de picture: el src roto del origen se sustituye por el primer source (el que ya usaba el navegador)')
        else:
            NOTES.append('img roto en el origen (sin archivo): ' + alt)
    attrs, style_color = el_attrs(node)
    if node.tag == 'a' and not any(isinstance(k, str) and k.strip() for k in node.children):
        tt = [k for k in dom.walk(node) if isinstance(k, dom.El) and k.tag == 'title']
        if tt and not any(a.startswith('aria-label=') for a in attrs):
            attrs.append('aria-label=' + attr_value(' '.join(text_of(tt[0].children).split())))
    if style_color:
        cls.append(style_color)
    if id(node) in HERO_ATTR:
        attrs.append('data-hero=' + attr_value(HERO_ATTR[id(node)]))
    if node.tag == 'svg' and not any(isinstance(k, dom.El) and k.tag == 'title' for k in node.children):
        attrs = [a for a in attrs if not a.startswith('role=')] + ([] if any(a.startswith('aria-hidden=') for a in attrs) else ["aria-hidden='true'"])
    if cls:
        attrs.insert(0, 'class=' + attr_value(' '.join(cls)))
    if node.tag == 'img':
        d_ = dict(node.attrs)
        if 'c-clients__client' in node.classes:
            attrs = [a for a in attrs if not a.startswith('loading=')]  # el slider es horizontal: lazy no carga lo que no se ve
        w_, h_ = d_.get('width'), d_.get('height')
        attrs = [a for a in attrs if not a.startswith(('width=', 'height='))]
        es_svg = (d_.get('src') or '').lower().endswith('.svg')
        if w_ and h_ and re.match(r'^\d+$', w_) and re.match(r'^\d+$', h_) and not es_svg:
            # los atributos width/height del origen sólo fijan la proporción: se convierte en aspect-ratio
            cls.append(f'aspect-[{w_}/{h_}]')
    tag_name = node.tag
    if broken_img and fallback_src:
        attrs = [a for a in attrs if not a.startswith(('src=', 'data-origen-src='))]
        attrs.insert(0, 'src=' + attr_value(rewrite_url(fallback_src)))
    elif broken_img:
        attrs = [a for a in attrs if not a.startswith(('alt=', 'width=', 'height=', 'src=', 'data-origen-src=', 'loading='))]
        attrs += ['role="img"', 'aria-label=' + attr_value(dict(node.attrs).get('alt') or '')]
        tag_name = 'div'
    head = tag_name + ('(' + ', '.join(attrs) + ')' if attrs else '')
    note = []
    if NOTES:
        note = [pad + '//- ' + n for n in NOTES]
        del NOTES[:]
    kids = node.children
    if node.tag == 'fieldset':
        kids = [k for k in kids if not (isinstance(k, str) and k.strip() == '')]
    if broken_img:
        kids = []
    if node.tag in dom.VOID or not kids:
        return note + [pad + head]
    if all(isinstance(k, str) for k in kids):
        t = re.sub(r'\s+', ' ', ''.join(kids)).strip()
        if t == '':
            return [pad + head]
        if '#{' not in t and '#[' not in t and '!{' not in t and len(t) < 160:
            return [pad + head + ' ' + t]
    lines = note + [pad + head]
    for k in kids:
        lines.extend(node_lines(k, depth + 1))
    return lines

def page_main_lines(html_path, depth=1):
    src = open(html_path, encoding='utf8').read()
    root = dom.parse_doc(src)
    main = dom.find_first(root, 'main')
    lines = []
    for k in main.children:
        lines.extend(node_lines(k, depth))
    return lines, src
