# --- Day 3: Mull It Over ---
import datetime
import re

def readFile() -> list:
    day = datetime.date.today().day
    file = open(f'Advent-of-Code-2024/Day{day}/Day{day}.in', 'r')
    inputData = file.read() 
            
    return inputData


def partOne() -> int:
    sectionData = readFile()
    pattern = r"mul\((\d+),(\d+)\)"
    
    ans = 0
    
    for section in sectionData:
        matches = re.findall(pattern, section)
        
        for match in matches:
            a, b = map(int, match)
            
            ans += a * b
        
    return ans


def partTwo() -> int:
    sectionData = readFile()
    pattern = r"don't\(\).*?do\(\)"
    pattern1 = r"mul\((\d+),(\d+)\)"
    
    ans = 0
    joinSection = ''
    
    for section in sectionData:
        joinSection += section.strip()

    cleaned_section = re.sub(pattern, '', joinSection)
    
    matches = re.findall(pattern1, cleaned_section)
    
    for match in matches:
        a, b = map(int, match)
        
        ans += a * b
        
    return ans

        
if __name__ == "__main__":
    # print(partOne())
    print(partTwo())