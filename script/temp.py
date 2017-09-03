#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 22:21:10 2017
Just trial
@author: kaku
"""

import os
import pandas as pd

data_path = '../data/'
test_path = data_path + 'test.csv'
train_path = data_path + 'train.csv'
submission_path = data_path + 'gender_submission.csv'

train = pd.read_csv(train_path)
test = pd.read_csv(test_path)
submission = pd.read_csv(submission_path)

survived = train[train['Survived']==1]
not_survived = train[train['Survived']==0]

print ("Survived: %i (%.1f%%)"%(len(survived), float(len(survived))/len(train)*100.0))
print ("Not Survived: %i (%.1f%%)"%(len(not_survived), float(len(not_survived))/len(train)*100.0))
print ("Total: %i"%len(train))


train.groupby('Pclass').Survived.value_counts()