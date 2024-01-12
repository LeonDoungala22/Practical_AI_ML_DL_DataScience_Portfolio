#Import libreries 

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
from scipy import stats

from sklearn.model_selection import learning_curve
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


##############################



def plot_learning_curve_with_overfitting_indicator(model, X, y, title):
    train_sizes, train_scores, test_scores = learning_curve(model, X, y, cv=5, scoring='neg_mean_squared_error', train_sizes=np.linspace(0.1, 1.0, 10))

    train_scores_mean = -np.mean(train_scores, axis=1)
    test_scores_mean = -np.mean(test_scores, axis=1)

    overfitting_indicator = train_scores_mean - test_scores_mean

    plt.figure(figsize=(15, 10))
    plt.plot(train_sizes, train_scores_mean, label='Training error')
    plt.plot(train_sizes, test_scores_mean, label='Testing error')
 
    plt.title(title)
    plt.xlabel('Training examples')
    plt.ylabel('Mean Squared Error')
    plt.legend()
    plt.show()

    
    
#################################



import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
from sklearn.ensemble import VotingClassifier
from tqdm import tqdm
import time

# Function to evaluate model performance
def evaluate_model(model, X_test, y_test):
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    recall = recall_score(y_test, predictions)
    precision = precision_score(y_test, predictions)
    f1 = f1_score(y_test, predictions)
    return accuracy, recall, precision, f1

# Function to compare model performance
def compare_models(random_forest_model, gradient_boosting_model, xgboost_model, adaboost_model, voting_classifier, X_test, y_test):
    # List of models and corresponding model instances
    models = [
        ('Random Forest', random_forest_model),
        ('Gradient Boosting', gradient_boosting_model),
        ('XGBoost', xgboost_model),
        ('AdaBoost', adaboost_model),
        ('Voting Classifier', voting_classifier)
    ]

    # Lists to store performance metrics
    accuracies = []
    recalls = []
    precisions = []
    f1_scores = []

    # Evaluate each model and update progress bar
    for model_name, model_instance in tqdm(models, desc='Evaluating models'):
        accuracy, recall, precision, f1 = evaluate_model(model_instance, X_test, y_test)
        accuracies.append((model_name, accuracy))
        recalls.append((model_name, recall))
        precisions.append((model_name, precision))
        f1_scores.append((model_name, f1))
        time.sleep(1)  # Simulating some processing time

    # Sort metrics for each model
    accuracies.sort(key=lambda x: x[1], reverse=True)
    recalls.sort(key=lambda x: x[1], reverse=True)
    precisions.sort(key=lambda x: x[1], reverse=True)
    f1_scores.sort(key=lambda x: x[1], reverse=True)

    # Set the figure size and create subplots
    fig, ax = plt.subplots(figsize=(15, 10))

    # Plotting bar plot
    bar_width = 0.2
    bar_positions = np.arange(len(models))

    bars1 = ax.bar(bar_positions - bar_width, [item[1] for item in accuracies], bar_width, label='Accuracy', color='blue')
    bars2 = ax.bar(bar_positions, [item[1] for item in recalls], bar_width, label='Recall', color='green')
    bars3 = ax.bar(bar_positions + bar_width, [item[1] for item in precisions], bar_width, label='Precision', color='orange')
    bars4 = ax.bar(bar_positions + 2 * bar_width, [item[1] for item in f1_scores], bar_width, label='F1 Score', color='red')

    # Adding numerical values on top of each bar
    def add_values_on_bars(ax, bars):
        for bar in bars:
            yval = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 3), ha='center', va='bottom')

    # Call the function for each set of bars
    add_values_on_bars(ax, bars1)
    add_values_on_bars(ax, bars2)
    add_values_on_bars(ax, bars3)
    add_values_on_bars(ax, bars4)

    # Adding labels and title
    ax.set_xlabel('Models')
    ax.set_ylabel('Scores')
    ax.set_title('Model Performance Comparison')
    ax.set_xticks(bar_positions)
    ax.set_xticklabels([item[0] for item in accuracies])
    ax.legend()

    # Show the plot
    plt.show()
