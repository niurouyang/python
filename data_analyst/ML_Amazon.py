# use a machine learning api to train and predict the sentiment
import pandas as pd
df = pd.read_csv("python/data_analyst/amazon_cells_labelled.txt", names =['review', 'sentiments'], sep ='\t')

# use pip3 install -U scikit-learn scipy matplotlib to install sklearn
from sklearn.model_selection import train_test_split
reviews = df['review'].values
sentiments = df['sentiments'].values
reviews_train, reviews_test, sentiment_train, sentiment_test = train_test_split(reviews, sentiments, test_size=0.2, random_state=500)

from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
vectorizer.fit(reviews)
X_train = vectorizer.transform(reviews_train)
X_test = vectorizer.transform(reviews_test)

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(X_train, sentiment_train)

accuracy = classifier.score(X_test, sentiment_test)
print('Accuracy: ', accuracy)