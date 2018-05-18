# %load imports.py
import numpy as np
import pandas as pd
import seaborn as sns
import missingno as msno
import matplotlib.pyplot as plt
plt.style.use('ggplot')
#Plot styling/configurations
%matplotlib inline
%config InlineBackend.figure_format = 'retina'
plt.rcParams['figure.figsize'] = 14,8
plt.rcParams['axes.facecolor']='white'
plt.rcParams.update({'font.size': 13})
import warnings
warnings.filterwarnings('ignore')
seq_col_brew = sns.color_palette("YlGnBu_r", 4)
sns.set_palette(seq_col_brew)
pd.set_option('display.height', 1000)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
#The difference is the best programmers/problem-solvers are more curious about bugs/errors than irritated.
#1. Understand the problem. “If you can’t explain something in simple terms, you don’t understand it.”
#2. Plan
#3. Divide (first start with a solution that's more simple)
#4. Stuck? Google, take a deep breath, come back.
