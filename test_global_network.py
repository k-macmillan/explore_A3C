from network import GlobalNetwork
import tensorflow as tf
import numpy as np
from colorama import Fore, Back, Style

RESULT = {"pass" : Fore.BLACK + Back.GREEN + "PASSED" + Style.RESET_ALL, 
          "fail" : Fore.BLACK + Back.RED + "FAILED" + Style.RESET_ALL}

def test_input(sess, network):
    # trainer = tf.train.AdamOptimizer(learning_rate=1e-4)
    # network = GlobalNetwork("input_test", 3, 4, trainer)
    
    test_input = np.array([1.0, 1.0, 1.0])
    test_input = np.reshape(test_input, (1, len(test_input))) # Have to reshape for the expected batch (first value)
    temp = sess.run(fetches=network.input,
                    feed_dict={network.input : test_input})
    for item in temp[0]:
        if item != test_input[0][0]:
            print("{:<30} {:>35}".format("Single batch input", RESULT['fail']))
            return

    print("{:<30} {:>25}".format("Single batch input", RESULT['pass']))
    

    # Test batch size of 3 on the same network
    test_input = np.array([1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0])
    test_input = np.reshape(test_input, (3, 3)) # Have to reshape for the expected batch (first value)
    temp = sess.run(fetches=network.input,
                    feed_dict={network.input : test_input})
    for item in temp[0]:
        if item != test_input[0][0]:
            print("{:<30} {:>35}".format("Multi batch input", RESULT['fail']))
            return

    print("{:<30} {:>25}".format("Multi batch input", RESULT['pass']))
    return True

def main():
    print("\nTesting network")
    print("-"*55)
    try:
        tf.reset_default_graph()
        trainer = tf.train.AdamOptimizer(learning_rate=0.01)
        network = GlobalNetwork("test", 3, 4, trainer)
        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())
            with sess.as_default(), sess.graph.as_default(): 
                if sess.run(tf.constant(42)) != 42:
                    print("{:<30} {:>35}".format("TensorFlow session start", RESULT['fail']))
                    exit()
                else:
                    print("{:<30} {:>25}".format("TensorFlow session start", RESULT['pass']))

                assert(test_input(sess, network))
        return True
    except AssertionError:
        print("Testing halted due to critical test failure\n")
        exit()

if __name__ == '__main__':
    main()
