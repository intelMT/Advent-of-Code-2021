example = """16,1,2,0,4,2,7,1,2,14"""

import numpy as np

def preprocess (data :str)-> list:
    return [int(x) for x in data.split(',')]

def min_fuel(crabs: list) -> int:
    crabs = sorted(crabs)
    med = crabs[len(crabs)//2]
    return sum(abs(x-med) for x in crabs)

crabs = preprocess(example)
min_fuel(crabs=crabs) == 37

# Part-2
def min_fuel_2(crabs: list) -> int:
    scores = list()
    # The minimum fuel location seems to be shifting from the median to the mean as distance is more costly now (squared)
    med = np.median(crabs)
    print(f"The Median: {med}")
    avg = np.mean(crabs)
    print(f"The Average: {avg}")
    # Want to scan ~20% of the max-min range around the rounded mean value (part-2 data works with a 1% scan smallest)
    pct = 0.20
    space = (max(crabs)-min(crabs))*(pct/2)
    space = round(space)
    for x in range(int(avg)-space, int(avg)+space):
        s = 0    
        for crab in crabs:
            s += abs(x-crab)*(abs(x-crab)+1)/2
        scores.append(int(s))
    print("The location for the least fuel is {}".format(int(avg)-space + np.argmin(scores)) )
    return min(scores)

assert min_fuel_2(crabs=crabs) == 168

if __name__ == '__main__':
    with open('d7.txt') as f:
        content = f.read()
    
    CRABS = preprocess(content)
    print("The fuel consumption for the 1st part: {} \n".format(min_fuel(crabs= CRABS)))
    print("The fuel consumption for the 2nd part: {}".format(min_fuel_2(crabs= CRABS)))
