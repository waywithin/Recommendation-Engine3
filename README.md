# Recommendation Engine 3
## Appliances Recommendation

## Popularity and Content based book Recommendation System

## Project Overview
- This project is a popularity and content based recommendation system that recommends relevant Appliances based on the similar matches to the user's search.
- The user enters an appliances, and the system retrieves the most similar items 

## Dataset Information
- Source: Kaggle 
- Total Rows and columns in Appliances Data 9576 and 9

## Exploratory Data Analysis
- 478 missing values in ratings
- 478 missing values in no of ratings
- 362 in discount price
- 91 in actual price
- No duplicate records
- Combined name, main category and sub category inside product dataset

### Popularity Based Recommendation
- found average ratings, since the no of ratings is already given in the dataset
- filtered the books that have more than 250 number of ratings

### Content Based Recommendation 
- Used TfIdf matrix and similarity matrix to recommend most similar product to the user's search

## Recommendation Workflow
## Popularity Based Recommendation
- In home page the top 10 appliances will be recommended to the user that doesn't need user's input
## Content Based Recommendation
- The user types the appliances name, the system transform the input to vector form then the similarity score will be calculated
and then the user gets the recommendation that have high similarity with the user's input

## Technologies Used
- Python
- Pandas
- Scikit-learn
- Streamlit

## Future Improvements
- semantic recommendation using transformer embeddings
- Auto-suggestions while typing
- Hybrid recommendation system

## Live Demo
https://book-recommendation-3-1g0z.onrender.com/recommend

## Author
Nubula H
Data Science & Machine Learning Learner
