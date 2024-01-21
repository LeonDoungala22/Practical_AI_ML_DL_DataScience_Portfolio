# Statistics for ML and Data Science

Welcome to the comprehensive guide on Statistics for Machine Learning (ML) and Data Science! This guide aims to provide a detailed understanding of statistical concepts with in-depth explanations and practical examples.

- [1- Cheat sheet](https://stanford.edu/~shervine/teaching/cme-106/cheatsheet-statistics)
- [2- Cheat sheet ](https://www.stratascratch.com/blog/a-comprehensive-statistics-cheat-sheet-for-data-science-interviews/)

## Table of Contents

1. [Introduction to Statistics](#introduction-to-statistics)
2. [Descriptive Statistics](#descriptive-statistics)
3. [Probability](#probability)
4. [Inferential Statistics](#inferential-statistics)
5. [Regression Analysis](#regression-analysis)
6. [Statistical Tests for ML](#statistical-tests-for-ml)
7. [Machine Learning Evaluation Metrics](#machine-learning-evaluation-metrics)
8. [Bayesian Statistics](#bayesian-statistics)
9. [Examples and Practical Applications](#examples-and-practical-applications)

## Introduction to Statistics

### What is Statistics?

Statistics involves the collection, analysis, interpretation, presentation, and organization of data. It helps in understanding and drawing conclusions from data.

### Descriptive vs. Inferential Statistics

**Descriptive Statistics** focuses on summarizing and presenting data, such as mean, median, and standard deviation. **Inferential Statistics** makes predictions or inferences about a population based on a sample.

### Populations and Samples

- **Population:** The entire group under study.
- **Sample:** A subset of the population.

## Descriptive Statistics

### Measures of Central Tendency

#### Mean (μ):
The average of a set of values.

\[ \mu = \frac{\sum_{i=1}^{n} x_i}{n} \]

#### Median:
The middle value in a dataset.

#### Mode:
The value that appears most frequently in a dataset.

### Measures of Dispersion

#### Range:
The difference between the maximum and minimum values.

#### Variance (σ²):
The average of the squared differences from the mean.

\[ \sigma^2 = \frac{\sum_{i=1}^{n} (x_i - \mu)^2}{n} \]

#### Standard Deviation (σ):
A measure of the amount of variation or dispersion in a set of values.

\[ \sigma = \sqrt{\sigma^2} \]

### Skewness and Kurtosis

#### Skewness:
Measures the asymmetry of the distribution.

\[ \text{Skewness} = \frac{\sum_{i=1}^{n} (x_i - \mu)^3}{n \cdot \sigma^3} \]

#### Kurtosis:
Measures the "tailedness" of the distribution.

\[ \text{Kurtosis} = \frac{\sum_{i=1}^{n} (x_i - \mu)^4}{n \cdot \sigma^4} \]

## Probability

### Basic Probability Concepts

Probability is the likelihood of a particular event occurring.

### Probability Distributions

#### Uniform Distribution:
All outcomes are equally likely.

#### Binomial Distribution:
Models the number of successes in a fixed number of trials.

#### Normal Distribution:
Characterized by a bell-shaped curve.

### Conditional Probability

The probability of an event occurring given that another event has already occurred.

\[ P(A | B) = \frac{P(A \cap B)}{P(B)} \]

## Inferential Statistics

### Hypothesis Testing

1. **Null Hypothesis (H₀):** Assumes no effect or no difference.
2. **Alternative Hypothesis (H₁):** Assumes an effect or difference.

#### t-test Example:

Suppose we have two groups of data, `group1` and `group2`. A t-test can be performed to compare their means.

### Confidence Intervals

A range of values used to estimate the true value of a population parameter.

\[ \text{Confidence Interval} = \bar{x} \pm z \left( \frac{s}{\sqrt{n}} \right) \]

### p-values and Significance Levels

- p-value: Probability of observing a test statistic as extreme as the one computed from the sample.
- Significance Level (α): Threshold for rejecting the null hypothesis.

## Regression Analysis

### Simple Linear Regression

Modeling the relationship between a dependent variable (y) and one independent variable (x).

\[ y = \beta_0 + \beta_1 x + \varepsilon \]

### Multiple Linear Regression

Extension to multiple independent variables.

\[ y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \ldots + \beta_n x_n + \varepsilon \]

### Logistic Regression

Predicting the probability of a binary outcome.

\[ P(Y=1) = \frac{1}{1 + e^{-(\beta_0 + \beta_1 x)}} \]

## Statistical Tests for ML

- t-tests
- ANOVA
- Chi-Square Test

## Machine Learning Evaluation Metrics

- Accuracy, Precision, Recall, F1 Score
- ROC-AUC Curve
- Confusion Matrix

## Bayesian Statistics

### Bayesian Inference

Bayesian inference updates beliefs about a hypothesis as evidence accumulates.

### Prior, Likelihood, Posterior

The posterior probability is proportional to the product of the prior probability and the likelihood.

### Bayesian vs. Frequentist Approach

Bayesian statistics considers probability as a measure of belief, while frequentist statistics considers probability as a measure of frequency.

## Examples and Practical Applications

### Example 1: Descriptive Statistics

Calculating mean, median, and mode for a given dataset.

### Example 2: Hypothesis Testing

Conducting a hypothesis test to compare the means of two groups.

### Example 3: Regression Analysis

Applying regression analysis to model the relationship between variables.


