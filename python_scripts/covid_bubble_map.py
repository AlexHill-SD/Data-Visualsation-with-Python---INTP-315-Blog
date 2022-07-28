import pandas as pandas
import plotly.graph_objects as graphObject
import plotly.express as express

# print_full code taken from: https://stackoverflow.com/a/51593236
def print_full(x):
    pandas.set_option('display.max_rows', None)
    pandas.set_option('display.max_columns', None)
    pandas.set_option('display.width', 2000)
    pandas.set_option('display.float_format', '{:20,.2f}'.format)
    pandas.set_option('display.max_colwidth', None)
    print(x)
    pandas.reset_option('display.max_rows')
    pandas.reset_option('display.max_columns')
    pandas.reset_option('display.width')
    pandas.reset_option('display.float_format')
    pandas.reset_option('display.max_colwidth')

# code references: https://medium.com/analytics-vidhya/plotting-the-pandemic-with-python-and-plotly-e8011a141e3c

# data from: https://covid19.who.int/WHO-COVID-19-global-data.csv
sourceData = pandas.read_csv("..//WHO-COVID-19-global-data.csv")

# print_full(sourceData.head())
# print_full(sourceData.info())

sourceData['Date_reported'] = pandas.to_datetime(sourceData['Date_reported'], dayfirst=True)

sourceData.sort_values(by=['Date_reported', 'WHO_region'], ascending=True, inplace=True)

sourceData.reindex()

# print_full(sourceData.info())

continentalIndex = pandas.read_csv("../continents.csv")

sourceData = pandas.merge(sourceData,
						 continentalIndex[['Continent_Name', 'Two_Letter_Country_Code']].drop_duplicates('Two_Letter_Country_Code'),
						 how='left',
						 left_on='Country_code',
						 right_on='Two_Letter_Country_Code')

colour_map = {"Asia": "royalblue",
	           "Europe": "crimson",
	           "Africa": "lightseagreen",
	           "Oceania": "orange",
	           "North America": "gold",
	           "South America": 'mediumslateblue'
	           }

# print_full(sourceData.info())

# code to aggregate from : https://stackoverflow.com/questions/40553002/pandas-group-by-two-columns-to-get-sum-of-another-column
continental_data = sourceData.groupby(by=['Date_reported', 'Continent_Name']).agg({'New_cases': "sum"}).reset_index()

unique_dates = continental_data['Date_reported'][continental_data['Date_reported'] > pandas.to_datetime('03/01/2020')].sort_values(ascending=True).unique()
datesAsStrings = [pandas.to_datetime(str(x)).strftime('%d %b %y') for x in unique_dates]

# add a string column that has the date data from the original csv (basically undoing what we did when converting to datetime earlier)
# will be used to aggregate data for frames
continental_data['date'] = [pandas.to_datetime(str(x)).strftime('%d %b %y') for x in continental_data['Date_reported']]

# lat/long data from: https://www.travelmath.com/continent/South+America
continental_data['latitude'] = 0
continental_data['longitude'] = 0

continental_data.loc[continental_data['Continent_Name'] == 'Africa', 'latitude'] = 7.18805555556
continental_data.loc[continental_data['Continent_Name'] == 'Africa', 'longitude'] = 21.0936111111

continental_data.loc[continental_data['Continent_Name'] == 'Europe', 'latitude'] = 48.6908333333
continental_data.loc[continental_data['Continent_Name'] == 'Europe', 'longitude'] = 9.14055555556

continental_data.loc[continental_data['Continent_Name'] == 'Asia', 'latitude'] = 29.8405555556
continental_data.loc[continental_data['Continent_Name'] == 'Asia', 'longitude'] = 89.2966666667

continental_data.loc[continental_data['Continent_Name'] == 'Oceania', 'latitude'] = -18.3127777778
continental_data.loc[continental_data['Continent_Name'] == 'Oceania', 'longitude'] = 138.515555556

continental_data.loc[continental_data['Continent_Name'] == 'North America', 'latitude'] = 46.0730555556
continental_data.loc[continental_data['Continent_Name'] == 'North America', 'longitude'] = -100.546666667

continental_data.loc[continental_data['Continent_Name'] == 'South America', 'latitude'] = -14.6047222222
continental_data.loc[continental_data['Continent_Name'] == 'South America', 'longitude'] = -57.6561111111

# print_full(continental_data)

# Declare the basic outline of a figure aka a plotted graph
# data: this is what data will be displayed at a high level
# layout: layout of the plotted graph
# frames: each frame is one step in the animation, in this case each frame is a day
figure = {
	'data': [],
	'layout': {},
	'frames': [],
}

# pick the last day in the data as the splash screen display of the graph
initial_display_day = datesAsStrings[-1]
# extract the data from the data source for the initial day
chart_data = continental_data[continental_data['date'] == initial_display_day]

# extract unique continents, use the information from the table to dictate where/how/what will be plotted
for i, cont in enumerate(chart_data['Continent_Name'].unique()):
    colour = colour_map[cont]
    df_sub = chart_data[chart_data['Continent_Name'] == cont].reset_index()
    data_dict = dict(
    type='scattergeo',
    lat=df_sub['latitude'],
    lon=df_sub['longitude'],
    marker=dict(                                        # dictionary defining parameters of each marker on the figure
        size=df_sub['New_cases'] / 50,               # the size of each marker
        color=colour,                                   # the colour of the marker
        line_color='#ffffff',                           # the outline colour of the marker
        line_width=0.5,                                 # the width of the marker outline
        sizemode='area'),                               # how the size parameter should be translated, area/diameter
    name='{}'.format(cont),                             # series name (appears on the legend)
    text=[                                              # define what appears on the label for each country in the series
        '{}<BR>New Cases: {}'.format(                
            df_sub['Continent_Name'][x],
            df_sub['New_cases'][x]) for x in range(
                len(df_sub))])
    figure['data'].append(data_dict)

frames = []
steps = []

for day in datesAsStrings:
    chart_data = continental_data[continental_data['date'] == day]
    frame = dict(data=[], name=str(day))
    for i, cont in enumerate(chart_data['Continent_Name'].unique()):
        colour = colour_map[cont]
        df_sub = chart_data[chart_data['Continent_Name'] == cont].reset_index()
        data_dict = dict(
            type='scattergeo',
            lat=df_sub['latitude'],
            lon=df_sub['longitude'],
            marker=dict(
                size=df_sub['New_cases'] / 50,
                color=colour,
                line_color='#ffffff',
                line_width=0.5,
                sizemode='area'),
            name='{}'.format(cont),
            text=[
                '{}<BR>New Cases: {}'.format(
                    df_sub['Continent_Name'][x],
                    df_sub['New_cases'][x]) for x in range(
                    len(df_sub))])
        frame['data'].append(data_dict)
    figure['frames'].append(frame)
  
    step = dict(                                    
        method="animate",                          # how the transition should take place - should the chart be redrawn?
        args=[
            [day],                                 # should match the frame name                                                  
            dict(frame=dict(duration=100,          # speed and style of the transitions
                            redraw=True),
                mode="immediate",
                transition=dict(duration=100,
                                easing="quad-in"))
        ],
        label=day,                                  # name of the step

    )
    steps.append(step)

# changes the sliders at the bottom of the plotted graph
sliders = [dict(
    x=0.1,
    y=0,
    active=len(datesAsStrings) - 1,
    currentvalue=dict(prefix="",
                      visible=True,
                      ),
    transition=dict(duration=300),
    pad=dict(t=2),
    len = 0.9,
    steps=steps                                     # the list of steps is included here
)]

# changes title options
title_font_family = 'Arial'
title_font_size = 14

# assigns layout options to the original figure key
figure['layout'] = dict(
    titlefont=dict(                                  # parameters controlling title font
        size=title_font_size,
        family=title_font_family),
    title_text='<b> New COVID-19 Cases </b> <BR>', # Chart Title
    showlegend=True,                                 # Include a legend
    geo=dict(                                        # parameter controlling the look of the map itself
        scope='world',
        landcolor='rgb(217, 217, 217)',
        coastlinecolor='#ffffff',
        countrywidth=0.5,
        countrycolor='#ffffff',
    ),
    # https://plotly.com/python/animations/ & https://stackoverflow.com/questions/68894919/how-to-set-the-values-of-args-and-args2-in-plotlys-buttons-in-updatemenus
    updatemenus=[                                     # Where a 'play' button is added to enable the user to start the animation
        dict(
            type='buttons',
            direction='left',
            x=0.1,
            y=0.075,
            pad=dict(r=10,
                     t=70),
            buttons=list(
                [
                    dict(
                        args=[
                            None,
                            dict(
                                frame=dict(
                                    duration=200,
                                    redraw=True),
                                mode="immediate",
                                transition=dict(
                                    duration=200,
                                    easing="quad-in"))],
                        label="Play",
                        method="animate"),
                    dict(args=[
                        # Notice the use of [None] vs None. One is pause, one is play. Thanks Plotly & Python ...
                            [None],
                            dict(
                                frame=dict(
                                    duration=0,
                                    redraw=True),
                                mode="immediate",
                                transition=dict(
                                    duration=0,
                                    easing="quad-in"))],
                        label="Pause",
                        method="animate")
                ]
                )
            )
        ],
    sliders=sliders)                                   # Add the sliders dictionary


#print(figure['data'])
#print(figure['frames'])

# generate the plotted graph
new_covid_cases_bubble_map = graphObject.Figure(figure)

# display the plotted graph
new_covid_cases_bubble_map.show()

# save the plotted graph as HTML code for embedding on websites, without need to host it, and include plotly.js via CDN
new_covid_cases_bubble_map.write_html("./interactive_bubble_map.html", include_plotlyjs="cdn")