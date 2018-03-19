import tensorflow as tf
print dir(tf)
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))
