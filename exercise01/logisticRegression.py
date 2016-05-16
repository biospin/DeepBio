from datetime import datetime
import time
import os
from pprint import pprint
import numpy as np
import gzip, cPickle
import theano
import theano.tensor as T
from theano import function
from glob import glob
import timeit
import sys

class LogisticRegression(object):

    def __init__(self, input, n_in, n_out):
        # start-snippet-1
        # initialize with 0 the weights W as a matrix of shape (n_in, n_out)
        self.W = theano.shared(
            value=np.zeros(
                (n_in, n_out),
                dtype=theano.config.floatX
            ),
            name='W',
            borrow=True
        )
        # initialize the biases b as a vector of n_out 0s
        self.b = theano.shared(
            value=np.zeros(
                (n_out,),
                dtype=theano.config.floatX
            ),
            name='b',
            borrow=True
        )

        self.p_y_given_x = T.nnet.softmax(T.dot(input, self.W) + self.b)

        self.y_pred = T.argmax(self.p_y_given_x, axis=1)

        self.params = [self.W, self.b]

        self.input = input

    def negative_log_likelihood(self, y):
        return -T.mean(T.log(self.p_y_given_x)[T.arange(y.shape[0]), y])

    def errors(self, y):
        if y.ndim != self.y_pred.ndim:
            raise TypeError(
                'y should have the same shape as self.y_pred',
                ('y', y.type, 'y_pred', self.y_pred.type)
            )
        if y.dtype.startswith('int'):
            return T.mean(T.neq(self.y_pred, y))
        else:
            raise NotImplementedError()

def loadData():
    def dir_to_dataset(glob_files):
        for file_count, file_name in enumerate( sorted(glob(glob_files)) ):
            print(file_name)
            pklPartial=gzip.open(file_name)
            pklT= cPickle.load(pklPartial)
            if file_count==0:
                dataSet0=pklT[0]
                dataSet1=pklT[1]
            else:
                dataSet0 = np.concatenate((dataSet0,pklT[0]))
                dataSet1 = np.append(dataSet1,pklT[1])
            pklPartial.close()
            print len(dataSet0), len(dataSet1) 

        dataSet1=dataSet1-1
        #print np.amax(dataSet1)
        dataSet= (dataSet0, dataSet1)
        return dataSet

    def shared_dataset(data_xy, borrow=True):
        data_x, data_y = data_xy
        #print type(data_x), data_x.shape
        shared_x = theano.shared(data_x.astype(theano.config.floatX),borrow=True)
        shared_y = theano.shared(data_y.astype(theano.config.floatX),borrow=True)
        return shared_x, T.cast(shared_y, 'int32')

    trainingSet = dir_to_dataset('./*type1*')
    testSet =  dir_to_dataset('./*type3*')
    valSet = dir_to_dataset('./*type2*')

    trainingSetX, trainingSetY = shared_dataset(trainingSet)
    testSetX,testSetY= shared_dataset(testSet)
    valSetX,valSetY = shared_dataset(valSet)

    #trainingSetX, trainingSetY = trainingSet
    #testSetX,testSetY = testSet
    #valSetX,valSetY = valSet
    rVal=[(trainingSetX,trainingSetY),(testSetX,testSetY), (valSetX,valSetY)]

    return rVal

def sgdOptimization(dataSets):
    #load dataset
    trainingSetX, trainingSetY = dataSets[0]
    testSetX,testSetY= dataSets[1]
    valSetX,valSetY = dataSets[2]


    #parameters
    batch_size=10
    learning_rate=0.13
    n_epochs=1000

    nTrainBatches = trainingSetX.get_value(borrow=True).shape[0] / batch_size
    nValidBatches = valSetX.get_value(borrow=True).shape[0] / batch_size
    nTestBatches = testSetX.get_value(borrow=True).shape[0] / batch_size

    patience = 5000  
    patience_increase = 2
    improvement_threshold = 0.995
    validation_frequency = min(nTrainBatches, patience / 2)

    nClass=34

    ##################
    ### BUILD MODEL
    ##################

    print '... building the model'
    
    index = T.lscalar()
    x = T.matrix('x')
    y = T.ivector('y')

    classifier = LogisticRegression(input=x, n_in=20502, n_out=nClass)
    cost = classifier.negative_log_likelihood(y)

    test_model = theano.function(
        inputs=[index],
        outputs=classifier.errors(y),
        givens={
            x: testSetX[index * batch_size: (index + 1) * batch_size],
            y: testSetY[index * batch_size: (index + 1) * batch_size]
        }
    )

    validate_model = theano.function(
        inputs=[index],
        outputs=classifier.errors(y),
        givens={
            x: valSetX[index * batch_size: (index + 1) * batch_size],
            y: valSetY[index * batch_size: (index + 1) * batch_size]
        }
    )

    g_W = T.grad(cost=cost, wrt=classifier.W)
    g_b = T.grad(cost=cost, wrt=classifier.b)

    updates = [(classifier.W, classifier.W - learning_rate * g_W),
               (classifier.b, classifier.b - learning_rate * g_b)]

    train_model = theano.function(
        inputs=[index],
        outputs=cost,
        updates=updates,
        givens={
            x: trainingSetX[index * batch_size: (index + 1) * batch_size],
            y: trainingSetY[index * batch_size: (index + 1) * batch_size]
        }
    )
    
    #################
    ### TRAIN MODEL
    #################


    print '... training the model'


    best_validation_loss = np.inf
    test_score = 0.
    start_time = timeit.default_timer()

    done_looping = False
    epoch = 0
    while (epoch < n_epochs) and (not done_looping):
        epoch = epoch + 1
        for minibatch_index in xrange(nTrainBatches):
            minibatch_avg_cost = train_model(minibatch_index)
            iter = (epoch - 1) * nTrainBatches + minibatch_index

            if (iter + 1) % validation_frequency == 0:
                validation_losses = [validate_model(i)
                                     for i in xrange(nValidBatches)]
                this_validation_loss = np.mean(validation_losses)

                print(
                    'epoch %i, minibatch %i/%i, validation error %f %%' %
                    (
                        epoch,
                        minibatch_index + 1,
                        nTrainBatches,
                        this_validation_loss * 100.
                    )
                )

                if this_validation_loss < best_validation_loss:
                    if this_validation_loss < best_validation_loss *  \
                       improvement_threshold:
                        patience = max(patience, iter * patience_increase)

                    best_validation_loss = this_validation_loss

                    test_losses = [test_model(i)
                                   for i in xrange(nTestBatches)]
                    test_score = np.mean(test_losses)

                    print(
                        (
                            '     epoch %i, minibatch %i/%i, test error of'
                            ' best model %f %%'
                        ) %
                        (
                            epoch,
                            minibatch_index + 1,
                            nTrainBatches,
                            test_score * 100.
                        )
                    )

                    with open('best_model.pkl', 'w') as f:
                        cPickle.dump(classifier, f)

            if patience <= iter:
                done_looping = True
                break

    end_time = timeit.default_timer()
    print(
        (
            'Optimization complete with best validation score of %f %%,'
            'with test performance %f %%'
        )
        % (best_validation_loss * 100., test_score * 100.)
    )
    print 'The code run for %d epochs, with %f epochs/sec' % (
        epoch, 1. * epoch / (end_time - start_time))
    print >> sys.stderr, ('The code for file ' +
                          os.path.split(__file__)[1] +
                          ' ran for %.1fs' % ((end_time - start_time)))


if __name__ == '__main__':

    dataSets = loadData()

    print "Preparing complete!!==="

    sgdOptimization(dataSets)
