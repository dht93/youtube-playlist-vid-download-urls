import urllib2
import sys
from bs4 import BeautifulSoup
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *

class Render(QWebPage):                                #Render class renders the web page
  def __init__(self, url):                             #QWebPage is the input URL of web page to scrape
    self.app = QApplication(sys.argv)
    QWebPage.__init__(self)
    self.loadFinished.connect(self._loadFinished)
    self.mainFrame().load(QUrl(url))
    self.app.exec_()

  def _loadFinished(self, result):
    self.frame = self.mainFrame()
    self.app.quit()

def extract_video_links(playlist_url):                 #simple scraper to extract video links from the youtube page
    u=urllib2.urlopen(playlist_url)
    data=u.read()
    soup=BeautifulSoup(data,"html.parser")

    anchors=soup.find_all('a','pl-video-title-link yt-uix-tile-link yt-uix-sessionlink  spf-link ')

    lst=[]

    for a in anchors:
        lst.append("https://www.youtube.com"+str(a['href']))

    down_links=[]

    for link in lst:
        splits=link.split('www.')
        new_link=splits[0]+"www.ss"+splits[1]
        down_links.append(new_link)

    return down_links

'''
def rendered_html(url):                                #selenium implementation. not rendering for some some reason
    conn=urllib2.urlopen(url)
    data=conn.read()
    conn.close()

    f_name="D:\Learn\Code\PY\Projects\YT Playlist\html.txt"
    f=open(f_name,'wt')
    f.write(data)
    f.close()

    browser=webdriver.Firefox()
    browser.get('file:///'+f_name)
    rendered_html=browser.page_source.encode("utf-8")
    browser.quit()
    return rendered_html
'''

def rendered_html(url):
    r = Render(url)
    result = r.frame.toHtml()                           #result is not a string to be processed with BeautifulSoup
    return str(result.toAscii())                        #conversion to string

def get_video_download_url(rendered_html):              #takes in rendered html which contains the download url
    soup=BeautifulSoup(rendered_html,'html.parser')
    down_tag=soup.find_all('a','link link-download subname ga_track_events download-icon')
    down_link=str(down_tag[0]['href'])
    return down_link

playlist_url="https://www.youtube.com/playlist?list=PL67C037B48F36748D"

vid_links=extract_video_links(playlist_url)

download_urls=[]

for vid_link in vid_links[:1]:                           #some error occuring when run for the entire vid_links list
    r_html=rendered_html(vid_link)                       #runs correctly for one vid_link
    download_urls.append(get_video_download_url(r_html)) #yet to be corrected
    print "got one"

f=open('links.txt','w')
for url in download_urls:
    f.write(url)
f.close()

print "done"
