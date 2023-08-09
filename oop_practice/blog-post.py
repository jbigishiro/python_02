class Blog:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)
        post.set_blog(self)

    def __str__(self):
        post_titles = ", ".join(post.title for post in self.posts)
        return f"Blog: {self.title} by {self.author}\nPosts: {post_titles}"

class Post:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.blog = None

    def set_blog(self, blog):
        self.blog = blog

    def __str__(self):
        return f"Post: {self.title}\nContent: {self.content}"

# Create blog instances
blog1 = Blog("Tech Blog", "John Doe")
blog2 = Blog("Travel Adventures", "Jane Smith")

# Create post instances
post1 = Post("Introduction to Python", "Python is a versatile programming language...")
post2 = Post("Exploring Paris", "The Eiffel Tower stands tall in the heart of the city...")

# Associate posts with blogs
blog1.add_post(post1)
blog2.add_post(post2)

# Print blog information along with posts
print(blog1)
print(post1)
print(blog2)
