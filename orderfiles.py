import sys, os
from pathlib import Path
from operator import itemgetter

p = ''.join(sys.argv[1:])
if len(p) == 0:
    print('you must give a fully qualified directory path to process')
    exit()

files = list(Path(p).glob('*.MP4'))
if len(files) == 0:
    print('did not find any mp4 files')
    exit()

vids = []
for file in files:
    f = Path(file).stem
    if not f.startswith("GX"):
        print('expected filename to start with GX, but got {}'.format(f))
        exit()
    vids.append((
        f + '.MP4',
        int(f[2:4]),
        int(f[4:])
    ))

# sort by last number (series) then first number (order within series)
vids.sort(key=itemgetter(2,1))

for i, v in enumerate(vids):
    src = os.path.join(p, v[0])
    dest = os.path.join(p, str(i + 1) + '.MP4')
    print('{} => {}'.format(src, dest))
    os.rename(src, dest)
