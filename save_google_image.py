'''------------------------------------------------------------------------------------------------------------------

#Author: Shivanshu Anant Suryakar
#github: www.github.com/jiminnpark
#email : shivanshusurya192@gmail.com

------------------------------------------------------------------------------------------------------------------'''
# -This doesn't download images, It actually convert images given in the webpage and then saves into your local directory

from bs4 import BeautifulSoup as bsoup 
from selenium import webdriver
from time import sleep
import requests
import base64

search=input("Enter the keywords you want to include:")
l=search.split(" ")
keywords="+".join(l)

search="https://www.google.com/search?tbm=isch&q="+keywords


browser=webdriver.Chrome()
sd=browser.get(search)
start=input("Has your page totally rendered?(Press enter)")
print("-------OK! Starting to generate images---------")
response=browser.page_source
soup=bsoup(response,features="lxml")

imgtags=soup.findAll('img')

urls=[img.get('src') for img in imgtags]
# print(urls)

base=list()
source=list()

for x in urls:
	if  "data:image/jpeg;base64," in str(x):
		base.append(bytes(str(x).replace("data:image/jpeg;base64,",""),'utf-8'))
	elif "http" in str(x):
		source.append(x)
	else:
		continue


count=0

for x in source:
	rex=requests.get(x)
	with open(str(count)+".jpg","wb") as f:
		f.write(rex.content)
	count+=1

for x in base:
	with open(str(count)+".jpg","wb") as f:
		try:
			f.write(base64.decodebytes(x))
		except:
			print("Exception occured: "+str(x))
	count+=1


print("-----------------Done------------------")

