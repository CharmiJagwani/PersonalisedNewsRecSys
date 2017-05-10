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
    feed = feedparser.parse('http://www.hindustantimes.com/rss/india/rssfeed.xml')


    with open('myblog.txt', 'w') as outfile:
        for entry in feed.entries:
            ## Do your processing here
            content = entry.content[0].value
            clean_content = nltk.word_tokenize(nltk.html_clean(content))
            outfile.write(clean_content)

    json = render_template(feed.entries, 'news.tmpl')
    #entry.summary = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', feed.summary, flags=re.MULTILINE)
    #print entry.summary

    with open('yo1.py', 'wb') as output:
        output.write(json)
    output.close()

    my_file = open('yo1.py', "r")
    data = my_file.read()
    # data1 = data.replace('\'','')
    # data1 = data.replace('\\','')
    # with open('yo2.py', 'w') as yoyo:
    #     yoyo.write(data1)

    for line in my_file:
        # if 'summary' in text:
        #     print("hi")
        #     cleantext = re.sub(re.compile('<.*?>'), '', )
        if 'title'in text:
            print("test")
            data1 = data.replace('"','')

    data1 = data.replace('\'','')
    data1 = data.replace('\\','')

    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', data1)
    my_file.close()

    with open('yo1.py', 'w') as output:
        output.write(cleantext)
    output.close()

    # with open("yo.py") as inp:
    #     lines = inp.readlines()
    # inp.close()
    #
    # with open("yo.py", "w") as output:
    #     for line in lines:
    #         output.write(re.sub(r'"(\d+)"', r"\1", line))
    # output.close()



if __name__ == '__main__':
    main()
