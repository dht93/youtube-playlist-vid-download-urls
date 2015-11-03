# youtube-playlist-vid-download-urls
Python script to collect downloadable urls for all the videos in a YT playlist

Libraries used:
- Beautiful Soup
http://www.crummy.com/software/BeautifulSoup/
- PyQt4
https://wiki.python.org/moin/PyQt4


A python program to retrieve download links for each video in a Youtube playlist. A simple scrape first gets the urls for each video. These links are then turn-by-turn plugged in to the video download service 'savefrom.net'. Since the webpage of 'savefrom.net' is a Javascript rendered page, 'PyQt4' Webkit browser engine is used to render the page. The download links are then extracted from the rendered html.
