from package1 import module1
from pprint import pprint


def _():
    return 'module2', module1._()


if __name__ == '__main__':
    pprint(_())
