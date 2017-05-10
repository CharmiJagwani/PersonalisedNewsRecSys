# -*- coding: utf-8 -*-
from __future__ import print_function
import pysolr
import json
# Setup a Solr instance. The timeout is optional.
solr = pysolr.Solr('http://localhost:8983/solr/cora', timeout=10)

data=[
        
        {
            "url": "http://www.bbc.co.uk/news/entertainment-arts-39703764",
            "id": "http://www.bbc.co.uk/news/entertainment-arts-39703764",
            "published": "Tue, 25 Apr 2017 13:40:32 GMT",
            "summary_detail": "{'base': u'http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml', 'type': u'text/html', 'value': u'Zoe Saldana appears to let the cat out of the bag at Guardians of the Galaxy Vol. 2 premiere.', 'language': None}",
            "title": "Exclusive: Has Zoe Saldana revealed Avengers 4 title?"
        },
        
        {
            "url": "http://www.bbc.co.uk/news/entertainment-arts-39710409",
            "id": "http://www.bbc.co.uk/news/entertainment-arts-39710409",
            "published": "Tue, 25 Apr 2017 16:55:50 GMT",
            "summary_detail": "{'base': u'http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml', 'type': u'text/html', 'value': u'Hollywood blockbuster star Will Smith is also joined by fellow US star, Jessica Chastain.', 'language': None}",
            "title": "Will Smith joins Cannes film festival jury"
        },
        
        {
            "url": "http://www.bbc.co.uk/news/entertainment-arts-39703980",
            "id": "http://www.bbc.co.uk/news/entertainment-arts-39703980",
            "published": "Tue, 25 Apr 2017 13:06:53 GMT",
            "summary_detail": "{'base': u'http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml', 'type': u'text/html', 'value': u"New figures from the music industry show that Beyonce's Lemonade was last year's best-selling album.", 'language': None}",
            "title": "Beyonce actually outsold Drake in 2016"
        },
        
        {
            "url": "http://www.bbc.co.uk/news/uk-england-london-39703528",
            "id": "http://www.bbc.co.uk/news/uk-england-london-39703528",
            "published": "Tue, 25 Apr 2017 14:31:26 GMT",
            "summary_detail": "{'base': u'http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml', 'type': u'text/html', 'value': u'The Hollywood star detained the teenage rider after he jumped a red light and crashed into a car.', 'language': None}",
            "title": "Tom Hardy 'arrests fleeing motorbike thief' in London"
        },
        
        {
            "url": "http://www.bbc.co.uk/news/entertainment-arts-39704113",
            "id": "http://www.bbc.co.uk/news/entertainment-arts-39704113",
            "published": "Tue, 25 Apr 2017 11:08:57 GMT",
            "summary_detail": "{'base': u'http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml', 'type': u'text/html', 'value': u'The actress tells the Nightly News how she wished she had been able to make things all right on the night.', 'language': None}",
            "title": "Faye Dunaway feels 'very guilty' over Oscars blunder"
        },
        
        {
            "url": "http://www.bbc.co.uk/news/entertainment-arts-39700952",
            "id": "http://www.bbc.co.uk/news/entertainment-arts-39700952",
            "published": "Tue, 25 Apr 2017 07:59:27 GMT",
            "summary_detail": "{'base': u'http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml', 'type': u'text/html', 'value': u'He is recovering after falling violently ill on tour and spending two nights in intensive care.', 'language': None}",
            "title": "Elton John had potentially deadly infection"
        },
        
        {
            "url": "http://www.bbc.co.uk/news/uk-39710121",
            "id": "http://www.bbc.co.uk/news/uk-39710121",
            "published": "Tue, 25 Apr 2017 17:46:27 GMT",
            "summary_detail": "{'base': u'http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml', 'type': u'text/html', 'value': u'Dozens of celebrities including Kevin Keegan and Patsy Kensit have settled for undisclosed sums.', 'language': None}",
            "title": "Mirror Group settles phone-hacking claims"
        },
        
        {
            "url": "http://www.bbc.co.uk/newsbeat/articles/39705244",
            "id": "http://www.bbc.co.uk/newsbeat/articles/39705244",
            "published": "Tue, 25 Apr 2017 11:43:33 GMT",
            "summary_detail": "{'base': u'http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml', 'type': u'text/html', 'value': u'Guardians of the Galaxy Vol.2 is out this week and Miley Cyrus is in it.', 'language': None}",
            "title": "Miley Cyrus features in Guardians of the Galaxy Vol. 2"
        },
        
        {
            "url": "http://www.bbc.co.uk/news/entertainment-arts-39627759",
            "id": "http://www.bbc.co.uk/news/entertainment-arts-39627759",
            "published": "Tue, 25 Apr 2017 12:12:44 GMT",
            "summary_detail": "{'base': u'http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml', 'type': u'text/html', 'value': u'He was best known for writing Zen and the Art of Motorcycle Maintenance.', 'language': None}",
            "title": "Robert Pirsig: Zen and the Art of Motorcycle Maintenance author dies"
        },
        
        {
            "url": "http://www.bbc.co.uk/news/entertainment-arts-39692931",
            "id": "http://www.bbc.co.uk/news/entertainment-arts-39692931",
            "published": "Mon, 24 Apr 2017 17:03:11 GMT",
            "summary_detail": "{'base': u'http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml', 'type': u'text/html', 'value': u"As Bananarama's original line-up get back together, what other 80s bands would we like to see reunite?", 'language': None}",
            "title": "Seven bands from the 80s we wish would reunite"
        },
        
        {
            "url": "http://www.bbc.co.uk/news/entertainment-arts-39696450",
            "id": "http://www.bbc.co.uk/news/entertainment-arts-39696450",
            "published": "Mon, 24 Apr 2017 16:53:53 GMT",
            "summary_detail": "{'base': u'http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml', 'type': u'text/html', 'value': u"A photo of the pair sparks a film idea by fans on Twitter and they both say they're up for it.", 'language': None}",
            "title": "Rihanna and Lupita Nyong'o movie conjured up on Twitter"
        },
        
        {
            "url": "http://www.bbc.co.uk/news/entertainment-arts-38979384",
            "id": "http://www.bbc.co.uk/news/entertainment-arts-38979384",
            "published": "Tue, 25 Apr 2017 09:33:11 GMT",
            "summary_detail": "{'base': u'http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml', 'type': u'text/html', 'value': u'Apple have delayed the series, but judging by the trailer, it will be worth waiting for.', 'language': None}",
            "title": "Carpool Karaoke: Eight things to expect from the new series"
        },
        
        {
            "url": "http://www.bbc.co.uk/news/entertainment-arts-39691637",
            "id": "http://www.bbc.co.uk/news/entertainment-arts-39691637",
            "published": "Mon, 24 Apr 2017 18:24:27 GMT",
            "summary_detail": "{'base': u'http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml', 'type': u'text/html', 'value': u"Maylis de Kerangal's novel tells the story of a human heart which is donated after an accident.", 'language': None}",
            "title": "Wellcome Prize won by 'heart-breaking' transplant novel"
        },
        
        {
            "url": "http://www.bbc.co.uk/news/entertainment-arts-39693849",
            "id": "http://www.bbc.co.uk/news/entertainment-arts-39693849",
            "published": "Mon, 24 Apr 2017 14:23:18 GMT",
            "summary_detail": "{'base': u'http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml', 'type': u'text/html', 'value': u'After the success of Tom Hardy, Chris Evans is the latest movie star to read a CBeebies story.', 'language': None}",
            "title": "Captain America Chris Evans to read CBeebies bedtime story"
        },
        
        {
            "url": "http://www.bbc.co.uk/news/entertainment-arts-39691240",
            "id": "http://www.bbc.co.uk/news/entertainment-arts-39691240",
            "published": "Mon, 24 Apr 2017 08:04:15 GMT",
            "summary_detail": "{'base': u'http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml', 'type': u'text/html', 'value': u'Keren, Sara and Siobhan get back together for the first time since 1988, announcing a one-off tour.', 'language': None}",
            "title": "Original Bananarama line-up reunite for first ever tour"
        },
        
        {
            "url": "http://www.bbc.co.uk/news/entertainment-arts-39709620",
            "id": "http://www.bbc.co.uk/news/entertainment-arts-39709620",
            "published": "Tue, 25 Apr 2017 14:14:29 GMT",
            "summary_detail": "{'base': u'http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml', 'type': u'text/html', 'value': u'Hollywood actress Zoe Saldana reveals why she nearly turned down her latest film role.', 'language': None}",
            "title": "Why Zoe Saldana almost turned down Guardians of the Galaxy"
        },
        
        {
            "url": "http://www.bbc.co.uk/news/uk-england-birmingham-39707829",
            "id": "http://www.bbc.co.uk/news/uk-england-birmingham-39707829",
            "published": "Tue, 25 Apr 2017 12:31:26 GMT",
            "summary_detail": "{'base': u'http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml', 'type': u'text/html', 'value': u'"Hundreds" of fans were left outside the star's gig venue because of ticketing problems.', 'language': None}",
            "title": "Bruno Mars fans blast Birmingham show ticket 'farce'"
        },
        
        {
            "url": "http://www.bbc.co.uk/news/entertainment-arts-39672573",
            "id": "http://www.bbc.co.uk/news/entertainment-arts-39672573",
            "published": "Fri, 21 Apr 2017 15:23:53 GMT",
            "summary_detail": "{'base': u'http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml', 'type': u'text/html', 'value': u"The Duke and Duchess of Cambridge surprise Radio 1's Adele Roberts ahead of her marathon run.", 'language': None}",
            "title": "Prince William: 'I text Radio 1 for shoutouts'"
        },
        
        {
            "url": "http://www.bbc.co.uk/news/39683315",
            "id": "http://www.bbc.co.uk/news/39683315",
            "published": "Sun, 23 Apr 2017 04:27:04 GMT",
            "summary_detail": "{'base': u'http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml', 'type': u'text/html', 'value': u'Nafisah Baba, a 20-year-old dancer from London, has won the BBC Young Dancer 2017 Prize.', 'language': None}",
            "title": "Nafisah Baba wins BBC Young Dancer 2017 Prize"
        },
        
        {
            "url": "http://www.bbc.co.uk/news/entertainment-arts-39659562",
            "id": "http://www.bbc.co.uk/news/entertainment-arts-39659562",
            "published": "Thu, 20 Apr 2017 15:57:03 GMT",
            "summary_detail": "{'base': u'http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml', 'type': u'text/html', 'value': u"The rapper's new video has been released, parts of which were filmed a day before March's attack.", 'language': None}",
            "title": "Nicki Minaj video filmed on Westminster Bridge"
        },
        
        {
            "url": "http://www.bbc.co.uk/news/uk-39635066",
            "id": "http://www.bbc.co.uk/news/uk-39635066",
            "published": "Wed, 19 Apr 2017 09:20:12 GMT",
            "summary_detail": "{'base': u'http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml', 'type': u'text/html', 'value': u'Musicians around the world rally to raise money for trombonist who has cancer.', 'language': None}",
            "title": "Trombones play the same tune for charity"
        },
        
        {
            "url": "http://www.bbc.co.uk/newsbeat/articles/39712369",
            "id": "http://www.bbc.co.uk/newsbeat/articles/39712369",
            "published": "Tue, 25 Apr 2017 16:46:14 GMT",
            "summary_detail": "{'base': u'http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml', 'type': u'text/html', 'value': u'The singer will give young women the chance to study the creative arts, music, literature and African-American studies.', 'language': None}",
            "title": "Beyonce to offer US college scholarships to female students"
        },
        
        {
            "url": "http://www.bbc.co.uk/news/uk-england-birmingham-39703363",
            "id": "http://www.bbc.co.uk/news/uk-england-birmingham-39703363",
            "published": "Tue, 25 Apr 2017 11:33:47 GMT",
            "summary_detail": "{'base': u'http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml', 'type': u'text/html', 'value': u'Ticket problem leaves hundreds of fans waiting for hours in queue.', 'language': None}",
            "title": "Bruno Mars fans' anger at missing Barclaycard Arena gig"
        },
        
        {
            "url": "http://www.bbc.co.uk/news/entertainment-arts-39691580",
            "id": "http://www.bbc.co.uk/news/entertainment-arts-39691580",
            "published": "Mon, 24 Apr 2017 11:18:59 GMT",
            "summary_detail": "{'base': u'http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml', 'type': u'text/html', 'value': u'Viewers and critics react positively to the latest series, fronted by the former Friends actor.', 'language': None}",
            "title": "Top Gear: Has Matt LeBlanc saved the series?"
        },
        
        {
            "url": "http://www.bbc.co.uk/news/entertainment-arts-39665367",
            "id": "http://www.bbc.co.uk/news/entertainment-arts-39665367",
            "published": "Sat, 22 Apr 2017 23:50:31 GMT",
            "summary_detail": "{'base': u'http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml', 'type': u'text/html', 'value': u'America is "a beautiful but dangerous place," says Ray Davies, as he discusses his new album.', 'language': None}",
            "title": "To Ray Davies, America is a 'beautiful but dangerous' place"
        },
        
        {
            "url": "http://www.bbc.co.uk/news/entertainment-arts-39592206",
            "id": "http://www.bbc.co.uk/news/entertainment-arts-39592206",
            "published": "Sat, 22 Apr 2017 00:49:23 GMT",
            "summary_detail": "{'base': u'http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml', 'type': u'text/html', 'value': u"The eight-week entertainment show didn't get off to the strongest start but after ending more positively does it just need a second chance?", 'language': None}",
            "title": "Was ITV's The Nightly Show a success?"
        },
        
        {
            "url": "http://www.bbc.co.uk/news/entertainment-arts-39632898",
            "id": "http://www.bbc.co.uk/news/entertainment-arts-39632898",
            "published": "Wed, 19 Apr 2017 23:47:12 GMT",
            "summary_detail": "{'base': u'http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml', 'type': u'text/html', 'value': u'The music world lost an icon on 21 April 2016. Here are some of the things we discovered about Prince after he died.', 'language': None}",
            "title": "Prince: 12 things we've learned since his death"
        },
        
        {
            "url": "http://www.bbc.co.uk/news/in-pictures-39628370",
            "id": "http://www.bbc.co.uk/news/in-pictures-39628370",
            "published": "Thu, 20 Apr 2017 23:53:54 GMT",
            "summary_detail": "{'base': u'http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml', 'type': u'text/html', 'value': u'Belgian photographer Frederik Buyckx has been named the Sony World Photography Awardsu2019 2017 Photographer of the Year for his series of snow-covered landscapes.', 'language': None}",
            "title": "World Photography Award winners"
        },
        
        {
            "url": "http://www.bbc.co.uk/news/entertainment-arts-39623148",
            "id": "http://www.bbc.co.uk/news/entertainment-arts-39623148",
            "published": "Wed, 19 Apr 2017 06:39:33 GMT",
            "summary_detail": "{'base': u'http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml', 'type': u'text/html', 'value': u"New York's Tribeca Film Festival is making a big fuss of the immersive movie experience but is this really what audiences now want?", 'language': None}",
            "title": "Is 2017 the year of virtual reality film-making?"
        },
        
        {
            "url": "http://www.bbc.co.uk/news/entertainment-arts-39628619",
            "id": "http://www.bbc.co.uk/news/entertainment-arts-39628619",
            "published": "Tue, 18 Apr 2017 14:19:26 GMT",
            "summary_detail": "{'base': u'http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml', 'type': u'text/html', 'value': u"The 2001 compilation album saw sales surge after appearing in Peter Kay's Car Share - but why?", 'language': None}",
            "title": "What's so great about Now That's What I Call Music 48?"
        },
        
        {
            "url": "http://www.bbc.co.uk/news/entertainment-arts-39619840",
            "id": "http://www.bbc.co.uk/news/entertainment-arts-39619840",
            "published": "Mon, 17 Apr 2017 11:57:20 GMT",
            "summary_detail": "{'base': u'http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml', 'type': u'text/html', 'value': u'It had the strongest worldwide opening weekend in film history, estimates suggest.', 'language': None}",
            "title": "Why are the Fast & Furious films so popular?"
        },
        
        {
            "url": "http://www.bbc.co.uk/news/entertainment-arts-39477851",
            "id": "http://www.bbc.co.uk/news/entertainment-arts-39477851",
            "published": "Sun, 16 Apr 2017 23:51:17 GMT",
            "summary_detail": "{'base': u'http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml', 'type': u'text/html', 'value': u'S-Town and Serial might be hits, but will listening to podcasts ever be more than a niche pursuit?', 'language': None}",
            "title": "Why podcasts are struggling to catch on"
        },
        
        {
            "url": "http://www.bbc.co.uk/news/entertainment-arts-39579270",
            "id": "http://www.bbc.co.uk/news/entertainment-arts-39579270",
            "published": "Fri, 14 Apr 2017 00:03:57 GMT",
            "summary_detail": "{'base': u'http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml', 'type': u'text/html', 'value': u'From John Cleese to Charlie Chaplin - when celebrities make a U-turn.', 'language': None}",
            "title": "Never say never again: When celebrities eat their words"
        },
        
        {
            "url": "http://www.bbc.co.uk/news/magazine-39592281",
            "id": "http://www.bbc.co.uk/news/magazine-39592281",
            "published": "Sun, 16 Apr 2017 23:57:22 GMT",
            "summary_detail": "{'base': u'http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml', 'type': u'text/html', 'value': u'Outspoken Hollywood actor Shia LaBeouf has been the target of trolls - congregating on anonymous websites - ever since his anti-Trump performance art project began in January.', 'language': None}",
            "title": "How trolls pursued a Hollywood star to Finland"
        },
        
        {
            "url": "http://www.bbc.co.uk/news/entertainment-arts-39588040",
            "id": "http://www.bbc.co.uk/news/entertainment-arts-39588040",
            "published": "Thu, 13 Apr 2017 11:56:04 GMT",
            "summary_detail": "{'base': u'http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml', 'type': u'text/html', 'value': u'The US comedian, who found fame two decades after his brother Eddie, has died at the age of 57.', 'language': None}",
            "title": "Charlie Murphy: Seven things about the comedy star's life"
        },
        
	]

solr.add(data)