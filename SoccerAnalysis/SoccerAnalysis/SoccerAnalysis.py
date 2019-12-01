from matplotlib import pyplot as plt
import pandas as pd

year = pd.read_csv("birthyear.csv")

x_years = list(range(1967, 2000))
y_values = list(year.overall_score)

plt.plot(x_years, y_values, color="GoldenRod")
plt.title("Overall Score Vs Birth Year")
plt.xlabel("Birth Year")
plt.ylabel("Overall Score")
plt.show()
