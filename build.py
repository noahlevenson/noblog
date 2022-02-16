#!/usr/bin/python3

import os
import sys
import yaml
import datetime
from html.parser import HTMLParser

class TitleParser(HTMLParser):
  state = ""
  title = ""

  def handle_starttag(self, tag, attrs):
    self.state = tag

  def handle_data(self, data):
    if self.state == "title":
      self.title = data    
      self.state = ""

with open("config.yml", "r") as stream:
  cfg = yaml.safe_load(stream)

if not os.path.exists(f"{cfg['DIST']}"):
  print(f"Error: content path '{cfg['DIST']}' does not exist!")
  sys.exit()

posts = os.listdir(f"{cfg['DIST']}")

if "index.html" in posts:
  posts.remove("index.html")

posts_t = [{"post": p, "timestamp": None} for p in posts if 
  os.path.exists(f"{cfg['DIST']}/{p}/{cfg['PUB']}")]

for post in posts_t:
  with open(f"{cfg['DIST']}/{post['post']}/{cfg['PUB']}", "r") as stream:
    pub = yaml.safe_load(stream)
    post["timestamp"] = pub['TIMESTAMP']
    post["pin"] = pub["PIN"]

"""
posts_t is a list of regular posts, sorted by timestamp; we extract the pinned posts from that 
list and keep them in a list called pinned
"""
posts_t.sort(key=lambda x: x["timestamp"], reverse=True)
pinned = list(filter(lambda x: x["pin"] == True, posts_t))

for pinned_post in pinned:
  posts_t.remove(pinned_post)

with open(f"{cfg['DIST']}/index.html", "w") as index:
  index.write(f"<link rel=\"stylesheet\" href=\"style.css\"><title>{cfg['BLOG_TITLE']}</title><body id=\"index\"><table>")
  
  # Write all the pinned posts to the top
  for pinned_post in pinned:
    parser = TitleParser()

    with open(f"{cfg['DIST']}/{pinned_post['post']}/index.html", "r") as html:
      parser.feed(html.read())
    
    title = parser.title
    index.write("<tr>")
    index.write(f"<td>*</td>")
    index.write(f'<td><strong><a href="/{pinned_post["post"]}">{title}</a></strong></td>')
    index.write("</tr>")

  # Write all the regular posts below the pinned posts

  for post in posts_t:
    parser = TitleParser()

    with open(f"{cfg['DIST']}/{post['post']}/index.html", "r") as html:
      parser.feed(html.read())
    
    title = parser.title
    index.write("<tr>")
    index.write(f"<td>{datetime.date.fromtimestamp(int(post['timestamp'])).strftime('%m/%Y')}</td>")
    index.write(f'<td><a href="/{post["post"]}">{title}</a></td>')
    index.write("</tr>")

  index.write("</table></body>")

print(f"Built! ({len(posts_t)} posts, {len(pinned)} pinned)")
