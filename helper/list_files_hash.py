import os
import hashlib

for x in os.listdir('.'):
    md5 = hashlib.md5()
    with open(x, 'r', encoding='utf-8') as f:
        md5.update(f.read().encode('utf-8'))
        print('%-60s%s' % (x, md5.hexdigest()))
