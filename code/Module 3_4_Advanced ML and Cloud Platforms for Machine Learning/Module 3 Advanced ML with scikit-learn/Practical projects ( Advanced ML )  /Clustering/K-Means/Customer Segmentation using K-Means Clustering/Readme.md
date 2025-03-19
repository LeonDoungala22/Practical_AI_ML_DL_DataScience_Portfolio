# Advanced Customer Segmentation with K-Means, PCA, and AI-Driven Marketing

## Project Overview

This project demonstrates sophisticated customer segmentation using K-Means clustering, PCA dimensionality reduction, and generative AI to create personalized marketing recommendations. By analyzing the Mall Customers dataset, we identify distinct customer segments and develop targeted marketing strategies.

## Technologies Used

- **Python** with scikit-learn, pandas, numpy, matplotlib
- **K-Means Clustering** with optimized parameter selection
- **Principal Component Analysis (PCA)** for dimensionality reduction
- **LangChain Framework** for LLM integration
- **OpenAI API** for generating personalized marketing content

## Dataset

The Mall Customers dataset contains:

- Customer ID
- Gender
- Age
- Annual Income (k$)
- Spending Score (1-100)

## Key Features

- **Comprehensive EDA** with statistical analysis and visualizations
- **Advanced clustering** with silhouette analysis and elbow method optimization
- **PCA implementation** for improved cluster visualization and interpretation
- **AI-powered recommendation system** generating personalized marketing messages
- **Segment-specific marketing strategies** based on customer profiles

## Project Structure

- `main.ipynb`: Jupyter notebook containing the complete analysis and implementation
- `Dataset/Mall_Customers.csv`: Customer data used for segmentation
- `README.md`: Project documentation

## Setup Instructions

1. Clone the repository
2. Install required packages: `pip install -r requirements.txt`
3. Create a `.env` file with your OpenAI API key (see `.env.example`)
4. Run the Jupyter notebook: `jupyter notebook main.ipynb`

## Results

The analysis identified distinct customer segments with unique characteristics:

- High-income, high-spending customers ideal for premium offerings
- Budget-conscious shoppers responsive to promotions and sales
- Mid-range customers with specific spending patterns
- And more detailed segments described in the notebook

## Business Applications

- Personalized marketing campaigns for each customer segment
- Optimized resource allocation for marketing budget
- Enhanced customer engagement through tailored communications
- Improved customer retention with segment-specific strategies

## Future Work

- Implementation of more advanced clustering algorithms
- Integration with real-time customer data
- Development of a dashboard for marketing team usage
- A/B testing of AI-generated marketing messages
