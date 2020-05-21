from module_seed.jobs import \
    job_one_seed,\
    job_two_seed
from module_seed.utils.logger_utils import get_logger
from module_seed.utils.spark_utils import create_spark_session


jobs = {
    'job_one_seed': job_one_seed.process,
    'job_two_seed': job_two_seed.process
}


def run(parameters):
    logger = get_logger()

    for parameter, value in parameters.items():
        logger.info('Param {param}: {value}'.format(param=parameter, value=value))

    spark_config = parameters['spark_config']
    spark = create_spark_session(spark_config=spark_config)

    job_name = parameters['job_name']

    process_function = jobs[job_name]
    process_function(
        spark=spark,
        input_path=parameters['input_path'],
        output_path=parameters['output_path'],
        save_mode='append'
    )
