import uuid
import datetime
from .database.database import db


class Post:
    def __init__(self, blog_id, title, content, author, created_date=datetime.datetime.utcnow(), id=None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.created_date = created_date
        self.id = uuid.uuid4().hex if id is None else id

    def save_to_mongo(self):
        db.insert("posts", self.json())

    def json(self):
        return {
            "id": self.id,
            "blog_id": self.blog_id,
            "author": self.author,
            "content": self.content,
            "title": self.title,
            "created_date": self.created_date
        }

    @classmethod
    def from_mongo(cls, post_id):
        return db.find_one("posts", {"_id": post_id})

    @classmethod
    def from_blog(cls, blog_id):
        return [post for post in db.find("posts", {"blog_id": blog_id})]


