import matplotlib.pyplot as plt
import math
import mplcursors
import numpy as np
import seaborn as sns
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix


def plot_column_distributions(df):
    """
    Visualize column distributions in a DataFrame with vibrant bar charts using Plotly.

    Parameters:
    - df (DataFrame): Input DataFrame.

    Returns:
    None
    """
    columns = df.columns
    total_columns = len(columns)
    
    # Set rows to the total number of columns
    rows = total_columns

    # Increase vertical height of each subplot
    fig, axes = plt.subplots(rows, 1, figsize=(20, 10 * rows), gridspec_kw={'wspace': 0.8, 'hspace': 0.9, 'bottom': 0.4})

    # Flatten axes for easy iteration
    axes = axes.flatten()

    # Use Set3 color map for distinct colors
    colors = plt.cm.Set3.colors

    for i, column in enumerate(columns):
        value_counts = df[column].value_counts()
        
        # Plotting a bar chart with distinct colors and styles
        bars = value_counts.plot(kind='bar', ax=axes[i], color=colors[i % len(colors)], alpha=0.7, edgecolor='black', linewidth=0.7)
        
        # Add exact counts on top of bars
        for bar, count in zip(bars.patches, value_counts):
            height = bar.get_height()
            axes[i].text(bar.get_x() + bar.get_width() / 2, height, f'{count}', ha='center', va='bottom', fontsize=8)
        
        # Modify the title 
        axes[i].set_title(f'Distribution of {column}', fontsize=12)
        axes[i].set_xlabel(column, fontsize=10)
        axes[i].set_ylabel('Count', fontsize=10)
        
        # Set tick label size and rotation for better readability
        axes[i].tick_params(axis='x', labelsize=8, rotation=45)  # Adjust the rotation angle as needed
        
        # Enable scrollbar for bars
        mplcursors.cursor(bars, hover=True)

    plt.tight_layout()
    plt.show()
    
    
    
    
    

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

