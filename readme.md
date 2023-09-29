Files
1) amazon
2) main
3) requirements.txt

Steps:
Description:
Step 1: First explored the website
Step 2 Verified how the data is coming by doing following steps:
i) robots.txt in given url
ii) Checked for API
iii) Checked through requests
The data is coming through requests. 
Step 3: Started writing the code accordingly.

Files
amazon: This file has following functions
i) get_soup(url) - Takes url as string and returns soup as an object
ii) get_amazon_product(asin) -  This function takes asin number and stores required data in mongodb. Calls other functions like get_title(soup), get_ratings(soup) etc. to extract the data.

main: This file calls the get_amazon_product() function

requirements: This file has required packages

Installation:
Install all required packages

Execution:
python3 filename.py
