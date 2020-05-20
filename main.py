import ast
import sys
from module_seed.jobs import \
    job_one_seed,\
    job_two_seed
from module_seed.utils.logger_utils import get_logger
from module_seed.utils.spark_utils import create_spark_session


def main(parameters):
    logger = get_logger()
    spark = create_spark_session()

    for parameter, value in parameters.items():
        logger.info('Param {param}: {value}'.format(param=parameter, value=value))

    job_name = parameters['job_name']

    process_function = jobs[job_name]
    process_function(
        spark=spark,
        input_bucket=parameters['input_bucket'],
        output_bucket=parameters['output_bucket'],
        output_bucket_prefix=parameters['output_bucket_prefix'],
        save_mode='append')


if __name__ == '__main__':
    jobs = {
        'job_one_seed': job_one_seed.process,
        'job_two_seed': job_two_seed.process
    }

    str_parameters = sys.argv[1]
    parameters = ast.literal_eval(str_parameters)
    main(parameters)