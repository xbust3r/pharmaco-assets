import sys, re, os
sys.path.insert(0, '/private/tmp/claude-502/-Users-miguel-servers-pharmaco-assets/628bef5e-2ce6-469e-bb61-14e50d4f299c/scratchpad/comp')
import compile as c
REPO = '/Users/miguel/servers/pharmaco-assets/.claude/worktrees/task-006-migracion'

def build(name):
    html_path = f'{REPO}/assets/{name}.html'
    lines, src = c.page_main_lines(html_path)
    title = re.search(r'<title>([^<]*)</title>', src).group(1)
    m = re.search(r'<meta name="description" content="([^"]*)"', src)
    desc = m.group(1) if m else 'Pharmaco'
    out = ['extends ../layouts/main-template', '', 'block title', '    title ' + title, 'block description',
           "    meta(name='description', content=" + '"' + desc.replace('"', '&quot;') + '")', 'block content']
    out.extend(lines)
    path = f'{REPO}/src/pages/{name}.pug'
    open(path, 'w', encoding='utf8').write('\n'.join(out) + '\n')
    return path, len(lines)

if __name__ == '__main__':
    for n in sys.argv[1:]:
        print(build(n))
    print('unsupported', sum(c.UNSUPPORTED.values()), c.UNSUPPORTED.most_common(3))
