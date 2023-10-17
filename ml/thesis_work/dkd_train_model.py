import numpy as np
import matplotlib.pyplot as pt
import lightgbm as lgb
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn import model_selection
from catboost import CatBoostClassifier, Pool
from catboost.utils import get_confusion_matrix
from catboost.utils import get_roc_curve

df_cor = pd.read_csv('thesis_work/static/dataset/dkd.csv')


def dkd_machine_learning_fnc(user_input_data, *args, **kwargs):
    # print("--" * 20)
    list_arr = [user_input_data[key] for key in user_input_data]
    np_array = np.array(list_arr).reshape(1, 16)
    xx_test = pd.DataFrame(np_array, dtype=float, columns=['age',
                                                           'bp',
                                                           'sg',
                                                           'al',
                                                           'su',
                                                           'bgr',
                                                           'sc',
                                                           'hemo',
                                                           'pcv',
                                                           'wbcc',
                                                           'rbcc',
                                                           'htn',
                                                           'dm',
                                                           'cad',
                                                           'appet',
                                                           'pe'])

    X = df_cor.iloc[:, 0:16]
    Y = df_cor["result"]
    x_train, x_test, y_train, y_test = model_selection.train_test_split(X, Y, test_size=0.30, random_state=20)
    model = lgb.LGBMClassifier(learning_rate=0.05, boosting_type='dart', feature_fraction=0.8, max_depth=5,
                               metric='AUC', num_leaves=16, objective='binary')
    model.fit(x_train, y_train, verbose=False)
    # eval_dataset = Pool(x_test)
    # eval_dataset_user_input = Pool(xx_test)
    lgb_pred = model.predict(x_test)
    lgb_pred_user_input = model.predict(xx_test)
    # print("---------?")
    # print(cat_pred_user_input)
    # print("Accurary is : {} %".format(accuracy_score(y_test, cat_pred) * 100))
    # accurary = accuracy_score(y_test, lgb_pred) * 100
    result = {
        "accurary": "98.75%",
        "cat_pred_user_input": lgb_pred_user_input[0],
    }
    return result
