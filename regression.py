
import lightgbm as lgb
import xgboost as xgb
def run_lgb(train_X, train_y, val_X, val_y, test_X):
    params = {
        "objective" : "regression",
        "metric" : "rmse",
        "num_leaves" : 20,
        "learning_rate" : 0.008,
        "bagging_fraction" : 0.6,
        "feature_fraction" : 0.6,
        "bagging_frequency" : 6,
        "bagging_seed" : 42,
        "verbosity" : -1,
        "seed": 42
    }

    lgtrain = lgb.Dataset(train_X, label=train_y)
    lgval = lgb.Dataset(val_X, label=val_y)
    evals_result = {}
    model = lgb.train(params, lgtrain, 5000,
                      valid_sets=[lgtrain, lgval],
                      early_stopping_rounds=100,
                      verbose_eval=150,
                      evals_result=evals_result)

    pred_test_y = model.predict(test_X, num_iteration=model.best_iteration)
    return pred_test_y, model, evals_result


# pred_test, model, evals_result = run_lgb(dev_X, dev_y, val_X, val_y, X_test)


def run_xgb(train_X, train_y, val_X, val_y, test_X):
    params = {'objective': 'reg:linear',
          'eval_metric': 'rmse',
          'eta': 0.001,
          'max_depth': 10,
          'subsample': 0.6,
          'colsample_bytree': 0.6,
          'alpha':0.001,
          'random_state': 42,
          'silent': True}

    tr_data = xgb.DMatrix(train_X, train_y)
    va_data = xgb.DMatrix(val_X, val_y)

    watchlist = [(tr_data, 'train'), (va_data, 'valid')]
    evals_result={}
    model_xgb = xgb.train(params, tr_data, 200, watchlist, maximize=False,evals_result=evals_result,early_stopping_rounds = 100, verbose_eval=100)

    dtest = xgb.DMatrix(test_X)
    xgb_pred_y = model_xgb.predict(dtest, ntree_limit=model_xgb.best_ntree_limit)

    return xgb_pred_y, model_xgb,evals_result

# pred_test_xgb, model_xgb = run_xgb(dev_X, dev_y, val_X, val_y, X_test)

# def catboost():
#     cb_model = CatBoostRegressor(iterations=500,
#                              learning_rate=0.05,
#                              depth=10,
#                              eval_metric='RMSE',
#                              random_seed = 42,
#                              bagging_temperature = 0.2,
#                              od_type='Iter',
#                              metric_period = 50,
#                              od_wait=20)

#     cb_model.fit(dev_X, dev_y,
#              eval_set=(val_X, val_y),
#              use_best_model=True,
#              verbose=True)
# # pred_test_cat = cb_model.predict(X_test)
