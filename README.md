# PersonalisedNewsRecSys
Steps to run the system : <br>
1. Start solr (with the correct core name which has to be mentioned in news.tmpl and final.py files) <br>
2. python extract_tweets.py <twitter_handle> (to extract tweets from the twitter handle) <br>
3. python rss2json.py (by changing rss link to extract news which will be saved according to the template file news.tmpl) <br>
4. python final.py (which has tweet cleaning code, solr update code as well as solr search code) <br>
<br>
Steps to start solr : <br>
1. cd /opt <br>
2. cd solr <br>
3. bin/solr start <br>
<br>
If an error occurs saying port 8983 is busy, run the following command : <br>
netstat -tunlp | grep 8983 (this will give you the pid of the process using the port) <br>
<br>
Kill the process by : <br>
kill (process_id) <br>
