# Shape of War
Complex network of all international wars that happened in a time spam of 300 years.


Steps to accomplish this:

1. Get all interested links, in this case, all links that points to a page containing information about international wars
2. Remove the unnacessary links, for this work, only 1800 to 2017 were important
3. Scrape all the info from the tables (BeaufifulSoup has been used for this)
4. Clean and filter all the data that you collected (Brute force so far) 
5. Create the multigraph (NetworkX has been used for this)


The web scrape used here can scrape tables from wikipedia that use the "Wikitable" class on its table tag. It is not hard to modify the scrape function to scrape different html tags, but, the cleanning data function is very especific and should be deleted beforehand to use the algorithm in a different context.



![Imaget](https://image.ibb.co/gkWfWn/screenshot_170956.png)
## Metrics
Betwenness;
Overlap;
Assortativity;
Node degree Distribution;
Homophily;
Bridges;
Bridges Span;
Clustering;
Status balance (Only for signed social network from SNAP)
