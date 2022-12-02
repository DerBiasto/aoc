import pathlib
import matplotlib.pyplot as plt

timing_dir = pathlib.Path(__file__).parent

with (timing_dir / "output.txt").open("r") as f:
    part1 = list(map(float, f.readline().split(", ")))
    part2 = list(map(float, f.readline().split(", ")))
part1.append(sum(part1))
part2.append(sum(part2))

x = list(range(1, len(part1) + 1))
labels = x[:-1] + ["total"]

_fig, ax = plt.subplots()
plt.bar(x, part1, width=0.25)
plt.bar([v + 0.25 for v in x], part2, width=0.25)
plt.bar([v + 0.5 for v in x], [a + b for a, b in zip(part1, part2)], width=0.25)
ax.set_xticks(x, labels)
plt.show()
