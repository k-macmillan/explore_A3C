import test_environment
import test_global_network
from sys import argv

def main(argv):
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

if __name__ == "__main__":
    main(argv)