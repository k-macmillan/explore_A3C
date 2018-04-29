import sys
from os.path import abspath, join, dirname
sys.path.insert(0, abspath(join(dirname(__file__), ".."))) # brings the path to include the main directory

# import format_test_output as TestOutput
from format_test_output import TestOutput
from environment import Environment
from actions import Action

# TestOutput.pass_test(test_name)
    # TestOutput.fail_test(test_name)
def test_step(environment):
    test_name = "Environment.step "

    value, state = environment.step(Action.non)
    if value != 0 or state != 1:
        TestOutput.fail_test(test_name + "1")
        return

    value, state = environment.step(Action.sml)
    if value != 0 or state != 2:
        TestOutput.fail_test(test_name + "2")
        return

    value, state = environment.step(Action.med)
    if value != 0 or state != 3:
        TestOutput.fail_test(test_name + "3")
        return

    value, state = environment.step(Action.big)
    if value != 0 or state != 4:
        TestOutput.fail_test(test_name + "4")
        return

    value, state = environment.step(Action.non)
    if value != -1 or state != 0:
        TestOutput.fail_test(test_name + "5")
        return

    TestOutput.pass_test(test_name)
    return True


def test_reset(environment):
    test_name = "Environment.reset"
    for _ in range(environment.max_actions - 1):
        environment.step(Action.non)
    environment.reset()

    if len(environment.actions) != 0:
        TestOutput.fail_test(test_name)
    else:
        TestOutput.pass_test(test_name)
        return True


def main(argv):
    print("\nTesting environment")
    print("-"*56)
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
    main(sys.argv)