import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf
import numpy

a = numpy.zeros(8)
print(a)

b = numpy.ones([2, 3])
print(b.dtype)
print(b.ndim)
print(b.shape)
print(b)

a = tf.constant(2, name="a")
b = tf.constant(3, name="b")
x = tf.add(a, b)
with tf.Session() as sess:
    writer = tf.summary.FileWriter('./graphs', sess.graph)
    print(sess.run(x))
writer.close()
