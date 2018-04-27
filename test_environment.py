from environment import Environment
from actions import Action

def test_step(environment):
    value = environment.step(Action.non)
    if value != 0:
        print("Environment failed step 1, Action.non returned: ", value)
        return

    value = environment.step(Action.sml)
    if value != 1:
        print("Environment failed step 2, Action.sml returned: ", value)
        return

    value = environment.step(Action.med)
    if value != 3:
        print("Environment failed step 3, Action.med returned: ", value)
        return

    value = environment.step(Action.big)
    if value != -1:
        print("Environment failed step 4, Action.big returned: ", value)
        return

    print("Test Environment.step passed")

def main():
    env = Environment()
    test_step(env)
    print()


if __name__ == "__main__":
    main()