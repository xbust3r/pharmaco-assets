import re

def parse_rules(css):
    css = re.sub(r'/\*[\s\S]*?\*/', '', css)
    """Devuelve lista de reglas: dict(sel=[...], decls=[(prop,val,important)], media=('base'|('min',px)|('max',px)|('maxh',px)|'skip'), order=n)."""
    rules = []
    order = [0]

    def unit_px(v):
        v = v.strip()
        m = re.match(r'^([\d.]+)(em|px)$', v)
        if not m:
            return None
        n = float(m.group(1))
        return n * 16 if m.group(2) == 'em' else n

    def media_of(head):
        h = head.replace(' ', '')
        if h == '@mediascreen':
            return 'base'
        mm = re.search(r'\(min-width:([\d.]+(?:em|px))\)', h)
        if mm:
            return ('min', unit_px(mm.group(1)))
        mm = re.search(r'\(max-width:([\d.]+(?:em|px))\)', h)
        if mm:
            return ('max', unit_px(mm.group(1)))
        mm = re.search(r'\(max-height:([\d.]+(?:em|px))\)', h)
        if mm:
            return ('maxh', unit_px(mm.group(1)))
        return 'skip'

    def walk(s, media):
        i, n = 0, len(s)
        while i < n:
            j = s.find('{', i)
            if j < 0:
                break
            head = s[i:j].strip()
            depth, k = 1, j + 1
            while depth and k < n:
                if s[k] == '{':
                    depth += 1
                elif s[k] == '}':
                    depth -= 1
                k += 1
            body = s[j + 1:k - 1]
            if head.startswith('@media'):
                walk(body, media_of(head))
            elif head.startswith('@'):
                pass
            elif '{' not in body:
                decls = []
                for d in body.split(';'):
                    if ':' not in d:
                        continue
                    p, v = d.split(':', 1)
                    p = p.strip().lower()
                    v = v.strip()
                    imp = False
                    if v.lower().endswith('!important'):
                        v = v[:-10].strip()
                        imp = True
                    decls.append((p, v, imp))
                sels = [x.strip() for x in head.split(',') if x.strip()]
                order[0] += 1
                rules.append({'sel': sels, 'decls': decls, 'media': media, 'order': order[0]})
            i = k

    walk(css, 'base')
    return rules
