import re

string_test = 'asdadasfkmkkamomkoncnionenionibinionookasdac' #<- facebook
def find_substring(string):
    x = re.search("f.*a.*c.*e.*b.*o.*o.*k", string)
    if x:
        return 'Match found'
    else:
        return 'No match found'
print(find_substring(string_test)) 
print(find_substring('faceboo'))