#! /usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


base = declarative_base()
engine = create_engine("sqlite:///news.db")
session = sessionmaker(bind=engine)


class News(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    url = Column(String)
    comments = Column(String)
    points = Column(Integer)
    label = Column(String)


# создаём базу данных
Base.metadata.create_all(bind=engine)


# функция, которая будет сохранять собранные новости в базу данных
def save(pre_base):
    s = session() # начинаем сессию
    rows = s.query(News).filter(News.label == None).all() # собираем все новости, не имеющие лейбла
    bd_labels = []
    for row in rows: # добавляем все заголовки новостей без лейблов
        bd_labels.append(row.title)
    for current_new in pre_base: # для текущих параметров новости создаём запись в базу данных
        if current_new['title'] not in bd_labels:
            news = News(title=current_new['title'],
                        author=current_new['author'],
                        url=current_new['url'],
                        points=current_new['points'],
                        comments=current_new['comments'])
            s.add(news) # добавляем в таблицу news
    s.commit() # делаем коммит сессии, то есть подтверждаем все изменения
