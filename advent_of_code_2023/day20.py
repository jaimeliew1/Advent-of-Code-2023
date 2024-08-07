from dataclasses import dataclass
from math import lcm
from pathlib import Path

INPUT_FN = Path(__file__).parent.parent / "input/day20.txt"


@dataclass
class Command:
    From: str
    Signal: bool
    To: str


@dataclass
class FlipFlop:
    Output: list[str]
    State: bool = False

    def trigger(self, command: Command) -> list[Command]:
        if command.Signal:
            return []
        self.State = not self.State
        return [Command(command.To, self.State, out) for out in self.Output]


@dataclass
class Conjunction:
    Output: list[str]
    State: dict[bool]

    def trigger(self, com: Command) -> list[Command]:
        self.State[com.From] = com.Signal
        return [Command(com.To, not all(self.State.values()), x) for x in self.Output]


@dataclass
class Broadcaster:
    Output: list[str]

    def trigger(self, com: Command) -> list[Command]:
        return [Command(com.To, com.Signal, out) for out in self.Output]


def parse(fn: Path) -> dict:
    modules_raw = []
    for line in open(fn):
        modules_raw.append(
            (
                line[0],
                line[1:].split()[0],
                [x.strip() for x in line.split("->")[1].split(",")],
            )
        )

    has_inputs = {}
    for type, name, outputs in modules_raw:
        for output in outputs:
            if output not in has_inputs:
                has_inputs[output] = []
            has_inputs[output].append(name)

    modules = {"rx": Broadcaster([])}
    for type, name, outputs in modules_raw:
        match type:
            case "%":
                modules[name] = FlipFlop(outputs)
            case "&":
                modules[name] = Conjunction(
                    outputs, {k: False for k in has_inputs[name]}
                )
            case "b":
                modules["broadcaster"] = Broadcaster(outputs)
    return modules


def solve(modules: dict) -> int:
    cycles, count = [], {True: 0, False: 0}
    presses, ans1 = 0, 0
    
    # Part 2: assume output, rx, is connected to a conjunction of conjunctions.
    # monitor their cycles and find the lcm.
    to_monitor = list([m for m in modules.values() if "rx" in m.Output][0].State.keys())
    while True:
        presses += 1
        command_stack = [Command(None, False, "broadcaster")]
        while command_stack:
            command = command_stack.pop(0)
            count[command.Signal] += 1
            if command.From in to_monitor and command.Signal:
                cycles.append(presses)
                if len(cycles) == len(to_monitor):
                    return ans1, lcm(*cycles)
            command_stack.extend(modules[command.To].trigger(command))
        if presses == 1000:
            ans1 = count[True] * count[False]


if __name__ == "__main__":
    print(solve(parse(INPUT_FN)))
