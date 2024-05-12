

def build_permutations(nums):
    permutations = []
    for a in nums:
        for b in nums:
            if b == a:
                continue
            for c in nums:
                if c in [a, b]:
                    continue
                for d in nums:
                    if d in [a, b, c]:
                        continue
                    permutations.append([a, b, c, d])
    return permutations


def build_ops():
    ops = ['+', '-', '*', '/']
    ops_permutations = []
    for a in ops:
        for b in ops:
            for c in ops:
                ops_permutations.append([a, b, c])
    return ops_permutations




def solve_24(nums):
    # a, b, c, d = nums

    permutations = build_permutations(nums)
    
    print(permutations)
    print(len(permutations))

    ops_permutations = build_ops()
    
    print(ops_permutations)


    res = set()
    for p in permutations:
        for ops in ops_permutations:
            a, b, c, d = p
            op1, op2, op3 = ops

            # ((a . b) . c) . d
            try:
                if eval(f'(({a} {op1} {b}) {op2} {c}) {op3} {d}') == 24:
                    expr = f'(({a} {op1} {b}) {op2} {c}) {op3} {d}'
                    res.add(expr)
                    # return True

                # (a . (b . c)) . d
                if eval(f'({a} {op1} ({b} {op2} {c})) {op3} {d}') == 24:
                    expr = f'({a} {op1} ({b} {op2} {c})) {op3} {d}'
                    res.add(expr)

                # a . ((b . c ) . d)
                if eval(f'{a} {op1} (({b} {op2} {c}) {op3} {d})') == 24:
                    expr = f'{a} {op1} (({b} {op2} {c}) {op3} {d})'
                    res.add(expr)

                # a . (b . (c . d))
                if eval(f'{a} {op1} ({b} {op2} ({c} {op3} {d}))') == 24:
                    expr = f'{a} {op1} ({b} {op2} ({c} {op3} {d}))'
                    res.add(expr)

                # (a . b) . (c . d)
                if eval(f'({a} {op1} {b}) {op2} ({c} {op3} {d})') == 24:
                    expr = f'({a} {op1} {b}) {op2} ({c} {op3} {d})'
                    res.add(expr)
                
                # a . b . c . d
                if eval(f'{a} {op1} {b} {op2} {c} {op3} {d}') == 24:
                    expr = f'{a} {op1} {b} {op2} {c} {op3} {d}'
                    res.add(expr)
            except ZeroDivisionError:
                pass
    print(res)
    
        
        



solve_24([1, 2, 3, 4])
solve_24([6, 4, 1, 3])


