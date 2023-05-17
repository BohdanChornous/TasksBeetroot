import requests

def get_comments():
    url = f"https://en.wikipedia.org/robots.txt"
    response = requests.get(url)
    with open("robots.txt", "w", encoding='utf-8') as file:
        print(response.text, file=file)

if __name__ == '__main__':
    get_comments()
