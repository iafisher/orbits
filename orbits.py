import shutil
import time

import theory0


def view(theory, t):
    sun, earth = theory.solar_system(t)
    height = int(3 * _screen_height() / 4)
    graph = _Graph(height)
    scale = 2 * theory.EARTH_ORBIT_RADIUS / (height / 2)
    origin = (-1.5 * theory.EARTH_ORBIT_RADIUS, 1.5 * theory.EARTH_ORBIT_RADIUS)
    graph.plot(_adjust(sun, scale, origin), "S")
    graph.plot(_adjust(earth, scale, origin), "E")
    graph.draw()


def animate(theory, start, end, step=None, *, sleep=0.5):
    if not step:
        step = (end - start) // 10

    for t in range(start, end, step):
        _hline(f"t = {t}s")
        view(theory, t)
        _hline()

        if t + step < end:  # i.e., if not the last iteration
            print()
            print()
            time.sleep(sleep)


def orbit(theory):
    step = theory.EARTH_ORBIT_DURATION // 20
    animate(theory, 0, theory.EARTH_ORBIT_DURATION, step)


class _Graph:
    def __init__(self, height):
        self.points = []
        self.height = height

    def plot(self, xy, symbol):
        self.points.append((xy, symbol))
        # Sort first by y then by x.
        self.points.sort(key=lambda item: (item[0][1], item[0][0]))

    def draw(self):
        current_x = 0
        current_y = 0
        for (x, y), symbol in self.points:
            if current_y < y:
                print("\n" * (y - current_y), end="")
                print(" " * x, end="")
            else:
                print(" " * (x - current_x), end="")

            print(symbol, end="")

            current_x = x + 1
            current_y = y

        if current_y < self.height:
            print("\n" * (self.height - current_y), end="")


def _hline(msg=None):
    width = _screen_width()
    if msg:
        print("--[ " + msg + " ]", end="")
        print("-" * (width - len(msg) - 6))
    else:
        print("-" * width)


def _screen_width():
    return shutil.get_terminal_size()[0]


def _screen_height():
    return shutil.get_terminal_size()[1]


def _adjust(xyz, scale, origin):
    x, y, _ = xyz
    x = -origin[0] + x
    y = origin[1] - y
    return (int(x / scale), int(y / scale))
