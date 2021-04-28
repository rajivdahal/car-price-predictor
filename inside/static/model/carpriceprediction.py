import pandas as pd
import numpy as np
car = pd.read_csv (r'C:\Users\MR.D\Desktop\Minorproject\static\datasets\data.csv')
car=car[['Brand','Model','Model_year','Transmission','Engine_size(cc)',
 'Drivetrain','Fuel_type','Lot_no','Kilometer','Price']]
car.dropna(inplace=True)
#getting information of all columns either objects or integer or float
#print(car.info())
print(car.shape) # printing no. of rows and columns of datasets

#finding mistakes in datasets one by one
#print(car['Brand'].unique()) #all good in dataset , object is named previously so good
#print(car['Model'].unique()) #all good in dataset , object is named previously so good
#print(car['Model_year'].unique()) #data is not good:and there is nan  at one place
#print(car['Transmission'].unique()) #data is not good: delete nan value and one empty place i.e ''
#print(car['Engine_size(cc)'].unique())#data is not good: delete . at last and nan value
#print(car['Drivetrain'].unique())# data is not good delete WD at last and nan value
#print(car['Fuel_type'].unique())#data is not good: delete nan value present
#print(car['Lot_no'].unique())
#print(car['Kilometer'].unique())#data is not good: delete empty values,nan values
#print(car['Price'].unique())# data is not good: delete Rs. , empty values and nan values

################cleaning the data############################################
car['Drivetrain']=car['Drivetrain'].astype(int)

car['Model_year']=car['Model_year'].astype(int)

car['Engine_size(cc)']=car['Engine_size(cc)'].astype(int)

car['Lot_no'].replace('', np.nan, inplace=True)
car['Lot_no']=car['Lot_no'].astype(int)

car['Kilometer'].replace(' ', np.nan, inplace=True)
car= car.dropna(subset=['Kilometer'])
car['Kilometer']=car['Kilometer'].astype(int)

car['Transmission'].replace(' ', np.nan, inplace=True)

car['Price']=car['Price'].astype(int)

#print(car.shape)
print(car.info())

#there is loss of 1 row data while data cleanning

####################end of data cleaning###############################
car.reset_index()
############getting x and y data########
X=car.drop(columns='Price')
y=car['Price']
############ end of getting x and y data########

########## seperating training and testing data#######
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=593)


########## end of seperating training and testing data#######

######### seperating integer data######
list1=[]
for col in X_train.columns:
  if X_train[col].dtypes!='O':
   list1.append(col)
#output: ['Model_year', 'Engine_size(cc)', 'Drivetrain', 'Lot_no', 'Kilometer']

#######end of seperating integer data#####

######### seperating object data######
list2=[]
for col in X_train.columns:
  if X_train[col].dtypes=='O':
   list2.append(col)
#print(list2)
# output;['Model_year', 'Engine_size(cc)', 'Drivetrain', 'Lot_no', 'Kilometer']
#######end of seperating integer data#####
#print(X_train[list1].head())
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer,ColumnTransformer
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
ohe=OneHotEncoder()
ww=ohe.fit(X[list2])
print(ww)
column_trans=make_column_transformer((OneHotEncoder(categories=ohe.categories_),list2),remainder='passthrough')
lr=LinearRegression()
pipe=make_pipeline(column_trans,lr)
pipe.fit(X_train ,y_train)
y_pred=pipe.predict(X_test)
print(y_pred)
print(r2_score(y_test,y_pred))
#score=[]
#for i in range(1000):
 #   X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state=i)
  #  lr = LinearRegression()
   # pipe = make_pipeline(column_trans, lr)
    #pipe.fit(X_train, y_train)
    #y_pred = pipe.predict(X_test)
    #score.append(r2_score(y_test,y_pred))
#print(np.argmax(score))
print(list2)
y=pipe.predict(pd.DataFrame([['Ford','figo',2011, ' Manual',1200, 2,' Petrol',9,22000]],columns=['Brand','Model','Model_year','Transmission','Engine_size(cc)','Drivetrain','Fuel_type','Lot_no','Kilometer']))
print(y)
import matplotlib.pyplot as plt
plt.scatter(X_train,y_train,color='red')
plt.plot(X_train,pipe.predict(X_train))
plt.show()