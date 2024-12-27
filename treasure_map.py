row = ['O', 'O', 'O']
map = [row, row[:], row[:]]
print(f"{map[0]}\n{map[1]}\n{map[2]}")

position = input("Where do you want to put the treasure? ")
col = int(position[0]) - 1
row = int(position[1]) - 1
map[row][col] = 'X'

print(f"{map[0]}\n{map[1]}\n{map[2]}")