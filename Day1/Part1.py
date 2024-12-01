# --- Day 1: Historian Hysteria ---

def solve() -> int:
    file = open('Advent-of-Code-2024/Day1/Day1.in', 'r')
    inputData = file.readlines()
    
    nums1 = []
    nums2 = []
    
    for line in inputData:
        (first, second) = map(int, line.strip().split('   '))
        nums1 += [first]
        nums2 += [second]
    
    nums1.sort()
    nums2.sort()
    
    ans = 0
    
    for first, second in zip(nums1, nums2):
        # print(first, second)
        ans += abs(second - first)
        
    return ans
        
        
if __name__ == "__main__":
    print(solve())