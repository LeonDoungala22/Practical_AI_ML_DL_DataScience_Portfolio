# Statistics for ML and Data Science

import numpy as np
from scipy.stats import mode, skew, kurtosis, ttest_ind
from scipy.stats import norm, binom
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

## Descriptive Statistics

# Measures of Central Tendency

### Mean (average):

data = [12, 15, 18, 22, 25, 30, 35]
mean = np.mean(data)
print(f"Mean: {mean}")

### Median:

median = np.median(data)
print(f"Median: {median}")

### Mode:

mode_result = mode(data)
print(f"Mode: {mode_result.mode[0]} (occurs {mode_result.count[0]} times)")

# Measures of Dispersion

### Range:

data_range = np.ptp(data)
print(f"Range: {data_range}")

### Variance:

variance = np.var(data)
print(f"Variance: {variance}")

### Standard Deviation:

std_dev = np.std(data)
print(f"Standard Deviation: {std_dev}")

### Skewness:

skewness = skew(data)
print(f"Skewness: {skewness}")

### Kurtosis:

kurt = kurtosis(data)
print(f"Kurtosis: {kurt}")

## Probability

# Basic Probability Concepts

# Probability Distributions

### Uniform Distribution:

uniform_data = np.random.uniform(0, 1, 1000)

### Binomial Distribution:

n, p = 10, 0.5
binomial_data = binom.rvs(n, p, size=1000)

### Normal Distribution:

normal_data = np.random.normal(0, 1, 1000)

# Conditional Probability

# Assuming events A and B, and P(A and B)
P_A = 0.6
P_B = 0.4
P_A_and_B = 0.25

P_A_given_B = P_A_and_B / P_B
print(f"Conditional Probability P(A|B): {P_A_given_B}")

## Inferential Statistics

# Hypothesis Testing

### t-test Example:

group1 = [25, 30, 35, 40, 45]
group2 = [20, 28, 32, 38, 42]

t_stat, p_value = ttest_ind(group1, group2)
print(f"T-statistic: {t_stat}, p-value: {p_value}")

# Confidence Intervals

confidence_level = 0.95
z_score = norm.ppf((1 + confidence_level) / 2)

data_mean = np.mean(data)
data_std = np.std(data)
margin_of_error = z_score * (data_std / np.sqrt(len(data)))

confidence_interval = (data_mean - margin_of_error, data_mean + margin_of_error)
print(f"Confidence Interval: {confidence_interval}")

# p-values and Significance Levels

# Regression Analysis

## Simple Linear Regression

x = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([2, 4, 5, 4, 5])

model = LinearRegression()
model.fit(x, y)

# Predict for a new value
new_x = np.array([6]).reshape(-1, 1)
predicted_y = model.predict(new_x)
print(f"Simple Linear Regression Prediction: {predicted_y[0]}")

## Multiple Linear Regression

X = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
y = np.array([2, 4, 5, 4])

model = LinearRegression()
model.fit(X, y)

# Predict for new values
new_X = np.array([[5, 6]])
predicted_y = model.predict(new_X)
print(f"Multiple Linear Regression Prediction: {predicted_y[0]}")

## Logistic Regression

# Generate a binary classification dataset
X, y = make_classification(n_samples=100, n_features=2, n_classes=2, n_clusters_per_class=1, random_state=42)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit a logistic regression model
logreg_model = LogisticRegression()
logreg_model.fit(X_train, y_train)

# Predictions on the test set
predictions = logreg_model.predict(X_test)
print(f"Logistic Regression Predictions: {predictions}")
