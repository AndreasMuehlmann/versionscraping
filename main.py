import requests
from bs4 import BeautifulSoup


def main():
    url = "https://apps.microsoft.com/detail/9nblggh42ths?hl=de-de&gl=DE"
    request = requests.get(url)

    soup = BeautifulSoup(request.content, 'html.parser')
    print(soup.prettify())


if __name__ == "__main__":
    main()
