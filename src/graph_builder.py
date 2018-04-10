# Author Lucas Saraiva Ferreira

import csv
import os
import platform
import matplotlib.pyplot as plt
import networkx as nx
import country as ct
from networkx import Graph

from bs4 import BeautifulSoup
from urllib.request import urlopen


def scrape_wiki(url, G):
    html = urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    table_classes = {"class": ["wikitable"]}
    wikitables = soup.findAll("table", table_classes)

    for index, table in enumerate(wikitables):            
        convert_table_to_graph(table, G)


def convert_table_to_graph(table, G):
    saved_rowspans = []       

    for row in table.findAll("tr"):
        cells = row.findAll(["th", "td"])

        
        if len(saved_rowspans) == 0:
            saved_rowspans = [None for _ in cells]
    
        elif len(cells) != len(saved_rowspans):
            for index, rowspan_data in enumerate(saved_rowspans):
                if rowspan_data is not None:
                  
                    value = rowspan_data['value']
                    cells.insert(index, value)

                    if saved_rowspans[index]['rows_left'] == 1:
                        saved_rowspans[index] = None
                    else:
                        saved_rowspans[index]['rows_left'] -= 1

    
        for index, cell in enumerate(cells):
            if cell.has_attr("rowspan"):
                if contains_word(cell["rowspan"], "width"):
                    rowspan_data = {
                            'rows_left': int("1"),
                            'value': cell,
                     }
                else:

                    rowspan_data = {
                        'rows_left': int(cell["rowspan"]),
                        'value': cell,
                    }

                if not index >= len(saved_rowspans):
                    saved_rowspans[index] = rowspan_data

        if cells:           

            cleaned = clean_data(cells)
       
            columns_missing = len(saved_rowspans) - len(cleaned)
            if columns_missing:
                cleaned += "MISSING" * columns_missing

            
            if  not any("Belligerents" in s for s in cleaned):               
                if len(cleaned) > 7:                      
                                                   
                        splittedAlly = cleaned[6].split('/')
                        splitedCombatent = cleaned[7].split('/')
                            
                        year_start = cleaned[3]
                        year_end = cleaned[4]
                        


                        for ally in splittedAlly:                   
                            ally = ally.strip()    
                            foundAlly = False                 
                            continent_ally = ""
                           
                            for i in range(len(ct.countries)):
                                if ally == ct.countries[i]["name"] :
                                    foundAlly = True                                      
                                    continent_ally = ct.countries[i]["continent"]

                            if not G.has_node(ally):
                                if ally.strip() and foundAlly:
                                    G.add_node(ally, continent = continent_ally)   

                            for enemy in splitedCombatent:                                    
                                enemy = enemy.strip()
                                foundEnemy= False 
                                continent_enemy = ""
                                for i in range(len(ct.countries)):
                                    if enemy == ct.countries[i]["name"]: 
                                        foundEnemy = True  
                                        continent_enemy = ct.countries[i]["continent"]                                    

                                if not G.has_node(enemy) and enemy.strip() and foundEnemy:                                       
                                    G.add_node(enemy,  continent = continent_enemy) 

                                if enemy.strip() and ally.strip() and foundEnemy and  foundAlly: 

                                    G.add_edge(ally, enemy, relation='-', year_start=year_start, 
                                    year_end = year_end,
                                 
                                    color="Red")


                        alliance = []
                        size = len(splittedAlly) - 1
                        for i in range(size):
                            foundAlly = False              
                            
                            for j in range(len(ct.countries)):
                                if splittedAlly[i].strip() == ct.countries[j]["name"]:   
                                    foundAlly = True 
                                    
                                       
                            if foundAlly and splittedAlly[i].strip():
                                alliance.append(splittedAlly[i])


                        aux_splittedAlly = alliance
                        size = len(alliance) - 1
                        for i in range(size): 
                             G.add_edge(alliance[i].strip(), aux_splittedAlly[i+1].strip(), relation = '+', year_start=year_start, 
                                    year_end = year_end,
                                     color="Green")

                        combatants = []
                        size = len(splitedCombatent) - 1  
                        for i in range(size):
                            foundEnemy = False            
                              
                            for j in range(len(ct.countries)):
                                if splitedCombatent[i] == ct.countries[j]["name"]:   
                                    foundEnemy = True    
                            if foundEnemy and splitedCombatent[i].strip():
                                combatants.append(splitedCombatent[i])

                        aux_splitedCombatent = combatants
                        size = len(combatants) - 1
                        for i in range(size): 
                             G.add_edge(combatants[i].strip(), aux_splitedCombatent[i+1].strip(), relation = '+', year_start=year_start, 
                                    year_end = year_end,
                                   color="Green")    


def contains_word(s, w):
    return (' ' + w + ' ') in (' ' + s + ' ')

def clean_data(row):

    cleaned_cells = []

    for cell in row:  
        references = cell.findAll("sup", {"class": "reference"})
        if references:
            for ref in references:
                ref.extract()
        sortkeys = cell.findAll("span", {"class": "sortkey"})
        if sortkeys:
            for ref in sortkeys:
                ref.extract()
     
        text_items = cell.findAll(text=True)
        no_footnotes = [text for text in text_items if text[0] != '[']
        
        cleaned = (
            ''.join(no_footnotes)  
            .replace('\xa0', ' ')  
            .replace('\n', ' / ')  
            .strip()
        )
        cleaned_cells += [cleaned]  

    return cleaned_cells