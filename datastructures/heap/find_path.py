import heapq


map_ = """\
.......X..
.......X..
....XXXX..
..........
..........
"""


def parse_map(map_):
    lines = map_.splitlines()
    origin = 0, 0
    destination = len(lines[-1]) - 1, len(lines) - 1
    return lines, origin, destination


def is_valid(lines, position):
    x, y = position
    if not 0 <= y < len(lines) or not 0 <= x < len(lines[y]):
        return False
    return lines[y][x] != "X"


def get_neighbors(lines, current):
    x, y = current
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            position = x + dx, y + dy
            if is_valid(lines, position):
                yield position


def get_shorter_paths(tentative, positions, through):
    path = tentative[through] + [through]
    for position in positions:
        if position in tentative and len(tentative[position]) <= len(path):
            continue
        yield position, path


def find_path(map_):
    lines, origin, destination = parse_map(map_)
    tentative = {origin: []}
    candidates = [(0, origin)]
    certain = set()
    while destination not in certain and candidates:
        _, current = heapq.heappop(candidates)
        if current in certain:
            continue
        certain.add(current)
        neighbors = set(get_neighbors(lines, current)) - certain
        shorter = get_shorter_paths(tentative, neighbors, current)
        for neighbor, path in shorter:
            tentative[neighbor] = path
            heapq.heappush(candidates, (len(path), neighbor))
    if destination in tentative:
        return tentative[destination] + [destination]
    else:
        raise ValueError("no path")


def show_path(path, map_):
    lines = map_.splitlines()
    for x, y in path:
        lines[y] = f"{lines[y][:x]}@{lines[y][x + 1 :]}"
    return "\n".join(lines) + "\n"


path = find_path(map_)
print(show_path(path, map_))
