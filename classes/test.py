from pole_list import pole_list
from pole import pole

poles= pole_list()
poles.add_to_head(pole(battary= 55, temperature=20))
poles.add_to_head(pole(battary=20, temperature=37))
print(poles.tail.behind_pole.temperature)