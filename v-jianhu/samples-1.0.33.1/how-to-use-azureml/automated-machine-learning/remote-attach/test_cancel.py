# Test cancel of remote run

# Copyright (c) Microsoft Corporation. All rights reserved.
#
# Licensed under the MIT License.

import logging
import os
import random
import time
from azureml.core.compute import ComputeTarget, RemoteCompute

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
from azureml.widgets import RunDetails
from checknotebookoutput import checkNotebookOutput

if __name__ == "__main__":
    ws = Workspace.from_config()

    print(ws.resource_group)
    print(ws.subscription_id)

    # choose a name for the run history container in the workspace
    experiment_name = 'automl-remote-attach'
    # project folder
    project_folder = './sample_projects/automl-remote-attach'

    experiment = Experiment(ws, experiment_name)
    automl_runs = list(experiment.get_runs(type='automl'))

    assert(len(automl_runs) == 1)

    compute_name = 'mydsvmb'

    dsvm_compute = ws.compute_targets[compute_name]

    # create a new RunConfig object
    conda_run_config = RunConfiguration(framework="python")

    # Set compute target to the Linux DSVM
    conda_run_config.target = dsvm_compute

    cd = CondaDependencies.create(pip_packages=['azureml-sdk[automl]'], conda_packages=['numpy'])
    conda_run_config.environment.python.conda_dependencies = cd

    automl_settings = {
        "iteration_timeout_minutes": 60,
        "iterations": 100,
        "n_cross_validations": 5,
        "primary_metric": 'AUC_weighted',
        "preprocess": True,
        "max_cores_per_iteration": 2
    }

    automl_config = AutoMLConfig(task='classification',
                                 path=project_folder,
                                 run_configuration=conda_run_config,
                                 data_script=project_folder + "/get_data.py",
                                 **automl_settings)

    remote_run = experiment.submit(automl_config)

    # Canceling runs
    #
    # You can cancel ongoing remote runs using the *cancel()* and *cancel_iteration()* functions

    print(remote_run.id)

    time.sleep(180)

    # Cancel the ongoing experiment and stop scheduling new iterations
    remote_run.cancel()

    print('run cancelled')

    # Wait for the run to complete.  It should complete soon because it has been canceled.
    remote_run.wait_for_completion()

    children = list(remote_run.get_children())

    print(len(children))

    if(len(children) == 100):
        raise Exception('Run wasnt cancelled properly, child run count is 100 should have been less than 100')

    # Check the output cells of the notebook.
    checkNotebookOutput('auto-ml-remote-attach.nbconvert.ipynb', 'warning', 'nan')
