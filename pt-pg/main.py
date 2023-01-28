import torch
import requests

def main():
    '''This is the main function.'''
    # Examime the torch module
    # print(dir(torch))

    # Get data from the web
    get_data()

def get_data():
    '''This function gets data from the web.'''
    url = 'https://www.google.com'
    response = requests.get(url)
    print(response.status_code)

if __name__ == '__main__':
    main()