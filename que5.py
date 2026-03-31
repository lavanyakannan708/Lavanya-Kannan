logs = input().split()

total_errors = 0
max_streak = 0
current_streak = 0

for log in logs:
    if log == "ERROR":
        total_errors += 1
        current_streak += 1
        max_streak = max(max_streak, current_streak)
    else:
        current_streak = 0

print("Total Errors:", total_errors)
print("Longest Streak:", max_streak)
