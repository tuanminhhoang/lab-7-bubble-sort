import time


numbers = [5, 1, 4, 2, 8]


def bbs(numbers):
    sort = True
    while sort:
        swap = 0
        for i in range(0, len(numbers) - 1):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                swap += 1
        if swap == 0:
            break
    return numbers


def bubble_sort_steps(values):
    """Yield snapshots of the list after each swap (in-place sorting)."""
    # TODO: Decide if you also want to yield comparison states (not just swaps).
    # TODO: Add metadata to each frame (pass index, compare index, swap count).
    sort = True
    while sort:
        swap = 0
        for i in range(0, len(values) - 1):
            if values[i] > values[i + 1]:
                values[i], values[i + 1] = values[i + 1], values[i]
                swap += 1
                yield values[:]
        if swap == 0:
            break


def clear_and_home():
    """Move cursor to home and clear the terminal for in-place redraw."""
    # TODO: Keep fallback behavior for terminals without ANSI support.
    print("\033[H\033[J", end="")


def render_ascii_bars(frame, highlighted_index=None):
    """Render one frame as horizontal bars in the terminal."""
    # TODO: Handle negative numbers (offset, split axis, or custom symbol rules).
    # TODO: Scale very large values so they fit in the terminal width.
    print("Bubble Sort Visualization")
    print("-" * 30)
    for idx, value in enumerate(frame):
        marker = " <" if highlighted_index == idx else ""
        bar = "#" * max(value, 0)
        print(f"{idx:>2}: {bar} ({value}){marker}")


def animate_bubble_sort(values, delay=0.20):
    """Control loop for in-place redraw animation of bubble sort."""
    # TODO: Add controls for pause/resume/step mode.
    # TODO: Add a max frame guard for extremely large inputs.
    working = values[:]
    clear_and_home()
    render_ascii_bars(working)
    time.sleep(delay)

    for frame in bubble_sort_steps(working):
        clear_and_home()
        render_ascii_bars(frame)
        time.sleep(delay)

    return working


if __name__ == "__main__":
    # TODO: Replace this call with animate_bubble_sort(numbers) when you
    # finish the visualization details you want (colors, labels, controls).
    print(bbs(numbers))
