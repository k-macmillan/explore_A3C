import sys
from os.path import abspath, join, dirname
sys.path.insert(0, abspath(join(dirname(__file__), ".."))) # brings the path to include the main directory
import tensorflow as tf
import numpy as np

# import format_test_output as TestOutput
from format_test_output import TestOutput
from network import GlobalNetwork


def test_input(sess, network):
    test_name = "Single batch input"
    test_input = np.array([1.0, 1.0, 1.0])
    test_input = np.reshape(test_input, (1, len(test_input))) # Have to reshape for the expected batch (first value)
    temp = sess.run(fetches=network.input,
                    feed_dict={network.input : test_input})
    for item in temp[0]:
        if item != test_input[0][0]:
            TestOutput.fail_test(test_name)
            return

    TestOutput.pass_test(test_name)
   

    # Test batch size of 3 on the same network
    test_name = "Multi batch input"
    test_input = np.array([1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0])
    test_input = np.reshape(test_input, (3, 3)) # Have to reshape for the expected batch (first value)
    temp = sess.run(fetches=network.input,
                    feed_dict={network.input : test_input})
    for item in temp[0]:
        if item != test_input[0][0]:
            TestOutput.fail_test(test_name)
            return

    TestOutput.pass_test(test_name)
    return True

def main(argv):
    print("\nTesting network")
    print("-"*56)
    runall = False
    if len(argv) > 1:
        if argv[1] == "-true":
            runall = True

    try:
        test_name = "TensorFlow session start"
        tf.reset_default_graph()
        trainer = tf.train.AdamOptimizer(learning_rate=0.01)
        network = GlobalNetwork("test", 3, 4, trainer)
        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())
            with sess.as_default(), sess.graph.as_default(): 
                if sess.run(tf.constant(42)) != 42:
                    TestOutput.fail_test(test_name)
                    exit()
                else:
                    TestOutput.pass_test(test_name)

                assert(test_input(sess, network) or runall)
        return True
    except AssertionError:
        print("Testing halted due to critical test failure\n")
        exit()

if __name__ == '__main__':
    main(sys.argv)
