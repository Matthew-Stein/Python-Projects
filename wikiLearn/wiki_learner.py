#! python3
#This is designed to scrape a random wikipedia article, scrape the 
#intro and abstract as well as the link, and display to me at login. 
import os
os.getcwd()
os.chdir(r"C:\Users\Matthew\Documents\GitHub\Python-Projects\wikiLearn")
os.getcwd()

# https://en.wikipedia.org/wiki/Special:Random
import wikipedia
def random_page():
   random = wikipedia.random(1)
   try:
       result = wikipedia.page(random)
   except wikipedia.exceptions.DisambiguationError as e:
       result = random_page()
   print('\033[1m' + result.title + '\033[0m \n')
   print(result.summary + '\n')
   print(result.url)
            
random_page()





