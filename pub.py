#!/usr/bin/python3

import os
import sys
import yaml
import time
import subprocess

if len(sys.argv) < 2:
  print("Usage: pub.py [relative URL]")
  sys.exit()

url = sys.argv[1]

with open("config.yml", "r") as stream:
  cfg = yaml.safe_load(stream)

if not os.path.exists(f"{cfg['DIST']}"):
  print(f"Error: content path '{cfg['DIST']}' does not exist!")
  sys.exit()

path = f"{cfg['DIST']}/{url}"

if not os.path.exists(f"./{path}/index.html"):
  print(f"Error: No post found at {path}")
  sys.exit()

with open(f"{path}/{cfg['PUB']}", "w") as pub:
  pub.write(f"TIMESTAMP: {str(int(time.time()))}\n")

subprocess.call(["chmod", "755", f"./{path}"])
print(f"Published post: /{url}")
