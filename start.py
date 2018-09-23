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

from classification import *
from regression import *
from preprocessing import *
from prediction import predict


def task():
        task=0
        while task not in [1,2,3]:
            try:
                task=int(input('''
            Enter 1 for Classification
            Enter 2 for Regression
            Enter 3 to automatically detect the task \n'''))
            except ValueError:
                print("########## Please Enter Specified Numeric Values ############")
                task=0
        print("You selected :",task)
        return task



def process_task(task):
    if task==1:
        






def to_csv(df,test,sub):
	pred =predict(df,test)
	sub.iloc[:,-1]=pred
	print("### making submission to csv file ###")
	sub.to_csv('automlsub.csv',index=False)

	print("####################### Completed ###########################")
