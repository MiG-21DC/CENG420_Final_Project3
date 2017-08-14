import tensorflow as tf
from get_set import get_data
import numpy as np
# from tensorflow.examples.tutorials.mnist import input_data

# mnist = input_data.read_data_sets('/tmp/data',one_hot=True)

class NeuralNetwork:
    def __init__(self, layer_1=1000, layer_2=1000, layer_3=1000):
        self.n_nodes_hl1 = layer_1
        self.n_nodes_hl2 = layer_2
        self.n_nodes_hl3 = layer_3
    
        self.n_classes = 2
        self.batch_size = 1000
        self.train_x, self.train_y, self.test_x, self.test_y = get_data()
        self.x = tf.placeholder('float', [None, len(self.train_x[0])])
        self.y = tf.placeholder('float')
        self.accuracy_record = 0
        self.best_layer = []


    def neural_network_model(self, data):
        hidden_1_layer = {'weights':tf.Variable(tf.random_normal([len(self.train_x[0]), self.n_nodes_hl1])),
                          'biases':tf.Variable(tf.random_normal([self.n_nodes_hl1]))}

        hidden_2_layer = {'weights': tf.Variable(tf.random_normal([self.n_nodes_hl1, self.n_nodes_hl2])),
                          'biases': tf.Variable(tf.random_normal([self.n_nodes_hl2]))}

        hidden_3_layer = {'weights': tf.Variable(tf.random_normal([self.n_nodes_hl2, self.n_nodes_hl3])),
                          'biases': tf.Variable(tf.random_normal([self.n_nodes_hl3]))}

        output_layer = {'weights': tf.Variable(tf.random_normal([self.n_nodes_hl3, self.n_classes])),
                          'biases': tf.Variable(tf.random_normal([self.n_classes]))}

        l1 = tf.add(tf.matmul(data, hidden_1_layer['weights']), hidden_1_layer['biases'])
        l1 = tf.nn.relu(l1)


        l2 = tf.add(tf.matmul(l1, hidden_2_layer['weights']), hidden_2_layer['biases'])
        l2 = tf.nn.relu(l2)


        l3 = tf.add(tf.matmul(l2, hidden_3_layer['weights']), hidden_3_layer['biases'])
        l3 = tf.nn.relu(l3)

        output = tf.matmul(l3, output_layer['weights']) + output_layer['biases']

        return output

    # saver = tf.train.Saver()

    def train_neural_network(self,x):
        prediction = self.neural_network_model(x)
        cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits = prediction, labels = self.y))
        optimizer = tf.train.AdamOptimizer().minimize(cost)

        hm_epochs = 10

        with tf.Session() as sess:
            sess.run(tf.initialize_all_variables())

            for epoch in range(hm_epochs):
                epoch_loss = 0
                # for _ in range(int(mnist.train.num_examples/batch_size)):
                #     epoch_x, epoch_y = mnist.train.next_batch(batch_size)
                i = 0
                while i < len(self.train_x):
                    start = i
                    end = i+self.batch_size
                    batch_x = np.array(self.train_x[start:end])
                    batch_y = np.array(self.train_y[start:end])

                    # print(epoch_x, epoch_x.shape)
                    # print(epoch_y, epoch_y.shape)
                    _, c = sess.run([optimizer, cost], feed_dict = {self.x: batch_x, self.y: batch_y})
                    epoch_loss += c
                    i += self.batch_size
                print('Epoch', epoch, 'completed out of', hm_epochs,'loss:',epoch_loss)

            # self.saver.save(sess,'model.ckpt')
            correct = tf.equal(tf.argmax(prediction,1),tf.argmax(self.y,1))
            accuracy = tf.reduce_mean(tf.cast(correct,'float'))
            print('Accuracy',accuracy.eval({self.x:self.test_x, self.y:self.test_y}))
            return accuracy.eval({self.x:self.test_x, self.y:self.test_y})


    def start_running(self):
        acc = self.train_neural_network(self.x)
        # if acc > self.accuracy_record:
        #     self.accuracy_record = acc
        #     self.best_layer = [self.n_nodes_hl1, self.n_nodes_hl2, self.n_nodes_hl3]
        #     print('Best accuracy', acc, 'is found at layer',self.best_layer)


    def set_layer1(self,layer1):
        self.n_nodes_hl1 = layer1

    def set_layer2(self,layer2):
        self.n_nodes_hl2 = layer2

    def set_layer3(self,layer3):
        self.n_nodes_hl3 = layer3


test = NeuralNetwork(1000,1000,1000)
test.start_running()
# for layer1 in range(1,1001):
#     test.set_layer1(layer1)
#     for layer2 in range(1,1001):
#         test.set_layer2(layer2)
#         for layer3 in range(1,1001):
#             test.set_layer3(layer3)
#             test.start_running()

# print('final result')
# print('Best layer', test.best_layer, 'with accuracy', test.accuracy_record)

