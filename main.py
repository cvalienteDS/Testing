import os
import logging
from db_module import DB
from Utils.read_config import read_yaml_config
from Utils.setup_logging import setup_logging
from aux_functions import format_output, remove_prev_output, write_output

setup_logging(os.path.join(os.path.dirname(__file__), "Utils/logging.yaml"), Logs_path='Logs')

if __name__ == '__main__':
    cfg = read_yaml_config(r"Utils/config.yml")
    db_instance = DB(path=cfg['db']['path'])

    result01 = db_instance.mean_bought_given_user(user=cfg['queries']['mean_bought_given_user']['parameters']['user'])

    result02 = db_instance.sales_mean_by_month_given_year(year=cfg['queries']['sales_mean_by_month_given_year']['parameters']['year'])

    result03 = db_instance.sales_mean_by_product()

    output = format_output([result01, result02, result03])
    remove_prev_output(cfg['output']['filename'])
    write_output(cfg['output']['filename'], content=output)
