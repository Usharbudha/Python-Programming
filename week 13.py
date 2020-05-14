import pandas as pd
import sqlite3
connection = sqlite3.connect("company.db")

cursor = connection.cursor()


sql_command = """
CREATE TABLE employee ( 
staff_number INTEGER PRIMARY KEY, 
fname VARCHAR(20), 
lname VARCHAR(30), 
gender CHAR(1), 
joining DATE,
birth_date DATE);"""

cursor.execute(sql_command)

sql_command = """INSERT INTO employee (staff_number, fname, lname, gender, birth_date)
    VALUES (NULL, "William", "Shakespeare", "m", "1961-10-25");"""
cursor.execute(sql_command)


sql_command = """INSERT INTO employee (staff_number, fname, lname, gender, birth_date)
    VALUES (NULL, "Frank", "Schiller", "m", "1955-08-17");"""
cursor.execute(sql_command)
connection.commit()
connection.close()

connection = sqlite3.connect("company.db")
sql_command = """SELECT * from employee"""
cursor = connection.cursor()

cursor.execute(sql_command)
result = cursor.fetchall() 


df = pd.read_sql_query("SELECT * from employee", connection)

connection.commit()
connection.close()


connection = sqlite3.connect("wine.db")
df = pd.read_csv('winequality.csv',sep=';')
df.to_sql("wine", connection, if_exists="replace")

connection.commit()

connection.close()

connection = sqlite3.connect("wine.db")
newdf = pd.read_sql_query("select * from wine;", connection)
connection.close()


import plotly.graph_objects as go
import plotly.io as pio
from plotly.offline import plot
import plotly.express as px

from plotly.subplots import make_subplots
fig = make_subplots(rows=1, cols=2)
fig.add_trace(go.Scatter(y=[4, 2, 1], mode="lines"), row=1, col=1)
fig.add_trace(go.Bar(y=[2, 1, 3]), row=1, col=2)
plot(fig)

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", facet_col="species")
reference_line = go.Scatter(x=[2, 4],
                            y=[4, 8],
                            mode="lines",
                            line=go.scatter.Line(color="gray"),
                            showlegend=False)
fig.add_trace(reference_line, row=1, col=1)
fig.add_trace(reference_line, row=1, col=2)
fig.add_trace(reference_line, row=1, col=3)
plot(fig)

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")

fig.for_each_trace(
    lambda trace: trace.update(name=trace.name.replace("=", ": ")),
)

plot(fig)


fig = px.bar(df, x="sex", y="total_bill", color="smoker", barmode="group",
             facet_row="time", facet_col="day",
             category_orders={"day": ["Thur", "Fri", "Sat", "Sun"],
                              "time": ["Lunch", "Dinner"]})
plot(fig)


df = px.data.gapminder()
fig = px.scatter(df, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
           size="pop", color="continent", hover_name="country", facet_col="continent",
           log_x=True, size_max=45, range_x=[100,100000], range_y=[25,90])
plot(fig)



























