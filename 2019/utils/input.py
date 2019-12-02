import logging
import requests
import time


def _url(year, day):
    return "http://adventofcode.com/%d/day/%d/input" % (year, day)


def _get(url, cookies):
    r = requests.get(url, cookies=cookies)
    if r.status_code != 200:
        return None
    return r.text


def fetch(session_id, year, day, input_path):
    url = _url(year, day)
    cookies = dict(session=session_id)

    content = _get(url, cookies)
    while not content:
        logging.info("Retry in 2 seconds...")
        time.sleep(2)
        content = _get(url, cookies)

    logging.debug("Content found:")
    logging.debug(content)

    with open(input_path, 'w') as f:
        f.write(content)

