# Age Estimation using Convolutional Neural Network

To estimate the age of the person in the image using Convolutional Neural Network. The models are build from scratch, using pretrain Inception-ResNet and VGGFace.

## Prerequisites

- Python 3.6.8
- OpenCV 4.1.0
- joblib 0.13.2
- Keras 2.2.4
- h5py 2.9.0

## Getting Start

Download Adience Dataset:
> http://www.openu.ac.il/home/hassner/Adience/data.html

## Methodology

The image data will be import into the memory and normalized. Augmentation will be used to enhance the model performance.
The model will be fine-tune to prevent overfiting.
Credit: 
> https://github.com/zonetrooper32/AgeEstimateAdience

## Pretrain Model

    - VGGFace: http://www.robots.ox.ac.uk/~vgg/publications/2015/Parkhi15/parkhi15.pdf
    - Inception-ResNet: https://arxiv.org/abs/1602.07261

Model & Weight
Credit:
> https://sefiks.com/2018/08/06/deep-face-recognition-with-keras/

## Model Evaluation

Evaluation metrics, such as **Accuracy, F1 Score, Balanced Accuracy Score, ROC and PR curve**, are used to evaluate the best model.

## Analysis on Error

The misclassified comments will be visualized.

## Conclusion and Future Improvement

Evaluate and advise on future improvement that can be done.

## Authors

* **Panu Looareesuwan** 

* Be The Best That You Can Be
