Files
1) amazon
2) main
3) requirements.txt

Description:
First explored the website
Verified how the data is coming by doing following steps:
i) robots.txt in given url
ii) Checked for API
iii) Checked through requests
The data is coming through requests. Started writing the code accordingly.

amazon: This file has following functions
i) get_soup(url) - Takes url as string and returns soup as an object
ii) scrape_amazon_product(asin) -  This function takes asin number and stores required data in mongodb. Calls other functions like get_title(soup), get_ratings(soup) etc. to extract the data.

Installation:
Install all required packages

Execution:
python3 filename.py