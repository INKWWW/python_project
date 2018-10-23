#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Reference  https://www.kaggle.com/tanitter/grid-search-xgboost-with-scikit-learn

from __future__ import division
import sys
import os
import pandas as pd
import numpy as np

from sklearn.cross_validation import StratifiedShuffleSplit,cross_val_score
from sklearn.metrics.scorer import make_scorer
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import roc_curve, roc_auc_score, accuracy_score, scorer
import xgboost as xgb


class XGBoostClassifier(object):
    def __init__(self, **params):
        self.clf = None
        self.params = params


    def fit(self, X, y, num_boost_round=10):
        num_boost_round = self.params.get('num_boost_round') if self.params.get('num_boost_round') else num_boost_round
        dtrain = xgb.DMatrix(X, label=y,missing=-99.0)
        self.classes_ = set(y)
        watchlist = [(dtrain,'train')]
        if self.params.get('objective') == 'binary:logistic':
            self.clf = xgb.train(params=self.params, dtrain=dtrain,\
                                 num_boost_round=num_boost_round,early_stopping_rounds=20,\
                                 evals=watchlist, feval=ks_score_log, maximize=True)
        else:
            self.params.update({'num_class': len(self.classes_)})
            self.clf = xgb.train(params=self.params, dtrain=dtrain, num_boost_round=num_boost_round, early_stopping_rounds=20,\
                                 evals=watchlist, feval=ks_score_mul, maximize=True)

    # def predict(self, X):
    #     # num2label = {i: label for label, i in self.label2num.items()}
    #     Y = self.predict_proba(X)
    #     y = np.argmax(Y, axis=1)
    #     return np.array([num2label[i] for i in y])

    def predict_proba(self, X):
        dtest = xgb.DMatrix(X,missing=-99.0)
        if self.params.get('objective') == 'binary:logistic':
            classone_predictions = self.clf.predict(dtest)
            classzero_predictions = 1.0 - classone_predictions
            return np.vstack((classzero_predictions,classone_predictions)).transpose()
        else:
            return self.clf.predict(dtest)

    def score(self, X, groud_truth):
        fpr, tpr, thresholds= roc_curve(groud_truth, self.predict_proba(X)[:,1], pos_label=1)
        return  max(abs(fpr-tpr))

    def get_params(self, deep=True):
        return self.params

    def set_params(self, **params):
        if 'num_boost_round' in params:
            self.num_boost_round = params.pop('num_boost_round')
        if 'objective' in params:
            del self.params['objective']
        self.params.update(params)
        return self

def ks_score_log(pred_probs, dtrain):
    fpr, tpr, thresholds= roc_curve(dtrain.get_label(), pred_probs, pos_label=1)
    return  'ks_score', max(abs(fpr-tpr))

def ks_score_mul(pred_probs, dtrain):
    fpr, tpr, thresholds= roc_curve(dtrain.get_label(), pred_probs[:,1], pos_label=1)
    return  'ks_score', max(abs(fpr-tpr))

def my_custom_score(ground_truth, predictions):
    fpr,tpr,thresholds=roc_curve(ground_truth,predictions[:,1])
    ks = max(abs(tpr-fpr))
    return ks
ks_scorer = make_scorer(my_custom_score, greater_is_better=True,needs_proba=True)

def model_gridsearch():

    df_kmeans_missing = pd.read_csv('../../Total_Features.csv')
    d_feature = df_kmeans_missing.drop(['uid','status'],axis=1).values
    d_target = df_kmeans_missing.status.values.ravel()
    skf = StratifiedShuffleSplit(d_target, 5, test_size=0.25, random_state=0)

    clf = XGBoostClassifier(
        objective = 'multi:softprob',
        #objective = 'binary:logistic',
        nthread = 4,
        seed = 0,
        silent = 1
        )

    """parameters = {
        'objective':['binary:logistic','multi:softprob'],
        'num_boost_round': [100, 250, 500, 1000,2000],
        'eta': [0.01, 0.05, 0.1, 0.5],
        'max_depth': [4,5,6,7,8],
        'subsample': [0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
        'colsample_bytree': [0.3, 0.4,0.5, 0.6, 0.7, 0.8],
        'colsample_bylevel':[0.3, 0.4,0.5, 0.6, 0.7, 0.8],
        'gamma': [i/20 for i in range(0,10,2)],
        'lambda':[i/10 for i in range(0,20,2)],
        'alpha': [1e-5,1e-3,0.1,1,10],
        'scale_pos_weight':[6,7,8,9],
        'min_child_weight':range(1,6)
    }"""
    parameters = {
        'objective':['binary:logistic'],
        'num_boost_round': [100, 250],
        'eta': [0.01, 0.05, 0.1],
        'max_depth': [4,5,6,7,8],
        'subsample': [0.5, 0.6, 0.7, 0.8],
        'colsample_bytree': [0.3, 0.4,0.5, 0.6],
        'colsample_bylevel':[0.3, 0.4,0.5, 0.6],
        'gamma': [0.0,0.01,0.1],
        'lambda':[0.01,0.1,1],
        'alpha': [1e-3,0.1,1,10],
        'scale_pos_weight':[6,7,8,9],
        'min_child_weight':range(1,6)
    }

    grid = GridSearchCV(clf, parameters, n_jobs=10,
                       iid=False,cv=skf,verbose=2)
    grid.fit(d_feature, d_target)
    best_parameters, score, _ = max(grid.grid_scores_, key=lambda x: x[1])
    print('score:', score)
    for param_name in sorted(best_parameters.keys()):
        print("%s: %r" % (param_name, best_parameters[param_name]))


def model_crossvalidation():
    df_kmeans_missing = pd.read_csv('../../Total_Features.csv')
    d_feature = df_kmeans_missing.drop(['uid','status'],axis=1).values
    d_target = df_kmeans_missing.status.values.ravel()
    skf = StratifiedShuffleSplit(d_target, 5, test_size=0.25, random_state=0)

    clf = XGBoostClassifier(
        num_boost_round = 2000,
    #objective = 'multi:softprob',
       **{'objective':'binary:logistic',
        'nthread':4,
        'seed':0,
        'silent':1})

    clf.set_params(**{'max_depth':4,'min_child_weight':4,\
                   'colsample_bytree':0.62,'subsample':0.95,\
                   'lambda':0.083,'alpha':1,'gamma':0.00,\
                   'scale_pos_weight':1,'eta':0.01})

    #scores =cross_val_score(clf, d_feature, d_target, scoring=ks_scorer,cv=skf,fit_params={'num_boost_round':1000})
    scores =cross_val_score(clf, d_feature, d_target, scoring=ks_scorer,cv=skf)
    print(scores)
    print(np.mean(scores))

def model_output():
    """ loading data"""
    DATA_DIR = '../../../DATA'
    SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
    DIR_PATH = os.path.normpath(os.path.join(SCRIPT_DIR, DATA_DIR))
    train_data = pd.read_csv(os.path.join(DIR_PATH,'train_.csv'))
    test_data = pd.read_csv(os.path.join(DIR_PATH,'test3000.csv'))

    """ features and targets"""
    train_feature = train_data.fillna(-99.0).drop(['uid','status'],axis=1).values
    train_target = train_data.status.values.ravel()
    test_feature = test_data.fillna(-99.0).drop(['uid','status'],axis=1).values
    test_target = test_data.status.values.ravel()

    clf = XGBoostClassifier(
        num_boost_round = 2000,
    #objective = 'multi:softprob',"""
        objective = 'binary:logistic',
        nthread = 4, seed = 0, silent = 1)

    clf.set_params(**{'max_depth':4,'min_child_weight':4,\
               'colsample_bytree':0.62,'subsample':0.95,\
               'lambda':0.083,'alpha':1,'gamma':0.00,\
               'scale_pos_weight':1,'eta':0.01})

    clf.fit(train_feature,train_target)
    print (my_custom_score(test_target,clf.predict_proba(test_feature)))


if __name__ == '__main__':
    print(os.getcwd())


    # model_output()
