import asyncio

from utils.file import read_input

GameDraws = list[dict[str, int]]


def parse_cube(cube: str) -> tuple[str, int]:
    n, color = cube.strip().split(" ", maxsplit=1)
    return color[0], int(n)


def parse_line(line: str) -> tuple[int, GameDraws]:
    game, raw_draws = line.split(":")
    game_id = int(game[5:])
    draws = [dict(parse_cube(cube) for cube in draw.strip().split(", ")) for draw in raw_draws.split(";")]
    return game_id, draws


def is_possible_game(draws: GameDraws, load: tuple[int, int, int]) -> bool:
    r, g, b = load
    return all(draw.get("r", 0) <= r and draw.get("g", 0) <= g and draw.get("b", 0) < b for draw in draws)


async def main() -> None:
    games: dict[int, GameDraws] = dict(map(parse_line, read_input()))
    print(sum(game_id for game_id, draws in games.items() if is_possible_game(draws, (12, 13, 14))))

    print(
        sum(
            max(d.get("r", 0) for d in draws) * max(d.get("g", 0) for d in draws) * max(d.get("b", 0) for d in draws)
            for draws in games.values()
        )
    )


if __name__ == "__main__":
    asyncio.run(main())
