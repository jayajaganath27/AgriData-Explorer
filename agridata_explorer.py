import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine
import urllib.parse


username = 'root'
password = 'Dhruv@2212'
host = 'localhost'
database = 'agriculture_db'

encoded_password = urllib.parse.quote_plus(password)
engine = create_engine(f"mysql+pymysql://{username}:{encoded_password}@{host}/{database}")
query = "SELECT * FROM crop_production"
agri = pd.read_sql(query, con=engine)

print("✅ Data loaded successfully from MySQL!")
print("Shape of data:", agri.shape)

#Top 7 RICE PRODUCTION State Data(Bar_plot)
top_rice = (agri.groupby("state_name")["rice_production_(1000_tons)"].sum().nlargest(7).reset_index())           
fig = px.bar(top_rice, x="state_name", y="rice_production_(1000_tons)", title="Top 7 Rice Producing States in India", color="state_name", text_auto=True)
fig.update_xaxes(title="State", tickangle=45)
fig.update_yaxes(title="rice_production_(1000_tons)")
fig.update_layout(showlegend=False)
fig.show()

# Top 5 Wheat Producing States Data(Bar_chart)and its percentage(%)(Pie_chart)
top_wheat = (agri.groupby("state_name")["wheat_production_(1000_tons)"].sum().nlargest(5).reset_index())
# Bar chart for top 5 states
fig_bar = px.bar(top_wheat, x="state_name", y="wheat_production_(1000_tons)", title="Top 5 Wheat Producing States", color="state_name", text_auto=True)
fig_bar.update_xaxes(title="State", tickangle=45)
fig_bar.update_yaxes(title="Wheat Production (1000 tons)")
fig_bar.update_layout(showlegend=False)
fig_bar.show()
#  Pie chart showing percentage contribution 
fig_pie = px.pie(top_wheat, names="state_name", values="wheat_production_(1000_tons)", title="Wheat Production Share (%) of Top 5 States", hole=0.3)
fig_pie.update_traces(textinfo="percent+label")
fig_pie.show()

# Oil seed production by top 5 states
top_oilseeds = (agri.groupby("state_name")["oilseeds_production_(1000_tons)"].sum().nlargest(5).reset_index())
# Bar chart for top 5 states
fig_bar = px.bar(top_oilseeds, x="state_name", y="oilseeds_production_(1000_tons)",color="state_name",text_auto=True,title="Top 5 Oilseeds Producing States")
fig_bar.update_xaxes(title="State", tickangle=45)
fig_bar.update_yaxes(title="Oilseeds Production (1000 tons)")
fig_bar.update_layout(showlegend=False)
fig_bar.show()
#  Pie chart showing percentage contribution 
fig_pie = px.pie(top_oilseeds, names="state_name", values="oilseeds_production_(1000_tons)", title="Oilseeds Production Share (%) of Top 5 States")
fig_pie.update_traces(textinfo="percent+label")
fig_pie.show()

#Top 7 SUNFLOWER PRODUCTION  State
top_sunflower = (agri.groupby("state_name")["sunflower_production_(1000_tons)"].sum().nlargest(7).reset_index())
# Bar chart-
fig_bar = px.bar( top_sunflower, x="state_name", y="sunflower_production_(1000_tons)", color="state_name", text_auto=True,title="🌻 Top 7 Sunflower Producing States")
fig_bar.update_xaxes(title="State", tickangle=45)
fig_bar.update_yaxes(title="Sunflower Production (1000 tons)")
fig_bar.update_layout(showlegend=False)
fig_bar.show()
#  Pie chart for percentage share 
fig_pie = px.pie(top_sunflower,names="state_name",values="sunflower_production_(1000_tons)",title="Sunflower Production Share (%) of Top 7 States",hole=0.3)
fig_pie.update_traces(textinfo="percent+label")
fig_pie.show()

#India's SUGARCANE PRODUCTION From Last 50 Years(Line_plot)
sugarcane_yearly = (agri.groupby("year")["sugarcane_production_(1000_tons)"].sum().reset_index())
sugarcane_yearly = sugarcane_yearly.sort_values("year").tail(50)
# Line Plot 
fig = px.line(sugarcane_yearly,x="year",y="sugarcane_production_(1000_tons)",title="India's Sugarcane Production in Last 50 Years",markers=True)
fig.update_xaxes(title="Year")
fig.update_yaxes(title="Sugarcane Production (1000 tons)")
fig.update_layout(title_font=dict(size=20, family='Verdana', color='green'))
fig.show()