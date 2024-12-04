# --- Day 4: Ceres Search ---
import datetime
import re

def read_file() -> list:
    day = datetime.date.today().day
    file = open(f'Day{day}/Day{day}.in', 'r')
    inputData = file.readlines() 
            
    return inputData


def part_one(grid, word="XMAS") -> int:
    rows, cols = len(grid), len(grid[0]) - 1
    # print(rows, cols)
    word_len = len(word)
    directions = [
        (0, 1),  
        (0, -1), 
        (1, 0),  
        (-1, 0), 
        (1, 1),  
        (-1, -1), 
        (1, -1), 
        (-1, 1),
    ]
    
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def find_word(x, y, dx, dy):
        for i in range(word_len):
            nx, ny = x + i * dx, y + i * dy
            if not is_valid(nx, ny) or grid[nx][ny] != word[i]:
                return False
        return True

    count = 0
    for r in range(rows):
        for c in range(cols):
            for dx, dy in directions:
                if find_word(r, c, dx, dy):
                    count += 1
                    
    return count


def part_two(grid) -> int:
    rows, cols = len(grid), len(grid[0]) - 1
    pattern = "MAS"

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def check_x_mas(x, y):
        diag1 = [
            (x - 1, y - 1),  
            (x, y),         
            (x + 1, y + 1),
        ]
        diag2 = [
            (x - 1, y + 1), 
            (x, y),        
            (x + 1, y - 1), 
        ]

        diag1_chars = [grid[r][c] for r, c in diag1 if is_valid(r, c)]
        diag2_chars = [grid[r][c] for r, c in diag2 if is_valid(r, c)]

        return (
            "".join(diag1_chars) in (pattern, pattern[::-1])
            and "".join(diag2_chars) in (pattern, pattern[::-1])
        )

    count = 0
    for r in range(rows):
        for c in range(cols):
            if check_x_mas(r, c):
                count += 1

    return count

        
if __name__ == "__main__":
    # print(part_one(read_file()))
    print(part_two(read_file()))