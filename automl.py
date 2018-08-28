import pandas as pd
import sys
import regex
from sklearn.model_selection import train_test_split
from sklearn import preprocessing, model_selection, metrics


# with open(sys.argv[1]) as f:
# 	aa=pd.rea


df=pd.read_csv(sys.argv[1])
test=pd.read_csv(sys.argv[2])

def class_or_regress():
	print('Shape of your dataset is',df.shape)
	print('Columns of your dataset',df.columns)
	print('#'*40)
	target=input('Enter the column name or Index of target variable\n')
	try :
		try:
			assert(type(int(target)))!= type(1) # if this gives value error than its a string so excecut beloe otherwise
		except ValueError:	
			X=df.drop([target],axis=1)
			Y=df[target]
	except AssertionError:
		X=df.drop(df.columns[int(target)], axis=1)
		Y=df.iloc[:,int(target)]
	print('Shape',X.shape,Y.shape)
	print('#'*40)
	print(X.head(),Y)

	print('#'*40)
	print('Specify the task - Regression or Classification ')
	def task():
		try:
			task=int(input('''
Enter 1 for Classification
Enter 2 for Regression
Enter 3 to automatically detect the task \n'''))
			return task	

		except ValueError:
			print('please enter numeric values')
			print('#'*40)
		if task not in [1,2,3]:
			print('please renter the specified number')
			task()	

	return task()	

# class_or_regress()

def remove_ids():
	id_cols=[]
	for i in df.columns:
	    if df[i].nunique()==df.shape[0]
	        id_cols.append(i)
	if id_cols!=[]:        
		df.drop(id_cols,axis=1,inplace=True)        


def constant_column():
	colsToRemove = []
	for col in df.columns:
	        if df[col].std() == 0: 
	            colsToRemove.append(col)
	        
	df.drop(colsToRemove, axis=1, inplace=True)
	test.drop(colsToRemove, axis=1, inplace=True) 

def drop_sparse():
    flist = [x for x in df.columns]
    for f in flist:
        if len(np.unique(df[f]))<2:
            df.drop(f, axis=1, inplace=True)
            test.drop(f, axis=1, inplace=True)
    return df, test

def label_encode():
	for f in df.columns :
	        if (df[f].dtype=='object'):
	           
	            lbl = preprocessing.LabelEncoder()
	            lbl.fit(list(df[f].values))
	            df[f] = lbl.transform(list(df[f].values))
	            test[f] = lbl.transform(list(test[f].values))


print(class_or_regress())