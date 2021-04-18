#program to compute grades using a computegrade function
def computegrade(score):
    if score > 1.0:
        return 'Bad score'
    elif score >= 0.9:
        return 'A'
    elif score >= 0.8:
        return 'B'
    elif score >= 0.7:
        return 'C'
    elif score >= 0.6:
        return 'D'
    elif score < 0.6:
        return 'F'


try:
    score = input('Enter score: ')
    score = float(score)
    grade = computegrade(score)
    print(grade)

except Exception:
    print('Bad score')
