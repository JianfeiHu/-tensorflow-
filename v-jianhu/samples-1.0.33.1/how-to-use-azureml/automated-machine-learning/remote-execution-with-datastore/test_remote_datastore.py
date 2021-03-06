# Test remote DataStore

# Copyright (c) Microsoft Corporation. All rights reserved.
#
# Licensed under the MIT License.

import logging
import os
import random
import time

from matplotlib import pyplot as plt
from matplotlib.pyplot import imshow
import numpy as np
import pandas as pd
from sklearn import datasets

import azureml.core
from azureml.core.experiment import Experiment
from azureml.core.workspace import Workspace
from azureml.train.automl import AutoMLConfig
from azureml.train.automl.run import AutoMLRun
from azureml.core.conda_dependencies import CondaDependencies
from azureml.core.runconfig import RunConfiguration
from checknotebookoutput import checkNotebookOutput

ws = Workspace.from_config()

# choose a name for the run history container in the workspace
experiment_name = 'automl-remote-datastore-file'
# project folder
project_folder = './sample_projects/automl-remote-datastore-file'

experiment = Experiment(ws, experiment_name)
automl_runs = list(experiment.get_runs(type='automl'))

assert(len(automl_runs) == 1)

ml_run = AutoMLRun(experiment=experiment, run_id=automl_runs[0].id)

properties = ml_run.get_properties()
status = ml_run.get_details()
assert(status['status'] == 'Completed')
assert(properties['num_iterations'] == '4')

children = list(ml_run.get_children())
for iteration in children:
    metrics = iteration.get_metrics()
    iteration_status = iteration.get_status()
    print(iteration.id)
    print(metrics['AUC_weighted'])
    assert(metrics['AUC_weighted'] > 0.6)
    assert(metrics['AUC_weighted'] <= 1.0)
    print(iteration_status)
    assert(iteration_status == 'Completed')

# Check the output cells of the notebook.
checkNotebookOutput('auto-ml-remote-execution-with-datastore.nbconvert.ipynb', 'warning', 'nan')
