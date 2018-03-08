#! /usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import (
    route, run, template, request, redirect
)

from scraputils import get_news
from db import News, session, save
from bayes import NaiveBayesClassifier


@route('/')
@route('/news')
def news_list():
    rows = s.query(News).filter(News.label == None).all()
    return template('news_template', rows=rows)


@route("/add_label/")
def add_label():
    label = request.query.label
    news_id = request.query.id
    row = s.query(News).filter(News.id == news_id).one()
    row.label = label
    s.commit()
    if request.query.classify == 'True':
        redirect('/classify')
    else:
        redirect('/news')


@route('/update')
def update_news():
    save(get_news('https://news.ycombinator.com/newest', 1))
    redirect('/')


@route('/classify')
def classify_news():
    recently_news_with_label = s.query(News).filter(News.title not in x_title and News.label != None).all()
    title_ex = [row.title for row in recently_news_with_label]
    label_ex = [row.label for row in recently_news_with_label]
    classifier.fit(title_ex, label_ex)
    news_without_label = s.query(News).filter(News.label == None).all()
    x = [row.title for row in news_without_label]
    labels = classifier.predict(x)
    for i in range(len(news_without_label)):
        news_without_label[i].label = labels[i]
    s.commit()
    classified_news = s.query(News).filter(News.label == 'good').all()
    return template('news_template', rows=classified_news)


if __name__ == "__main__":

	s = session()
	classifier = NaiveBayesClassifier()
	news_with_label = s.query(News).filter(News.label != None).all()
	x_title = [row.title for row in news_with_label]
	y_lable = [row.label for row in news_with_label]
	classifier.fit(x_title, y_lable)
    run(host="localhost", port=8080)
