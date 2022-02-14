#!/usr/bin/python3

import sys
import os
import yaml
import shutil
import subprocess

with open("config.yml", "r") as stream:
  cfg = yaml.safe_load(stream)

if os.path.exists(f"{cfg['DIST']}"):
  print(f"Error: content path '{cfg['DIST']}' exists!")
  sys.exit()

os.mkdir(cfg["DIST"])
shutil.copyfile(cfg['POST_CSS'], f"{cfg['DIST']}/{cfg['POST_CSS']}")
shutil.copyfile(cfg['INDEX_CSS'], f"{cfg['DIST']}/{cfg['INDEX_CSS']}")
subprocess.call([f"./{cfg['NEW']}", "test-post", "Test post"])
subprocess.call([f"./{cfg['PUBLISH']}", "test-post"])
subprocess.call([f"./{cfg['BUILD']}"])
print(f"Initialized new blog in '{cfg['DIST']}'")
