import re

pattern = '(^)abc($)'
print(re.match(pattern, 'abcggggabc'))
