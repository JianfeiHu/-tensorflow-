# Test remote run

# Copyright (c) Microsoft Corporation. All rights reserved.
#
# Licensed under the MIT License.

from checknotebookoutput import checkNotebookOutput
from checkexperimentresult import checkExperimentResult

checkExperimentResult(experiment_name='automl-remote-dsvm',
                      expected_num_iteration='20',
                      expected_minimum_score=0.9,
                      metric_name='AUC_weighted')

# Check the output cells of the notebook.
checkNotebookOutput('auto-ml-remote-execution.nbconvert.ipynb', 'warning', 'nan')
