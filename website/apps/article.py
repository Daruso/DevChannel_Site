import datetime
from functools import singledispatch
from collections import abc
import html

import tinydb

db = tinydb.TinyDB('database/articles.json')


class Article:
    def __init__(self, author, text, publish_date=None):
        self.author = author
        self.text = text
        if publish_date is None:
            publish_date = str(datetime.datetime.now().date())
        self.publish_date = publish_date

    def __repr__(self):
        return str({'author': self.author, 'text': self.text, 'publish_date': self.publish_date})

    def body_to_html(self):
        html = ''
        for elem in self.text:
            html += htmlify(elem) + '\n'
        return html


@singledispatch
def htmlify(obj):
    return html.escape(repr(obj))


@htmlify.register(str)
def _(text):
    content = html.escape(text).replace('\n', '<br><br>\n')
    return '<p class="announcement">' + content + '</p>'


@htmlify.register(tuple)
@htmlify.register(abc.MutableSequence)
def _(seq):
    content = '</li>\n<li>'.join(htmlify(item) for item in seq)
    return '<ul>\n<li>{}</li>\n</ul>'.format(content)


def get_articles():
    return db.all()


def save_article(obj):
    db.insert(obj.__dict__)
