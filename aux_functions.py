import os
import logging

logger = logging.getLogger(__name__)


def format_output(results):
    manylines = ""
    if isinstance(results[2], list):
        for tup in results[2]:
            manylines += f"     {tup[0]} mean prince is {tup[1]:.2f}\n"

    formatted_output = ""
    if results[0]:
        formatted_output += f"mean_bought_given_user is {results[0]:.2f} \n"
    if results[1]:
        formatted_output += (
            "----\n" f"sales_mean_by_month_given_year is {results[1]:.2f} \n"
        )
    if manylines:
        formatted_output += "----\n" f"sales_mean_by_product:\n{manylines}\n"
    return formatted_output


def remove_prev_output(fname):
    logger.info("Removing previous output '{}'".format(fname))
    try:
        os.remove(fname)
    except OSError:
        pass


def write_output(fname, content):
    logger.info("Writing to disk '{}'".format(fname))
    with open(fname, "w") as f:
        f.write(content)
