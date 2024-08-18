# Amazon Web Scraping Using Python #

# Imports the necessary libraries

from bs4 import BeautifulSoup
import requests
import time
import datetime
import csv
import pandas as pd

# Stores a URL in the variable 'URL'
URL = 'https://www.amazon.co.uk/explaining-right-Funny-Analyst-T-Shirt/dp/B08XYL6GRM/ref=sr_1_2?crid=3HLQ1FSN477GA&dib=eyJ2IjoiMSJ9.uo1ZKoIvETOJEhK0t0YddYhQlUqn15Izn7BFt_NMv7_VymlwueQbUtl5b_D-Mxzf_aAdL_o_QvBzTK7Q2HrhNecmiN050M1I2SO-QOYwxc5W3BKZe5y6UyozlOwh_MIhKGHEUTGEF3HuzOXwKYauTw7pmbB2-L3VI47oGOXfU17CyQZl_RykEncXKYBwdoh-eHzFssj5F7Aw1fZK9ryMK8E5ts8jNyTuiZTDJsaw_tRDnDJfw3XpmpEdR4_7iEAyY2A_fLPenvJ4slg8vEPhLLZfwPcH17WSu4GOQaMqVjs.rDaHonMaAc2uy-zrs025TRT4N7juCz9eQWDqnrHgohM&dib_tag=se&keywords=funny+data+analyst+shirt&qid=1723971685&sprefix=funny+data+analyst+shirt%2Caps%2C93&sr=8-2'

# Assigns the HTTP headers in the form of key:value pairs (obtained from httpbin.org/get) in the variable 'headers'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36', 'Accept-Encoding':'gzip, deflate, br, zstd', 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'DNT':'1','Connection':'close', 'Upgrade-Insecure-Requests':'1'}

# Stores the result of using the 'GET' method in the variable 'page'
page = requests.get(URL, headers = headers)

# Stores the result of the 'CONTENT' method in the variable 'soup1'
soup1 = BeautifulSoup(page.content, 'html.parser')

# Stores the result of the 'PRETTIFY' method in the variable 'soup2'
soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')

# Stores the results of the 'GET_TEXT' method in the variables 'title' and 'price' after stripping the text values found
title = soup2.find(id='productTitle').get_text(strip = True)
price = soup2.find('span', class_='aok-offscreen').get_text(strip = True)
price = price.strip()[1:]


# Fetches today's date and stores it in a variable
today = datetime.date.today()

# Stores a list in the variable 'header' and a list in the variable 'data'
header = ['Title', 'Price', 'Date']
data = [title, price, today]

# 'Opens' a new CSV file named 'AmazonWebScraping.csv' under the write operation and writes both a header and any data
with open('AmazonWebScraping.csv', 'w', newline = '', encoding = 'UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)

# Appends a row to the CSV file
with open('AmazonWebScraping.csv', 'a+', newline = '', encoding = 'UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)

# Function that can be used to automate the process of appending new rows to the CSV file
def check_pricing():
    URL = 'https://www.amazon.co.uk/explaining-right-Funny-Analyst-T-Shirt/dp/B08XYL6GRM/ref=sr_1_2?crid=3HLQ1FSN477GA&dib=eyJ2IjoiMSJ9.uo1ZKoIvETOJEhK0t0YddYhQlUqn15Izn7BFt_NMv7_VymlwueQbUtl5b_D-Mxzf_aAdL_o_QvBzTK7Q2HrhNecmiN050M1I2SO-QOYwxc5W3BKZe5y6UyozlOwh_MIhKGHEUTGEF3HuzOXwKYauTw7pmbB2-L3VI47oGOXfU17CyQZl_RykEncXKYBwdoh-eHzFssj5F7Aw1fZK9ryMK8E5ts8jNyTuiZTDJsaw_tRDnDJfw3XpmpEdR4_7iEAyY2A_fLPenvJ4slg8vEPhLLZfwPcH17WSu4GOQaMqVjs.rDaHonMaAc2uy-zrs025TRT4N7juCz9eQWDqnrHgohM&dib_tag=se&keywords=funny+data+analyst+shirt&qid=1723971685&sprefix=funny+data+analyst+shirt%2Caps%2C93&sr=8-2'
    
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36', 'Accept-Encoding':'gzip, deflate, br, zstd', 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'DNT':'1','Connection':'close', 'Upgrade-Insecure-Requests':'1'}
    
    page = requests.get(URL, headers = headers)
    soup1 = BeautifulSoup(page.content, 'html.parser')
    soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')
    
    title = soup2.find(id='productTitle').get_text(strip = True)
    price = soup2.find('span', class_='aok-offscreen').get_text(strip = True)
    price = price.strip()[1:]
    
    today = datetime.date.today()
    
    header = ['Title', 'Price', 'Date']
    data = [title, price, today]

    with open('AmazonWebScraping.csv', 'a+', newline = '', encoding = 'UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)

# Timer that calls the function check_pricing() every X number of seconds
while(True):
    check_pricing()
    time.sleep(86400)

# Creates a new dataframe from the data stored in the CSV file and outputs the dataframe
df = pd.read_csv(r'C:\Users\joshu\AmazonWebScraping.csv')
print(df)