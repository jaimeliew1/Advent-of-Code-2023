import importlib
from time import perf_counter

t_total = 0.0
for day in range(1, 25 + 1):
    try:
        package = importlib.import_module(f"day{day:02}")
    except ModuleNotFoundError:
        break

    t_start = perf_counter()
    ans = package.solve(package.parse(package.INPUT_FN))
    t_elapsed = perf_counter() - t_start

    print(f"day{day:02}: {ans} in {t_elapsed:.3f}s")
    t_total += t_elapsed

print(f"\ntotal time: {t_total:.3f}s")
