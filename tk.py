import tkinter as tk
from typing import Iterator

#data
numbers = [5, 4, 1, 2, 8]

root = tk.Tk()
root.title("Bubble Sort")

#canva
canvas = tk.Canvas(root, width=500, height=400, bg="white")
canvas.pack()

def draw(numbers, a, b):
    canvas.delete("all")
    max_display_height = 300
    base_y = 350
    canvas_width = 500
    padding = 50 

    #flexible height
    max_number = max(numbers)
    scale = max_display_height / max_number

    #flexible width
    available_width = canvas_width - (2 * padding)
    width_col = available_width / len(numbers) * 0.8
    gap = available_width / len(numbers) * 0.2

    #draw
    for idx, val in enumerate(numbers):
        x1 = 50 + idx * (width_col + gap)
        y1 = base_y - val * scale 
        x2 = x1 + width_col
        y2 = base_y
        
        if idx in (a, b):
            canvas.create_rectangle(x1, y1, x2, y2, fill="red", outline="red", width=2)
        else:
            canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="blue", width=2)
        canvas.create_text(x1 + width_col/2, y1 - 10, text=str(val))

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

def bbs_animated(generator):
    try:
        step, a, b = next(generator)
        draw(step, a, b)
        root.after(500, lambda: bbs_animated(generator  ))
    except StopIteration:
        print("Done!")

my_generator = bbs(numbers)
bbs_animated(my_generator)

root.mainloop()