---
layout: post
title:  "Why is data visualisation so important?"
date:   2022-06-06 13:44:55 -0600
image:  blog_title_imgs/circuit_board_colour.jpg
tags:   [python, data visualisation, matplotlib, plotly]
description: "Being able to easily convey the patterns hidden within a dataset is one of the most vital abilities a developer can have."
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

The dataset mentioned above could easily contain millions of rows of data, depending on the size of the user base. Showcasing such data in it's raw form can be confusing for clients. If the data was stored in a database, or table, then naturally we could just query the location that had the highest number of users. However, this method has a few downsides. Firstly, it isn't appealing, and secondly, it doesn't cover the entire dataset. This is where data visualisation can be a great tool to use.

Data visualisation methods, such as a heatmap, provide not just the answer to the posed question, but simultaneous access to information about the entirity of a dataset with minimal extra effort once the visualisation is created.

To expand upon the example, let's presume a few things. 

> * The client has a userbase of 1 million individual users.
> * There are 365 data points per user, totalling 365 million rows of data.
> * The scope of the task will expand to cover the top 5 locations instead of just the top 1 location.

The simple fact that there are 365 million rows of data means it will be nearly impossible to understand the dataset in it's raw form at a glance. However, through the use of data visualisation tools like matplotlib and plotly, just to name a few, we can transform the raw data into something that's not only visually appealing but also expandable and, most importantly, understandable for the client.

As I've mentioned there are numerous forms of data visualisation. You could use histograms, pie charts, or a heat map overlayed onto a world map. All of these would allow even the most casual observor to understand which location has the highest proportion of users.

In order to provide a side by side comparison of how effective data visualisation can be, let's look at the following table of data that describes the number of covid cases per country.

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

Given the relatively small dataset, it's not terribly hard to find the country with the highest number of covid cases, however this dataset only consists of 44 rows. Imagine a dataset that has hundreds of thousands, or even millions, of rows of data that you have to summarise for a client. 

The image below, however, is an example of a bubble map, of the number of covid cases in europe as of March 13 2021, overlayed onto a map of Europe. As you can see it is easy to see that the largest concentration of covid cases at the time was centered around Italy, with no need to scroll through rows upon rows of raw data.

> ![]({{site.baseurl}}/img/2022-06-06_imgs/bubble_map_covid_example.png)
<!--
 TO ADD SPECIFIC WIDTH/HEIGHT SHIT DO THIS: {: height="200px"}
-->
*This example bubble map shows proportion of dataset by geographical location  
Generated by [everviz.com](https://app.everviz.com/create?uuid=mnrw1212)*

In terms of our earlier example problem, a bubble map overlayed onto a map could be a perfect solution as it can both look elegant and provide ample information, even if the scope is expanded past the initial question.
