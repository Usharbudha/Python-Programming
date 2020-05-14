import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.io as pio
pio.renderers.default="browser"
import plotly.graph_objects as go
import plotly.express as px

fig=px.scatter(x=[0,1,2,3,4],y=[0,1,4,9,16])
pio.show(fig)

df=px.data.tips()
fig=px.bar(df,x="sex",y="total_bill",color="time")
fig.show()

fig=px.bar(df,x="sex",y="total_bill",color='smoker',barmode='group',height=400)
fig.show()

fig=px.bar(df,x="sex",y="total_bill",color='smoker',barmode='group',facet_row="time",facet_col="day",category_orders={"day":["Thurs","Fri","Sat","Sun"],"time":["Lunch","Dinner"]})
fig.show()

animals=['giraffes','deer','monkeys']
fig=go.Figure(data=[go.Bar(name='SF Zoo',x=animals,y=[20,14,23],hovertext=['20 giraffes','14 deer','23 monkeys']),go.Bar(name='LA Zoo',x=animals,y=[12,18,29])])
fig.update_layout(barmode='group')
fig.show()


df=px.data.gapminder().query("continent=='Europe' and year == 2007 and pop >2.e06")
fig=px.bar(df,y='pop',x='country',text='pop')
fig.update_traces(texttemplate='%{text:.2s}',textposition='outside')
fig.update_layout(uniformtext_minsize=8,uniformtext_mode='hide')
fig.show()


df=px.data.gapminder().query("continent=='Europe'").query("year==2007")
fig=px.pie(df,values='pop',names='country',title='Population of American Continent',hover_data=['lifeExp'],labels={'lifeExp':'life expantancy'})
fig.update_traces(textposition='inside',textinfo='percent+label')
fig.show()


labels=['Oxygen','Hydrogen','Carbon_Dioxide','Nitrogen']
values=[4500,2500,1053,500]

fig=go.Figure(data=[go.Pie(labels=labels,values=values)])
fig.show()


fig=go.Figure(data=[go.Pie(labels=labels,values=values,pull=[0,0,0.02,0])])
fig.show()


fig=go.Figure(data=[go.Pie(labels=labels,values=values,hole=.3)])
fig.show()

colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen']

fig = go.Figure(data=[go.Pie(labels=['Oxygen','Hydrogen','Carbon_Dioxide','Nitrogen'],
                             values=[4500,2500,1053,500])])
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
                  marker=dict(colors=colors, line=dict(color='#000000', width=2)))
fig.show()


df = px.data.gapminder().query("year == 2007")
fig = px.sunburst(df, path=['continent', 'country'], values='pop',
                  color='lifeExp', hover_data=['iso_alpha'],
                  color_continuous_scale='RdBu',
                  color_continuous_midpoint=np.average(df['lifeExp'], weights=df['pop']))
fig.show()

df = px.data.gapminder()

fig = px.scatter(df.query("year==2007"), x="gdpPercap", y="lifeExp",
        size="pop", color="continent",
                 hover_name="country", log_x=True, size_max=60)
fig.show()

df = px.data.gapminder()
fig = px.area(df, x="year", y="pop", color="continent",
     line_group="country")
fig.show()

df = px.data.tips()
fig = px.bar(df, x="total_bill", y="sex", color='day', orientation='h',
             hover_data=["tip", "size"],
             height=400,
             title='Restaurant bills')
fig.show()


fig = go.Figure(data=[go.Table(header=dict(values=['A Scores', 'B Scores']),
                 cells=dict(values=[[100, 90, 80, 90], [95, 85, 75, 95]]))
                     ])
fig.show()

df = px.data.gapminder().query("year == 2007")
df["world"] = "world" # in order to have a single root node
fig = px.treemap(df, path=['world', 'continent', 'country'], values='pop',
                  color='lifeExp', hover_data=['iso_alpha'],
                  color_continuous_scale='RdBu',
                  color_continuous_midpoint=np.average(df['lifeExp'], weights=df['pop']))
fig.show()













# from plotly.offline import plot
import plotly.graph_objects as go
import plotly.io as pio
pio.renderers.default = "browser"

fig = go.Figure(
    data=[go.Bar(y=[2, 1, 3])],
    layout_title_text="A Figure"
)
# fig.show()
# plot(fig)
pio.show(fig)


fig = {
    "data": [{"type": "bar",
              "x": [1, 2, 3],
              "y": [1, 3, 2]}],
    "layout": {"title": {"text": "A Bar Chart"}}
}

pio.show(fig)


fig = {
    "data": [{"type": "scatter",
              "x": [1, 2, 3],
              "y": [1, 3, 2]}],
    "layout": {"title": {"text": "A Bar Chart"}}
}

pio.show(fig)

fig = go.Figure({
    "data": [{"type": "bar",
              "x": [1, 2, 3],
              "y": [1, 3, 2]}],
    "layout": {"title": {"text": "A Bar Chart"}}
})
fig.show()

fig = go.Figure(
    data=[go.Bar(x=[1, 2, 3], y=[1, 3, 2])],
    layout=dict(title=dict(text="A Bar Chart"))
)
fig.show()

import plotly.express as px
px.data.iris().head()

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length")
fig.show()

fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")
fig.show()

fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", marginal_y="rug", marginal_x="histogram")
fig.show()


fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", marginal_y="violin",
           marginal_x="box", trendline="ols")
fig.show()


fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")
fig.add_trace(
    go.Scatter(
        x=[2, 4],
        y=[4, 8],
        mode="lines+markers",
        line=go.scatter.Line(color="gray"),
        showlegend=False)
)
fig.show()


from plotly.subplots import make_subplots
fig = make_subplots(rows=1, cols=2)
fig.add_trace(go.Scatter(y=[4, 2, 1], mode="lines"), row=1, col=1)
fig.add_trace(go.Bar(y=[2, 1, 3]), row=1, col=2)
fig.show()



fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", facet_col="species")
reference_line = go.Scatter(x=[2, 4],
                            y=[4, 8],
                            mode="lines",
                            line=go.scatter.Line(color="gray"),
                            showlegend=False)
fig.add_trace(reference_line, row=1, col=1)
fig.add_trace(reference_line, row=1, col=2)
fig.add_trace(reference_line, row=1, col=3)
fig.show()


df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")

fig.for_each_trace(
    lambda trace: trace.update(name=trace.name.replace("=", ": ")),
)

fig.show()


(px.scatter(df, x="sepal_width", y="sepal_length", color="species",
            facet_col="species", trendline="ols", title="Iris Dataset")
 .update_layout(title_font_size=24)
 .update_xaxes(showgrid=False)
 .update_traces(
     line=dict(dash="dot", width=4),
     selector=dict(type="scatter", mode="lines"))
).show()

fig = go.Figure(data=go.Bar(x=[1, 2, 3], y=[1, 3, 2]))
fig.data[0].marker.line.width = 4
fig.data[0].marker.line.color = "black"
fig.show()

df = px.data.tips()
fig = px.parallel_categories(df, color="size", color_continuous_scale=px.colors.sequential.Inferno)
fig.show()

df = px.data.gapminder()
fig = px.scatter(df, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
           size="pop", color="continent", hover_name="country", facet_col="continent",
           log_x=True, size_max=45, range_x=[100,100000], range_y=[25,90])
fig.show()

fig = px.scatter_geo(df, locations="iso_alpha", color="continent", hover_name="country", size="pop",
               animation_frame="year", projection="natural earth")
fig.show()

fig = px.choropleth(df, locations="iso_alpha", color="lifeExp", hover_name="country", animation_frame="year", range_color=[20,80])
fig.show()

df = px.data.wind()
fig = px.line_polar(df, r="frequency", theta="direction", color="strength", line_close=True,
            color_discrete_sequence=px.colors.sequential.Plasma_r)
fig.show()



fig = px.bar_polar(df, r="frequency", theta="direction", color="strength", template="plotly_dark",
            color_discrete_sequence= px.colors.sequential.Plasma_r)
fig.show()





import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[1, 2, 3, 4, 5],
))

fig.add_trace(go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[5, 4, 3, 2, 1],
))

fig.show()


fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[1, 2, 3, 4, 5],
))

fig.update_layout(showlegend=True)

fig.show()


fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[1, 2, 3, 4, 5],
))

fig.add_trace(go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[5, 4, 3, 2, 1],
))

fig.update_layout(showlegend=False)

fig.show()


fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[1, 2, 3, 4, 5],
    showlegend=False
))


fig.add_trace(go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[5, 4, 3, 2, 1],
))

fig.update_layout(showlegend=True)

fig.show()


fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[1, 2, 3, 4, 5],
    name="Positive"
))

fig.add_trace(go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[5, 4, 3, 2, 1],
    name="Negative"
))

fig.show()


fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[1, 2, 3, 4, 5],
    name="Increasing"
))

fig.add_trace(go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[5, 4, 3, 2, 1],
    name="Decreasing"
))

fig.update_layout(legend_title='<b> Trend </b>')
fig.show()

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[1, 2, 3, 4, 5],
))

fig.add_trace(go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[5, 4, 3, 2, 1],
))

fig.update_layout(legend_orientation="h")

fig.show()


fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[1, 2, 3, 4, 5],
))

fig.add_trace(go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[5, 4, 3, 2, 1],
))

fig.update_layout(legend=dict(x=-.1, y=1.2))

fig.show()


fig.add_trace(go.Scatter(
    x=[1, 2, 3],
    y=[2, 1, 3],
    legendgroup="group",  # this can be any string, not just "group"
    name="first legend group",
    mode="markers",
    marker=dict(color="Crimson", size=10)
))

fig.add_trace(go.Scatter(
    x=[1, 2, 3],
    y=[2, 2, 2],
    legendgroup="group",
    name="first legend group - average",
    mode="lines",
    line=dict(color="Crimson")
))

fig.add_trace(go.Scatter(
    x=[1, 2, 3],
    y=[4, 9, 2],
    legendgroup="group2",
    name="second legend group",
    mode="markers",
    marker=dict(color="MediumPurple", size=10)
))

fig.add_trace(go.Scatter(
    x=[1, 2, 3],
    y=[5, 5, 5],
    legendgroup="group2",
    name="second legend group - average",
    mode="lines",
    line=dict(color="MediumPurple")
))

fig.show()





























 