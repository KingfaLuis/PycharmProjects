import tensorflow as tf

# a = tf.constant(3,dtype=tf.float32)
# b = tf.constant(3,dtype=tf.float32)
# c = tf.constant(3,dtype=tf.float32)
a = tf.placeholder(tf.float32,[])
b = tf.placeholder(tf.float32,[])
c = tf.placeholder(tf.float32,[])
x = tf.placeholder(tf.float32,[])

y = a * x * x + b * x + c

# with tf.Session() as sess:
#     tf.initialize_all_variables().run(y)
#     tf.summary.FileWriter('kingfa',sess.graph)
with tf.Session() as sess:
    merged = tf.summary.merge_all()

    tf.summary.FileWriter('kingfa',sess.graph)

    print(sess.run(y,feed_dict={a:1,b:2,c:4,x:8}))