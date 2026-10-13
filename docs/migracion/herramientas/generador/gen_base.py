import re
css = open('/Users/miguel/servers/pharmaco-assets/.claude/worktrees/task-006-migracion/assets/css/main.css', encoding='utf8').read()
ELEM = re.compile(r'^(html|body|a|h[1-6]|p|ul|ol|li|img|svg|button|input|optgroup|select|textarea|fieldset|figure|hr|main|article|aside|footer|header|nav|section|abbr|b|strong|mark|small|sub|sup|\*|:|::-webkit|h1)')
MAP = {'#111029': 'var(--color-ink)', '#666': 'var(--color-gray-666)', '#ff0': 'var(--color-highlight)', '#000': 'var(--color-black)'}
out = []
def walk(s, media):
    i = 0; n = len(s)
    while i < n:
        j = s.find('{', i)
        if j < 0: break
        head = s[i:j].strip(); depth = 1; k = j + 1
        while depth and k < n:
            if s[k] == '{': depth += 1
            elif s[k] == '}': depth -= 1
            k += 1
        body = s[j+1:k-1]
        if head.startswith('@media'):
            walk(body, True)
        elif not head.startswith('@') and not media and '{' not in body:
            if ELEM.match(head) and 'data-aos' not in head and 'url(' not in body:
                out.append((head, body))
        i = k
walk(css, False)
lines = ['@layer base {', '    /* Reset del origen (normalize-scss e inuitCSS genéricos), sin AOS. Los hex son tokens. */']
for head, body in out:
    decls = [d.strip() for d in body.split(';') if d.strip()]
    decls = [re.sub(r'#[0-9a-fA-F]{3,6}\b', lambda m: MAP.get(m.group(0).lower(), m.group(0)), d) for d in decls]
    # quitar prefijos de navegador redundantes
    decls = [d for d in decls if not d.startswith('-webkit-') and not d.startswith('-ms-')]
    if not decls: continue
    lines.append('    ' + head.replace(',', ',\n    ') + ' {')
    for d in decls:
        lines.append('        ' + d + ';')
    lines.append('    }')
lines.append('}')
open('/private/tmp/claude-502/-Users-miguel-servers-pharmaco-assets/628bef5e-2ce6-469e-bb61-14e50d4f299c/scratchpad/base-layer.css', 'w', encoding='utf8').write('\n'.join(lines) + '\n')
print('rules', len(out))
