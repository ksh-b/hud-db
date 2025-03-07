import json
import subprocess

from pathlib import Path

data = Path("hud-data/")

huds = {}
for f in data.glob("*.json"):
  with open(f) as file:
    huds[f.stem] = json.load(file)

for hud_id, hud in huds.items():
  hud["hash"] = subprocess.check_output(["git", "ls-remote", hud["repo"], "HEAD"]).decode("utf-8").split()[0]

for hud_id, hud in huds.items():
  with open(data / f"{hud_id}.json", "w") as file:
    json.dump(hud, file, indent=2)
    file.write('\n')
