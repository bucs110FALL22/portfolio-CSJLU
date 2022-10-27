def percentage_to_letter(score=0):
  if (score >= 90):
    return "A"
  if (score >= 80 and score < 90):
    return "B"
  if (score >= 70 and score < 80):
    return "C"
  if (score >= 60 and score < 70):
    return "D"
  if (score < 60):
    return "F"

score = float(input("What is your grade? "))
result = percentage_to_letter(score)

def is_passing(result):
  return result in "ABC"

end_result = is_passing(result)
print(end_result)





