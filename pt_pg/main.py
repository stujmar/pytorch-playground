import torch
import requests
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def main():
    '''This is the main function.'''
    create_scalar()
    create_vector()
    # check_versions()

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

def create_scalar():
    """This function creates a scalar."""
    scalar = torch.tensor(7)
    print(scalar)
    # print(dir(scalar)) # long winded.
    print(scalar.item()) # This is the preferred way to get the value of a scalar.

def create_vector():
    '''This function creates a vector.'''
    print("... Creating a vector ...")
    vector = torch.tensor([1, 2, 3])
    print(vector, vector.dtype)
    print(vector.shape, vector.size(), vector.ndim)
    try:
        print(vector.item())
    except Exception as e:
        print(e, "This only works for scalars.")

def add(a, b):
    '''This function adds two numbers.'''
    return a + b

if __name__ == '__main__':
    main()