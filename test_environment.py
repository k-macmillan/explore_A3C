from environment import Environment
from actions import Action
from colorama import Fore, Back, Style
from sys import argv

RESULT = {"pass" : Fore.BLACK + Back.GREEN + "PASSED" + Style.RESET_ALL, 
          "fail" : Fore.BLACK + Back.RED + "FAILED" + Style.RESET_ALL}

def test_step(environment):
    value, state = environment.step(Action.non)
    if value != 0 or state != 1:
        print("{:<30} {:>35}".format("Environment failed step 1", RESULT['fail']))
        return

    value, state = environment.step(Action.sml)
    if value != 0 or state != 2:
        print("{:<30} {:>35}".format("Environment failed step 2", RESULT['fail']))
        return

    value, state = environment.step(Action.med)
    if value != 0 or state != 3:
        print("{:<30} {:>35}".format("Environment failed step 3", RESULT['fail']))
        return

    value, state = environment.step(Action.big)
    if value != 0 or state != 4:
        print("{:<30} {:>35}".format("Environment failed step 4", RESULT['fail']))
        return

    value, state = environment.step(Action.non)
    if value != -3 or state != 0: # -1
        print("{:<30} {:>35}".format("Environment failed step 4", RESULT['fail']))
        return

    print("{:<30} {:>25}".format("Test Environment.step passed", RESULT['pass']))
    return True


def test_reset(environment):
    for _ in range(environment.max_actions - 1):
        environment.step(Action.non)
    environment.reset()

    if len(environment.actions) != 0:
        print("{:<30} {:>35}".format("Environment reset", RESULT['fail']))
    else:
        print("{:<30} {:>25}".format("Environment reset", RESULT['pass']))
        return True


def main(argv):
    print("\nTesting environment")
    print("-"*55)
    runall = False
    if len(argv) > 1:
        if argv[1] == "-true":
            runall = True

    try:
        env = Environment()
        assert(test_step(env) or runall)
        assert(test_reset(env) or runall)
        return True
    except AssertionError:
        print("Testing halted due to critical test failure\n")
        exit()


if __name__ == "__main__":
    main(argv)