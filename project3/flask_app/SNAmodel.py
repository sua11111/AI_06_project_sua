import pandas as pd
import numpy as np
import pickle

df = pd.read_csv('Social_Network_Ads.csv') #Social_Network_Ads.csv

# 원핫인코딩 - 범주형 데이터를 모형이 인식할 수 있도록 숫자형으로 변경
# male, female -> [0, 1], [1, 0]
onehot_sex = pd.get_dummies(df['Gender'])
df = pd.concat([df, onehot_sex], axis=1)

# 기존 컬럼 삭제 # User ID 칼럼은 y값을 예측하는데 전혀 도움이 되지 않음
df.drop(['Gender','User ID'], axis=1, inplace=True)

from sklearn.preprocessing import StandardScaler

# 수치형 데이터 정규화
scaler = StandardScaler()
df[['Age', 'EstimatedSalary']] = scaler.fit_transform(df[['Age', 'EstimatedSalary']])

#분리
X = df[['Age','EstimatedSalary','Female','Male']]
y = df['Purchased']

#traing, test data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=77)

#boost 
from sklearn.ensemble import GradientBoostingClassifier

boost = GradientBoostingClassifier(max_depth=3, learning_rate=0.05)
boo = boost.fit(X_train, y_train)

pickle.dump(boo, open('sna.pkl', 'wb'))
#boost.predict


#from keras.models import Sequential
#from keras.layers import Dense
# 모델 구성
#model = Sequential()
#model.add(Dense(10, input_dim=4, activation='relu'))
#model.add(Dense(5, activation='relu'))
#model.add(Dense(1, activation='sigmoid')) # 이진분류 sigmoid

#model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

#history = model.fit(X_train, y_train, epochs=160,batch_size=16)