# Thai Language Sentiment Analysis of Three Major Hospitals using Deep Learning

This project aims to experiment sentiment analysis using Thai comments. The project divided into two experiments, train the model with and without Thai stopwords. This was done to find whether removing stopwords would help in model prediction or not. The data were scraped from https://www.honestdocs.co/.

## Prerequisites

- Jupyter Notebook
- Python3
- h5py
- Tensorflow & Keras


## Methodology

Thai comments are preprocessed and tokenized using the package from pythainlp. LSTM model is used in this experiment and randomsearch is use to find optimal hyperparameter.

## Model Evaluation

Evaluation metrics, such as **Accuracy, ROC and PR curve**, are used to determine the model that give the best prediction.

## Analysis on Error

The misclassified comments will be analyzed to find pattern that might cause the prediction error.

## Authors

* **Panu Looareesuwan** 



* Be The Best That You Can Be

