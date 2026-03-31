credit_score = int(input())
income = int(input())
emi = int(input())
employment = input()

status = ""
interest = "N/A"

if credit_score < 600:
    status = "Rejected"

elif credit_score < 750:
    status = "Review"

else:
    if income < 25000 or emi > (income * 0.5):
        status = "Rejected"
    elif employment not in ["Salaried", "Self-Employed"]:
        status = "Rejected"
    else:
        status = "Approved"
        if credit_score >= 800:
            interest = "7%"
        else:
            interest = "8%"

print("Status:", status)
print("Interest Rate:", interest)
