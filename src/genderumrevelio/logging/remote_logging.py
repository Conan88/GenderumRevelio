#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json
import requests


def remote_log(log):
    """TODO: Docstring for remote_log.
    :returns: TODO

    """
    """Setup for post request"""
    pk_id = 1
    headers = {'Content-type': 'application/json'}
    address = "http://188.166.124.208/logging/"

    """Getting the data from keras"""
    trainingdata = log[0]
    final_acc = log[1]
    score = log[2]

    """Extracting the data"""
    val_loss = trainingdata['val_loss']
    val_acc = trainingdata['val_acc']
    loss = trainingdata['loss']
    acc = trainingdata['acc']

    """Send finalscore"""
    json_data = json.dumps({"logging_id":pk_id, "final_acc":final_acc, "score":score})
    r = requests.post(address, data = json_data, headers = headers)

    """Send trainingdata"""
    for i in range(0, len(val_acc)):
        json_data = json.dums({"epoch":i, "val_loss":val_loss[i], "val_acc":val_acc[i],
                               "loss":loss[i], "acc":acc[i], "fk_finalscore":pk_id})
        r = requests.post(address, data = json_data, headers = headers)

