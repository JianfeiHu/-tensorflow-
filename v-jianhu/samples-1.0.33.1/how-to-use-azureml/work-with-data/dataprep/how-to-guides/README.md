# How to use Data Prep SDK

This folder includes sample notebooks for key functionalities of Data Prep SDK.

## Table of Contents
- [Load Data](#load)
- [Explore Data](#explore)
- [Append and Join](#append)
- [Transform Data](#transform)
- [Advanced Transformation Powered by AI](#advanced-transform)
- [Write Data](#write)
- [Other Functionalities](#others)
- [Support](#support)

<a id="load"></a>
## Load Data
- [Data Ingestion](data-ingestion.ipynb) shows how to load data of different types, including txt, csv, excel, Parquet, json, Azure SQL, Azure Blob and pandas DataFrame.
- [Auto Read File](auto-read-file.ipynb) is a more advanced feature of Data Prep, which can take any text based file (including csv, txt, excel, json and parquet) and auto-detect how to parse the file. It will also attempt to auto-detect the types of each column and apply type transformations to the columns it detects.
- [Read From And Write To Datastores](datastore.ipynb).
- [Work With File Streams](working-with-file-streams.ipynb).
- [External Reference](external-references.ipynb) shows how to create and persist Dataflows that reference another Dataflow that has been persisted to a .dprep file.

<a id="explore"></a>
## Explore Data
- [Data Profile](data-profile.ipynb) collects summary statistics on each column of the data produced by a Dataflow, which can be used to understand the input data, identify anomalies and missing values.
- [Semantic Types](semantic-types.ipynb), including email address, US zip codes or IP address, can be recognized in Data Profile and then be split in specific ways.
- [Assertions](assertions.ipynb) shows how to create assertion rules to verify that our assumptions on the data continue to be accurate and, when not, to handle failures in a clean way.
- [Summarize](summarize.ipynb) data by providing you a synopsis based on aggregates over specific columns.

<a id="append"></a>
## Append and Join
- [Append Columns And Rows](append-columns-and-rows.ipynb) to concatenate two or more Dataflows.
- [Join](join.ipynb) two Dataflows.

<a id="transform"></a>
## Transform Data
- [Add Column Using Data Prep Expression](add-column-using-expression.ipynb) to calculate values for the new column from existing columns.
- [Filter](filtering.ipynb) columns or rows.
- [Column Manipulations](column-manipulations.ipynb) shows how to select, drop, duplicate, keep, map and rename columns.
- [Column Type Transforms](column-type-transforms.ipynb) shows how to convert column data types.
- [Impute Missing Values](impute-missing-values.ipynb).
- [Deal With Error, Null Values](replace-fill-error.ipynb).
- [Label Encoder](label-encoder.ipynb) to encode categorical values.
- [One Hot Encoder](one-hot-encoder.ipynb) to create a new binary column for each categorical label encountered in the selected column.
- [Min-Max Scaler](min-max-scaler.ipynb) to scale column values to a desired range (typically [0, 1]).
- [Quantile Transformation](quantile-transformation.ipynb) to transform the data into a normal or uniform distribution.
- [Custom Python Transforms](custom-python-transforms.ipynb) shows how to use custom python code for data transformations.

<a id="advanced-transform"></a>
## Advanced Transformation Powered by AI
- [Derive Column By Example](derive-column-by-example.ipynb) attempts to achieve the intended derivation inferred from provided examples.
- [Split Column By Example](split-column-by-example.ipynb) attempts to achieve the intended derivation inferred from provided examples.
- [Fuzzy Grouping](fuzzy-group.ipynb) adds a column where similar values from the source column are fuzzy-grouped to their canonical form.

<a id="write"></a>
## Write Data
- [Write Data](writing-data.ipynb) in delimited or Parquet files to Local File System, Azure Blob Storage, or Azure Data Lake Storage.

<a id="others"></a>
## Other Functionalities
- [Sampling And Subsetting](subsetting-sampling.ipynb) to work with a smaller portion of a Dataflow.
- [Random Split](random-split.ipynb) a data set into training and test data sets for machine learning.
- [Open And Save Dataflows](open-save-dataflows.ipynb) in order to persist a Dataflow and use it elsewhere.
- [Replace DataSource Reference](replace-datasource-replace-reference.ipynb) to re-apply the transformation steps saved in Dataflow to a different data set (typically production data). 
- [Cache](cache.ipynb) shows how to cache processed data to make local runs more efficient.
- [Provide Secrets](secrets.ipynb) to register the required secrets to use during Dataflow execution in a new session.

<a id="support"></a>
## Support
If you have any questions or feedback, send us an email at: [askamldataprep@microsoft.com](mailto:askamldataprep@microsoft.com).