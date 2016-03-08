# -*- coding: utf-8 -*-

from scipy.misc import imread # using scipy's imread
import cv2
import numpy as np

def boundaries(binarized,axis):
    # variables named assuming axis = 0; algorithm valid for axis=1
    # [1,0][axis] effectively swaps axes for summing
    rows = np.sum(binarized,axis = [1,0][axis]) > 0
    rows[1:] = np.logical_xor(rows[1:], rows[:-1])
    change = np.nonzero(rows)[0]
    ymin = change[::2]
    ymax = change[1::2]
    height = ymax-ymin
    too_small = 10 # real letters will be bigger than 10px by 10px
    ymin = ymin[height>too_small]
    ymax = ymax[height>too_small]
    return zip(ymin,ymax)

def separate(img):
    orig_img = img.copy()
    pure_white = 255.
    white = np.max(img)
    black = np.min(img)
    thresh = (white+black)/2.0
    binarized = img<thresh
    row_bounds = boundaries(binarized, axis = 0) 
    cropped = []
    for r1,r2 in row_bounds:
        img = binarized[r1:r2,:]
        col_bounds = boundaries(img,axis=1)
        rects = [r1,r2,col_bounds[0][0],col_bounds[0][1]]
        cropped.append(np.array(orig_img[rects[0]:rects[1],rects[2]:rects[3]]/pure_white))
    return cropped

# Example usage
big_img_a = imread("a.png", flatten = True) # flatten = True converts to greyscale
big_img_b = imread("b.png", flatten = True)
big_img_c = imread("c.png", flatten = True)

imgs_a = separate(big_img_a) # separates big_img (pure white = 255) into array of little images (pure white = 1.0)
imgs_b = separate(big_img_b)
imgs_c = separate(big_img_c)
imgs = []
for img in range(len(imgs_a)):
    imgs_a[img] = cv2.resize(imgs_a[img], (8,8), interpolation = cv2.INTER_AREA)
    imgs_b[img] = cv2.resize(imgs_b[img], (8,8), interpolation = cv2.INTER_AREA)
    imgs_c[img] = cv2.resize(imgs_c[img], (8,8), interpolation = cv2.INTER_AREA)
    imgs.append(imgs_a[img])
    imgs.append(imgs_b[img])
    imgs.append(imgs_c[img])


def partition(data, target, percent):
    fraction = percent/100.
    train_len = int(len(data) * fraction)
    train_data = data[:train_len]
    train_target = target[:train_len]
    test_data = data[train_len:]
    test_target = target[train_len:]

    #vary the sampling data order
    # train_data = data[:train_len:-1]
    # train_target = target[:train_len:-1]
    # test_data = data[train_len::-1]
    # test_target = target[train_len::-1]

    #vary sample space
    # train_len = len(data) - train_len
    # train_data = data[train_len:]
    # train_target = target[train_len:]
    # test_data = data[:train_len]
    # test_target = target[:train_len]
    return train_data, train_target, test_data, test_target

# Standard scientific Python imports
import matplotlib.pyplot as plt

# Import datasets, classifiers and performance metrics
from sklearn import datasets, svm, metrics

# The digits dataset
digits = datasets.load_digits()
partpercent =  10

target = np.array([x % 3 for x in range(len(imgs))])
train_data,train_target, test_data, test_target = partition(imgs,target, partpercent)
# The data that we are interested in is made of 8x8 images of digits, let's
# have a look at the first 3 images, stored in the `images` attribute of the
# dataset.  If we were working from image files, we could load them using
# pylab.imread.  Note that each image must have the same size. For these
# images, we know which digit they represent: it is given in the 'target' of
# the dataset.
images_and_labels = list(zip(train_data, train_target))
for index, (image, label) in enumerate(images_and_labels[:4]):
    plt.subplot(2, 4, index + 1)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('Training: %i' % label)

# To apply a classifier on this data, we need to flatten the image, to
# turn the data in a (samples, feature) matrix:
train_data = np.array(train_data)
test_data = np.array(test_data)
data = train_data.reshape((len(train_data), -1))
pdata = test_data.reshape((len(test_data), -1))


# Create a classifier: a support vector classifier
classifier = svm.LinearSVC()
#classifier = svm.SVC(gamma = 1) #1 or 2 work the best

# We learn the digits on the first half of the digits
classifier.fit(data, train_target)

#print digits.images
predicted = classifier.predict(pdata)

images_and_predictions = list(zip(test_data, predicted))
for index, (image, prediction) in enumerate(images_and_predictions[:4]):
    plt.subplot(2, 4, index + 5)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('Prediction: %i' % prediction)

print "Predicted: ", predicted
print "Truth: ", test_target
counter = 0.
for i,j in zip(predicted,test_target):
    if i == j:
        counter += 1
print "Accuracy: ", counter/len(predicted)*100, "%"

plt.show()
