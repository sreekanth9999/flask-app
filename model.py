import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle


train = pd.read_csv("titanic.csv")
# drop null values
train.dropna(inplace=True)
# features and target
target = 'Survived'
features = ['Pclass', 'Age', 'SibSp', 'Fare']

# X matrix, y vector
X = train[features]
y = train[target]
# model 
model = LogisticRegression()
model.fit(X, y)
model.score(X, y)
pickle.dump(model, open('model.pkl', 'wb'))


