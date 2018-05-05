#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This is a skeleton file that can serve as a starting point for a Python
console script. To run this script uncomment the following line in the
entry_points section in setup.cfg:

    console_scripts =
     fibonacci = genderumrevelio.skeleton:run

Then run `python setup.py install` which will install the command `fibonacci`
inside your current environment.
Besides console scripts, the header (i.e. until _logger...) of this file can
also be used as template for Python modules.

Note: This skeleton file can be safely removed if not needed!
"""
from __future__ import division, print_function, absolute_import

import argparse
import sys
import logging
#from genderumrevelio import __version__

# Our imports
from networkconfigs import lstmtest, russian, lstm_v2, lstm_v3, lstm_v4, gaussian_naive_bayes
from datasets.load_files import load_blogs
from data_logging import local_logging
from data_logging import remote_logging


__author__ = "Christoffer Berglund, James Khoi Giang"
__copyright__ = "Christoffer Berglund, James Khoi Giang"
__license__ = "mit"

_logger = logging.getLogger(__name__)


def parse_args(args):
    """Parse command line parameters

    Args:
      args ([str]): command line parameters as list of strings

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    parser = argparse.ArgumentParser(
        description="Runner the neural network")
    parser.add_argument(
        '--version',
        action='version')
       # version='GenderumRevelio {ver}'.format(ver=__version__))
    parser.add_argument(
        '-v',
        '--verbose',
        dest="loglevel",
        help="set loglevel to INFO",
        action='store_const',
        const=logging.INFO)
    parser.add_argument(
        '-vv',
        '--very-verbose',
        dest="loglevel",
        help="set loglevel to DEBUG",
        action='store_const',
        const=logging.DEBUG)
    return parser.parse_args(args)


def setup_logging(loglevel):
    """Setup basic logging

    Args:
      loglevel (int): minimum loglevel for emitting messages
    """
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(level=loglevel, stream=sys.stdout,
                        format=logformat, datefmt="%Y-%m-%d %H:%M:%S")


def main(args):
    """Main entry point allowing external calls

    Args:
      args ([str]): command line parameter list
    """
    args = parse_args(args)
    setup_logging(args.loglevel)
    _logger.debug("Starting crazy calculations...")
    _logger.info("Script ends here")

#    log = lstm_v2.lstm_run(load_blogs(load_dataset='blog', activation='sigmoid', datasplit=0.75, datacut=0.2))
    gaussian_naive_bayes.run_gaussian(load_blogs(load_dataset='book', datasplit=0.75))
    #gaussian_naive_bayes.testing(load_blogs(load_dataset='book', datasplit=0.75))

    #  TODO: add timestamp and pass them to logging
    #try:
    #    local_logging.log(log)
    #except Exception as e:
    #    print("Local error:")
    #    print("args:", e.args)
    #    print("traceback:", e.with_traceback)
    #    print("e:", e)
    #try:
    #    remote_logging.remote_log(log)
    #except Exception as e:
    #    print("Remote error:")
    #    print("args:", e.args)
    #    print("traceback:", e.with_traceback)
    #    print("e:", e)
"""
    log = lstm_v3.lstm_run(load_blogs(load_dataset='book', activation='sigmoid', datasplit=0.5))
    #  TODO: add timestamp and pass them to logging
    try:
        local_logging.log(log)
    except Exception as e:
        print("Local error:")
        print("args:", e.args)
        print("traceback:", e.with_traceback)
        print("e:", e)
    try:
        remote_logging.remote_log(log)
    except Exception as e:
        print("Remote error:")
        print("args:", e.args)
        print("traceback:", e.with_traceback)
        print("e:", e)

    log = lstm_v4.lstm_run(load_blogs(load_dataset='book', activation='sigmoid', datasplit=0.5))
    #  TODO: add timestamp and pass them to logging
    try:
        local_logging.log(log)
    except Exception as e:
        print("Local error:")
        print("args:", e.args)
        print("traceback:", e.with_traceback)
        print("e:", e)
    try:
        remote_logging.remote_log(log)
    except Exception as e:
        print("Remote error:")
        print("args:", e.args)
        print("traceback:", e.with_traceback)
        print("e:", e)
"""
def run():
    """Entry point for console_scripts
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
