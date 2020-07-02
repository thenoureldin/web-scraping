import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')
links = soup.select('.storylink')
links2 = soup2.select('.storylink')
subtext = soup.select('.subtext')
subtext2 = soup2.select('.subtext')
mega_links = links + links2
mega_subtext = subtext + subtext2

def sort_stories(hnlist):
    return sorted(hnlist, key=lambda x:x['votes'], reverse=True)


def create(links,subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points',''))
            if points > 99:
                hn.append({'title':title, 'link':href, 'votes':points})
    return sort_stories(hn)

pprint.pprint(create(mega_links,mega_subtext))