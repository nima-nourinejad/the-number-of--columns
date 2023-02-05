import pandas as pd
from google.colab import drive 
drive.mount('/content/drive')
t=pd.read_excel("/content/drive/MyDrive/Colab Notebooks/test.xlsx")
f=t.shape
c=f[1]
print('The number of columns is '+ str(c))
