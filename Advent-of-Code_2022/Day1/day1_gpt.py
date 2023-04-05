# Read the input data
calories = []
while True:
  try:
    line = input()
  except EOFError:
    break
  if line:
    calories.append(int(line))
  else:
    calories.append(0)

# Initialize variables to keep track of the Elf carrying the most Calories and the total number of Calories they are carrying
max_calories = 0
max_elf = 0

# Iterate through the list of Calories and keep track of the Elf carrying the most Calories
current_elf = 0
current_calories = 0
for i in range(len(calories)):
  current_calories += calories[i]
  if current_calories > max_calories:
    max_calories = current_calories
    max_elf = current_elf
  if calories[i] == 0:
    current_elf += 1
    current_calories = 0

# Print the results
print("Elf", max_elf + 1, "is carrying the most Calories with a total of", max_calories, "Calories.")