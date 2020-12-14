from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

with open("/home/Lakshmi/mysite/TfidfVec.pickle","rb") as f:
    TfidfVec=pickle.load(f)

vectorizer=TfidfVectorizer(vocabulary=TfidfVec)

with open("/home/Lakshmi/mysite/multinominalNB.pickle","rb") as f:
    nb=pickle.load(f)

def predict(review):
    TReview = vectorizer.fit_transform([review])
    rating = nb.predict(TReview)
    return rating



