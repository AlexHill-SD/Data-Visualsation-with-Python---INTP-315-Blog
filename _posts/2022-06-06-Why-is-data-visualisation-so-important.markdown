---
layout: post
title:  "Why is data visualisation so important?"
date:   2022-06-06 13:44:55 -0600
image:  blog_title_imgs/circuit_board_colour.jpg
tags:   [python, data visualisation, matplotlib, plotly]
description: "Being able to easily convey the patterns hidden within a dataset is one of the most vital abilities a developer can have."
datatable: true
---
# The importance of data visualisation
In today's data driven world, being able to easily convey the patterns, or trends, hidden within a dataset is one of the most vital abilities a developer can have.

When it comes to transforming raw data into something even a casual observer can understand then the most important tool in a developers toolbox is data visualisation. There are, of course, numerous ways to display data visually, such as line graphs, histograms, pie charts, and heatmaps. Each method has its own strengths and weaknesses, pie charts are perfect to show the distribution of data within specific categories, line graphs allow an easy way to compare two sets of data in a linear fashion, and heatmaps (or bubble maps) are often used in combinations with a map to show geographical groupings. 

In order to understand why data visualisation is so important let's look at the following example. 

> Show a client where to focus their energy, when it comes to tailoring their platform, based on the geographic location of the biggest proportion of their user base.

At face value this seems relatively simple, and while that's true there are numerous ways to approach this task. Since this blog is covering the importance of data visualisation, let's see how data visualisation can provide a solution that will satisfy the requirements while being easy to understand.

Let's skip ahead past the technical details, and presume we have:
> * a dataset containing number of users and their geographic location.
> * knowledge of how to create data visualisations from a dataset.

The dataset mentioned above could easily contain millions of rows of data, depending on the size of the user base. Showcasing such data in its raw form can be confusing for clients. If the data was stored in a database, or table, then naturally we could just query the location that had the highest number of users. However, this method has a few downsides. Firstly, it isn't appealing, and secondly, it doesn't cover the entire dataset. This is where data visualisation can be a great tool to use.

Data visualisation methods, such as a heatmap, provide not just the answer to the posed question, but simultaneous access to information about the entirety of a dataset with minimal extra effort once the visualisation is created.

To expand upon the example, let's presume a few things. 

> * The client has a user base of 1 million individual users.
> * There are 365 data points per user, totalling 365 million rows of data.
> * The scope of the task will expand to cover the top 5 locations instead of just the top 1 location.

The simple fact that there are 365 million rows of data means it will be nearly impossible to understand the dataset in it's raw form at a glance. However, through the use of data visualisation tools like matplotlib and plotly, just to name a few, we can transform the raw data into something that's not only visually appealing but also expandable and, most importantly, understandable for the client.

As I've mentioned there are numerous forms of data visualisation. You could use histograms, pie charts, or a heat map overlayed onto a world map. All of these would allow even the most casual observer to understand which location has the highest proportion of users.

In order to provide a side by side comparison of how effective data visualisation can be, let's look at the following table of data that describes the number of Covid cases per country.

> | **Country**            | **# of cases** |
> |:-----------------------|---------------:|
> | Albania                | 23             |
> | Andorra                | 1              |
> | Austria                | 361            |
> | Belarus                | 21             |
> | Belgium                | 399            |
> | Bosnia and Herzegovina | 11             |
> | Bulgaria               | 23             |
> | Croatia                | 25             |
> | Cyprus                 | 6              |
> | Czech Republic         | 116            |
> | Denmark                | 676            |
> | Estonia                | 27             |
> | Finland                | 155            |
> | France                 | 2876           |
> | Germany                | 2369           |
> | Greece                 | 133            |
> | Hungary                | 16             |
> | Iceland                | 117            |
> | Ireland                | 70             |
> | Italy                  | 15113          |
> | Latvia                 | 16             |
> | Liechtenstein          | 4              |
> | Lithuania              | 3              |
> | Luxembourg             | 26             |
> | Macedonia              | 9              |
> | Malta                  | 9              |
> | Moldova                | 6              |
> | Monaco                 | 1              |
> | Netherlands            | 614            |
> | Norway                 | 621            |
> | Poland                 | 49             |
> | Portugal               | 78             |
> | Republic of Serbia     | 24             |
> | Romania                | 64             |
> | Russia                 | 34             |
> | San Marino             | 67             |
> | Slovakia               | 21             |
> | Slovenia               | 96             |
> | Spain                  | 3004           |
> | Sweden                 | 620            |
> | Switzerland            | 854            |
> | Turkey                 | 2              |
> | Ukraine                | 3              |
> | United   Kingdom       | 590            |

Given the relatively small dataset, it's not terribly hard to find the country with the highest number of Covid cases, however this dataset only consists of 44 rows. Imagine a dataset that has hundreds of thousands, or even millions, of rows of data that you have to summarise for a client. 

The image below, however, is an example of a bubble map, of the number of Covid cases in Europe as of March 13<sup>th</sup>, 2021, overlayed onto a map of Europe. As you can see it is easy to see that the largest concentration of Covid cases at the time was centered around Italy, with no need to scroll through rows upon rows of raw data.

> {% include lightbox.html url="img/2022-06-06_imgs/bubble_map_Covid_example.png" thumb_width="100%" title="This example bubble map shows proportion of dataset by geographical location" lightbox_gallery="photo-1" caption="This example bubble map shows proportion of dataset by geographical location  
Generated by [everviz.com](https://app.everviz.com)"%}

In terms of our earlier example problem, a bubble map overlayed onto a map could be a perfect solution. 

> #### Data visualisation provides a method of data presentation that's expandable, professional looking, and easy to understand. 

---------------------

# Advantages of data visualisation

> * Reduce the length of reports
> * Easy to understand
> * Ease of use
> * Visually appealing

The bullet points above cover just a few of the advantages to data visualisation, to get a further idea of how data visualisation can provide advantages in today's data driven world this section will take a deeper dive into how these combine to create an end product that's worth learning to master.

As we've already covered, sometimes datasets can contain hundreds of thousands of pieces of information. The earlier example of Covid cases was a small dataset that consisted of only 2 columns, and 44 rows. Let's take a look at the following sample table that shows the total number of Covid cases per continent since the beginning of the pandemic. This table is much larger than the previous example table, but still only consists of a fraction of the larger global dataset, which has 230 columns. 

<blockquote>
    <table style="max-width:100%;overflow:auto;max-height:500px;display:block">
      {% for row in site.data.continental_covid_new_cases %}
        {% if forloop.first %}
        <tr>
          {% for pair in row %}
            <th>{{ pair[0] }}</th>
          {% endfor %}
        </tr>
        {% endif %}
        {% tablerow pair in row %}
          {{ pair[1] }}
        {% endtablerow %}
      {% endfor %}
    </table>
</blockquote>

Since the dataset is so much larger, it's harder for a casual observer to look at the data and quickly come to a conclusion. What makes this dataset even more challenging is that each row isn't a cumulative total of all previous rows, instead each row is merely the daily new case count. I'm sure there are people out there who could scroll through this table and keep a mental tally of the totals for each column but I suspect most people couldn't, I know I can't. It probably took you a while just to scroll through the table, if you even bothered to do more than read the header and the first few rows of data. 

This is where data visualisation comes in, it can take structured data and provide a snapshot that conveys the key details with just a single image. It can turn a seemingly complex and incomprehensible dataset into something so simple that gets its meaning across in an instant. Below is a sample image of a bubble map built off the same dataset, showing total cases since the pandemic began. As you can see, we've taken that structured data and turned it into a single image that conveys it's meaning almost instantly.

> {% include lightbox.html url="img/2022-06-06_imgs/bubble_map_Covid_example_2.png" thumb_width="100%" title="Bubble map showing total Covid cases by continent" lightbox_gallery="photo-1" caption="Bubble map showing total Covid cases by continent  
Generated by [everviz.com](https://app.everviz.com)"%}

Some of the final advantages for data visualisations that I'll talk about are the ability to show the changes in a dataset over time, and the ability to quickly and easily upgrade visualisations as datasets evolve.

The wide variety of types of data visualisation out there allow for a large number of permutations when it comes to displaying a dataset. Some examples of the types of data visualisation at our disposal are charts, graphs, tables, maps, infographics, and dashboards. Here are some specific examples of the types of data visualisations out there:

> * Area Chart
> * Bar Chart
> * Box-and-whisker Plots
> * Bubble Cloud
> * Bullet Graph
> * Cartogram
> * Circle View
> * Dot Distribution Map
> * Gantt Chart
> * Heat Map
> * Highlight Table
> * Histogram
> * Matrix
> * Network
> * Polar Area
> * Radial Tree
> * Scatter Plot (2D or 3D)
> * Streamgraph
> * Text Tables
> * Timeline
> * Treemap
> * Wedge Stack Graph
> * Word Cloud

Keep in mind these are just some of the types that are out there, and when you combine multiple visualisations together you get a dashboard. Now we've all seen a movie where you see a control room that has impressive, futuristic looking, displays that show reams and reams of relevant data; well, that's what data visualisations give us when we create a dashboard. For an example of a dashboard, take a look at the image below of one created by ArcGIS for a sample lesson from their website. 

> {% include lightbox.html url="img/2022-06-06_imgs/dashboard_covid_example.png" thumb_width="100%" title="A sample Covid dashboard by ArcGIS" lightbox_gallery="photo-1" caption="A sample Covid dashboard by ArcGIS  
Generated by [ArcGIS](https://learn.arcgis.com/en/projects/create-a-covid-19-dashboard/)"%}

As you can see they've combined a bubble map, a basic bar chart, along with some data tables to provide a "one stop shop", if you will, for a Covid tracking system. I'm sure you'll spot some issues with certain parts of this dashboard, and we'll talk about those in the next section.

> #### Data visualisation is half science, half art. Done well it's a valuable tool in the arsenal, but done poorly and it does nothing more than detract from the whole.

---------------------

# Limitations & pitfalls of data visualisation

We've talked about the advantages of data visualisation but in order to maintain a well rounded overview it is important to also talk about the limitations and pitfalls as well. Keep in mind such things as:

> * Bad dataset
> * Visual clutter
> * Wrong visualisation type

Each of the above mentioned issues can turn a useful tool into one that's more confusing or misleading than the raw data, as well as being an overall waste of time. Take a look at the following bubble map, it has all the same settings as the previous continental Covid case bubble map, but instead of continents uses a dataset that consists of the total Covid cases for every country on earth.

> {% include lightbox.html url="img/2022-06-06_imgs/bubble_map_Covid_bad_example.png" thumb_width="100%" title="Bubble map showing total Covid cases by country" lightbox_gallery="photo-1" caption="Bubble map showing total Covid cases by country  
Generated by [everviz.com](https://app.everviz.com)"%}

While you can slightly make out the large red dark circles, that indicate the highest number of cases, it is impossible to determine which country they belong to. As with structured data, you have to be careful to match your choice of data visualisation with the dataset in order to get the meaning of the data across without any confusion. 

Here is the same bubble map, as the one above, but this time with it's settings tweaked so that you can more clearly see each individual bubble. While better, it is still somewhat confusing in locations where countries are more closely clustered.

> {% include lightbox.html url="img/2022-06-06_imgs/bubble_map_Covid_bad_example_2.png" thumb_width="100%" title="Bubble map, with tweaked settings, showing total Covid cases by country" lightbox_gallery="photo-1" caption="Bubble map, with tweaked settings, showing total Covid cases by country  
Generated by [everviz.com](https://app.everviz.com)"%}

Now here's an example of the same information but shown in a doughnut pie chart style, as you can see it is much easier to see which countries have the highest number of cases at a glance, compared to the bubble map.

> {% include lightbox.html url="img/2022-06-06_imgs/bubble_map_Covid_bad_example_3.png" thumb_width="100%" title="Doughnut pie chart showing total Covid cases by country" lightbox_gallery="photo-1" caption="Doughnut pie chart showing total Covid cases by country  
Generated by [everviz.com](https://app.everviz.com)"%}

If you were the client, which would you rather look at? It is important to keep in mind that data visualisation is a tool, and like any tool you have to chose the right one for the job. Sometimes data visualisation isn't the best choice, but with the wide range of visualisation types there is nearly always a way to get your data across in a useful and engaging way.

> #### Making sure to choose the right type of data visualisation is as important as making sure your data is well structured for the task at hand.

---------------------