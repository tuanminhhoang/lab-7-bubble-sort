import time
from typing import Iterator

from rich.console import Console, Group
from rich.live import Live
from rich.text import Text

"""Terminal animation of bubble sort using Rich."""

numbers = [5, 4, 1, 2, 8]

console = Console()

def bbs(numbers: list[int]) -> Iterator[tuple[list[int], int | None, int | None]]:
    """Yield list states during bubble-sort comparisons."""
    yield numbers, None, None
    while True:
        swap = 0
        for i in range(len(numbers) - 1):
            yield numbers, i, i + 1
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swap += 1
        if swap == 0:
            break

def render_frame(step: list[int], a: int | None, b: int | None) -> Group:
    """Build one visual frame and highlight the currently compared bars."""
    lines = []
    for idx, n in enumerate(step):
        style = "bold red" if idx in (a, b) else "white"
        lines.append(Text(f'{"█" * n} ({n})', style=style))
    return Group(*lines)

def bbs_animated(numbers: list[int]) -> None:
    """Animate bubble sort in-place in the terminal."""
    with Live(render_frame(numbers, None, None), console=console, refresh_per_second=20, screen=False) as live:
        for step, a, b in bbs(numbers):
            live.update(render_frame(step, a, b))
            time.sleep(0.5)

bbs_animated(numbers)