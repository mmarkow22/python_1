import requests

class RetrievalError(Exception):
    pass

class NotFoundError(RetrievalError):
    pass

class AccessDeniedError(RetrievalError):
    pass

def get_file_from_url(url, name="latest.csv"):
    response = requests.get(url)
    if response.status_code == 200:
        with open(name, 'wb') as file:
            file.write(response.content)
    elif response.status_code == 404:
        raise NotFoundError(f"File not found: {url}")
    elif response.status_code == 403:
        raise AccessDeniedError(f"Access denied: {url}")
    else:
        raise RetrievalError(f"Failed to retrieve file from {url}, status code: {response.status_code}")


get_file_from_url("https://oleksandr-fedoruk.com/wp-content/uploads/2025/10/sample.csv")