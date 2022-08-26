from bs4 import BeautifulSoup, SoupStrainer
import pandas as pd
import requests
import logging
import random
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

    def get_directory(self):
        self.directory = dict()
        
        for link in self.soup.select('a[href*=shtm]'):
            link_text = link.text.strip()

            if len(link_text.splitlines()) == 1:
                self.directory[link_text] = link['href']
            else:
                reaction = ' '.join([line.strip() for line in link_text.splitlines()])
                self.directory[reaction] = link['href']

    def get_network(self):
        self.network = dict()
        url = 'https://www.organic-chemistry.org/namedreactions/'
        
        for reaction in self.directory:
#        for i in range(50):
#            reaction = random.choice(list(self.directory.keys()))
            rq = requests.get(url + self.directory[reaction])
            try:
                assert rq.status_code == 200
                try:
                    soup = BeautifulSoup(rq.text, 'lxml')
                    container = soup.find(string='Related Reactions').parent.parent
                    related = [link.string.strip().strip('\n') for link in container.find_all('a')]
                    self.network[reaction] = [rel for rel in related if rel in self.directory]

                except AttributeError:
                    logging.info(f'{reaction} has no related reactions')
                    self.network[reaction] = list()
                    
            except AssertionError:
                logging.error('HTTP request unsuccessful')


    def build_network(self):
        path = '/Users/ayman/Documents/Obsidian/Chemistry/Organic/reactions/'
        with open('template.md') as file:
            template = file.read()

        for reaction, related in self.network.items():
            try:
                with open(path + f'{reaction}.md', 'w') as file:
                    content = template + '\n'.join(['- [[' + item + ']]' for item in related])
                    file.write(content)
                    logging.info("'" + reaction + ".md' created")
            except FileNotFoundError:
                logging.info(f"'{reaction}' doesn't make good filename")

rxn = ReactionScraper()
rxn.get_directory()
rxn.get_network()
rxn.build_network()
