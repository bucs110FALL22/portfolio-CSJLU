article = "Teachers tend to promote debate in English or social science classes but do not associate it with mathematics. There should be equal emphasis, if not more, on debating mathematics.Debating becomes a critical teaching tool to make students realise that logic takes precedence in learning mathematical concepts. Students will be able to calculate mean and median using the formula, but many won’t be able to identify the actual difference between mean and median.They may be puzzled when asked to choose between mean and median to calculate the weight of students in a classroom or provide reason for using the cost price as the denominator while calculating profit and loss. They should not follow the teacher blindly and instead try to find out ‘what if’ the selling price was the denominator. Mathematics and science are essentially based on debate, research, and experiments."

dictionaries = {
  "English":"Language",
  "logic":"brain",
  "Students":"Teachers",
  "Teachers":"Students",
  "Mathematics":"Anxiety-inducing class",
  "denominator":"bottom part of a fraction",
  "blindly":"without looking",
  "release":"did not realize",
  "experiments":"human trials",
  "selling":"buying",
  "calculating":"guessing",
  "science:":"life"
}

for key, value in dictionaries.items():
  article = article.replace(key, value)

print(article)
