# Adding and Maintaining Posts

All blog posts are stored in the `posts` directory.
Each blog post shall be it's own HTML file containing
the same template as the rest of the site.

The blog posts are to be hard coded so that they stand alone.
This will decrease load time and allow for some blog posts to
be plain text while others can contain images, videos, etc.

## Steps to Create a Post

To create a blog post you need to do the following:

1. Create an HTML file in the `posts` directory
2. Create an entry for that post in `posts/posts.js`

The blog tab will automatically render the title, date, and description
of each post according to the object in `posts/posts.js`.

If you want to work on a blog post and keep it invisible,
just don't include it in the posts object or comment out it's entry.

## Displaying Posts By Tag

Each post can have a number of tags attached to it.
Using the `paintPosts` method you can pass in a tag
and it will only render posts that have that tag.
