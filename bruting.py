import requests
from requests.auth import HTTPBasicAuth

def test_login(username, password, url):
    try:
        with requests.Session() as session:
            response = session.get(url, auth=HTTPBasicAuth(username, password))

            # Check if the login was successful (status code 200)
            if response.status_code == 200:
                print(f"Login successful for {url}")
            else:
                print(f"Login failed for {url}. Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error during login for {url}: {e}")

# Replace these with your actual username and password
username = 'your_username'
password = 'your_password'

# List of URLs to test
urls_to_test = ['https://example.com/login1', 'https://example.com/login2', 'https://example.com/login3']

# Test login for each URL
for url in urls_to_test:
    test_login(username, password, url)

