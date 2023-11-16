import matplotlib.pyplot as plt
import math

def plot_column_distributions(df):
    columns = df.columns
    total_columns = len(columns)
    rows = math.ceil(total_columns / 2)  

    # Create subplots with gridspec_kw
    fig, axes = plt.subplots(rows, 2, figsize=(12, 3 * rows), gridspec_kw={'wspace': 0.5, 'hspace': 1})

    # Flatten axes for easy iteration
    axes = axes.flatten()

    # Use tab10 color map for distinct colors
    colors = plt.cm.tab10.colors

    for i, column in enumerate(columns):
        value_counts = df[column].value_counts()
        
        # Plotting a bar chart with distinct colors
        value_counts.plot(kind='bar', ax=axes[i], color=colors[i % len(colors)])
        
        # Modify the title 
        axes[i].set_title(f'{column} Distribution')
        axes[i].set_xlabel(column)
        axes[i].set_ylabel('Count')

    # Adjust layout to prevent overlapping
    plt.tight_layout()
    plt.show()
    
    
    
  ##################################################################################   
   
    
def replace_missing_with_mean(df):
  
    column_means = df.mean()
    df.fillna(column_means, inplace=True)

 ##################################################################################   
    
#Features importance 
from sklearn.ensemble import RandomForestClassifier

def calculate_feature_importance(data_frame, target_variable, top_n=10):
    # Get all features excluding the target variable
    all_features = data_frame.columns.difference([target_variable])

    # Split the data into features (X) and target variable (y)
    X = data_frame[all_features]
    y = data_frame[target_variable]

    # Initialize RandomForestClassifier
    rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)

    # Fit the classifier
    rf_classifier.fit(X, y)

    # Get feature importances
    feature_importances = rf_classifier.feature_importances_

    # Create a DataFrame to display feature importances
    feature_importance_df = pd.DataFrame({'Feature': all_features, 'Importance': feature_importances})

    # Sort the DataFrame by importance in descending order
    feature_importance_df = feature_importance_df.sort_values(by='Importance', ascending=False)

    # Display the top N important columns
    print(f"Top {top_n} Important Columns:")
    print(feature_importance_df.head(top_n))

    # Plot the feature importances 
    plt.figure(figsize=(10, 6))
    plt.barh(feature_importance_df['Feature'].head(top_n), feature_importance_df['Importance'].head(top_n))
    plt.xlabel('Importance')
    plt.title(f'Top {top_n} Feature Importances')
    plt.show()

 ##################################################################################   
  
    
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder, StandardScaler

def preprocessing(data_frame, categorical_features, numeric_features):
    # Convert all values in categorical features to strings
    data_frame[categorical_features] = data_frame[categorical_features].astype(str)

    # Initialize the OrdinalEncoder
    encoder = OrdinalEncoder()

    # Fit and transform the DataFrame for categorical features
    categorical_encoded = encoder.fit_transform(data_frame[categorical_features])

    # Convert the result to a DataFrame
    categorical_encoded_df = pd.DataFrame(categorical_encoded, columns=data_frame[categorical_features].columns)

    # Initialize the StandardScaler
    scaler = StandardScaler()

    # Fit and transform the DataFrame for numerical features
    numerical_scaled = scaler.fit_transform(data_frame[numeric_features])

    # Convert the NumPy arrays to DataFrames
    df_numerical_scaled = pd.DataFrame(numerical_scaled, columns=numeric_features)
    df_categorical_encoded = pd.DataFrame(categorical_encoded_df, columns=categorical_features)

    # Merge the DataFrames on the index
    merged_df = pd.merge(df_numerical_scaled, df_categorical_encoded, left_index=True, right_index=True)

    return merged_df

