from package1.libs import lib1
import pandas
from pprint import pprint


def _():
    return 'module1', lib1._(), pandas.__version__


if __name__ == '__main__':
    pprint(_())
