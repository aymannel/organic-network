from bs4 import BeautifulSoup, SoupStrainer
import pandas as pd
import requests
import logging
import os
import re

logging.basicConfig(level=logging.INFO, format='(%(levelname)-s) %(asctime)s %(message)s', datefmt='%d-%m %H:%M:%S')

class ReactionScraper:
    def __init__(self):
        if os.path.exists('source.html'):
            logging.info('Page source via "source.html"')

            with open('source.html') as file:
                self.soup = BeautifulSoup(file.read(), 'lxml', parse_only=SoupStrainer('a'))
        else:
            logging.info('Page source via requests')
            rq = requests.get('https://www.organic-chemistry.org/namedreactions/')

            try:
                assert rq.status_code == 200
                logging.info('HTTP request successful')
                
                self.soup = BeautifulSoup(rq.text, 'lxml', parse_only=SoupStrainer('a'))
                with open('source.html', 'w') as file:
                    file.write(rq.text)
            except:
                logging.error('HTTP request unsuccessful')
                pass

        self.get_reactions()

#    if link.has_attr('href'):
#        print(link['href'])


    def get_reactions(self):
        self.reactions = dict()

        for link in self.soup.select('a[href*=shtm]'):
#            link_stripped = '\t'.join([line.strip() for line in link.text])

            link_text = link.text.strip()
            if len(link_text.splitlines()) == 1:
                self.reactions[link_text] = link['href']
            else:
                reaction = ' '.join([line.strip() for line in link_text.splitlines()])
                self.reactions[reaction] = link['href']
    
rxn = ReactionScraper()
rxn.get_reactions()
