#Using Beautiful Soup to Get Data from Zameen.com
#I'll only want Title, Area, Location, Price, Bedrooms, and Bathrooms

 from bs4 import BeautifulSoup
 import requests
 
website = requests.get('https://www.zameen.com/Homes/Multan-15-1.html')
print(website)

soup = BeautifulSoup(website.content, 'html.parser')
print(soup)

print(soup.prettify())
print(soup.text)
print(soup.h2)

h2tags = soup.find_all('h2')
for soups in h2tags:
 	print(soups)
     
     
id = soup.find(id = 'f343d9ce')

data = soup.find_all('div', class_ = 'f343d9ce')
print(data)

print(id.text)     
     
     
     