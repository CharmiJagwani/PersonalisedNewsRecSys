#!/usr/bin/env python
import feedparser
import re
import json
from jinja2 import Environment
from jinja2.loaders import FileSystemLoader

def render_template(data, template_name, filters=None):
    """Render data using a jinja2 template"""
    env = Environment(loader=FileSystemLoader(''))

    if filters is not None:
        for key, value in filters.iteritems():
            env.filters[key] = value

    template = env.get_template(template_name)
    return template.render(feed=data).encode('utf-8')

def main():
    feed = feedparser.parse('http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml')

    json = render_template(feed.entries, 'news.tmpl')


    with open('r2jop.py', 'wb') as output:
        output.write(json)
    output.close()

    my_file = open('r2jop.py', "r")
    data = my_file.read()

    for line in my_file:
        if 'title'in text:
            print("test")
            data1 = data.replace('"','')

    data1 = data.replace('\'','')
    data1 = data.replace('\\','')

    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', data1)
    my_file.close()

    with open('r2jop.py', 'w') as output:
        output.write(cleantext)
    output.close()


if __name__ == '__main__':
    main()
