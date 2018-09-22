import pandas as pd
import sys
import regex
from sklearn.model_selection import train_test_split
from sklearn import preprocessing, model_selection, metrics
from sklearn.ensemble import RandomForestRegressor
import numpy as np

df=pd.read_csv(sys.argv[1])

test=pd.read_csv(sys.argv[2])

sub=pd.read_csv(sys.argv[3])

from train import *





def preliminary(df,test):
	print('Shape of your dataset is',"train - ",df.shape," test - ",test.shape)
	print(df.dtypes)
	global original_dtypes
	original_dtypes=[i for i in df.dtypes]
	print('#'*40)
	print('Columns of your dataset')
	for i,j in enumerate(df.columns):
			print(i,":",j)
	print('#'*40)
	global target
	target=input('Enter the column name or Index of target variable\n')

def fill_missing(df,test):
	for i,j in enumerate(df.isnull().any()):
		if j==True:
			if df[df.columns[i]].dtypes=='object': 
				df[df.columns[i]].fillna(value=df[df.columns[i]].mode()[0], inplace=True)
				test[test.columns[i]].fillna(value=test[test.columns[i]].mode()[0], inplace=True)
			else:
				df[df.columns[i]].fillna(value=df[df.columns[i]].mean(), inplace=True)
				test[test.columns[i]].fillna(value=test[test.columns[i]].mean(), inplace=True)
	return df,test           

def onehot(df,test):	
	if len(df.columns)<500:
		for i in test.columns:
			if ((df[i].dtype==object) and (df[i].nunique()<1000)):
				df= pd.concat([df, pd.get_dummies(df[i], prefix=i[:3])], axis=1)
				test = pd.concat([test, pd.get_dummies(test[i], prefix=i[:3])], axis=1)			
	return df,test
def label_encode(df,test):
	for f in df.columns :
	        if (df[f].dtype=='object'):
	           
	            lbl = preprocessing.LabelEncoder()
	            lbl.fit(list(df[f].values))
	            df[f] = lbl.transform(list(df[f].values))
	            test[f] = lbl.transform(list(test[f].values))
	# _,original_dtypes=preliminary(df,test)
	new_datatypes=map(lambda x:np.int if x=="object" else x,original_dtypes)

	for i,j in zip(test.columns,list(new_datatypes)): 
			df[i]=df[i].astype(j) 
			test[i]=test[i].astype(j)
	return df,test                                   


def split(df,test,target):
	try :
		try:
			assert(type(int(target)))!= type(1) # if this gives value error than its a string so excecut beloe otherwise
		except ValueError:	
			X=df.drop([target],axis=1)
			Y=df[target]
	except AssertionError:
		X=df.drop(df.columns[int(target)], axis=1)
		Y=df.iloc[:,int(target)]
	return X,Y,test


def pipeline(df,test):
	# return split(onehot(label_encode(fill_missing(df,test))))
	# target,_=preliminary(df,test)
	print("#"*10," Please be patient.........(Processing in Background) ","#"*10)
	X,Y,test=split(df,test,target)
	X,test=fill_missing(X,test)
	X,test=label_encode(X,test)
	X,test=onehot(X,test)
	dev_X, val_X, dev_y, val_y = train_test_split(X,Y, test_size = 0.2, random_state = 42)
	return X,Y,dev_X, val_X, dev_y, val_y,test
# 
def predict(df,test):
	X,Y,dev_X, val_X, dev_y, val_y,test=pipeline(df,test)
	print("############## Running light GBM ###################")
	pred_test, model, evals_result_lgb = run_lgb(dev_X, dev_y, val_X, val_y,test)
	print("############## Running XGBOOST ###################")
	pred_test_xgb, model_xgb,evals_result_xgb = run_xgb(dev_X, dev_y, val_X, val_y,test)
	print("############## Final Score ###################")
	print("LGBM",":",min(evals_result_lgb['valid_1']["rmse"]))
	# print(evals_result.keys())
	print("XGB",":",min(evals_result_xgb['valid']['rmse']))

	print("Best Score will be selected")

	if min(evals_result_lgb['valid_1']["rmse"])<min(evals_result_xgb['valid']['rmse']):
		return pred_test
	else:
		return pred_test_xgb

def to_csv(df,test,sub):
	pred =predict(df,test)
	sub.iloc[:,-1]=pred
	print("### making submission to csv file ###")
	sub.to_csv('automlsub.csv',index=False)

	print("####################### Completed ###########################")

	# print(score)

preliminary(df,test)
to_csv(df,test,sub)




