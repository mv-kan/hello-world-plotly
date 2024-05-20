import plotly.express as px
import pandas as pd
# Load the CSV file into a DataFrame
df = pd.read_csv('./titanic/train.csv')
# df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
df["Survived"] = df["Survived"].astype(str)
print(df.head())
mask = df["Sex"] == "female"
print(len(df))
print(len(df[mask]))
fig = px.scatter(df[mask], x="Pclass", y="Age", color="Survived", hover_data=["PassengerId", "Name", "Pclass", "Sex"])
fig.show()