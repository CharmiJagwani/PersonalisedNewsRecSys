# PersonalisedNewsRecSys

Steps to run the system : <br>
Start solr (with the correct core name which has to be mentioned in news.tmpl and check.py files) <br>
python generate_tweets.py <twitter_handle> (to generate tweets) <br>
python rss2json.py (by changing rss link to extract news which will be saved according to the template file news.tmpl) <br>
pyhton final.py (which has tweet cleaning code, solr update code as well as solr search code) <br>
<br>
Steps to start solr : <br>
cd /opt <br>
cd solr <br>
bin/solr start <br>
<br>
If an error occurs saying port 8983 is busy, run the following command : <br>
netstat -tunlp | grep 8983 (this will give you the pid of the process using the port) <br>
<br>
Kill the process by : <br>
kill <pid> <br>
