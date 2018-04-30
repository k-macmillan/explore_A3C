import sys
from os.path import abspath, join, dirname
sys.path.insert(0, abspath(join(dirname(__file__), ".."))) # brings the path to include the main directory

import test_environment
import test_global_network


def main(argv):
    print("\nBeginning tests")
    print("-"*56)
    runall = False
    args = [0, "False"]
    if len(argv) > 1:
        args = [0, argv[1]]
        if argv[1] == "-true":
            runall = True
    try:
        assert(test_environment.main(args) or runall)
        assert(test_global_network.main(args) or runall)

    except AssertionError:
        print("Testing halted due to critical test failure\n")

    print("\nEnd of tests")
    print("-"*56 + "\n")

if __name__ == "__main__":
    main(sys.argv)