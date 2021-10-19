def getWrongAnswers(C: str) -> str:
  # Write your code here
  new_string = ''
  for i in C:
    if i == 'A':
        new_string+='B'
    else:
        new_string += 'A' 
      
  return new_string
test = 'AAAAB'
# BBBBA
getWrongAnswers(test)
print(getWrongAnswers(test))