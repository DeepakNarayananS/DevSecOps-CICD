import requests  # Using requests just as an example

def fetch_data(url):
    response = requests.get(url)
    return response.text

if __name__ == "__main__":
    print(fetch_data("https://www.example.com"))