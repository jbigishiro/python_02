class Author:
    def __init__(self, name):
        self.name = name
        self.posts = []

    def create_post(self, title, content):
        post = Post(title, content, self)
        self.posts.append(post)
        return post

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

# Create author instances
author1 = Author("John Doe")
author2 = Author("Jane Smith")

# Create posts
post1 = author1.create_post("Introduction to Python", "Python is a versatile programming language.")
post2 = author1.create_post("Object-Oriented Programming", "OOP is a key concept in software development.")
post3 = author2.create_post("Web Development Basics", "Learn about HTML, CSS, and JavaScript.")

# Print author and post information
for author in [author1, author2]:
    print(f"Author: {author.name}")
    if author.posts:
        print("Posts:")
        for post in author.posts:
            print(f"- {post.title}: {post.content}")
    else:
        print("No posts by this author\n")

    print()
