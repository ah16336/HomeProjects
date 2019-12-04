from matplotlib import pyplot as plt
import pandas as pd

year = pd.read_csv("birthyear.csv")

x_years = list(range(1967, 2000))
y_values = list(year.overall_score)

plt.figure(figsize = (20, 20))
ax1=plt.subplot(2, 1, 1)
plt.plot(x_years, y_values, color="DarkCyan")
ax1.set_title("Overall Score Vs Birth Year", fontname='Segoe UI', fontsize=18)
ax1.set_xlabel("Birth Year", fontname='Segoe UI', fontsize=14)
ax1.set_ylabel("Overall Score", fontname='Segoe UI', fontsize=14)

#plt.savefig('birthyear.png')

random = pd.read_csv("random_teams.csv")

home_goal = list(random.Home_goal_diff)
away_goal = list(random.Away_goal_diff)
x_range = list(range(6))

x_values1 = [2*element*2 + 1 for element in x_range]
x_values2 = [2*element*2 + 2 for element in x_range]

ax = plt.subplot(2, 1, 2)
plt.bar(x_values1, home_goal, color='LightSeaGreen', label='Home')
plt.bar(x_values2, away_goal, color='RoyalBlue', label='Away')
ax.set_xticks([1.5, 5.5, 9.5, 13.5, 17.5, 21.5])
ax.set_xticklabels(['AC Arles-Avignon', 'FC Arouca', 'Termalica Bruk-Bet Nieciecza', 'Tondela', 'Carpi', 'Royal Excel Mouscron'], fontname='Segoe UI')
ax.set_xlabel("Team", fontname='Segoe UI', fontsize=14)
ax.set_ylabel("Home/Away Goal Difference", fontname='Segoe UI', fontsize=14)
ax.set_title("Home vs Away Goal Difference for 6 Teams", fontname='Segoe UI', fontsize=18)
plt.legend()

#plt.savefig('HomeVsAway.png')

plt.subplots_adjust(hspace=0.25)
plt.show()  

plt.close('all')
count = pd.read_csv("birthday_count.csv")

y_count = list(count.Count)

plt.figure(figsize = (20, 20))
ax2 = plt.subplot()
plt.bar(x_years, y_count, color='RoyalBlue')
ax2.set_xlabel("Birth Year", fontname='Segoe UI', fontsize=14)
ax2.set_ylabel("Count of Players", fontname='Segoe UI', fontsize=14)
ax2.set_title("Count of footballers born between 1967 and 1997", fontname='Segoe UI', fontsize=18)
plt.show()