"""Mục đích file này là để tạo table , cấu hình cols"""
from sqlalchemy import Column, Integer, String
# from sqlalchemy.orm import relationship
# from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from database import Base


class ContentTable(Base):
    __tablename__ = "content"

    id = Column(Integer, primary_key=True, index=True)
    hoten = Column(String, unique=False, index=True)
    email = Column(String, unique=True, index=True)
    topic = Column(String, unique=False, index=True)
    content = Column(String,unique=False, index=True)
