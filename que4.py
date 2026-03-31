amount = int(input())
location = input()
time = input()
failed_attempts = int(input())

# LOCK condition
if failed_attempts >= 3:
    print("Risk Level: LOCK")

else:
    risk = 0

    if amount > 50000:
        risk += 1

    if location == "new":
        risk += 1

    hour = int(time.split(":")[0])
    if 0 <= hour <= 5:
        risk += 1

    if risk >= 2:
        print("Risk Level: HIGH")
    else:
        print("Risk Level: LOW")
