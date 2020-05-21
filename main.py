import ast
import sys
from module_seed.run import run


if __name__ == '__main__':
    str_parameters = sys.argv[1]
    parameters = ast.literal_eval(str_parameters)
    run(parameters)