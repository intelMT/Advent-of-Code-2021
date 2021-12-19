example = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""

def power_consumption(data :str)-> int:

    binaries = [x.strip() for x in data.split("\n")]
    counts = [0 for _ in binaries[0]]

    for bi_num in binaries:  
        for i, num in enumerate(str(bi_num)):
            if num == '1':
                counts[i] += 1

    gamma = [1 if count > len(binaries)/2 else 0 for count in counts ]
    gamma = "".join(str(item) for item in gamma)

    epsilon = [1 if count < len(binaries)/2 else 0 for count in counts ]
    epsilon = "".join(str(item) for item in epsilon)

    return int(gamma,2)*int(epsilon,2)

assert power_consumption(example) == 198

#Part-2
def life_support_rating(data :str)-> int:
    binaries = [x.strip() for x in data.split("\n")]
    counts = [0 for _ in binaries[0]]

    binO2 = optimize(binaries, O2=True)
    binCO2 = optimize(binaries, O2=False)
    return int(binO2,2) *int(binCO2,2)

def filter(nums : list, col :int, O2: bool)-> list:
    # Majority wins for O2 generator
    if O2:
        if sum(int(item[col]) for item in nums) >= len(nums)/2:
            result = '1'
        else:
            result = '0'
    else: # Minority wins for CO2 scrubber
        if sum(int(item[col]) for item in nums) < len(nums)/2:
            result = '1'
        else:
            result = '0'
    return [item for item in nums if item[col]==result]

def optimize(binaries : list, O2:bool) -> str:
    x = binaries.copy()
    i = 0
    while len(x)>1:
        x = filter(x, col=i, O2=O2)
        i += 1
    return "".join(x)    

assert life_support_rating(example) == 230


if __name__ == '__main__':
    with open('d3.txt') as f:
        content = f.read()

    print(power_consumption(content))
    print(life_support_rating(content))