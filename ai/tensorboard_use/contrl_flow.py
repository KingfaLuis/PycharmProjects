import tensorflow as tf

t0 = tf.constant(3,dtype=tf.int32)

t1 = tf.constant([3,4.1,5.2],dtype=tf.float32)

t2 = tf.constant([['I','love'],['learning','tensorflow']],dtype=tf.string)

t3 = tf.constant([[[[5],[6],[7]],[[4],[3],[2]]]])

print(t0)

print(t1)

print(t2)

print(t3)

w = tf.constant(3,dtype=tf.float32)
b = tf.constant(4,dtype=tf.float32)

x = tf.placeholder(tf.float32,[])
y = w * x + b

sess = tf.Session()
merged = tf.summary.merge_all()
tf.summary.FileWriter('luis',sess.graph)




