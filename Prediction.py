import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn')
sns.set(font_scale=2.5)

import missingno as msno

import warnings
warnings.filterwarnings('ignore')

_train = pd.read_csv('train.csv')
_test = pd.read_csv('test.csv')

print(_train.columns)

# msno.matrix(_train.iloc[:,:], figsize=(8,8), color=(0.2, 0.5, 0.4))

