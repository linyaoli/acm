```ruby
'.' : matches any character except newline.
'^' : matches the start of a string.
'$' : matches the end of a string.
'*' : matches 0 or more repetitions of the preceding RE. i.e. 'ab*' matches a followed with any number of b.
'+' : similar to '*', but 'ab+' will not match 'a'.
'?' : match 0 or 1 of preceding RE.
{m} : matches exactly m copies of preceding RE.
{m, n}: matches number of copies  from m to n.
'\' : escape special chars.
[] : indicate a set of chars.i.e. [amk] will match 'a', 'm' or 'k'.
others : https://docs.python.org/2/library/re.html

Performing matching in python:
import re

match = re.search('dog', 'dog cat pig')
match.start()
>> 0
match.end()
>> 3
#others:
#re.match()
#re.findall()

contactInfo = "Doe, John: 555-1212"
match = re.search('(\w+), (\w+): (\S+)', contactInfo)
match.group(1)
>> 'Doe'
match.group(2)
>> 'John'
match.group(3)
>> '555-1212'
```
