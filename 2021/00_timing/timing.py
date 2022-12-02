import pathlib
import time

timing_dir = pathlib.Path(__file__).parent
year_dir = timing_dir.parent

part1, part2 = [], []

for i in range(1, 26):
    for subdir in year_dir.iterdir():
        if subdir.is_dir() and subdir.name.startswith("{:0>2}".format(i)):
            filename = "aoc{}{:0>2}".format(year_dir.name, i)
            m = getattr(__import__(subdir.name + "." + filename), filename)
            puzzle_input = m.parse((subdir / "input.txt").read_text())
            start = time.time()
            m.part1(puzzle_input)
            part1.append(time.time() - start)
            puzzle_input = m.parse((subdir / "input.txt").read_text())
            start = time.time()
            m.part2(puzzle_input)
            part2.append(time.time() - start)

with (timing_dir / "output.txt").open("w", ) as f:
    f.write(", ".join(map(str, part1)))
    f.write("\n")
    f.write(", ".join(map(str, part2)))
