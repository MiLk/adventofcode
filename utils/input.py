#!/usr/bin/env python

from __future__ import print_function
from __future__ import unicode_literals

import os
import requests
import sys
import time

from datetime import datetime


def _get_args():
    session_id = os.environ['AOC_SESSION_ID']

    cwd = os.getcwd()
    cwds = cwd.split('/')
    if cwds[-1].startswith('day') and \
       cwds[-1][3:].isdigit() and \
       cwds[-2].isdigit():
        return session_id, int(cwds[-2]), int(cwds[-1][3:])

    return session_id, int(sys.argv[1]), int(sys.argv[2])


def _now():
    return datetime.now().strftime('%H:%M:%S')


def _url(year, day):
    return "http://adventofcode.com/%d/day/%d/input" % (year, day)


def _get(url, cookies):
    r = requests.get(url, cookies=cookies)
    if r.status_code != 200:
        return None
    return r.text


def _write_file(year, day, content):
    filepath = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "..",
        str(year),
        "day%d" % day,
        "input.txt"
    )
    with open(filepath, 'w') as f:
        f.write(content)


def fetch(session_id, year, day):
    url = _url(year, day)
    cookies = dict(session=session_id)

    content = _get(url, cookies)
    while not content:
        print("[%s] Retry in 2 seconds..." % _now())
        time.sleep(2)
        content = _get(url, cookies)

    print("[%s] Content found:" % _now())
    print(content)

    _write_file(year, day, content)


if __name__ == "__main__":
    fetch(*_get_args())
