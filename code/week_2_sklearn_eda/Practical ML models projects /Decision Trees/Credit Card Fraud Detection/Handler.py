import matplotlib.pyplot as plt
import math
import mplcursors
import numpy as np
import pandas as pd 
import seaborn as sns
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from scipy.stats import zscore
import pickle



def custum_corr_matrix (df):
    # Calculate correlation matrix
    correlation_matrix = df.corr()

    # Set up the matplotlib figure
    plt.figure(figsize=(20, 12))

    # Plot the heatmap
    heatmap = sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=.5, cbar_kws={"shrink": 0.75})

    # Increase font size of annotations
    heatmap.set_xticklabels(heatmap.get_xticklabels(), fontsize=12)
    heatmap.set_yticklabels(heatmap.get_yticklabels(), fontsize=12)

    # Rotate y-axis labels for better readability
    plt.yticks(rotation=0)

    # Add color bar
    cbar = heatmap.collections[0].colorbar
    cbar.ax.tick_params(labelsize=12)

    # Add a title
    plt.title("Correlation Matrix", fontsize=16)

    # Show the plot
    plt.show()

################################################################
      
    
def handle_outliers(df):
    """
    Identify and replace outliers in a DataFrame using the Z-score method.

    Parameters:
    - df (pd.DataFrame): Input DataFrame containing numerical columns.

    Returns:
    None
    """

    z_threshold = 5

    # Display the percentage of outliers before replacement
    print("# Percentage of Outliers Before Replacement")
    for column in df.columns:
        if df[column].dtype in ['int64', 'float64']:
            z_scores = zscore(df[column])
            original_outliers_percentage = (abs(z_scores) > z_threshold).sum() / len(df) * 100
            print(f"- Outliers in {column}: {original_outliers_percentage:.2f}%")

    # Replace outliers with the median
    for column in df.columns:
        if df[column].dtype in ['int64', 'float64']:
            z_scores = zscore(df[column])
            is_outlier = abs(z_scores) > z_threshold
            df[column] = np.where(is_outlier, df[column].median(), df[column])

    # Display the percentage of replaced outliers after replacement
    print("\n# Percentage of Replaced Outliers After Replacement")
    for column in df.columns:
        if df[column].dtype in ['int64', 'float64']:
            replaced_outliers_percentage = (df[column] != df[column].median()).sum() / len(df) * 100
            print(f"- Outliers replaced in {column}: {replaced_outliers_percentage:.2f}%")

    # Display the percentage of outliers after replacement
    print("\n# New Percentage of Outliers After Replacement")
    for column in df.columns:
        if df[column].dtype in ['int64', 'float64']:
            new_outliers_percentage = (abs(zscore(df[column])) > z_threshold).sum() / len(df) * 100
            print(f"- Outliers in {column} after replacement: {new_outliers_percentage:.2f}%")

                
################################################################
                
                
def evaluate_and_plot_performance(y_test, y_pred, class_labels=None):
    """
    Evaluate the performance of a classification model and plot the confusion matrix.

    Parameters:
    - y_test: True labels of the test set
    - y_pred: Predicted labels of the test set
    - class_labels: Labels for classes (default=None, assumes binary classification)

    Returns:
    - None
    """
    # Performance metrics
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    # Display metrics
    print("Performance metrics for model:\n")
    print(f"Accuracy: {accuracy * 100:.2f}%")
    print(f"Precision: {precision * 100:.2f}%")
    print(f"Recall: {recall * 100:.2f}%")
    print(f"F1 Score: {f1 * 100:.2f}%")

    # Display confusion matrix
    print("\nConfusion Matrix:")
    cm = confusion_matrix(y_test, y_pred)

    # Plot confusion matrix
    sns.heatmap(cm, annot=True, fmt="d", cmap="YlGnBu", cbar=False,
                xticklabels=class_labels, yticklabels=class_labels)
    plt.title('Confusion Matrix')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.show()

    # Additional metrics
    print("\nAdditional Metrics:")
    print(f'Accuracy: {accuracy * 100:.2f}%')

# Example usage
# evaluate_and_plot_performance(y_test, y_pred_rbf_tuned, class_labels=np.unique(y))

################################################################
      

def save_dataset(data, file_path):
    with open(file_path, 'wb') as data_file:
        pickle.dump(data, data_file)
        print(f"Data saved successfully: {file_path}")
        
        



