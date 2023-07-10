import numpy as np
import pandas as pd
import os
from pathlib import Path

from sklearn.model_selection import train_test_split

import pickle
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder


import csv
from django.http import HttpResponse


def Pre_process(data):

    # Remove unnecessary feature
    # data = data.drop(['isFlaggedFraud' , "step"] , axis =1)

    # One hot encoding
    dummies = pd.get_dummies(data["type"], prefix="Type")
    data = pd.concat([data, dummies], axis=1)
    data = data.drop("type", axis=1)

    # Label Encoding
    le = LabelEncoder()
    data['nameOrig'] = le.fit_transform(data['nameOrig'])
    data['nameDest'] = le.fit_transform(data['nameDest'])

    # Feature Scaling
    mms = MinMaxScaler()
    data[["amount", "nameOrig", "oldbalanceOrg", "newbalanceOrig",	"nameDest",	"oldbalanceDest",	"newbalanceDest"]] = mms.fit_transform(
        data[["amount", "nameOrig", "oldbalanceOrg", "newbalanceOrig",	"nameDest",	"oldbalanceDest",	"newbalanceDest"]])

    return data


def check(path):

    # "/content/drive/MyDrive/Project Fraud/Test_Transaction.csv"
    Transaction = pd.read_csv(path)

    Processed_transaction = Pre_process(Transaction)

    base_dir = Path(__file__).resolve().parent.parent

    model_path = os.path.join(base_dir, "fraud_detection_model_RF.pkl")

    with open(model_path, 'rb') as file:
        model = pickle.load(file)

    mapping = {1: 'Fraud Transaction', 0: 'Legimate Transaction'}
    Transaction["Prediction Result"] = model.predict(Processed_transaction)

    Transaction["Prediction Result"] = Transaction["Prediction Result"].replace(
        mapping)

    transaction_summery = Transaction.to_csv()

    response = HttpResponse(transaction_summery,content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="transaction_summery.csv"'

    return response
