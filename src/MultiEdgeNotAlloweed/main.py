# Author Lucas Saraiva Ferreira

import os
import shutil
import GrafoNormal as graph_builder
from urllib.request import urlopen
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import networkx as nx
from networkx import Graph

import re

try:
    shutil.rmtree('output')
except FileNotFoundError:
    pass

print("Openning Wikipedia link")
html = urlopen("https://en.wikipedia.org/wiki/Category:Lists_of_wars_by_date")
bsObj = BeautifulSoup(html, "html.parser")

t = open("testeLinks.txt", 'w')

linksList = []


for link in bsObj.find("div", {"aria-labelledby":"Lists_of_wars_by_date"}).findAll( "a", href=re.compile("^(/wiki/)((?!:).)*$") ):
    if 'href' in link.attrs: 
        t.write(str(link.attrs['href']) + "\n")
        linksList.append(str(link.attrs['href']))


G=nx.Graph()


 
i = 0
print("Processing LINKS...")

del linksList[0]
del linksList[0]
del linksList[0]

del linksList[len(linksList)-1]
for link in linksList:
	print("Srapping page "+ str(link))
	graph_builder.scrape_wiki(url="https://en.wikipedia.org"+link, G = G)
	print("Exporting graph builded so far...")
	nx.write_gexf(G, "graphs/graph_version"+str(i)+".gexf")
	i = i+1
	print("Exported\n\n")

print("Finished, now you may run analytics.py")


