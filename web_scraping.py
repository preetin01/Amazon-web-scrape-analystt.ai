from bs4 import BeautifulSoup
import requests       # to collect the data
import csv            # to convert the data frame to csv
import pandas as pd    # module pandas so we can play with the panel data

# container
# create a list to store the description
Product_URL=[]
Product_Name=[]
Product_Price=[]
Rating=[]
Reviews=[]


pages =list(range(1,21))
for page in pages:
    req=requests.get("https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_{}".format(page)).text

    Soup=BeautifulSoup(req,'html.parser')

    pdt_url=Soup.find_all('a',class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal')
    start_link='https://www.amazon.in/'
    for i in range(len(pdt_url)):
        Product_URL.append(start_link+pdt_url[i].text)
    len(Product_URL)

    pdt_name=Soup.find_all('span',class_='a-size-medium a-color-base a-text-normal')
    for i in range(len(pdt_name)):
        Product_Name.append(pdt_name[i].text)
    len(Product_Name)
    
    pdt_price=Soup.find_all('span',class_='a-price-whole')
    for i in range(len(pdt_price)):
        Product_Price.append(pdt_price[i].text)
    len(Product_Price)    
    
    pdt_rate=Soup.find_all('i',class_='a-icon a-icon-star-small a-star-small-4 aok-align-bottom')
    for i in range(len(pdt_rate)):
        Rating.append(pdt_rate[i].text)
    len(Rating)    
    
    reviews=Soup.find_all('span',class_='a-size-base s-underline-text')
    for i in range(len(reviews)):
        Reviews.append(reviews[i].text)
    len(Reviews) 
    
print(len(Product_URL))
print(len(Product_Name))
print(len(Product_Price))
print(len(Rating))
print(len(Reviews)) 

df = {'URL': Product_URL[1:10],'Name': Product_Name[1:10], 'Price': Product_Price[1:10], 'Rating': Rating[1:10], 'Reviews': Reviews[1:10]}
dataset = pd.DataFrame(data = df)

dataset.to_csv('Bags_Backpack.csv')

print(dataset)
