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
    create_matrix()
    create_tensor()
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

def create_matrix():
    '''This function creates a matrix.'''
    print("... Creating a matrix ...")
    matrix = torch.tensor([[1, 2, 3], [4, 5, 6]])
    print(matrix, matrix.dtype)
    print(matrix.shape, matrix.size(), matrix.ndim)
    try:
        print(matrix.item())
    except Exception as e:
        print(e, "This only works for scalars.")

def create_tensor():
    '''This function creates a tensor.'''
    print("... Creating a tensor ...")
    # A tensor is a generalization of a vector and a matrix.
    # A tensor is a multidimensional array.
    # This is a three dimensional tensor.
    TENSOR = torch.tensor([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
    print("TENSOR number of dimensions:", TENSOR.ndim)

def add(a, b):
    '''This function adds two numbers.'''
    return a + b

if __name__ == '__main__':
    main()