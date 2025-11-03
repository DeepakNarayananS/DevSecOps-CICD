import requests  # Using requests just as an example

def fetch_data(url):
    response = requests.get(url, timeout=10)  # Set timeout to 10 seconds
    return response.text

if __name__ == "__main__":
    print(fetch_data("https://www.example.com"))