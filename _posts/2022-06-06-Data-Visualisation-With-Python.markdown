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

When it comes to transforming raw data into something even a casual observer can understand then the most important tool in a developers toolbox is data visualisation. There are, of course, numerous ways to display data visually, such as line graphs, histograms, pie charts, and heatmaps. Each method has its own strengths and weaknesses, pie charts are perfect to show the distribution of data within specific categories, line graphs allow an easy way to compare two sets of data in a linear fashion, and heatmaps are often used in combinations with a map to show geographical groupings. 

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

![]({{site.baseurl}}/img/heatmap_colour.jpg)
<!--
 TO ADD SPECIFIC WIDTH/HEIGHT SHIT DO THIS: {: height="200px"}
-->
*This example heatmap shows proportion of dataset by geographical location*

The image above shows an example of a heatmap of covid cases by country, which, as you can see is pretty cluttered. Like any form of visual representation, you have to be careful about making sure that you don't overload an area with too much information, or you end up with a similar problem to trying to make sense of the raw data itself.

