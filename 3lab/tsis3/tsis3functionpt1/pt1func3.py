def solve(heads, legs):
    rabbit = (legs - 2 * heads) / 2
    chicken = heads - rabbit
    print(chicken, rabbit)
solve(35, 94)