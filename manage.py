# -*- coding: utf-8 -*-
""" Module for managing tasks through a simple cli interface. """
# Libraries
import os
import sys

from os.path import abspath, dirname
sys.path.insert(0, dirname(abspath(__file__)))

from manager import Manager

from goblin import run_app, register_component

manager = Manager()

@manager.command
def run():
    """ Starts server on port 5xxx """
    register_component("press")
    run_app(host="0.0.0.0", port=8080, debug=True, workers=os.cpu_count())

if __name__ == '__main__':
    manager.main()
