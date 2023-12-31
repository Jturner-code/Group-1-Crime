import numpy as np
import pandas
from scipy import stats
from sklearn.metrics import log_loss
from sklearn.model_selection import train_test_split
from DataConstruction import construct_cat_value
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

train_data = construct_cat_value('./train.csv/train.csv', ['Category', 'Descript', 'DayOfWeek', 'PdDistrict',
                                                           'Resolution'])

train_data['Address'] = train_data['Address'].str.replace(r'[0-9]+ Block of ', '', regex=True)
train_data['Address'] = train_data['Address'].astype('category')
train_data['Address'] = train_data['Address'].cat.codes

train_data['Dates'] = pandas.to_datetime(train_data['Dates'])
train_data['Hours'] = train_data['Dates'].dt.hour
train_data['Minutes'] = train_data['Dates'].dt.minute
train_data['Month'] = train_data['Dates'].dt.month
train_data['Year'] = train_data['Dates'].dt.year

train_data = train_data[(np.abs(stats.zscore(train_data['X'])) < 3)]
train_data = train_data[(np.abs(stats.zscore(train_data['Y'])) < 3)]

x_all = train_data.drop(['Category', 'Descript', 'Resolution', 'Dates'], axis=1)
y_all = train_data['Category']

x_train, x_test, y_train, y_test = train_test_split(x_all, y_all, test_size=0.25, random_state=42)

std = StandardScaler()
x_train['X'] = std.fit_transform(x_train[['X']])
x_test['X'] = std.transform(x_test[['X']])
x_train['Y'] = std.fit_transform(x_train[['Y']])
x_test['Y'] = std.transform(x_test[['Y']])

k_value = 100
classifier = KNeighborsClassifier(n_neighbors=k_value, weights='distance', metric='euclidean')
classifier.fit(x_train, y_train)

y_pred = classifier.predict_proba(x_test)
print("K-Value " + str(k_value) + ": ")
print(log_loss(y_test, y_pred))
