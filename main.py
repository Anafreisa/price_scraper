import requests
from bs4 import BeautifulSoup
import smtplib

my_email = Your Email
password = Your Password
url = "https://www.amazon.com/Duo-Evo-Plus-esterilizadora-vaporizador/dp/B07W55DDFB/ref=sr_1_4?qid=1597660904"
target_price = 100

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko)"
                  " Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url, headers=headers)
product_url = response.text

soup = BeautifulSoup(product_url, "lxml")
price_url = soup.find(name="span", id="priceblock_ourprice")
price = float(price_url.getText().split("$")[1])
title_url = soup.find(id="productTitle")
title = title_url.getText().strip()

if price < target_price:
    message = f"{title} is now {price}".encode("utf8")
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs= EMAIL TO SEND,
            msg=f"Subject: Amazon Price Alert!\n\n{message}\n{url}"
        )
