# Movie Recommendation System

This project is a **Movie Recommendation System** built using Python. The system recommends movies to users based on their similarity to other movies. The similarity is computed using features extracted from a movie dataset.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Installation

To run this project locally, follow these steps:

1. Clone the repository:

       git clone https://github.com/your-username/Movie-Recommendation-System.git
       cd Movie-Recommendation-System
   
3. Create and activate a virtual environment (optional but recommended):
   
       python -m venv venv
       source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   
5. Install the required dependencies:
   
       pip install -r requirements.txt

7. Ensure that you have the required data files:

        tmdb_5000_movies.csv: The dataset containing movie information.
        tmdb_5000_credits.csv: The dataset containing credits information.
        movie_dict.pkl: Dictionary containing processed movie data.
        similarity.pkl: Precomputed similarity matrix.

8. Run the Jupyter notebook:

        jupyter notebook "Movie Recommender System.ipynb"

## Usage :
    To use the system, follow these steps within the Jupyter notebook:

1. Load Data:

      Import the necessary libraries (numpy, pandas).
      Load the movie dataset (tmdb_5000_movies.csv) and credits dataset (tmdb_5000_credits.csv).
      Merge the two datasets based on movie titles to create a unified dataset.

2. Pre-process Data:
   
      Clean and pre-process the data to extract relevant features like genres, keywords, and cast.

3. Vectorization:

      Transform text data into numerical vectors using techniques like TF-IDF or Count Vectorizer to compute the similarity matrix.

4. Make Recommendations:

      Based on the user's input (such as a movie title), the system will recommend movies that are most similar according to the computed similarity matrix.

## Features
  1. Data Pre-processing:
                   Merges and cleans movie and credits data for a unified dataset.
  2. Vectorization:
                   Converts text features into numerical vectors for similarity computation.
  3. Similarity Computation:
                   Recommends movies based on cosine similarity or other metrics between movie vectors.
  4. Pickle Integration:
                   Saves precomputed data to pkl files for faster loading.
  5. Similarity Computation:
                   Calculates cosine similarity scores between movies to generate recommendations.
  6. Pickle Integration:
                    Precomputed data is stored in pkl files for faster loading and reuse.
  7. Interactive Jupyter Notebook:
                    The project is presented in a Jupyter notebook, allowing for exploration and visualization of data and recommendations.
  8. Interactive Notebook:
                    Explore and visualize the data and recommendations directly within the Jupyter notebook.

## Data
 The data used in this project is sourced from The Movie Database (TMDb). It consists of two main files:
       tmdb_5000_movies.csv: Contains information about 5000 movies.
       tmdb_5000_credits.csv: Contains information about the cast and crew of the movies.
       
## Modeling Approach
This recommendation system is content-based, meaning it relies on the metadata associated with movies to find similarities. The key steps in the modeling approach include:

. Data Preprocessing: 
                     Cleaning and merging the datasets.
                     
Feature Engineering: 
                     Combining relevant textual data into a single feature.
                     
Vectorization: 
                     Transforming textual data into numerical vectors.
                     
Similarity Calculation: 
                     Using cosine similarity to find the most similar movies.

                     
Future improvements do include integrating collaborative filtering methods or hybrid models to enhance the recommendation accuracy.
