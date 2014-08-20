from sqlalchemy import Column, Integer, String
from database import Base

class BlogPost(Base):
    __tablename__ = 'blog_posts'

    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    content = Column(String(120))

    def __init__(self, title=None, content=None):
      self.title = title
      self.content = content

    def __repr__(self):
      return '<BlogPost %r>' % (self.title)


