# Movie Recommendation System

This repository contains code for a movie recommendation system built using Python. The dataset used for this system is pulled from Kaggle using the Kaggle API. The dataset, provided by TMDB, consists of information on 10,000 movies including their tags and genres.

## Prerequisites

To run this movie recommendation system, you will need the following:

- Python (version 3.7 or higher)
- Docker Compose
- Jupyter Notebook

## Installation

1. Clone this repository to your local machine:

2. Change into the project directory:

3. Install the required dependencies:
  
4. Start the Docker Compose environment:

5. Access Jupyter Notebook in your web browser at `http://localhost:8888`.

The dataset used for this movie recommendation system is provided by TMDB and consists of 10,000 movies. It includes information such as movie titles, tags, and genres.

To retrieve the dataset, the Kaggle API is used. Please make sure you have a Kaggle account and API credentials. You can obtain your API credentials by following the instructions provided on the [Kaggle API documentation](https://www.kaggle.com/docs/api).

## Feature Engineering

To prepare the data for the recommendation system, the tags and genres columns are merged. Then, the bag of words/count vectorizer technique is applied for feature engineering. Alternatively you can also use tfidfvectorizer from sklearn for calculating the cosine similarity

## Similarity Calculation

The similarity between movies is calculated using cosine similarity. Cosine similarity measures the distance between vectors and is commonly used in recommendation systems to determine the similarity between items.

## Streamlit Application

A Streamlit application is created for the front end of the recommendation system. Streamlit is a Python library that allows you to build interactive web applications for data science and machine learning projects.

The application uses the TMDB API to fetch movie posters for the recommended movies, enhancing the user experience and visual appeal.

To run the Streamlit application, execute the following command:

## Contributing

Contributions to this movie recommendation system are welcome. If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

## Acknowledgments

- The dataset used in this project is provided by TMDB through Kaggle.
- Streamlit for creating the user-friendly application.
- Docker for containerization of the project.

