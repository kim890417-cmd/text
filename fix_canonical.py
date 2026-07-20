import os
import re
from urllib.parse import quote

repo_path = r'C:\Users\User\Desktop\키워드 글쓰기\healthfit_repo'
wrong_pattern = re.compile(r'<link rel="canonical" href="https://healthfit100\.com/health/[^"]+\">')
base_url = 'https://healthfit100.com'

fixed = []
for root, dirs, files in os.walk(os.path.join(repo_path, 'health')):
    for file in files:
        if file == 'index.html':
            filepath = os.path.join(root, file)
            rel_path = os.path.relpath(root, repo_path).replace('\\', '/')
            parts = rel_path.split('/')
            encoded_parts = [quote(p, safe='') for p in parts]
            correct_canonical = base_url + '/' + '/'.join(encoded_parts) + '/'

            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            match = wrong_pattern.search(content)
            if match:
                current = match.group(0)
                new_tag = '<link rel="canonical" href="' + correct_canonical + '">'
                if current != new_tag:
                    print('[NEEDS FIX] ' + rel_path)
                    print('  OLD: ' + current[:100])
                    print('  NEW: ' + new_tag)
                    fixed.append((filepath, content, current, new_tag))
                else:
                    print('[OK] ' + rel_path)

print('\n수정 필요 파일: ' + str(len(fixed)) + '개')

# Actually apply fixes
for filepath, content, old_tag, new_tag in fixed:
    new_content = content.replace(old_tag, new_tag, 1)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('수정 완료: ' + filepath.split('healthfit_repo\\')[1])

print('\n모든 canonical 수정 완료!')
