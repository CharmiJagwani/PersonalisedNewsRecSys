# Import the necessary package to process data in JSON format
#import HTMLParser
import nltk
import re
import itertools
import pysolr
import csv
import tkinter
import csv
from tkinter import *
from nltk.corpus import stopwords
solr = pysolr.Solr('http://localhost:8983/solr/cora', timeout=10)
try:
    import json
except ImportError:
    import simplejson as json
#nltk.download("stopwords")


# We use the file saved from last step as example
tweets_filename ='twitter_tweets.json'
tweets_file = open(tweets_filename, "r")

output_file = open('output_file.csv',"wt")
writer = csv.writer(output_file)
writer.writerow(('Tweets','News'))

#html_parser = HTMLParser.HTMLParser()
wordDic = {
'booster': 'rooster',
'rocket': 'pocket',
'solid': 'salted',
'tunnel': 'funnel',
'ship': 'slip'}

def multipleReplace(text, wordDic):
    """
    take a text and replace words that match the key in a dictionary
    with the associated value, return the changed text
    """
    for key in wordDic:
        text = text.replace(key, wordDic[key])
    return text


for line in tweets_file:
    try:
        # Read in one line of the file, convert it into a json object
        tweet = json.loads(line.strip())
        if 'text' in tweet: # only messages contains 'text' field is a tweet
            temp = tweet['text']

            temp = temp.decode('utf-8').encode('ascii','ignore')
            temp = re.sub(re.compile('<.*?>'), '', temp)                                                                                      #remove html tags
            temp = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', temp, flags=re.MULTILINE)                                       #remove url
            temp = ''.join(''.join(s)[:2] for _, s in itertools.groupby(temp))#standarize words
            temp = multipleReplace(temp, wordDic)#remove slang words
            temp = re.sub('(?!^)([A-Z][a-z]+)', r' \1', temp)#split attached words
            temp = ' '.join([word for word in temp.split() if word not in (stopwords.words('english'))])# remove stopwords

            results = solr.search(temp, rows=1)
            for result in results:
                print("News  '{0}'.".format(result['url']))
                writer.writerow((temp,result['url']))

    except:
        # read in a line is not in JSON format (sometimes error occured)
        continue
output_file.close()

root = tkinter.Tk()
root.title("Personalised News Recommender System")
file_ops = open("output_file.csv","r")
reader = csv.reader(file_ops)

   # r and c tell us where to grid the labels
r = 0
for col in reader:
    c = 0
    for row in col:
         # i've added some styling
        label = tkinter.Label(root, width = 100, height = 2,padx = 2, \
                               text = row, relief = tkinter.RIDGE)
        label.grid(row = r, column = c)
        c += 1
    r += 1

root.mainloop()
