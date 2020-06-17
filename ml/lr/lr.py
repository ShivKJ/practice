import pandas as pd
import tensorflow as tf


def vehicle_data():
    df = pd.read_csv('refined_mile_per_gallon.csv')
    df = df[[
        'cylinders',
        'displacement',
        'horsepower',
        'weight',
        'acceleration',
        'mpg'
    ]]

    data = df.values
    size = 200
    x_train, y_train = data[:size, :-1], data[:size, -1].reshape((size, 1))
    x_test, y_test = data[size:, :-1], data[size:, -1].reshape((len(data) - size, 1))

    return x_train, y_train, x_test, y_test


def linear_regression(alpha):
    with tf.name_scope('Graph'):
        feature_size = 5
        output_size = 1

        x = tf.compat.v1.placeholder(dtype=tf.float64, shape=[None, feature_size], name='x')
        y = tf.compat.v1.placeholder(dtype=tf.float64, shape=[None, output_size], name='y')

        w = tf.Variable(tf.compat.v1.random_normal([feature_size, output_size], dtype=tf.float64),
                        name='W', dtype=tf.float64)

        b = tf.Variable(tf.compat.v1.random_normal([output_size], dtype=tf.float64),
                        name='b', dtype=tf.float64)

        y_pred = x @ w + b

        # cost = tf.reduce_mean(tf.square(y_pred - y)) + alpha * tf.reduce_mean(w * w)
        cost = tf.reduce_mean(tf.square(y_pred - y)) + alpha * tf.reduce_mean(abs(w))
        # cost = tf.reduce_mean(tf.square(y_pred - y)) + alpha * (tf.transpose(w) @ w)

        return x, y, y_pred, cost


def run():
    x_batch, y_batch, x_test, y_test = vehicle_data()
    x, y, y_pred, cost = linear_regression(0.001)

    learning = 0.1

    optimizer = tf.compat.v1.train.AdamOptimizer(learning_rate=learning).minimize(cost)
    init = tf.compat.v1.global_variables_initializer()

    tf.compat.v1.summary.FileWriter('./log', graph=tf.compat.v1.get_default_graph())

    with tf.compat.v1.Session() as sess:
        sess.run(init)

        for epoch in range(50000):
            _, batch_cost = sess.run([optimizer, cost], feed_dict={x: x_batch, y: y_batch})

        y_t = sess.run(cost, {x: x_test, y: y_test})

        print(y_t)


if __name__ == '__main__':
    tf.compat.v1.disable_eager_execution()

    run()
