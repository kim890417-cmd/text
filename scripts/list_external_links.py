import glob
import re
from collections import Counter

files = glob.glob('health/*/index.html')
all_externals = Counter()

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    links = re.findall(r'href=["\'](https?://[^"\']+)["\']', c)
    for l in links:
        if 'healthfit100.com' not in l and 'fonts.googleapis' not in l and 'fonts.gstatic' not in l and 'schema.org' not in l:
            all_externals[l] += 1

print(f"Total external link references: {sum(all_externals.values())}")
print(f"Unique external links: {len(all_externals)}")
for k, v in all_externals.most_common():
    print(f"[{v} times] {k}")
