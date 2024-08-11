import requests
from bs4 import BeautifulSoup


def main():
    uri = 'https://store.rg-adguard.net/api/GetFiles'
    data = {
        'type': 'url',
        'url': 'https://apps.microsoft.com/detail/9nblggh42ths?hl=de-de&gl=DE',
        'ring': 'Retail'
    }

    response = requests.post(
            uri,
            data=data,
            headers={'Content-Type': 'application/x-www-form-urlencoded'}
            )

    soup = BeautifulSoup(response.content, 'html.parser')
    a_tags = soup.find_all('a')
    packages = filter(lambda a_tag:
                      a_tag.text.endswith('.appx')
                      or a_tag.text.endswith('.appxbundle')
                      or a_tag.text.endswith('.msix')
                      or a_tag.text.endswith('.msixbundle'), a_tags)
    packages = filter(lambda package: '_neutral_' in package.text, packages)

    for package in packages:
        print(package['href'])


if __name__ == "__main__":
    main()
