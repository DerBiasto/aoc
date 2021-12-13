"""AoC 12, 2021: Passage Pathing"""

from aocd import get_data

InputType = dict[str, "Node"]
OutputType = int


class Node:
    def __init__(self, name: str):
        self.name = name
        self.small = name.islower()
        self.connections: InputType = {}

    def register_connection(self, other: "Node") -> None:
        self.connections[other.name] = other
        other.connections[self.name] = self


def parse(puzzle_input: str) -> InputType:
    """Parse file input."""
    nodes = {}
    for line in puzzle_input.split("\n"):
        a, b = line.split("-")
        if a not in nodes:
            nodes[a] = Node(a)
        if b not in nodes:
            nodes[b] = Node(b)
        nodes[a].register_connection(nodes[b])
    return nodes


def part1(data: InputType) -> OutputType:
    """Solve part 1."""
    start = data["start"]
    end = data["end"]
    all_paths = []
    q = [(start, "start")]
    for node, current_path in q:
        if node == end:
            all_paths.append(current_path)
            continue
        for n in node.connections.values():
            if not n.small or n.name not in current_path:
                q.append((n, current_path + "," + n.name))
    return len(all_paths)


def part2(data: InputType) -> OutputType:
    """Solve part 2."""
    start = data["start"]
    end = data["end"]
    all_paths = set()
    small_caves = {name for name in data if name.islower()} - {"start", "end"}
    for twice_visited_cave in small_caves:
        q: list[tuple[Node, str, int]] = [(start, "start", 0)]
        for node, current_path, count in q:
            if node == end:
                all_paths.add(current_path)
                continue
            for n in node.connections.values():
                if n.small:
                    if n.name == twice_visited_cave:
                        if count < 2:
                            q.append((n, current_path + "," + n.name, count + 1))
                        continue
                    elif n.name in current_path:
                        continue
                q.append((n, current_path + "," + n.name, count))
        print(sorted(all_paths))
    return len(all_paths)


def solve(data: InputType) -> list[str]:
    """Solve the puzzle for the given input."""
    solution1 = part1(data)
    solution2 = part2(data)

    ret = [str(solution1)]
    if solution2 is not None:
        ret.append(str(solution2))

    return ret


if __name__ == "__main__":
    data = parse(get_data(year=2021, day=12))
    print("\n".join(solve(data)))
