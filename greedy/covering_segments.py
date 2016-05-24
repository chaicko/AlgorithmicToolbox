# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):
    segments.sort(key=lambda x: x.end)
    points = [segments.pop(0).end]
    for s in segments:
        if s.start > points[-1]:
            points.append(s.end)
    return points


def main():
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(
        map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')

if __name__ == '__main__':
    main()
