import requests
import smtplib
from bs4 import BeautifulSoup

MY_EMAIL = "YOUR_EMAIL"
MY_PASS = "YOUR_PASS"

# AMAZON_URL = "https://www.amazon.in/Apple-iPhone-Pro-Max-1TB/dp/B09G9L2LH9" \
#              "/ref=sr_1_16?keywords=iphone+13+pro+max&qid=1662099906&sprefix" \
#              "=iphone%2Caps%2C241&sr=8-16"

AMAZON_URL2 = "https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463"

HEADERS = {
    "Accept-Language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
    "User-Agent":   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}

response = requests.get(url=AMAZON_URL2, headers=HEADERS)
content = response.text

soup = BeautifulSoup(content, "lxml") # "html.parser"
title = soup.find(id="productTitle").get_text().encode("utf-8")
print(title)

BUY_PRICE = 200

price = soup.find("span", class_="a-price-whole")
price_separated = price.getText().split(".")
price_to_float = float(price_separated[0].replace(",", ""))

if price_to_float <= BUY_PRICE:
    message = f"{title} is now {price_to_float}."

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASS)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="xyz@yahoo.com",
            msg=f"Subject:Price Alert!\n\n{message}\n{AMAZON_URL2}"
        )
