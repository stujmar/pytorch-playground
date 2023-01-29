import torch
import requests
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def main():
    '''This is the main function.'''
    check_versions()

    # Examime the torch module
    # print(dir(torch))

    # Get data from the web
    get_data()

def get_data():
    '''This function gets data from the web.'''
    url = 'https://www.google.com'
    response = requests.get(url)
    print(response.status_code)

def check_versions():
    '''This function checks the versions of the modules.'''
    print("pytorch version:", torch.__version__)
    print("pandas version:", pd.__version__)
    print("numpy version:", np.__version__)
    print("matplotlib version:", matplotlib.__version__)

def add(a, b):
    '''This function adds two numbers.'''
    return a + b

if __name__ == '__main__':
    main()