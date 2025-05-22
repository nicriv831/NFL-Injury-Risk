

# Library imports

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
pd.set_option('display.max_columns', None)

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler, FunctionTransformer, MinMaxScaler
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from imblearn.over_sampling import SMOTE
from imblearn.pipeline import make_pipeline as make_imb_pipeline
from imblearn.pipeline import Pipeline as ImbPipeline
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection  import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline

import shap
import xgboost as xgb

from sklearn import set_config
set_config(transform_output='pandas')

# Model classification/metric function

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, classification_report, ConfusionMatrixDisplay

def eval_classification(model, X_train, y_train, X_test, y_test, model_name = 'model', results_frame = None, pos_label=1, average='binary', roc_auc_avg = 'macro'):

  model.fit(X_train, y_train)
  train_pred = model.predict(X_train)
  test_pred = model.predict(X_test)

  if y_train.nunique() > 2 and average == 'binary':
    average = 'macro'

  print('Train Evaluation')
  print(classification_report(y_train, train_pred))
  ConfusionMatrixDisplay.from_predictions(y_train, train_pred, normalize='true', cmap='Blues')
  plt.show()

  print('Test Evaluation')
  print(classification_report(y_test, test_pred))
  ConfusionMatrixDisplay.from_predictions(y_test, test_pred, normalize='true', cmap='Greens')
  plt.show()

  results = pd.DataFrame(index=[model_name])
  results['train_acc'] = accuracy_score(y_train, train_pred)
  results['test_acc'] = accuracy_score(y_test, test_pred)
  results['train_prec'] = precision_score(y_train, train_pred, pos_label=pos_label, average=average)
  results['test_prec'] = precision_score(y_test, test_pred, pos_label=pos_label, average=average)
  results['train_recall'] = recall_score(y_train, train_pred, pos_label=pos_label, average=average)
  results['test_recall'] = recall_score(y_test, test_pred, pos_label=pos_label, average=average)
  results['train_f1'] = f1_score(y_train, train_pred, pos_label=pos_label, average=average)
  results['test_f1'] = f1_score(y_test, test_pred, pos_label=pos_label, average=average)
  results['train_auc'] = roc_auc_score(y_train, model.predict_proba(X_train)[:,1], average=roc_auc_avg, multi_class='ovr')
  results['test_auc'] = roc_auc_score(y_test, model.predict_proba(X_test)[:,1], average=roc_auc_avg, multi_class='ovr')

  if results_frame is not None:
    results = pd.concat([results_frame, results])

  return results

# Correlation function

def corr(df, df_col):
  corr_mat = df.select_dtypes(include='number').corr()
  corr_df = pd.DataFrame()
  corr_df['raw'] = corr_mat[df_col]
  corr_df['abs'] = corr_mat[df_col].abs()
  return corr_df.sort_values(by='abs', ascending=False)
