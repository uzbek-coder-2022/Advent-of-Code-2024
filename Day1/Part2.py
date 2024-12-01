# --- Part Two ---

def solve() -> int:
    file = open('Advent-of-Code-2024/Day1/Day1.in', 'r')
    inputData = file.readlines()
    
    nums = []
    frequency = {}
    
    for line in inputData:
        (first, second) = map(int, line.strip().split('   '))
        nums += [first]
        frequency[second] = frequency.get(second, 0) + 1
    
    ans = 0
    
    for num in nums:
        ans += num * frequency.get(num, 0)
        
    return ans
        
        
if __name__ == "__main__":
    print(solve())