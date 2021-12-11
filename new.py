#!/usr/bin/python3

import sys
import os
import yaml
import subprocess

if len(sys.argv) < 3:
  print("Usage: new.py [relative URL] [title for post]")
  sys.exit()

url = sys.argv[1]
title = " ".join(sys.argv[2:])

with open("config.yml", "r") as stream:
  cfg = yaml.safe_load(stream)

path = f"{cfg['DIST']}/{url}"

if not os.path.exists(f"./{cfg['DIST']}"):
  print(f"Error: content path '{cfg['DIST']}' does not exist!")
  sys.exit()

if os.path.exists(f"./{cfg['DIST']}/{url}"):
  print(f"Error: relative URL /{url} is already taken!")
  sys.exit()

print(f"Adding '{title}' as /{url}...");
os.mkdir(f"{cfg['DIST']}/{url}")

with open(f"{cfg['TEMPLATE']}", "r") as template:
  titled = template.read().replace(cfg['TITLE'], title)

with open(f"{path}/index.html", "w") as index:
  index.write(titled)

subprocess.call(["chmod", "700", f"./{path}"])
print(f"New unpublished post: /{url}")
