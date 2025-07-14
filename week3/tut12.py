import numpy as np

week_spendings = np.array([50, 120, 30, 40, 200, 90, 300])

index = 1
days = {1:'mon', 2:'tues', 3:'wed', 4:'thurs', 5:'fri', 6:'sat', 7:'sun'}

big_spending = week_spendings[0]
for i in range(len(week_spendings)):
	if week_spendings[i] > big_spending:
		big_spending = week_spendings[i]
		index = i + 1
		
print(big_spending, days[index])