#Handle Ouliers 

import pandas as pd
import numpy as np
import math
import seaborn as sns
import matplotlib.pyplot as plt



def replace_outliers_with_mean(df, threshold=1.5):
    df_no_outliers = df.copy()

    # Loop through each numeric column
    for column in df_no_outliers.select_dtypes(include=[np.number]).columns:
        # Calculate the IQR (Interquartile Range)
        Q1 = df_no_outliers[column].quantile(0.25)
        Q3 = df_no_outliers[column].quantile(0.75)
        IQR = Q3 - Q1

        # Define the lower and upper bounds for outliers
        lower_bound = Q1 - threshold * IQR
        upper_bound = Q3 + threshold * IQR

        # Identify and replace outliers with the mean
        outliers = (df_no_outliers[column] < lower_bound) | (df_no_outliers[column] > upper_bound)
        df_no_outliers.loc[outliers, column] = df_no_outliers[column].mean()

    return df_no_outliers

######################


