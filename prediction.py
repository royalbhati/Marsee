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
