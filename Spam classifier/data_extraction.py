import os
import numpy as np 
import pandas as pd 
import csv
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import plot_confusion_matrix
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import mean_squared_error
from sklearn import metrics
import math

for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

path = "../input/email-archive/email archive/"
file = open("email_data.csv", "w", newline = "")
fileIDnames = ['Type_of_Email', 
               'Subject', 
               'Num_Words_Subject', 
               'Length_Subject', 
               'Upper_case_subject',
               'Text_Body', 
               'Num_Words_Text', 
               'Length_Text', 
               'Repetition_Words', 
               "Unique", 
               'Most_Repeated', 
               'Upper_case_text']

writer = csv.DictWriter(file, fieldnames=fileIDnames)
writer.writerow({
        'Type_of_Email': 'Type_of_Email',
        'Subject':'Subject', 
        'Num_Words_Subject': 'Num_Words_Subject', 
        'Length_Subject':'Length_Subject',
        'Upper_case_subject':'Upper_case_subject', 
        'Text_Body':'Text_Body', 
        'Num_Words_Text':'Num_Words_Text', 
        'Length_Text':'Length_Text', 
        'Repetition_Words':'Repetition_Words', 
        'Unique':'Unique', 
        'Most_Repeated':'Most_Repeated', 
        'Upper_case_text':'Upper_case_text'})

for filename in os.listdir(path):
    curr_open = open(path + filename, "r")
    curr_read = curr_open.read()
    print(curr_read)
    
    print(filename[0:5])
    if filename[0:5] == "spmsg":
        email_type = "Spam"
    else:
        email_type = "Ham"
    
    start = curr_read.find("Suject: ")+len("Subject: ") + 1
    end = curr_read.find("\n\n")
    subject = curr_read[start:end]
    subject_len = len(subject)
    list_subject = subject.split()
    num_subject_words = len(list_subject)
    num_upper_subject = 0
    for word in list_subject:
        if word.isupper() == True:
            num_upper_subject+=1
    
    text_body = curr_read[end:]
    text_len = len(text_body)
    list_words = text_body.split()
    num_text_words = len(list_words)
    num_upper_text = 0
    for word in list_words:
        if word.isupper() == True:
            num_upper_text+=1
    
    
    writer.writerow({
        'Type_of_Email': email_type,
        'Subject':subject, 
        'Num_Words_Subject': num_subject_words, 
        'Length_Subject':subject_len,
        'Upper_case_subject':num_upper_text, 
        'Text_Body':text_body, 
        'Num_Words_Text':num_text_words, 
        'Length_Text': text_len, 
        'Repetition_Words':"NA", 
        'Unique':"NA", 
        'Most_Repeated':"NA", 
        'Upper_case_text':num_upper_text})

ham_email = email_df[email_df['Type_of_Email']=="Ham"]
spam_email = email_df[email_df['Type_of_Email']=="Spam"]

ham_email = ham_email['Text_Body']
spam_email = spam_email['Text_Body']

ham_processed = pd.DataFrame(columns=['Text_Body'])
spam_processed = pd.DataFrame(columns=['Text_Body'])


for ham_e in ham_email:
    ham_em = word_tokenize(ham_e)
    ham_e = " ".join(word for word in ham_em if word.isalpha())
    ham_processed = ham_processed.append({'Text_Body': ham_e}, ignore_index=True)


vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(ham_processed['Text_Body'])
feature_names = vectorizer.get_feature_names()
dense = vectors.todense()
denselist = dense.tolist()
df_ham = pd.DataFrame(denselist, columns=feature_names)

df_ham = df_ham.append({"Type" : 1}, ignore_index=True)
df_ham = df_ham.replace(np.nan, 1)



for spam_e in spam_email:
    spam_em = word_tokenize(spam_e)
    spam_e = " ".join(word for word in spam_em if word.isalpha())
    spam_processed = spam_processed.append({'Text_Body': spam_e}, ignore_index=True)

vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(spam_processed['Text_Body'])
feature_names = vectorizer.get_feature_names()
dense = vectors.todense()
denselist = dense.tolist()
df_spam = pd.DataFrame(denselist, columns=feature_names)

df_total = df_ham.append(df_spam , ignore_index=True)
df_total = df_total.replace(np.nan, 0)

# split 
train, test  = train_test_split(df_total, test_size=0.2, random_state=42)

y_train = train['Type']
x_train = train.drop(['Type'], axis = 1)

y_test = test['Type']
x_test = test.drop(['Type'], axis = 1)

# train 

clf = GaussianNB()
clf.fit(x_train,y_train)
y_pred = clf.predict(x_test)
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
score = clf.score(x_test,y_test)
print("Score: " + str(score))
mse = metrics.mean_squared_error(y_test, y_pred)
rmse = math.sqrt(mse)
print("RMSE: "+ str(rmse))

titles_options = [("Confusion matrix, without normalization", None),
                  ("Normalized confusion matrix", 'true')]

for title, normalize in titles_options:
    disp = plot_confusion_matrix(clf, x_test, y_test,
                                 cmap=plt.cm.Blues,
                                 normalize=normalize)
    disp.ax_.set_title(title)
plt.show()

