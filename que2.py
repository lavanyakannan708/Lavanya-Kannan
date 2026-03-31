total_messages = int(input())

if total_messages <= 100:
    print(f"Status: Normal, Active: {total_messages}, Compressed: 0")
else:
    compressed = total_messages - 100
    print(f"Status: Optimized, Active: 100, Compressed: {compressed}")
