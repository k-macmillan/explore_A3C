from network import GlobalNetwork
import tensorflow as tf
import numpy as np

def test_input(sess, network):
    # trainer = tf.train.AdamOptimizer(learning_rate=1e-4)
    # network = GlobalNetwork("input_test", 3, 4, trainer)
    test_input = np.array([1.0, 1.0, 1.0])
    test_input = np.reshape(test_input, (1, len(test_input))) # Have to reshape for the expected batch (first value)
    temp = sess.run(fetches=network.input,
                    feed_dict={network.input : test_input})
    for item in temp[0]:
        if item != test_input[0][0]:
            print("Network input layer failed to initialize")
            exit()

    print("Single batch input passed")


    # Test batch size of 3 on the same network
    test_input = np.array([1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0])
    test_input = np.reshape(test_input, (3, 3)) # Have to reshape for the expected batch (first value)
    temp = sess.run(fetches=network.input,
                    feed_dict={network.input : test_input})
    for item in temp[0]:
        if item != test_input[0][0]:
            print("Network batch input layer failed to initialize")
            exit()

    print("Multi batch input passed")

def test_hlayers(sess, network):
    
    test_input = np.array([1.0, 0.0, 2.0])

    test_input = np.reshape(test_input, (1, len(test_input))) # Have to reshape for the expected batch (first value)
    for _ in range(300):
        noise = np.random.normal(0, 0.1, len(test_input))
        temp = sess.run(fetches=network.q,
                        feed_dict={network.input : test_input+noise})
        print(temp[0])

    # print(temp[0])
    exit()

    print("Network living/breathing test passed")


def main():
    trainer = tf.train.AdamOptimizer(learning_rate=1e-4)
    network = GlobalNetwork("test", 3, 4, trainer)
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        
        
        with sess.as_default(), sess.graph.as_default(): 
            if sess.run(tf.constant(42)) != 42:
                print("Failed to start a TensorFlow session")
                exit()

            test_input(sess, network)
            test_hlayers(sess, network)
            
            


if __name__ == '__main__':
    main()
