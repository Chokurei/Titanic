#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 22:21:10 2017

@author: kaku
"""

import os
import pandas as pd

data_path = '../data/'
test_path = data_path + 'test.csv'
train_path = data_path + 'train.csv'
submission_path = data_path + 'gender_submission.csv'

train_data = pd.read_csv(train_path)
test_data = pd.read_csv(test_path)
submission_data = pd.read_csv(submission_path)