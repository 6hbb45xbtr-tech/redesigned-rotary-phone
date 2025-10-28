# Drop links (one per line) in urls.txt, then run:
#   python rip_crate.py
import os, subprocess, sys
outdir = 'tracks'; os.makedirs(outdir, exist_ok=True)
urls_file = 'urls.txt'
if not os.path.exists(urls_file):
  print("Add your links to urls.txt (one per line)."); sys.exit(1)
with open(urls_file) as f:
  urls=[u.strip() for u in f if u.strip()]
for url in urls:
  print("Ripping:", url)
  cmd=['yt-dlp','-x','--audio-format','mp3','-o',f'{outdir}/%(title)s.%(ext)s',url]
  subprocess.run(cmd)
print("Done. MP3s in ./tracks")