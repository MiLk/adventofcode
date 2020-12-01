#!/usr/bin/env python

import os
from os import path

import click
import datetime
import logging
from pathlib import Path
from importlib import import_module
from utils.input import fetch


@click.command()
@click.option('--day', type=int, help='Day of the month.', default=datetime.datetime.today().day)
@click.option('--session', type=str, help='Your Advent of Code session cookier', envvar='AOC_SESSION_ID')
@click.option('--debug/--no-debug')
def main(day, session, debug):
    loglevel = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=loglevel)

    package_name = f'day{day}'
    input_path = Path(__file__).resolve().parent / package_name / 'input.txt'

    logging.debug(f"using input located at {input_path}")

    if not path.exists(input_path) or os.path.getsize(input_path) == 0:
        if session:
            fetch(session, 2020, day, input_path)
        else:
            raise RuntimeError("no input file present and no Advent of Code session set")

    with open(input_path) as f:
        module_object = import_module(package_name)
        p1, p2 = getattr(module_object, 'p1'), getattr(module_object, 'p2')
        lines = getattr(module_object, 'parse_input')(f.readlines())

        logging.debug('part 1: start')
        s1 = p1(lines)
        print('Part 1:', s1)
        logging.debug('part 1: end')
        logging.debug('part 2: start')
        s2 = p2(lines)
        print('Part 2:', s2)
        logging.debug('part 2: end')


if __name__ == "__main__":
    main()
