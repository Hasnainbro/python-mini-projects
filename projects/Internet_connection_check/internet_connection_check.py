import requests  # Import the requests library for making HTTP requests
from requests.exceptions import ConnectionError  # Import the ConnectionError exception

def internet_connection_test():
    url = 'https://www.google.com/'  # URL to test internet connection
    print(f'Attempting to connect to {url} to determine internet connection status.')
    
    try:
        # Attempt to connect to the URL
        resp = requests.get(url, timeout=10)  # Send a GET request with a timeout of 10 seconds
        resp.text  # Access the response text (not used here, just to check if response is successful)
        resp.status_code  # Access the status code of the response (not used here, just to check if response is successful)
        print(f'Connection to {url} was successful.')  # Print success message
        return True  # Return True to indicate successful connection
    except ConnectionError as e:
        print(f'Failed to connect to {url}.')  # Print failure message
        return False  # Return False to indicate failed connection
    except Exception as e:  # Catch any other exceptions
        print(f'Failed with unparsed reason: {e}.')  # Print failure message with the reason
        return False  # Return False to indicate failed connection

internet_connection_test()  # Call the function to test internet connection

