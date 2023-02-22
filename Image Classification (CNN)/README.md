
# Image Classification Project

## Overview
This is a deep learning project for image classification. The goal of this project is to classify images into several categories using a convolutional neural network (CNN). The CNN is trained on a dataset of labeled images, and the trained model is used to predict the labels of new images.

## Dataset
The dataset used in this project was prepared by myself and student colleagues. The dataset contains images of four classes which are:

- Onion
- Apple
- Fork
- Book

The dataset consists of 100 images per class, for a total of 400 training images. The images are in JPEG & PNG format having a resolution of 224x224 pixels. The dataset was collected using a web camera with `capture.py` python file.

## Model
The initial version of the model used in this project was prepared with VGG19, a pre-trained convolutional neural network that has achieved state-of-the-art results on several image classification tasks. The pre-trained VGG19 model was loaded using the `tf.keras.applications.VGG19` function from TensorFlow.

To adapt the pre-trained VGG19 model to our specific task, some of the layers in the model were frozen to prevent them from being updated during training. In addition to the pre-trained layers, several new layers were added to the model to further train the model on our specific dataset. These new layers included several convolutional layers, max pooling layers, and dense layers.

The final layer of the model uses softmax activation to output the predicted probabilities for each class.

## Training
The model was trained on our dataset using the Adam optimizer and sparse categorical crossentropy loss function. The dataset was split into training and validation sets, with 80% of the data used for training and 20% for validation. The model was trained for 100 epochs with an initial learning rate of 0.0001.

## Evaluation
The trained model is evaluated on a test set of 66 images. The test accuracy is reported as the evaluation metric.

## Usage
To use the trained model for prediction on new images, you can load the saved model using the `tf.keras.models.load_model` function, and then call the `predict` method on the model with the input image as a parameter.

## Dependencies
This project requires the following Python libraries:

- TensorFlow
- Matplotlib
- NumPy
- Pandas
- Opencv-python

## Acknowledgements
The pre-trained VGG19 model used in this project is part of the Keras Applications module, which is available under the MIT license.