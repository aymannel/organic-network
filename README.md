# organic-network

![projectimage](img/network1.png)
![projectimage](img/network2.png)
![projectimage](img/network3.png)

## Description
organic-network is a Python script that scrapes [organic-chemistry.org](https://www.organic-chemistry.org) to return a list of all named reactions and the reactions they are related to. This link is then iterated over to create a collection of markdown files. These markdown files are created directly in my Obsidian vault allowing me to visualise the network of reactions. To be used as a revision resource.


## Aims
1. Interactive network map depicting relationship between most commonly used organic reactions.
2. Overlay 'chemical' nodes showing which reagents are associated with which reactions.
4. Each node contains an Anki tag so that card scheduling can be done from Obsidian.

## Notes
So far this has primarily been a scraping project. Scraping bot uses `requests` and `beautifulsoup4` as no active JavaScript present.