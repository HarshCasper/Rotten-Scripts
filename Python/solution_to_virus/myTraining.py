import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import pickle

def data_split(data, ratio):
    np.random.seed(42)
    shuffled = np.random.permutation(len(data))
    test_set_size = int(len(data) * ratio)
    test_indices = shuffled[:test_set_size]
    train_indices = shuffled[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]

if __name__ == "__main__":
    
     df = pd.read_csv('data.csv.csv')
     train, test = data_split(df, 0.2)
     X_train = train[['FEVER','BODYPAIN','AGE','RUNNYNOSE','DIFFBREATH']].to_numpy()
     X_test = test[['FEVER','BODYPAIN','AGE','RUNNYNOSE','DIFFBREATH']].to_numpy()

     Y_train = train[['INFECTION PROBABILITY']].to_numpy().reshape(2500,)
     Y_test = test[['INFECTION PROBABILITY']].to_numpy().reshape(624,)

     clf = LogisticRegression()
     clf.fit(X_train, Y_train)
    
    

     #open a file where you want to store the data
     file = open('model1.pk1', 'wb')

     # dump information to that file
     pickle.dump(clf, file)
     file.close()






    