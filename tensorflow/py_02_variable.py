import tensorflow as tf

# x = tf.Variable([1,2])
# a = tf.constant([3,3])
# #增加一个减法的op
# sub = tf.subtract(x,a)
# add = tf.add(x,sub)
#
# init = tf.global_variables_initializer()

# with tf.Session() as sess:
#     sess.run(init)
#     print(sess.run(sub))
#     print(sess.run(add))
#
# state = tf.Variable(0,name='counter')
# new_value = tf.add(state,1)
#
# update = tf.assign(state,new_value)
#
# init = tf.global_variables_initializer()
#
# with tf.Session() as sess:
#     sess.run(init)
#     print(sess.run(state))
#     for _ in range(5):
#         sess.run(update)
#         print(sess.run(state))

'''
https://stackoverflow.com/questions/34001922/failedpreconditionerror-attempting-to-use-uninitialized-in-tensorflow
'''

x = tf.Variable([1,2])
a = tf.Variable([3,3])

sub = tf.subtract(x,a)
add = tf.add(x,sub)

init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    print(sess.run(sub))
    print(sess.run(add))

state = tf.Variable(0,name='conuter')
new_value = tf.add(state,1)

update = tf.assign(state,new_value)
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    print(sess.run(state))
    for _ in range(5):
        sess.run(update)
        print(sess.run(state))