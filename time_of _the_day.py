# we want to extract the time of the day and the day of the week

import re
# This is the string that we will work on it

test_date = "12:34pm today is Sunday"


pattern = re.compile(r"\d{2}:\d{2}(am|pm)")
matches = pattern.search(test_date)
print(matches)
