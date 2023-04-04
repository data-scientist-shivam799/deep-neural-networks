# import tensorflow as tf
# import tensorflow_datasets as tfds
#
# (train_data, test_data), ds_info = tfds.load('mnist',split=['train', 'test'],shuffle_files=True,as_supervised=True,with_info=True,)
#
# def normalize_img(image, label):
#   return tf.cast(image, tf.float32) / 255., label
#
# train_data = train_data.map(normalize_img, num_parallel_calls=tf.data.AUTOTUNE)
# train_data = train_data.cache()
# train_data = train_data.shuffle(ds_info.splits['train'].num_examples)
# train_data = train_data.batch(128)
# train_data = train_data.prefetch(tf.data.AUTOTUNE)
#
# test_data = test_data.map(normalize_img, num_parallel_calls=tf.data.AUTOTUNE)
# test_data = test_data.batch(128)
# test_data = test_data.cache()
# test_data = test_data.prefetch(tf.data.AUTOTUNE)
#
# model = tf.keras.models.Sequential([
#   tf.keras.layers.Flatten(input_shape=(28, 28)),
#   tf.keras.layers.Dense(128, activation='relu'),
#   tf.keras.layers.Dense(10)
# ])
# model.compile(
#     optimizer=tf.keras.optimizers.Adam(0.001),
#     loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
#     metrics=[tf.keras.metrics.SparseCategoricalAccuracy()],
# )
#
# model.fit(train_data,epochs=6,validation_data=test_data)
# print(model.predict(test_data))

import tensorflow as tf
import tensorflow.compat.v1 as tf
tf.disable_eager_execution()

W = tf.get_variable(shape=[4,3], name = 'W')
X = tf.get_variable(shape=[3,1], name = 'X')
X = tf.reshape(X,(1,3))
b = tf.get_variable(shape=[4,1], name = 'b')
addition = tf.add(tf.add(tf.multiply(W, X),tf.multiply(b,(tf.multiply(W, X)))),b)
subtraction = tf.subtract(tf.subtract(tf.multiply(W, X),tf.multiply(b,(tf.multiply(W, X)))),b)
division = tf.divide(tf.subtract(tf.multiply(W, X),tf.multiply(b,(tf.multiply(W, X)))),b)

v = tf.global_variables_initializer()

with tf.Session() as session:
    v.run()
    result = addition.eval()
    print(" *********************** Addition with tensor as graph *********************** ")
    print(result)
    result = subtraction.eval()
    print("\n  *********************** Subtraction with tensor as graph *********************** ")
    print(result)
    result = division.eval()
    print("\n *********************** Division with tensor as graph *********************** ")
    print(result)
session.close()