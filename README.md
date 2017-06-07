# PersonalisedNewsRecSys

Steps to run the system : 
Start solr (with the correct core name which has to be mentioned in news.tmpl and check.py files)
python test.py <twitter_handle> (to generate tweets)
python rss2json.py (by changing rss link to extract news which will be saved according to the template file news.tmpl)
pyhton check.py (which has tweet cleaning code, solr update code as well as solr search code)

Steps to start solr : 
cd /opt
cd solr
bin/solr start

If an error occurs saying port 8983 is busy, run the following command : 
netstat -tunlp | grep 8983 (this will give you the pid of the process using the port)

Kill the process by :
kill <pid>
