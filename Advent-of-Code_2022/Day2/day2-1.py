print("-----------------------")
print("Advent of Code Day2-1")
print("-----------------------")

A = "Rock"
B = "Paper"
C = "Scissors"
X = "Rock"
Y = "Paper"
Z = "Scissors"

map = {"A X": 4, "A Y": 8, "A Z": 3, "B X": 1, "B Y": 5, "B Z": 9, "C X": 7, "C Y": 2, "C Z": 6}

playRock = 1
playPaper = 2
playScissors = 3

outcomeLoss = 0
outcomeDraw = 3
outcomeWin = 6

result = 0
totalScore = 0

with open('input2.txt') as input:
    inputLines = input.read()

for lineCount, singleLine in enumerate(inputLines.split("\n")):
    print(f"Processing Line: {lineCount}")
    print(f"Line Data: {singleLine}")

    totalScore += map[singleLine]
    print(totalScore)
