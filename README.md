# Twee-Shirts

## DSCI-6007 (Data Engineering) Final Project [March 2016]

### Summary

This project assumes the hypothetical business model of setting up a t-shirt screen printer outside of a sports arena. Immediately after a game, t-shirts can be made and sold on the spot with hashtags that trended during the game printed on them. This program collects live tweets relating to the game (usually via specifying a team name), and stores them in a Mongo database.

After the game, the entries are exported to CSV, opened in an iPython notebook, and manipulated so that the most frequent hashtags used in the team-related tweets are displayed in a table. As a bonus, the table’s colors match the colors of the team whose tweets were being gathered. 

### Technologies Used

* MongoDB
* The Twitter API
* Pandas
* Tweepy
* Plotly

### Ideas for Improvement

All school projects run short on time. If I were to extend this project, I would have the tweets from the database imported directly into the iPython notebook, thus skipping the CSV step. This would eliminate a manual step, and make the program more accessible. 
