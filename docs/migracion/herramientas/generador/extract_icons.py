import re, os
ORIG = '/Users/miguel/servers/pharmaco-assets/.claude/worktrees/task-006-migracion/assets/images/icons/icons.svg'
OUTD = '/Users/miguel/servers/pharmaco-assets/.claude/worktrees/task-006-migracion/src/assets/icons'
USED = ['arrow-down', 'arrow-left', 'arrow-right', 'chevron-right', 'close', 'facebook', 'instagram', 'linkedin', 'menu', 'search', 'to-top', 'web', 'youtube']
s = open(ORIG, encoding='utf8').read()
defs = re.search(r'<defs>(.*?)</defs>', s, re.S)
defs_inner = defs.group(1) if defs else ''
# elementos de defs con id
def_items = re.findall(r'(<(clipPath|linearGradient|radialGradient|mask|pattern|path|g|rect|filter)\b[^>]*id="([^"]+)"[\s\S]*?</\2>)', defs_inner)
os.makedirs(OUTD, exist_ok=True)
for name in USED:
    m = re.search(r'<symbol[^>]*id="icon-%s"[^>]*viewBox="([^"]+)"[^>]*>([\s\S]*?)</symbol>' % re.escape(name), s)
    if not m:
        m2 = re.search(r'<symbol[^>]*id="icon-%s"[^>]*>([\s\S]*?)</symbol>' % re.escape(name), s)
        raise SystemExit(f'sin viewBox: {name}')
    vb, inner = m.group(1), m.group(2)
    refs = set(re.findall(r'#([A-Za-z0-9_-]+)', inner))
    chosen = [full for full, tag, id_ in def_items if id_ in refs]
    body = ''.join(chosen) + inner
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}">{body}</svg>\n'
    open(os.path.join(OUTD, f'icon-{name}.svg'), 'w', encoding='utf8').write(svg)
    print(name, vb, 'defs:', len(chosen), 'bytes', len(svg))
