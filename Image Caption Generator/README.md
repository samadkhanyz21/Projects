
# Image Caption Generator

This project is an implementation of an image caption generator using deep learning models. The generator is capable of producing textual descriptions of an image in natural language. The models used are a combination of a pre-trained VGG19 network, GloVe word embeddings, and an LSTM network.

## Requirements
* os
* Python 3.x
* TensorFlow
* Keras
* NumPy
* Pillow
* Pickle
* Tqdm
* Collections
* Natural Language Toolkit (nltk)

## Usage
### Dataset
I have used the `Flickr8k dataset` to train and test our model. The dataset contains 8091 images, each with 5 captions describing the image. The images are of different sizes and aspect ratios. The dataset can found on [kaggle](https://www.kaggle.com/datasets/adityajn105/flickr8k) or can be downloaded from below links.
* [Flickr8k_Dataset_Images](https://github.com/jbrownlee/Datasets/releases/download/Flickr8k/Flickr8k_Dataset.zip)
* [Flickr8k_text](https://github.com/jbrownlee/Datasets/releases/download/Flickr8k/Flickr8k_text.zip)
### GloVe
GloVe is an unsupervised learning algorithm for obtaining vector representations for words. We will be using the pre-trained embeddings with 50 dimensions. For training the GloVe Pretrained Model [download from here](https://nlp.stanford.edu/projects/glove/).

### VGG19
VGG19 is a pre-trained convolutional neural network that has been trained on the ImageNet dataset. We will be using the VGG19 network as a feature extractor for the images.
### LSTM
LSTM is a type of recurrent neural network that is capable of learning long-term dependencies. We will be using an LSTM network to generate the captions.
### Evaluation
I will be using the `BLEU` score to evaluate the performance of our model. BLEU score is a metric used to evaluate the quality of machine-translated text. It measures the similarity between the generated text and the reference text.

