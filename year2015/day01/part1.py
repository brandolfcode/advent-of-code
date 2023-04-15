
def calc_floor(directions: str) -> int:
    return 2*directions.count('(') - len(directions)


with open('input.txt') as f:
    inputs = f.read().splitlines(keepends=False)

for input in inputs:
    print(calc_floor(input))
