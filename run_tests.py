import test_environment
import test_global_network

def main():
    try:
        assert(test_environment.main())
        assert(test_global_network.main())
    except AssertionError:
        print("Testing halted due to critical test failure\n")

if __name__ == "__main__":
    main()