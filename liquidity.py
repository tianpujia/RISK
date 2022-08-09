# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd
data = pd.read_csv("https://github.com/tianpujia/RISK/blob/main/TSLA%20financial%20data.csv")

def liquidity_ratio(df,date):
    ratio = round((df.loc[7, date] - df.loc[5, date])/df.loc[14, date], 2)
    if ratio > 1:
        level = 'good'
    else:
        level = 'bad'
    return(f'liquidity ratio of this date is {ratio}, the level is {level}')

print(liquidity_ratio(data, 'March 31,2022'))
print(liquidity_ratio(data, 'June 30,2022'))


import matplotlib.pyplot as plt

data = {'March 31,2022': 1.04, 'June 30,2022': 1.06}
courses = list(data.keys())
values = list(data.values())

fig = plt.figure(figsize=(10, 5))

# creating the bar plot
plt.bar(courses, values, color='maroon', width=0.4)

plt.xlabel("Date")
plt.ylabel("Liquidity Ratio")
plt.title("Liquidity Ratio of TSLA")


plt.savefig('C:/Users/jk sb/Desktop/Liquidity Ratio of TSLA.png')

plt.show()
