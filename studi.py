import requests as rq

from pandas import DataFrame as df
import plotly.graph_objects as go
import plotly.express as px
r = rq.get('https://coronavirus-tracker-api.herokuapp.com/v2/locations/')
print(r.status_code)
r=df(r.json()['locations'])
lon=[]
lat=[]
for x in r["coordinates"]:
    lon.append(x['longitude'])
    lat.append(x['latitude'])
deaths = []
death_size = []
confirmed = []
confirmed_size = []
recovered = []
recovered_size = []
for x in r['latest']:
        confirmed.append(x['confirmed'])
        confirmed_size.append((int (x['confirmed']) /30000))
        deaths.append(x['deaths'])
        death_size.append(abs(int(x['deaths'])))
        recovered.append(x['recovered'])
        recovered_size.append(int(float(x['recovered']) / 30000))
r['confirmed'] = df(confirmed)
r['confirmed_size'] = df(confirmed_size)
r['deaths'] = df(deaths)
r['death_size'] = df(death_size)
r['recovered'] = df(recovered)
r['recovered_size'] = df(recovered_size)
r['lat'] = df(lat)
r['lon'] = df(lon)
map_confirmed = go.Scattermapbox(
        customdata=r.loc[:,['confirmed',"deaths","recovered"]],
        name='Confirmed Cases',
        lon=r['lon'],
        lat=r['lat'],
        mode='markers',
        text=r['country'],
        hovertemplate=
        "<b>%{text}</b><br><br>" +
        "Confirmed: %{customdata[0]}<br>" +
        "<extra></extra>",
        fillcolor='mediumturquoise',
        showlegend=True,
        marker=go.scattermapbox.Marker(
            size=r['confirmed_size'],
            color='mediumturquoise',
            opacity=0.5
        ),
        opacity=0.5,

    )
map_deaths = go.Scattermapbox(
    customdata=r.loc[:, ['confirmed', "deaths", "recovered"]],
    name='Deaths',
    lon=r['lon'],
    lat=r['lat'],
    mode='markers',
    text=r['country'],
    hovertemplate=
    "<b>%{text}</b><br><br>" +
    "death: %{customdata[1]}<br>" +
    "<extra></extra>",
    fillcolor='yellow',
    showlegend=True,
    marker=go.scattermapbox.Marker(
        size=r['deaths'] / 5000,
        color='red',
        opacity=0.5
    ),
    opacity=0.5,
)

map_recovered = go.Scattermapbox(
    customdata=r.loc[:, ['confirmed', "deaths", "recovered"]],
    # deaths = r['deaths'],
    # recovered = r['recovered'],
    name='recovered',
    lon=r['lon'],
    lat=r['lat'],
    text=r['country'],
    hovertemplate=
    "<b>%{text}</b><br><br>" +
    "<extra></extra>",
    showlegend=True,
    marker=go.scattermapbox.Marker(
        size=(r['recovered']),
        color='green',
    ),
    opacity=0.5,
)
layout = go.Layout(
    height=800,
    mapbox_style="white-bg",
    autosize=True,
    mapbox_layers=[
        {
            "below": 'traces',
            "sourcetype": "raster",
            "source": [
                "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"

            ]
        }
    ],
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="#7f7f7f"
    ),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
)

data = [map_confirmed, map_recovered, map_deaths]

fig = go.Figure(data=data, layout=layout)
fig.show()