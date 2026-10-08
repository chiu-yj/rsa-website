# -*- coding: utf-8 -*-
"""Generate responsive widths for site images.  python3 tools/images.py

Originals live in assets/img/work/ and assets/img/rsa/. Resized copies go to
<folder>/640, /960 and /1440 (only widths smaller than the original).
"""
import glob, os, json
from PIL import Image
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
WIDTHS = (640, 960, 1440)
manifest = {}
for folder in ('assets/img/work', 'assets/img/rsa'):
    for f in sorted(glob.glob(os.path.join(ROOT, folder, '*.webp'))):
        name = os.path.basename(f)
        im = Image.open(f).convert('RGB')
        rel = f'{folder}/{name}'
        entry = {'w': im.width, 'h': im.height, 'sizes': []}
        for w in WIDTHS:
            if w >= im.width:
                continue
            d = os.path.join(ROOT, folder, str(w))
            os.makedirs(d, exist_ok=True)
            out = os.path.join(d, name)
            r = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
            r.save(out, 'WEBP', quality=80, method=6)
            entry['sizes'].append(w)
        manifest[rel] = entry
with open(os.path.join(ROOT, 'tools', 'images.json'), 'w') as fh:
    json.dump(manifest, fh, indent=1, sort_keys=True)
print(len(manifest), 'images')
