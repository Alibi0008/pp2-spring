from datetime import datetime

date1 = datetime(2022, 1, 1, 0, 0, 0)
date2 = datetime(2022, 1, 2, 0, 0, 0)

difference = (date2 - date1).total_seconds()

print(difference)