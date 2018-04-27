from environment import Environment
from actions import Action

def main():
    env = Environment()
    print(env.step(Action.non))
    print("Done!")




if __name__ == "__main__":
    main()