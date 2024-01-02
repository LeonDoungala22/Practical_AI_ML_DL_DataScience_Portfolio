# Heart Disease Prediction using SVM

## Objective
Develop a machine learning model to predict the presence or absence of heart disease in individuals using Support Vector Machines (SVM) for both linear and non-linear scenarios.

## Steps

1. **Data Exploration:**
   - Download the [Heart Disease UCI](https://www.kaggle.com/ronitf/heart-disease-uci) dataset from Kaggle.
   - Explore the dataset to understand its structure and characteristics.
   - Check for missing values and perform any necessary data cleaning.

2. **Preprocessing:**
   - Handle categorical features through one-hot encoding or other suitable methods.
   - Standardize or normalize numerical features.
   - Split the dataset into training and testing sets.

3. **Linear SVM:**
   - Implement a linear SVM classifier using a library like Scikit-Learn.
   - Train the model on the training data.
   - Evaluate the model on the testing data and report accuracy.

4. **Non-linear SVM:**
   - Implement a non-linear SVM using a kernel trick, such as the Radial Basis Function (RBF) kernel.
   - Train the model on the training data.
   - Evaluate the model on the testing data and compare the results with the linear SVM.

5. **Hyperparameter Tuning:**
   - Fine-tune the hyperparameters of the SVM models to achieve better performance.
   - Experiment with different values for regularization parameters and kernel parameters.

6. **Performance Metrics:**
   - Use appropriate performance metrics such as accuracy, precision, recall, and F1 score to evaluate the models.

7. **Visualization (optional):**
   - Depending on the dimensionality of the dataset, you may consider visualizing decision boundaries or feature importance.

## Dataset
You can download the "Heart Disease UCI" dataset from [Kaggle](https://www.kaggle.com/ronitf/heart-disease-uci).

Make sure to follow Kaggle's terms of use and data usage policies when working with the dataset.

This project allows you to work with a real-world health-related dataset and gain insights into predicting heart disease using SVMs.
