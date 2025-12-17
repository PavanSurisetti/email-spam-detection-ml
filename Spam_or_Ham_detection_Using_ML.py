import pandas as p #for extracing/loading the dataset
from sklearn.linear_model import LogisticRegression# for classifying spam/ham
from sklearn.model_selection import train_test_split#for splitting the dataset into 2 Parts
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import CountVectorizer#this is for converting text into the bag of words and then numbers
import pickle  #for saving the model
#dataset fetching
data_set=p.read_csv('email.csv')
#loading from the dataset
input=data_set['Message']
output=data_set['Category']
#since it is text we cannot use directly, so we need to convert using vector
vector=CountVectorizer()
input=vector.fit_transform(input)
#splitting the data into 2 parts
x_train,x_test,y_train,y_test=train_test_split(input,output,random_state=42,test_size=0.2)
#creating a model
model=LogisticRegression()
#training the model
model.fit(x_train,y_train)
#model prediction
y_pred=model.predict(x_test)
#print(f'the prediction is:{y_pred}')
#i want to give my own message 
msg1=['You have been selected as the lucky winner of our $10,000 cash prize. To claim your reward, please click the link below and provide your bank details immediately']
msg2=['Hi Rakesh,Just a quick update — the project meeting has been rescheduled from 2 PM to 3 PM today. Please let me know if you’re still available at that time.']
#now i am converting into vectors
vector1=vector.transform(msg1)
vector2=vector.transform(msg2)
print(f'the message->{msg1[0]} is :{model.predict(vector1)[0]} mail \n\n')
print(f'the message->{msg2[0]} is :{model.predict(vector2)[0]} mail\n\n')
#calculating the accracy
accsc=accuracy_score(y_test,y_pred)
print(f'the accuracy is:{accsc}')
#------------------ SAVING MODEL & VECTORIZER ------------------
pickle.dump(model, open("spam_model.pkl", "wb"))
pickle.dump(vector, open("vectorizer.pkl", "wb"))
print("Model and Vectorizer saved successfully!")