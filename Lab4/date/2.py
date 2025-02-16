from datetime import *

d1 = date.today() - timedelta(1)
d2 = date.today()
d3 = date.today() + timedelta(1)

print(f"Today is {d2}, yesterday was {d1} and tomorrow is {d3}")