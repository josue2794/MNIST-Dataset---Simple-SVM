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

lenght = 500
x_train = x_train[:lenght]
y_train = y_train[:lenght]
x_test = x_test[:lenght/2]
y_test = y_test[:lenght/2]

print (len(x_train))

#print (type(x_train), len(x_train))
data = {'train': {'X': x_train,
                  'y': y_train},
        'test': {'X': x_test,
                 'y': y_test}}

#data ['train'] = dict(data['train'].items()[:500])
print (type(data['train']), len(data['train']))

print (len(data['train']['X']), len(data['test']['X']))
