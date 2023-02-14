import torch
import requests
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def main():
    '''This is the main function.'''
    # create_scalar()
    # create_vector()
    # create_matrix()
    # create_tensor()
    # random_tensor()
    # random_controled_tensor((2, 3))
    # random_controled_tensor((2, 3))
    # random_controled_tensor((2, 3))
    create_image_tensor(256)
    # check_versions()
    # Examime the torch module
    # print(dir(torch))

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
    NINE_TENSOR = torch.tensor([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
    print("TENSOR number of dimensions:", TENSOR.ndim)
    print("TENSOR shape:", TENSOR.shape, NINE_TENSOR.shape)
    print("zeroth:", NINE_TENSOR[0])
    print("first:", NINE_TENSOR[0][1]) # > [4, 5, 6]
    print("second:", NINE_TENSOR[0][2][1]) # > 8

def random_tensor():
    '''This function creates a random tensor.'''
    print("... Creating a random tensor ...")
    # The default is a float32 tensor.
    random_tensor = torch.rand(2, 3)
    print(random_tensor)
    print("dtype:", random_tensor.dtype)
    print(random_tensor.shape, random_tensor.size(), random_tensor.ndim)

def random_controled_tensor(size):
    '''This function creates a random tensor with a controlled seed.'''
    print("... Creating a random tensor with a controlled seed ...")
    torch.manual_seed(0)
    random_tensor = torch.rand(size)
    print(random_tensor)
    print("dtype:", random_tensor.dtype)
    print(random_tensor.shape, random_tensor.size(), random_tensor.ndim)

def create_image_tensor(size):
    '''This function creates an image tensor.'''
    image_tensor = torch.rand(size=(size, size, 3))
    print(image_tensor.shape, image_tensor.ndim)

if __name__ == '__main__':
    main()