import datetime

d1str = input("First date is (write in form yyyy mm dd): ")
d2str = input("Second date is (write in form yyyy mm dd): ")


date1 = datetime.datetime.strptime(d1str, "%Y %m %d")
date2 = datetime.datetime.strptime(d2str, "%Y %m %d")

print(f"Difference in seconds: {int(abs((date2 - date1).total_seconds()))}")