import asyncio
import logging
import os
import pathlib
import sys

from aiohttp import ClientSession

from datetime import datetime, UTC


logging.basicConfig(
    level=logging.DEBUG,
    stream=sys.stdout,
    format="%(asctime)s %(message)s",
    datefmt="%Y/%m/%d %I:%M:%S",
)


def _get_session_id():
    if session_id := os.environ.get("AOC_SESSION_ID"):
        return session_id
    filepath = os.path.realpath(
        os.path.join(
            os.path.dirname(os.path.realpath(__file__)), "..", "session_id.txt"
        )
    )
    if os.path.exists(filepath):
        with open(filepath, mode="r") as f:
            return next(f, "").strip()

    return input("Please enter your session ID:\n> ")


def _now():
    return datetime.now().strftime("%H:%M:%S")


def _write_file(day, content):
    filepath = os.path.realpath(
        os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            "..",
            "day%d" % day,
            "input.txt",
        )
    )
    pathlib.Path(os.path.dirname(filepath)).mkdir(parents=True, exist_ok=True)
    pathlib.Path(os.path.join(os.path.dirname(filepath), "__init__.py")).touch(
        exist_ok=True
    )
    with open(filepath, "w") as f:
        f.write(content)


async def _fetch(session_id: str, year: int, day: int) -> str:
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    cookies = dict(session=session_id)

    async with ClientSession() as session:

        async def _get_content() -> str:
            async with session.get(url, cookies=cookies) as response:
                response.raise_for_status()
                return await response.text()

        while not (content := await _get_content()):
            logging.info(f"Retry in 2 seconds...")
            await asyncio.sleep(2)

        return content


async def main():
    logging.info("Start")
    session_id = _get_session_id()
    now = datetime.now(tz=UTC)
    max_day = 25 if now.month != 12 else now.day
    for day in range(1, max_day + 1):
        content = await _fetch(session_id, 2023, day)
        logging.info(f"Content found for day {day}")

        _write_file(day, content)


if __name__ == "__main__":
    asyncio.run(main())
