import torch
import requests
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def main():
    '''This is the main function.'''
    compare_floats()
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

def compare_floats():
    a = np.array([0.123456789121212,2,3], dtype=np.float16)
    print("16bit: ", a[0])

    b = np.array([0.123456789121212,2,3], dtype=np.float32)
    print("32bit: ", b[0])

    c = np.array([0.123456789121212121212,2,3], dtype=np.float64)
    print("64bit: ", c[0])

def add(a, b):
    '''This function adds two numbers.'''
    return a + b

if __name__ == '__main__':
    main()
