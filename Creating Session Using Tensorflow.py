# Coded by Shivam Kumar
# PRN 20190802073

# Importing required dependencies
import tensorflow.compat.v1 as tf
import numpy as np


class sessionOperation:
    def __init__(self):
        # Checking for tensorflow version
        print('The current working version of tensorflow is', tf.__version__)
        # Initializing global initializer of tensorflow
        self.init = tf.global_variables_initializer()

    def myOperation(self):
        # Create the session using tf.Session() and run it with sess.run()
        with tf.Session() as sess:
            np.random.seed(1)
            # creating a random array X, W, and b
            # np.random.randn(...) to initialize randomly
            # Initializes W to be a random tensor of shape (4,3)
            X = tf.constant(np.random.randn(3, 1), name="X")
            print(X)
            # Initializes X to be a random tensor of shape (3,1)
            W = tf.constant(np.random.randn(4, 3), name="W")
            print(W)
            # Initializes b to be a random tensor of shape (4,1)
            b = tf.constant(np.random.randn(4, 1), name="b")
            print(b)
            # Applying operations on X, W and b
            # tf.matmul(..., ...) to do a matrix multiplication
            # tf.add(..., ...) to do an addition
            a = tf.matmul(W, X)
            Y = tf.add(a, b)
            return sess.run(Y)


apprunner = sessionOperation()
apprunner.myOperation()