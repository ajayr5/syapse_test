import re

pattern = '^a...s$'
test_string = '12'
result = re.match(pattern, test_string)
print(result)
if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")