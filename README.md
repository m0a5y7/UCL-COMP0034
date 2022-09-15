[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-f059dc9a6f8d3a56e377f745f24479a46679e63a5d9fe6f495e02850cd0d8118.svg)](https://classroom.github.com/online_ide?assignment_repo_id=6693690&assignment_repo_type=AssignmentRepo)
# COMP0034 Coursework 1 and 2 repository

# COMP0034 Coursework 2

GitHub Repository: https://github.com/ucl-comp0035/comp0034-cw1-g-group-13-1.git

Video demo: https://www.youtube.com/watch?v=PHRmwioKV38

Requirements are found in requirements.txt

Run [app.py](flask_app/app.py) to run the code.

The [tests](tests) directory contains all tests.


Blog structure adapted from the Ruscica (2022) tutorial.

## References

Ruscica, T. (2022). Flask-Blog-Tutorial. [online] GitHub. Available at: https://github.com/techwithtim/Flask-Blog-Tutorial/blob/main/tutorial5/website/templates/create_post.html [Accessed 4 Apr. 2022].

# COMP0034 Coursework 1 Group 13

GitHub Repository: https://github.com/ucl-comp0035/comp0034-cw1-g-group-13-1.git

Video demonstration of dash app: https://youtu.be/UV5Woj1m5IQ

## Instructions

Run [main.py](flask_app/dash_app/main.py) to run the code.
The [apps](flask_app/dash_app/apps) directory contains the individual pages for each visualisation.
The [tests](tests) directory contains tests done using dash testing.

## Research background

Questions:
Different countries offer different environments for a business to thrive, and it is often difficult to identify what countries offer the most potential growth of a business. If a company chooses poorly when moving to another country, it may result in severe financial losses. It is essential for a business to choose to expand to a country that would maximise its revenue. This can be especially relevant to newly expanding companies that want to minimise the risk of failing in their new enterprise. Here we are given two indicators: Ease of Doing Business Score and Paying Taxes Score. We can use these values to determine how business-friendly certain countries are, which is useful information in the above scenario. The question we will thus try to answer using in this project are:
Which countries score the highest in the two indicators in the past 5 years?
Which countries have shown the most growth in the past 5 years in each indicator?
Answering these questions will hopefully lead to more insight for our users to decide on which countries to invest their resources in.

Target Audience:
This web application would be of use to large-scale investors and executive officers at multi-national corporations, since it would allow them to explore different options when expanding their businesses.

## Visualisations

Here, we explain the context of our visualisations, and discuss the strengths and limitations of our chosen designs.

We have two main indicators for which countries are best to do business in: 'ease of doing business' and 'paying taxes'. Both are measured out of 100. We have data for these from 2016-2020. After researching different visualisation methods and considering potential limitations (Restori, 2018), we decided that a **scatterplot** would best represent our data. Hovering over each country point shows the data for that country. By using a scatter plot, each country's datapoint can be easily visualised, making it easier to compare between the countries' data. For example, we can see that countries like New Zealand and Hong Kong score highly on both indicators, and that there is a positive correlation between the two indicators. We also added a slider that allows the user to view plot based on different years, which makes it possible to track a country's growth.

However, there are some potential limitations with only using a scatterplot. Most importantly, the number of countries may make it confusing to understand which countries are where in the plot. This is why we additionally decided to show the data in a **choropleth map**. This helps greatly in understanding the data in a geographical context - and quickly finding the data for only the countries that the viewer is interested in. The choropleth map provides an excellent overview of how countries and regions score in a given indicator in an analytically abundant way (Maps For Excel, 2013). However, it is limited in the amount of detail on each individual country. Biases may also arise if certain geographical areas appear to be overall 'bad for business' - or if the colours of the map attract the viewers' attention rather than the data itself (Maps for Excel, 2013). It may be that for certain countries the two indicators being presented are not the best to measure their viability for business.

To give a more detailed analysis of each country's performance, we included **line graphs** that show each country's performance over time, with more information provided on the percentage growth shown by each country in each indicator. This makes it so that the user has a better understanding of how a country performs relative to its own past, rather than comparing it to other countries. The user may then infer on how a country may develop in the future, which is information they can use to decide on where to invest their resources. This resolves some of the bias that may occur with the other visualisations. CUEMATH (n.d.) also highlights that a line graph may be able to highlight small growth and differences in data in a way that other graph types may not. They also highlight the use of decimal point data as a potential limitation, something that is applicable to our data.

To finish, we added a **ranking table** for viewers who might wish to simply view in table form which country is the best to do business in, per indicator. Having this at the end may be beneficial for those who prefer to only find out the rank of top countries. A potential limitation of the ranking table is that it is too long for viewers to comfortably go through. To mitigate this limitation, we are only displaying the top 10 countries per year. Of course, this means that any country below that gets disregarded.

## References

### Literature
CUEMATH (n.d.). Line Graph - Reading and Creation, Advantages and Disadvantages. [online] Cuemath. Available at: https://www.cuemath.com/data/line-graphs/.

Maps for Excel (2013). Choropleth map in the analysis on the map. [online] Maps for Excel - Simple Excel Add-In to create filled maps & dashboards in Excel. Available at: https://maps-for-excel.com/blog/choropleth-map-in-the-analysis-on-the-map/.

Restori, M. (2018). What is a Scatter Plot and When to Use It. [online] Chartio. Available at: https://chartio.com/learn/charts/what-is-a-scatter-plot/.

### GeoJson
Natural Earth (2019). [online] Natural Earth. Available at: http://www.naturalearthdata.com/downloads/10m-cultural-vectors/

