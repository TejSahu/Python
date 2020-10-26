"""How would you write a regex that matches a sentence where the first
word is either Alice, Bob, or Carol; the second word is either eats, pets, or
throws; the third word is apples, cats, or baseballs; and the sentence ends
with a period? This regex should be case-insensitive. It must match the
following:"""

import re
search_string = re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s*(apples|cats|baseballs)(.$)', re.I)

try:
    print(search_string.search('Alice eats apples.').group())
except AttributeError:
    print("Sorry I cannot find a match in the regular expression")
"""How would you write a regex that matches the full name of someone
whose last name is Nakamoto? You can assume that the first name that
comes before it will always be one word that begins with a capital letter.
The regex must match the following:"""

search_part = re.compile(r'(^[A-Z]\w+)\s(Nokamoto)')
print(search_part.search("Su Nokamoto").group())
