from package1.libs import lib1
from package1 import module1
import pandas
from pprint import pprint


def _():
    return 'package1.__main__', module1._(), lib1._(), pandas.__version__


if __name__ == '__main__':
    pprint(_())
