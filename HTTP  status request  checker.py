# This program makes an HTTP request status checker.
import datetime
import requests

# checking if GitHub is up.
print(datetime.datetime.now())
response = requests.get("https://github.com")
if response.status_code == 200:
    print("github is up and running")


def checking_if_up(url):
    try:
        if requests.get(url).status_code == 200:
            print(f"{url} us up and running")
        else:
            print(f"sorry, {url} is down")
    except:
        print("something went terribly wrong")


# the user inputting which website He wants to check and then the code backs to the function.
checking_if_up(input("enter your website please:"))
