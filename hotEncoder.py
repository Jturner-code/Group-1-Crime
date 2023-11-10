import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from numpy import savetxt

# Import the data required from a CSV file named 'adultDataCorrected.csv' into a Pandas DataFrame
data = pd.read_csv('train.csv')

# Convert categorical columns to category data type and create new numerical columns
# These new numerical columns will contain the category codes of the original categorical data
data['Dates'] = data['Dates'].astype('category')
data['Catagory'] = data['Catagory'].astype('category')
data['Descript'] = data['Descript'].astype('category')
data['DayOfWeek'] = data['DayOfWeek'].astype('category')
data['PdDistrict'] = data['PdDistrict'].astype('category')
data['Resolution'] = data['Resolution'].astype('category')
data['Address'] = data['Address'].astype('category')
data['X'] = data['X'].astype('category')
data['Y'] = data['Y'].astype('category')

# data['Dates_new'] = data['Dates'].cat.codes
# data['Catagory_new'] = data['Catagory'].cat.codes
# data['Descript_new'] = data['Descript'].cat.codes
# data['DayOfWeek_new'] = data['DayOfWeek'].cat.codes
# data['PdDistrict_new'] = data['PdDistrict'].cat.codes
# data['Resolution_new'] = data['Resolution'].cat.codes
# data['Address_new'] = data['Address'].cat.codes
# data['X_new'] = data['X'].cat.codes
# data['Y_new'] = data['Y'].cat.codes

# Create an instance of the OneHotEncoder
encoder = OneHotEncoder()

# Perform one-hot encoding on selected columns and convert the result to a DataFrame
enc_data = pd.DataFrame(encoder.fit_transform(data[['Dates_new', 'Catagory_new',
                                                    'Descript_new', 'DayOfWeek_new',
                                                    'PdDistrict_new', 'Resolution_new', 'Address_new',
                                                    'X_new', 'Y_new']]).toarray())

# Join the original data DataFrame with the encoded DataFrame to create a new DataFrame
New_df = data.join(enc_data)

# # Print the new DataFrame
print(New_df)

# # Extract only the numerical part of New_df to a CSV file
# numerical_data = New_df.select_dtypes(include=[np.number])

# # Get the column labels (column names) of the numerical_data DataFrame
# column_labels = numerical_data.columns.tolist()

# # Convert New_df to a NumPy array
# compatibleArr = numerical_data.values

# # Save the NumPy array to a CSV file named 'hotData.csv'
# savetxt('hotData.csv', compatibleArr, delimiter=',')

# # Print the column labels
# print("Column Labels:", column_labels)
