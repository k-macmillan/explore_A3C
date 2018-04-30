from colorama import Fore, Back, Style

class TestOutput:
    RESULT = {'pass' : Fore.BLACK + Back.GREEN + "PASSED" + Style.RESET_ALL, 
              'fail' : Fore.BLACK + Back.RED + "FAILED" + Style.RESET_ALL,
              'skip' : Fore.BLACK + Back.BLUE + "SKIPPED" + Style.RESET_ALL,}

    COLUMN = {'test' : '{:<30}',
              'pass' : '{:>25}',
              'fail' : '{:>40}',
              'skip' : '{:>33}',}

    @classmethod
    def pass_test(cls, test_name):
        print(cls.COLUMN['test'].format(test_name) + cls.COLUMN['pass'].format(cls.RESULT['pass']))

    @classmethod
    def fail_test(cls, test_name):
        print(cls.COLUMN['test'].format(test_name) + cls.COLUMN['fail'].format(cls.RESULT['fail']))

    @classmethod
    def skip_test(cls, test_name):
        print(cls.COLUMN['test'].format(test_name) + cls.COLUMN['skip'].format(cls.RESULT['skip']))
