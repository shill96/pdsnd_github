##### 11 November 2021,9:18 pm

# Explore US Bikeshare Data

![Image of bikes](https://video.udacity-data.com/topher/2018/March/5aa7718d_divvy/divvy.jpg)

### Table of Content
1. Description
2. Project Overview
3. The Datasets
4. List of software required
5. Files used
6. Credits

### Description
In this project, Python is used to explore data related to bike share systems for three major cities in the United States—Chicago, New York City, and Washington. Codes are written to import the data and answer interesting questions about it by computing descriptive statistics. We also were tasked to write a script that takes in raw input to create an interactive experience in the terminal to present these statistics.

### Project Overview
Over the past decade, bicycle-sharing systems have been growing in number and popularity in cities across the world. Bicycle-sharing systems allow users to rent bicycles on a very short-term basis for a price. This allows people to borrow a bike from point A and return it at point B, though they can also return it to the same location if they'd like to just go for a ride. Regardless, each bike can serve several users per day.

Thanks to the rise in information technologies, it is easy for a user of the system to access a dock within the system to unlock or return bicycles. These technologies also provide a wealth of data that can be used to explore how these bike-sharing systems are used.

In this project, you will use data provided by Motivate, a bike share system provider for many major cities in the United States, to uncover bike share usage patterns. You will compare the system usage between three large cities: Chicago, New York City, and Washington, DC.

### The Datasets
Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:

    * Start Time (e.g., 2017-01-01 00:07:57)
    * End Time (e.g., 2017-01-01 00:20:53)
    * Trip Duration (in seconds - e.g., 776)
    * Start Station (e.g., Broadway & Barry Ave)
    * End Station (e.g., Sedgwick St & North Ave)
    * User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:

    * Gender
    * Birth Year


### List of software required
* You should have Python 3, NumPy, and pandas installed using Anaconda
* A text editor, like Sublime or Atom.
* A terminal application (Terminal on Mac and Linux or Cygwin on Windows).


### Files used
The following files are not uploaded to remote repo by using .gitignore because the files are too big:
    * chicago.csv
    * new_york_city.csv
    * washington.csv


### Credits
* [Pandas documentation](https://pandas.pydata.org/pandas-docs/stable/).
* [Numpy Manual](https://docs.scipy.org/doc/numpy-1.13.0/contents.html).    
* [Dataframe Documentation](https://pandas.pydata.org/pandas-docs/stable/reference/frame.html#dataframe).
* Convert to datetime datatype using the pandas [to_datetime()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html) method and extracting properties such as the hour with [datetime properties](https://pandas.pydata.org/pandas-docs/stable/reference/index.html) was helpful in working with datetime datatype.
* [Stackoverflow](www.stackoverflow.com) is a great way to get solutions to all your errors.
