
  
  
import json 
  
# Opening JSON file 
f = open('data.json',) 
img = open('img',)
  
# returns JSON object as  
# a dictionary 
data = json.load(f) 
  
# Iterating through the json 
# list 
for i, z in data: 
    print('TITLE'+ i['title']) 
    print(i['brand']) 
    print(i['rating']) 
    print(i['colour']) 
    print(i['instock'])
    print(i['reviews']) 
    print(i['description']) 
 
    print('--------')
  
# Closing file 
f.close() 