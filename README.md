noblog is a static blog framework that's almost like having no static blog framework at all. It 
accomplishes things using POSIX utilities and file permissions, like your father and his father 
before him.

Instructions:

1. Initialize a new blog with `init.py`. 

2. Create a new unpublished post with `new.py [relative URL] [title for post]`.

3. Edit your unpublished post as HTML.

4. Publish a post with `pub.py [relative URL]`.

5. Rebuild the index with `build.py`.

To delete a post, just rm -rf its directory and rebuild. To edit a post, just edit its HTML and 
rebuild. To modify a post's URL, just rename its directory and rebuild. You can't unpublish a post 
yet, but maybe I'll add that soon.
