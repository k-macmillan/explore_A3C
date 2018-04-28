import tensorflow as tf


class GlobalNetwork:
    def __init__(self, scope, input_size, action_size, trainer):
        self.scope = scope          # Names the scope (mostly important for TensorBoard graph)
        self.i_size = input_size    # Input layer size
        self.a_size = action_size   # Number of actions possible
        self.trainer = trainer      # Optimizer
        
        with tf.variable_scope(scope):
            # Placeholder shape is [batch_size, input layer size]
            self.input = tf.placeholder(shape=[None, self.i_size], dtype=tf.float32)
            self.h_layer1 = tf.layers.dense(inputs=self.input,
                                            units=4,
                                            activation=tf.nn.selu,
                                            bias_initializer=tf.random_uniform_initializer(-1, 1))
            self.h_layer2 = tf.layers.dense(inputs=self.h_layer1,
                                            units=4,
                                            activation=tf.nn.selu,
                                            bias_initializer=tf.random_uniform_initializer(-1, 1))
            self.q = tf.contrib.layers.fully_connected(inputs=self.h_layer2,
                                                       num_outputs=2,
                                                       weights_initializer=tf.orthogonal_initializer(0.1))
            
            self.best = tf.argmax(self.q, axis=-1)
