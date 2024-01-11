#Import libreries 

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
from scipy import stats

import missingno as msno


#####################################

def univariate_analysis_plots(df):
    # Set up the figure and axes
    num_features = len(df.columns)
    fig, axes = plt.subplots(nrows=num_features, ncols=2, figsize=(18, 4 * num_features))
    fig.suptitle('Univariate Analysis')

    # Custom colors
    hist_color = 'skyblue'
    box_color = 'salmon'

    # Dynamically analyze each feature
    for i, col in enumerate(df.columns):
        # Plotting Histogram
        sns.histplot(df[col], kde=True, ax=axes[i, 0], color=hist_color)
        axes[i, 0].set_title(f'Histogram - {col}')

        # Plotting Box Plot
        sns.boxplot(x=df[col], ax=axes[i, 1], color=box_color)
        axes[i, 1].set_title(f'Box Plot - {col}')

    # Adjust layout
    plt.tight_layout(rect=[0, 0, 1, 0.96])

    # Show the plot
    plt.show()


