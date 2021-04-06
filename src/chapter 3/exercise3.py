# program determining grades depending on the user's score.
# it includes try, except
score = float(input("Enter score: "))
if score >= 0.9:
    print("A")
elif score >= 0.8:
    print("B")
elif score >= 0.7:
    print("C")
elif score >= 0.6:
    print("D")
else:
    print("F")
try:
    score = str(input("Enter score: "))
except Exception:
    print("Error, input a real number")
