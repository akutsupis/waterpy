import os, glob, pdb
import uuid
from scipy.ndimage import gaussian_filter1d
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
os.chdir(r'C:\Users\mallo\Documents\Thesis\GIS Project')
print(os.getcwd())
files = ['Spectral_Array_1.xlsx', 'Spectral_Array_2.xlsx']
for file in files:
    print (file)
    df = pd.read_excel(file)
    pdb.set_trace()
    df = df.values
    m= ((df[:,0]))
    n= ((df[:, 1]))
    pdb.set_trace()
    data = {}
    data['X'] = m
    data['y'] = n
    data['y1'] = gaussian_filter1d(data['y'], 1)
    data['y4'] = gaussian_filter1d(data['y'], 4)
    g = pd.DataFrame.from_dict(data)
    g.head()
    fig = plt.figure()
    ax = plt.gca()
    g.plot(x='X', y='y',label= 'Original data', linewidth= 1.5, ax=ax)
    g.plot(x='X', y='y1',color= 'magenta',linestyle= '--', label= '$\sigma = 1$',ax=ax)
    g.plot(x='X', y='y4',color= 'yellow', linestyle= '--', label= '$\sigma = 4$',ax=ax)
    plt.title("Gaussian Smoothed Spectral Data of Coal Slurry", fontsize=12)
    plt.ylabel("Gaussian Filter Response", fontsize=17.5)
    plt.xlabel("Wavelength (nm)", fontsize=18)
    plt.legend()
    plt.grid()
    #plt.tight_layout()
    figurename= str(uuid.uuid4())
    #plt.savefig('figurename.pdf')
    plt.show()
        
