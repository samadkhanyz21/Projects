
# Titanic Classification Project

## Problem Definition
In this notebook with help of machine learning I will find out which passengers survived the Titanic shipwreck.

## Dataset Information
The data has been split into two groups:

* training set (train.csv)
* test set (test.csv)
The `train.csv` should be used to build your machine learning models. For the training set, we provide the outcome (also known as the “ground truth”) for each passenger. The model will be based on “feature” `survival rate`. You can also use feature engineering to create new features.

The `test.csv` should be used to see how well your model performs on unseen data. For the test set, we do not provide the ground truth for each passenger. It is your job to predict these outcomes. For each passenger in the test set, use the model you trained to predict whether or not they survived the sinking of the Titanic.

## Dataset Features
`survival`: Survival Rate

* No = 0
* Yes = 1
`pclass`: Ticket class

* 1st = 1
* 2nd = 2
* 3rd = 3
`sex`: Sex\
`Age`: Age in years\
`sibsp`: # of siblings / spouses aboard the Titanic\
`parch`: # of parents / children aboard the Titanic\
`ticket`: Ticket number\
`fare`: Passenger fare\
`cabin`: Cabin number\
`embarked`: Port of Embarkation

* Cherbourg = C
* Queenstown = Q
* Southampton = S
pclass: A proxy for socio-economic status (SES)

* 1st = Upper
* 2nd = Middle
* 3rd = Lower
age: Age is fractional if less than 1. If the age is estimated, is it in the form of xx.5

sibsp: The dataset defines family relations in this way

* Sibling = brother, sister, stepbrother, stepsister
* Spouse = husband, wife (mistresses and fiancés were ignored)
parch: The dataset defines family relations in this way

* Parent = mother, father
* Child = daughter, son, stepdaughter, stepson
* Some children travelled only with a nanny, therefore parch=0 for them

More information regarding dataset can be found on [Kaggle](https://www.kaggle.com/competitions/titanic/data).

