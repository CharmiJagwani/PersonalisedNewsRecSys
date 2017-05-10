# Import the necessary package to process data in JSON format
import HTMLParser
import re
try:
    import json
except ImportError:
    import simplejson as json

# We use the file saved from last step as example
tweets_filename = 'user_timeline_iamsrk.json'
tweets_file = open(tweets_filename, "r")
html_parser = HTMLParser.HTMLParser()
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
            temp=tweet['text']
            temp=html_parser.unescape(temp)
            temp=temp.decode("utf8").encode(‘ascii’,’ignore’)
            temp = " ".join([APPOSTOPHES[word] if word in APPOSTOPHES else word for word in temp.split()])
            temp= “ ”.join(re.findall(‘[A-Z][^A-Z]*’, temp))
            temp = multiwordReplace(temp, wordDic)
            temp= re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', temp, flags=re.MULTILINE)
            temp=''.join(''.join(s)[:2] for _, s in itertools.groupby(temp))
            obj= {u"id": tweet['id'], u"created_at": tweet['created_at'], u"text": tweet['text'], u"screen_name": tweet['user']['screen_name'], u"name": tweet['user']['name']}
            print json.dumps(obj, indent=4)
            #print tweet['id'] # This is the tweet's id
            #print tweet['created_at'] # when the tweet posted
            #print html_parser.unescape(tweet['text'].decode("utf8")) # content of the tweet
                        

    except:
        # read in a line is not in JSON format (sometimes error occured)
        continue