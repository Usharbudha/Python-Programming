
#conda install -c anaconda plotly

import plotly.io as pio
pio.renderers.default="browser"
import plotly.graph_objects as go
import plotly.express as px

fig=px.scatter(x=[0,1,2,3,4],y=[0,1,4,9,16])
pio.show(fig)

df=px.data.gapminder().query("country=='Canada'")

fig=px.line(df,x="year",y="lifeExp",title="Life expentancy in Canada")
pio.show(fig)


new_df=df[-df["country"].isin(["Afghanistan","Bangladesh"])]

px.data.gapminder().query("country=='Canada'")
fig=px.line(df,x="year",y="lifeExp",title="life expantancy in Canada")
pio.show(fig)

df=px.data.gapminder().query("continent=='Oceania'")
fig=px.line(df,x="year",y="lifeExp",title="Life expentancy in Canada",color="country")
pio.show(fig)

df=px.data.gapminder().query("continent=='Europe'")
fig=px.line(df,x="year",y="lifeExp",color="continent",line_group="country",hover_name="country")
fig.show()

df=px.data.gapminder()
fig=px.line(df,x="year",y="lifeExp",color="continent",line_group="country",hover_name="country")
fig.show()

data_can=px.data.gapminder().query("country=='Canada'")
fig=px.bar(data_can,x="year",y="pop",hover_data=["lifeExp","gdpPercap"],color="lifeExp",labels={"pop":"population of Canada"},height=400)
fig.show()

