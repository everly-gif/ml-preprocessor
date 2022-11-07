# ML Preprocessor

## Abstract
Using raw data reduces prediction accuracy. Therefore, data preprocessing is considered essential. On analyzing the challenges faced in usual data preprocessing methods, our project aims at developing a Command Line Interface also known as CLI for data preprocessing to save time and improve workspace efficiency. Data preprocessing is a crucial step before running the data into any ML model as the quality of data and the useful information being given to the model directly affects the ability of the model to learn. This process in considered time consuming by many analysts and developers and hence there is a need to efficiently carry out such tasks. This CLI will focus on applying the crucial data preprocessing steps such as handing null values in the dataset, encoding categorical data, feature scaling and also taking inputs and giving users the ability to download data preprocessed datasets.

## Problem Statement
Data preprocessing is a tedious yet integral part of building an ML model as the quality of data and the useful information being given to the model directly affects the ability of the model to learn. This process in considered time consuming by many analysts and developers and hence there is a need to efficiently carry out such tasks. 

## Objectives
To create a MVP/Working model of a CLI tool that will improve workspace efficiency by addressing the challenges that was discussed earlier. It will abstract the process of data preprocessing in such a way that by giving simple commands in the command prompt the user will be able to download their preprocessed data.

## Proposed Work
This section presents the objective of this project and the innovation we have brought in when compared to the existing models in the data pre-processing domains. The data collected from the real world is noisy, inconclusive, and inconsistent. Preprocessing data prior to prediction is therefore necessary to ensure accuracy. Data preprocessing is described in the literature as data reduction, data integration, cleansing, and transformation. However, it is not required to apply all four procedures toa single dataset. The procedures involved in data preparation are decided by the type and nature of the data set.

Data preprocessing tries to enhance the quality and meaning of the data. Problems with noisy data are fixed during the data cleaning stage. 
When gathering data from several data sources, a data integration process is also employed. Data is converted between formats during the data conversion stage,
and data size is decreased at the data reduction stage. The explanation above leads to the conclusion that each data preprocessing stage has distinctive 
qualities and a unique significance. Additionally, it appears that data preprocessing processes extend computing time. The main purpose of our project is 
to eradicate the additional time taken to preprocess the data by individually performing various steps involved in the usual methods.
This simple CLI tool will save your time so that you can utilize it in applying different machine learning algorithms i.e., 
reducing the total computation time of the model. This tool implements command line instructions to preprocess data such that a 
data scientist can preprocess the data without writing the code. Besides that, this tool can be extended to also provide advanced features such
as univariate analysis along with graph plotting, bivariate analysis, and data wrangling as a future scope.


## Architecture/Block Diagram of the proposed model
<p align="center">
<img src="https://user-images.githubusercontent.com/77877486/199954041-1881fbc9-dea7-4f0c-8487-44826ba18958.png" width=350px/>
</p>

## Requirements

Have python3 and pip installed locally. 

## Execution

1. Fork this repository or download the code zip file.<br><br>
2. Clone the repository if forked.
```bash
git clone https://github.com/<username>/ml-preprocessor.git
```
3. Navigate to base folder `ml-preprocessor` and execute below command

```python
pip install --editable .
```
4. Enter into the cli by typing `preprocesscli` in the terminal.

5. Move your dataset within this directory and start preprocessing your dataset with simple commands!

## Screenshots

![](https://user-images.githubusercontent.com/77877486/199954854-04c08b93-9ca9-4000-9f59-a632b5940624.png)
![](https://user-images.githubusercontent.com/77877486/199955026-a9e125b5-cf6b-407c-9d87-4e245e2cc469.png)
![](https://user-images.githubusercontent.com/77877486/199955054-76afcbe0-9ec8-4310-8522-6cc2696fdb2e.png)
![](https://user-images.githubusercontent.com/77877486/199955083-9ed416a9-0856-4f67-b1c9-114ea03c6990.png)
![](https://user-images.githubusercontent.com/77877486/199955156-5900ded4-44fd-4c28-934b-c96b66645cb2.png)
![](https://user-images.githubusercontent.com/77877486/199955194-7b9940ce-34b3-4399-af8a-4e09239200c1.png)
![](https://user-images.githubusercontent.com/77877486/199955269-6ad5b373-458f-4a2a-9b0b-25590dffae46.png)
![](https://user-images.githubusercontent.com/77877486/199954688-834cea76-d211-4b8b-ab92-90935c60ac9f.png)

## Contributors
<div align="center">
<table>
  <tbody><tr>
     <td align="center"><a href="https://github.com/everly-gif"><img alt="https://avatars.githubusercontent.com/u/77877486?v=4" src="https://avatars.githubusercontent.com/u/77877486?v=4" width="130px;"><br><sub><b>Everly Precia Suresh</b></sub></a><br></td>
    <td align="center"><a href="https://github.com/RPK2103"><img alt="https://avatars.githubusercontent.com/u/60558428?v=4" src="https://avatars.githubusercontent.com/u/60558428?v=4" width="130px;"><br><sub><b>Kaviyashre Ragupathy</b></sub></a><br></td>
  </tr>
  
</tbody></table>
</div>
