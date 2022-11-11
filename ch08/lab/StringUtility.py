class StringUtility:
  def __init__(self, test_strings):
    '''
    Takes string as parameter and stores as instance variable
    '''
    self.test_strings = test_strings
    
  def __str__(self):
    '''
    Converts the words to strings

    Returns the string unchanged
    '''
    return f"{self.test_strings}"

  def vowels(self):
    '''
    Checks if there are vowels in the string. If there are less than five vowels, prints the vowels. If there are five or more vowels, prints many.

    Returns the number of vowels or many
    '''
    self.vowels = "aeiou"
    self.numVowels = 0
    for ch in self.test_strings:
      if ch in self.vowels:
        self.numVowels += 1
    if self.numVowels < 5:
      return f"{self.numVowels}"

    if self.numVowels > 4:
      return "many"

  def bothEnds(self):
    '''
    Takes the first two characters and last two characters of the string and concatenates it. If the string length is less than or equal to two, returns the string as is.

    Returns new string or the string as is
    '''
    if len(self.test_strings) <= 2:
      return ""
    self.newString = ''
    self.newString = str(self.test_strings[0]) + str(self.test_strings[1]) + str(self.test_strings[-2]) + str(self.test_strings[-1])
    return self.newString

  def fixStart(self):
    '''
    Every repeating value of the first character of the string (aside from the first character of the string) gets replaced with a *. 

    Returns new string with * replacing all the subsequent characters of the first character.
    '''
    if len(self.test_strings) <= 1:
      return self.test_strings
    firstLetter = self.test_strings[0]
    newString = ""
    counter = 0
    for ch in range(len(self.test_strings)):
      if firstLetter == self.test_strings[ch] and counter != 0:
        newString += "*"
      else:
        counter = 1
        newString += str(self.test_strings[ch])
    return newString

  def asciiSum(self):
    '''
    Finds the ascii values of the strings and sums it together

    Returns the sum of the ascii value 
    '''
    sum = 0
    for ch in self.test_strings:
      sum += ord(ch)
    return sum

  def cipher(self):
    '''
    Encodes string by incrementing all letters by the length of the string

    Returns encoded string
    '''
    newString = ""
    for ch in self.test_strings:
      if ord(ch) == 32: #if letter or not
        newString += ch
        # continue
      else:
        shift = ord(ch) + len(self.test_strings)
        #if shift > 122 and 97 <= ord(ch) < 122:
        if 97 <= ord(ch) <= 122:
          while shift > 122:
            reset = 123 - shift
            shift = ord("a") + abs(reset)
          newString += chr(shift)
        elif 65 <= ord(ch) <= 90: 
          while shift > 90:
            reset = 91 - shift
            shift = ord("A") + abs(reset)
          newString += chr(shift)
        else:
          newString += chr(shift) 
    return newString
