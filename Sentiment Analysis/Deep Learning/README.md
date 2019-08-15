# Sentiment Analysis of Three Major Hospitals using Deep Learning

The aim of this project is to predict the sentiment of the customers who used service from Ramathibodi hospital, Chulalongkorn Hospital and Siriraj from the comments from https://www.honestdocs.co/. This data will be useful to find insight of the customers which will give the appropriate approach to improve the hospital services.

## Methodology

The comments will be obtained by using **web-scraping** and then translated from Thai into English language. Data preprocessing are done in order into normalize text, reduce noise and balance the dataset. After that, the text is transformed into sequential data. Deep learning model, **Long-short Term Memmory (LSTM)** and **Gate Recurrent Unit (GRU)**, are used for predicting the comment whether it is negative or positive comment. These model will be evaluated to find which model has better performance. Also, a word vector transfer learning, **Global Vectors for Word Representation (GloVe)**, is used and will be compared with newly trained model.

## Model Evaluation

Evaluation metrics, such as Accuracy, ROC and PR curve, are used to determine the model that give the best prediction. Also, the noun phrase will be extracted from the predicted comments and visualize using **Wordcloud** to find which words are common.

## Analysis on Error

The misclassified comments will be analyzed to find pattern that might cause the error in prediction.

## Authors

* **Panu Looareesuwan** 

## Contributors

* https://github.com/ponthongmak
* https://github.com/patratorn
* https://github.com/perlestot

* Be The Best That You Can Be

