example = """199
200
208
210
200
207
240
269
260
263"""

def count_increase(data: str)-> int:
    numbers = [int(x) for x in data.split("\n")]
    count = 0;
    for i in range(len(numbers)-1):
        if numbers[i+1] > numbers[i]:
            count += 1
    return count

assert count_increase(example) == 7

#Part-2
def count_window_increase(data: str, size :int =3)-> int:
    numbers = [int(x) for x in data.split("\n")]
    count = 0;
    for i in range(len(numbers)-size):
        if numbers[i+size] > numbers[i] : # Since other/inner numbers are the same
            count += 1
    return count

assert count_window_increase(example) == 5

if __name__ == '__main__':
    with open("d1.txt") as f:
        content = f.read()

    print(count_increase(content))
    print(count_window_increase(content))
        
