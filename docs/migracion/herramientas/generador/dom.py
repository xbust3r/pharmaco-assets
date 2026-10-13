import re
from html.parser import HTMLParser

VOID = {'area','base','br','col','embed','hr','img','input','link','meta','source','track','wbr','use','path','rect','circle','polygon','polyline','ellipse','line','stop'}

class El:
    __slots__ = ('tag', 'attrs', 'children', 'parent', 'need_group', 'classes', 'raw_style')
    def __init__(self, tag, attrs, parent):
        self.tag = tag
        self.attrs = attrs  # list of (name, value or None)
        self.children = []
        self.parent = parent
        self.need_group = False
        self.classes = [c for c in (dict(attrs).get('class') or '').split() if c]

    def elements(self):
        return [c for c in self.children if isinstance(c, El)]

class Builder(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.root = El('#root', [], None)
        self.stack = [self.root]
    def handle_starttag(self, tag, attrs):
        el = El(tag, attrs, self.stack[-1])
        self.stack[-1].children.append(el)
        if tag not in VOID:
            self.stack.append(el)
    def handle_startendtag(self, tag, attrs):
        el = El(tag, attrs, self.stack[-1])
        self.stack[-1].children.append(el)
    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, 0, -1):
            if self.stack[i].tag == tag:
                del self.stack[i:]
                return
    def handle_data(self, data):
        self.stack[-1].children.append(data)
    def handle_entityref(self, name):
        self.stack[-1].children.append('&' + name + ';')
    def handle_charref(self, name):
        self.stack[-1].children.append('&#' + name + ';')
    def handle_comment(self, data):
        pass
    def handle_decl(self, data):
        pass
    def handle_pi(self, data):
        pass
    def unknown_decl(self, data):
        pass

def parse_doc(html):
    b = Builder()
    b.feed(html)
    return b.root

def find_first(el, tag):
    for c in el.children if hasattr(el, 'children') else []:
        if isinstance(c, El):
            if c.tag == tag:
                return c
            r = find_first(c, tag)
            if r:
                return r
    return None

# ---------- selector matching ----------
TOKEN = re.compile(r'\s*(>|\+|~|\s)\s*|([a-zA-Z*][\w-]*)|\.([\w-]+)|#([\w-]+)|\[([^\]]+)\]|::?([\w-]+)(\((?:[^()]|\([^()]*\))*\))?')

def parse_selector(sel):
    """Devuelve lista [(comb, compound)], compound = dict(tag, classes, attrs, pseudos, pseudo_elements, not_classes)."""
    s = sel.strip()
    chain = []
    cur = None
    comb = None
    i = 0
    n = len(s)
    def new_compound():
        return {'tag': None, 'classes': [], 'attrs': [], 'states': [], 'not': [], 'elem': []}
    pos = 0
    cur = new_compound()
    pending_comb = None
    while pos < n:
        m = re.compile(r'\s+').match(s, pos)
        if m:
            # espacio: combinador descendiente salvo que haya > + ~ alrededor
            pos = m.end()
            if pos < n and s[pos] in '>+~':
                continue
            if cur['tag'] or cur['classes'] or cur['attrs'] or cur['states'] or cur['elem'] or cur['not']:
                chain.append((pending_comb or ' ', cur))
                cur = new_compound()
                pending_comb = ' '
            continue
        ch = s[pos]
        if ch in '>+~':
            if cur['tag'] or cur['classes'] or cur['attrs'] or cur['states'] or cur['elem'] or cur['not']:
                chain.append((pending_comb or ' ', cur))
                cur = new_compound()
            pending_comb = ch
            pos += 1
            continue
        m = re.compile(r'\*|[a-zA-Z][\w-]*').match(s, pos)
        if m and cur['tag'] is None and not cur['classes'] and not cur['attrs'] and not cur['states'] and not cur['elem']:
            cur['tag'] = m.group(0); pos = m.end(); continue
        m = re.compile(r'\.((?:\\.|[\w-])+)').match(s, pos)
        if m:
            cur['classes'].append(re.sub(r'\\(.)', r'\1', m.group(1))); pos = m.end(); continue
        m = re.compile(r'::([\w-]+)').match(s, pos)
        if m:
            cur['elem'].append(m.group(1)); pos = m.end(); continue
        m = re.compile(r'\[([^\]]+)\]').match(s, pos)
        if m:
            cur['attrs'].append(m.group(1)); pos = m.end(); continue
        m = re.compile(r':not\(\[([\w-]+)\]\)').match(s, pos)
        if m:
            cur.setdefault('notattr', []).append(m.group(1)); pos = m.end(); continue
        m = re.compile(r':not\((\.[\w-]+)\)').match(s, pos)
        if m:
            cur['not'].append(m.group(1)[1:]); pos = m.end(); continue
        m = re.compile(r':([\w-]+)(\([^)]*\))?').match(s, pos)
        if m:
            name = m.group(1)
            if name in ('before', 'after', 'placeholder', 'marker', 'selection', 'file-selector-button'):
                cur['elem'].append(name)
            else:
                cur['states'].append(name + (m.group(2) or ''))
            pos = m.end(); continue
        raise ValueError('selector no soportado: ' + sel + ' en ' + s[pos:])
    if cur['tag'] or cur['classes'] or cur['attrs'] or cur['states'] or cur['elem'] or cur['not']:
        chain.append((pending_comb or ' ', cur))
    return chain

def compound_ok(el, c):
    if not isinstance(el, El):
        return False
    if c['tag'] and c['tag'] != '*' and el.tag != c['tag']:
        return False
    for cl in c['classes']:
        if cl not in el.classes:
            return False
    for cl in c['not']:
        if cl in el.classes:
            return False
    for na in c.get('notattr', []):
        if na in dict(el.attrs):
            return False
    for a in c['attrs']:
        m = re.match(r'^([\w-]+)(?:([~|^$*]?=)(.*))?$', a)
        name = m.group(1)
        d = dict(el.attrs)
        if name not in d:
            return False
        if m.group(2):
            val = m.group(3).strip().strip('"\'')
            v = d[name] or ''
            op = m.group(2)
            if op == '=' and v != val: return False
            if op == '^=' and not v.startswith(val): return False
            if op == '$=' and not v.endswith(val): return False
            if op == '*=' and val not in v: return False
    # estados y pseudoelementos no son estructurales: se ignoran aquí
    for st in c['states']:
        if st in ('first-child',):
            if el.parent is None or el.parent.elements()[0] is not el:
                return False
        elif st in ('last-child',):
            if el.parent is None or el.parent.elements()[-1] is not el:
                return False
        elif st in ('only-child',):
            if el.parent is None or len(el.parent.elements()) != 1:
                return False
        elif st.startswith('nth-child('):
            if not nth_ok(el, st[len('nth-child('):-1]):
                return False
        elif st.startswith('not('):
            return False
    return True

def sibling_prev(el):
    p = el.parent
    if p is None:
        return []
    els = p.elements()
    idx = els.index(el)
    return els[:idx]

def match(el, chain, i):
    """Devuelve (True, subject_states, group_states[(ancestor, state)]) si la cadena encaja."""
    comb, c = chain[i]
    if not compound_ok(el, c):
        return None
    if i == 0:
        return ([s for s in c['states']] + c['elem'], [])
    if comb == '>':
        cands = [el.parent] if el.parent is not None else []
    elif comb == '+':
        prev = sibling_prev(el)
        cands = prev[-1:] if prev else []
    elif comb == '~':
        cands = list(reversed(sibling_prev(el)))
    else:
        cands = []
        a = el.parent
        while a is not None:
            cands.append(a)
            a = a.parent
    for cand in cands:
        r = match(cand, chain, i - 1)
        if r is not None:
            subj, grp = r
            anc_states = [s for s in c['states'] if s not in ('first-child', 'last-child')]
            if anc_states:
                # estado en un ancestro: sólo se traduce a group-*
                cand.need_group = True
                grp = grp + [(cand, s) for s in anc_states] + [(cand, e) for e in c['elem'] if False]
            return (subj, grp)
    return None


def walk(el):
    for c in el.children:
        if isinstance(c, El):
            yield c
            yield from walk(c)


def nth_ok(el, expr):
    if el.parent is None:
        return False
    els = el.parent.elements()
    pos = els.index(el) + 1
    e = expr.strip().replace(' ', '')
    if e == 'odd':
        return pos % 2 == 1
    if e == 'even':
        return pos % 2 == 0
    m = re.match(r'^([+-]?\d*)n([+-]\d+)?$', e)
    if m:
        a = m.group(1)
        a = 1 if a in ('', '+') else (-1 if a == '-' else int(a))
        b = int(m.group(2) or 0)
        if a == 0:
            return pos == b
        k = (pos - b) / a
        return k >= 0 and k == int(k)
    return pos == int(e)
