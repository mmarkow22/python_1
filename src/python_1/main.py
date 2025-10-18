import requests

def get_file_from_url(url, name="latest.csv"):
    response = requests.get(url)
    if response.status_code == 200:
        with open(name, 'wb') as file:
            file.write(response.content)
    else:
        raise Exception(f"Failed to retrieve file from {url}, status code: {response.status_code}")


get_file_from_url("https://oleksandr-fedoruk.com/wp-content/uploads/2025/10/sample.csv")