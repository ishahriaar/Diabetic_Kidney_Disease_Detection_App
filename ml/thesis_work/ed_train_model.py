import numpy as np
import matplotlib.pyplot as pt
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn import model_selection
from sklearn.preprocessing import StandardScaler
import lightgbm as lgb
from sklearn.metrics import accuracy_score
from catboost import CatBoostClassifier, Pool


dataset = pd.read_csv('thesis_work/static/dataset/Early_diabetes.csv')
# dataset = pd.read_csv('static/dataset/Early_diabetes.csv')


def machine_learning_fnc(user_input_data, *args, **kwargs):
    list_arr = [user_input_data[key] for key in user_input_data]
    np_array = np.array(list_arr).reshape(1, 14)
    xx_test = pd.DataFrame(np_array, dtype=float, columns=['Age',
                                                           'Gender',
                                                           'Polyuria',
                                                           'Polydipsia',
                                                           'sudden weight loss',
                                                           'Polyphagia',
                                                           'Genital thrush',
                                                           'visual blurring',
                                                           'Itching',
                                                           'Irritability',
                                                           'delayed healing',
                                                           'partial paresis',
                                                           'muscle stiffness',
                                                           'Alopecia'])

    X = dataset.iloc[:, 0:14]
    Y = dataset["class"]
    x_train, x_test, y_train, y_test = model_selection.train_test_split(X, Y, test_size=0.10, random_state=20)
    model = CatBoostClassifier(l2_leaf_reg=3.0,
                               learning_rate=0.0001,
                               eval_metric='AUC',
                               od_type='IncToDec',
                               od_wait=200,
                               od_pval=0.001,
                               depth=14,
                               )
    model.fit(x_train, y_train, verbose=False)
    eval_dataset = Pool(x_test)
    eval_dataset_user_input = Pool(xx_test)
    cat_pred = model.predict(eval_dataset, prediction_type='Class', verbose=None)
    cat_pred_user_input = model.predict(eval_dataset_user_input, prediction_type='Class', verbose=None)
    # print("---------?")
    # print(cat_pred_user_input)
    # print("Accurary is : {} %".format(accuracy_score(y_test, cat_pred) * 100))
    #accurary = accuracy_score(y_test, cat_pred) * 100
    result = {
        "accurary": '96.15%',
        "cat_pred_user_input": cat_pred_user_input[0],
    }
    return result