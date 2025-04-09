d1 = {}
n = int(input("Enter the number of students: "))

for i in range(n):
    key = input("Enter student's name: ")
    marks = int(input("Enter student's marks: "))
    d1[key] = marks

#for ascending of marks
ascending = sorted(d1.items(), key=lambda v: v[1])
print("Students sorted by marks (ascending):", ascending)
#for desending of marks
descending = sorted(d1.items(), key=lambda v: v[1], reverse=True)
print("Students sorted by marks (descending):", descending)
#for top 3 students based on marks
top_3_students = descending[:3]
print("Top 3 students with highest marks:", top_3_students)
#for sorting alphabetically
alphabetical = sorted(d1.items())
print("Students sorted by name (alphabetically):", alphabetical)
####2#####
players = []
n = int(input("Enter the number of players: "))

for i in range(n):
    name = input("Enter player name: ")
    goals = int(input("Enter goals scored: "))
    players.append((name, goals))

# Sorting in ascending order by goals
ascending = sorted(players, key=lambda v: v[1])
print("Players sorted by goals (ascending):", ascending)

# Sorting in descending order by goals
descending = sorted(players, key=lambda v: v[1], reverse=True)
print("Players sorted by goals (descending):", descending)

# Finding the top 3 goal scorers
top_3_players = descending[:3]
print("Top 3 goal scorers:", top_3_players)

# Sorting players by name alphabetically
alphabetical = sorted(players, key=lambda v: v[0])
print("Players sorted by name (alphabetically):", alphabetical)
