import matplotlib.pyplot as plt
import math
import mplcursors
import numpy as np
import seaborn as sns
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix


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

