import argparse

class Solver24:
    def __init__(self, nums):
        self.nums = nums

    def build_permutations(self):
        permutations = []
        for a in self.nums:
            for b in self.nums:
                if b == a:
                    continue
                for c in self.nums:
                    if c in [a, b]:
                        continue
                    for d in self.nums:
                        if d in [a, b, c]:
                            continue
                        permutations.append([a, b, c, d])
        return permutations

    def build_ops(self):
        ops = ['+', '-', '*', '/']
        ops_permutations = []
        for a in ops:
            for b in ops:
                for c in ops:
                    ops_permutations.append([a, b, c])
        return ops_permutations

    def solve(self):
        permutations = self.build_permutations()
        ops_permutations = self.build_ops()
        res = set()

        for p in permutations:
            for ops in ops_permutations:
                a, b, c, d = p
                op1, op2, op3 = ops

                expressions = [
                    f'(({a} {op1} {b}) {op2} {c}) {op3} {d}',
                    f'({a} {op1} ({b} {op2} {c})) {op3} {d}',
                    f'{a} {op1} (({b} {op2} {c}) {op3} {d})',
                    f'{a} {op1} ({b} {op2} ({c} {op3} {d}))',
                    f'({a} {op1} {b}) {op2} ({c} {op3} {d})',
                    f'{a} {op1} {b} {op2} {c} {op3} {d}'
                ]

                for expr in expressions:
                    try:
                        if eval(expr) == 24:
                            res.add(expr)
                    except ZeroDivisionError:
                        pass

        print(res)
        return res

def main():
    parser = argparse.ArgumentParser(description="Let's play 24.")
    parser.add_argument('nums', metavar='N', type=int, nargs=4,
                        choices=range(1, 14),
                        help='Choose 4 numbers from 1 to 13.')
    args = parser.parse_args()

    solver = Solver24(args.nums)
    solver.solve()

if __name__ == '__main__':
    main()
