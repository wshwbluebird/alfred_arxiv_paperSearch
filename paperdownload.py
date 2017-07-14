#!/usr/local/bin/python
# encoding: utf-8


from bs4 import BeautifulSoup
import urllib2
import cookielib
import re
import alfred



import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def get_recent_posts(url):
    cookie = cookielib.CookieJar()
    handler = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(handler)
    response1 = opener.open(fullurl=url)
    source = response1.read()
    
    pre_url = 'https://arxiv.org'
    
    soup = BeautifulSoup(source, "lxml")
    precc = soup.find(id="dlpage")
    paper_list = precc.find_all('div',{'class':re.compile('list-title')})
    link_list = precc.find_all('a',{'title':re.compile('Download PDF')})
    
    
    
    
    feedback = alfred.Feedback()
    dd = min(len(paper_list),9)
    for i in range(dd):
        link = pre_url+link_list[i].get("href")
        name = paper_list[i].get_text()[7:]
        feedback.addItem(
                title=name,
                subtitle='press enter to enter this class',
                arg=link,
                autocomplete=link,
                icontype='filicon',
                icon="mood.png"
        )
    feedback.output()





def main():
    query = sys.argv[1]
    get_recent_posts(query)


if __name__ == "__main__":
    main()
