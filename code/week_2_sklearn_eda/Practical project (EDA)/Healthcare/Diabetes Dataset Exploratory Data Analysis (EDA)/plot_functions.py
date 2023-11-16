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


