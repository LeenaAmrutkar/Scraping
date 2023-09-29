import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

# Set up MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['amazon']
collection = db['product_details']

def get_soup(url, header):
    '''
    This function takes url and header and returns soup as an object
    Input: Url, header
    Output: Soup as object'''
    response = requests.get(url, headers= header)
    soup = BeautifulSoup(response.text,"lxml")
    return soup

def get_title(soup):
    '''
    This function extracts title of product
    Input: Soup
    Output: Title as a string
    '''
    try:
        product_title = soup.find('span', {'id': 'productTitle'}).text.strip()
    except:
        product_title = ""
    return product_title

def get_rating(soup):
    '''
    This function extracts rating of product
    Input: Soup
    Output: Ratings as a string'''
    try:
        rating = soup.find('span', {'class': 'a-icon-alt'}).text.strip()
    except:
        rating = ""
    return rating

def get_price(soup):
    '''
    This function extracts price of product
    Input: Soup
    Output: Price as a string'''
    try:
        price = soup.find('span', {'class': 'a-price-whole'}).text.strip()
    except:
        price = ""
    return price

def get_sellername(soup):
    '''
    This function extracts seller name of product
    Input: Soup
    Output: Seller name as a string'''
    try:
        seller_name = soup.find('a', {'id': 'bylineInfo'}).text.strip()
    except:
        seller_name = ""
    return seller_name

def get_numratings(soup):
    '''
    This function extracts number of ratings of product
    Input: Soup
    Output: Number of ratings as a string'''
    try:
        num_ratings = soup.find('span', {'id': 'acrCustomerReviewText'}).text.strip()
    except:
        num_ratings = ""
    return num_ratings

def get_addinfo(soup):
    '''This function extracts additional info of product
    Input: Soup
    Output: List of strings'''
    info = []
    try:
        additional_info = soup.find('div',{'id':'feature-bullets'})
        add_info = additional_info.findAll('li')
        for i in add_info:
            details = i.find('span',{'class':'a-list-item'}).text.strip()
            info.append(details)
    except:
        info = []
    return info

def get_technical(soup):
    '''
    This function extracts technical details of product
    Input: Soup
    Output: Technical details as dict'''
    try:
        tech_data = soup.find('table',{'class':'a-normal a-spacing-micro'})
        tech_d = tech_data.select('tr')
        data = {}
        for row in tech_d:
            key = row.find('span', {'class': 'a-size-base a-text-bold'}).text.strip()
            value = row.find('span', {'class': 'a-size-base po-break-word'}).text.strip()
            data[key] = value
    except:
        data = {}
    return data

def get_amazon_product(asin):
    '''
    This function takes asin number and stores required data in mongodb
    Input: Asin number
    Output: Required data'''
    product_url = f'https://www.amazon.in/dp/{asin}/'
    h = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}
    soup = get_soup(product_url,h)
    product_title = get_title(soup)
    rating = get_rating(soup)
    price = get_price(soup)
    seller_name = get_sellername(soup)
    num_ratings = get_numratings(soup)
    info = get_addinfo(soup)
    technical_data = get_technical(soup)
    # Store data in MongoDB
    try:
        product_data = {
            'asin': asin,
            'product_title': product_title,
            'rating': rating,
            'price': price,
            'seller_name': seller_name,
            'num_ratings': num_ratings,
            'additional_info': info,
            'technical_details': technical_data
        }
        # Insert into MongoDB collection
        collection.insert_one(product_data)
        print("Data stored successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")