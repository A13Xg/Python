from unicodedata import numeric


print("-----------------------")
print("Advent of Code Day1-1")
print("-----------------------")

with open('input1.txt') as input:
    inputLines = input.readlines()

maxValue = 0
value = 0
inventoryList = []

for lineCount,singleLine in enumerate(inputLines):
    print(f"Processing Line: {lineCount}")
    if singleLine != '\n':
        value += int(singleLine)
    else:
        inventoryList.append(value)
        value = 0
        print(inventoryList)
inventoryList.sort(reverse=True)
print(f"Final Readout: {inventoryList}")
print("")
print(f"Top 3 Elf Calorie Values: {inventoryList[0]}, {inventoryList[1]}, {inventoryList[2]}")
topTotal = inventoryList[0] + inventoryList[1] + inventoryList[2]
print(f"Total Calories for Top 3 Elfs: {topTotal}")