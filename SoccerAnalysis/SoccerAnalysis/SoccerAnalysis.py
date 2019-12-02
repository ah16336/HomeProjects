from matplotlib import pyplot as plt
import pandas as pd

year = pd.read_csv("birthyear.csv")
random = pd.read_csv("random_teams.csv")

x_years = list(range(1967, 2000))
y_values = list(year.overall_score)

plt.plot(x_years, y_values, color="LightCoral")
plt.title("Overall Score Vs Birth Year")
plt.xlabel("Birth Year")
plt.ylabel("Overall Score")
plt.show()


home_goal = list(random.Home_goal_diff)
away_goal = list(random.Away_goal_diff)
x_range = list(range(6))

x_values1 = [2*element*2 + 1 for element in x_range]
x_values2 = [2*element*2 + 2 for element in x_range]

plt.bar(x_values1, home_goal, color='Crimson', label='Home')
plt.bar(x_values2, away_goal, color='Gold', label='Away')
plt.xlabel("Team")
plt.ylabel("Home/Away Goal Difference")
plt.legend()
plt.show()