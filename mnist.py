#!/usr/bin/env python3

"""
Train a SVM to categorize 28x28 pixel images into digits (MNIST dataset).
"""

import imp
import numpy as np
from PIL import Image
from sklearn.externals import joblib

def main():
    """Orchestrate the retrival of data, training and testing."""
    data = get_data()
    filename = 'classifier.pkl'

    kernels = ["rbf"]#, "poly", "linear", "sigmoid"]#, "precomputed"]

    for kern in kernels:
        # Get classifier
        from sklearn.svm import SVC
        clf = SVC(probability=False,  # cache_size=200,
                  kernel=kern, C=2.8, gamma=.0073) # rbf poly linear sigmoid precomputed

        print('\n',"Start fitting with ", kern, ". This may take a while")

        # take all of it - make that number lower for experiments
        examples = len(data['train']['X'])
        
        clf.fit(data['train']['X'][:examples], data['train']['y'][:examples])
        save_classifier(clf, filename)
        analyze(clf, data)
        clf = joblib.load(filename)
        guess_number (clf)

def guess_number(clf):
    img = Image.open('number.png').convert('L').resize((28, 28))
    arr = np.array(img)
    flat_arr = arr.ravel()
    view_image(flat_arr.reshape((28, 28)))
    predicted = clf.predict([flat_arr])
    print ('Predicción de la imagen:',predicted[0])

def save_classifier(clf, filename):
    joblib.dump(clf, filename, compress = 9)

def analyze(clf, data):
    """
    Analyze how well a classifier performs on data.

    Parameters
    ----------
    clf : classifier object
    data : dict
    """
    # Get confusion matrix
    from sklearn import metrics
    predicted = clf.predict(data['test']['X'])
    print("Confusion matrix:\n%s" %
          metrics.confusion_matrix(data['test']['y'],
                                   predicted))
    print("Accuracy: %0.4f" % metrics.accuracy_score(data['test']['y'],
                                                     predicted))

    try_id = 1
    size = int(len(data['test']['X'][try_id])**(0.5))
    view_image(data['test']['X'][try_id].reshape((size, size)), data['test']['y'][try_id])


def view_image(image, label=""):
    """
    View a single image.

    Parameters
    ----------
    image : numpy array
        Make sure this is of the shape you want.
    label : str
    """
    from matplotlib.pyplot import show, imshow, cm
    print("Label: %s" % label)
    imshow(image, cmap=cm.gray)
    show()


def get_data():
    """
    Get data ready to learn with.

    Returns
    -------
    dict
    """
    from sklearn.datasets import fetch_mldata
    from sklearn.utils import shuffle
    mnist = fetch_mldata('MNIST original')

    x = mnist.data
    y = mnist.target

    # Scale data to [-1, 1] - This is of mayor importance!!!
    x = x/255.0*2 - 1

    x, y = shuffle(x, y, random_state=0)

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y,
                                                        test_size=0.33,
                                                        random_state=42)

    data = {'train': {'X': x_train,
                      'y': y_train},
            'test': {'X': x_test,
                     'y': y_test}}
    return data


if __name__ == '__main__':
    main()
