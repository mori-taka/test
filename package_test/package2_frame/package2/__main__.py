from package1 import __main__
from pprint import pprint


def _():
    return 'package2.__main__', __main__._()


if __name__ == '__main__':
    pprint(_())
