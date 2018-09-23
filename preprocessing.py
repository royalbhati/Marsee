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




	# print(score)

preliminary(df,test)
to_csv(df,test,sub)
