import requests
from bs4 import BeautifulSoup

user_email = str(input("Enter your email: "))
user_pass = str(input("Enter your password: "))
headers = {
    "Content-Type": "application/json"
}

login_data = {
    "email": user_email,
    "password": user_pass
}
url = "https://whispering-badlands-96166.herokuapp.com/api/auth"
r = requests.post(url=url, data=login_data)
print(r.content)
