#! python3
#This is designed to scrape a random wikipedia article, grab the 
#intro and abstract as well as the link, and display to me at login. 
### Did not know about the Wikipedia API when i started this, didnt realise it would basically do all the work... 
   # Wasted a lot of time fiddling with trying to understand Html code. 
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





