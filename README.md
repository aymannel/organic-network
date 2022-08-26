# organic-network

![projectimage](img/network1.png)
![projectimage](img/network2.png)
![projectimage](img/network3.png)

## Description
organic-network is a Python script that scrapes [organic-chemistry.org](https://www.organic-chemistry.org) for all of its named reactions and the reactions they are related to. A collection of markdown files are generated directly into my Obsidian vault. It is then possible to visualise which reactions are related to each other. To be used as a revision resource.

## Features
- Interactive network map depicting relationship between named reactions from [organic-chemistry.org](https://www.organic-chemistry.org)
- Each node contains information about the reaction and links to its Anki cards

## Notes
So far this has primarily been a scraping project. Scraping bot uses `requests` and `beautifulsoup4` as no active JavaScript present.