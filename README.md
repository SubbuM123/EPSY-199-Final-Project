# EPSY-199-Final-Project
Chess Intelligent Tutoring System

This document is my official report and contains all of the deliverables for my final project. There’s a few components, so I’d like to explain them real quick:

Github and Overview - The next page contains the link to the Github repository that contains all the files from this project. This has all of the code and datasets I used for this project. Also, under the Github link, I have given a short description of all of the files in the repository as well. These descriptions can also be found in the README file in the repository, but I included it here for ease.
Here, I start the report portion of this assignment. Here is where I explain my project and go through the steps I took to complete it. It also covers a section on results, reflections, and future improvements. Here are the parts of the report:
Intro/Main Goal - Gives an overview of the project and its goals
Evidence and Psychology - Covers the studies and psychological phenomena that support this model’s goals and intentions, showing why it works
Process - This is the most technical section, where I walk through the code I wrote for this assignment
Results - This section looks at the analysis of my findings, and what can be used for the project and what may need to be redone
Reflection - Focuses on the main changes I would make with more time and resources, and different ways to improve what I already have
References - This page contains the references to all outside information I used

Github Link: https://github.com/SubbuM123/EPSY-199-Final-Project 

Overview:

Games.csv - This dataset contains over 20,000 chess games of various ratings. This was the sole dataset used in the project
Analysis.ipynb - This Jupyter Notebook contains a short analysis of my findings. The “Results” page of this report directly corresponds to it
Regression.py - Contains 2 regression models of the data. These are also present in Analysis.ipynb
main.py - This is a look at how the final product would look. It contains both the python and javascript code to take in user input and predict their ratings
Index.html - contains the html and css code for a website
Clustering
GroupsKMeans.py - This file has the clustering model for all the datapoints from games.csv
IndKMeansAnalysis.py - This file generates multiple KMeans models, based on rating ranges defined in the report
ClusterAnalysis.py - This file just has print statements to ensure formatting of the csv files are correct
KMeansData - This file contains the data of every single game from games.csv. It only contains the relevant features that we extracted. The name of each file in this folder corresponds to the rating range it spans
Jupyter Data
Mean.csv - This csv file contains data on the average centroid of each KMeans cluster feature for each rating range
STD.csv - This csv file contains data on the standard deviation of each centroid of each KMeans cluster feature for each rating range
Data Collection
Scrape.py - This file contains the code to obtain a player’s game moves in a usable format when they provide a link to their game
Format.py - This file takes in the moves and formats them into a DataFrame, allowing it to be easily analyzed
Game_analysis.py - This file extracts the features of each game, and these are the same features used for clustering


Intro/Main Goal:

The purpose of this project is threefold: first is to gather data regarding chess games, and figure out which features in a game most determine different skill levels; second is to use these features to build a model that can accurately predict a players rating range based on a game they just played; finally, this information should be used to build an AI model that can pick apart features in a one’s game, and offer suggestions of what can be done to further improve upon their play, to increase skill.

To implement these three purposes, we will first start with using a clustering model (KMeans) and utilize the power of unsupervised learning to find the best predictive features. Next, we will likely use a prediction ML model, likely not regression, but something like classification, to predict different ratings. Finally, we will feed the model large amounts of data so it can recognize the parts of game play that truly separate one skill level from the other. Then it can be deployed and tested to ensure it is doing what it is supposed to do – help one learn about their style of play, and improve upon it as much as possible.

These goals will all be delivered in a Github portfolio, with the code being written in Python, using the pandas and numpy programming languages

Evidence and Psychology

Since this model will serve more as a coach or tutor, most of the evidence for the practicality of the model will come from Van Lehn’s research on intelligent tutors.

Following the loop model below, I will go through each portion of the loop, and how it correlates to the project:


Task Domain: The AI model will teach the user how to become a better chess player – specifically, fix the weaknesses in play, but improve upon their current strengths.
Task: The task that the user will participate in will be a game of chess
Step: In the context of the chess game, there are two interpretations of a step. The first, more obviously, is each move the user plays, since each of these moves can be looked at for accuracy. The second, could be the phase of play – the opening, middle, or endgame.
Knowledge Component: The knowledge component of the user can be twofold. The first is all of their previous chess knowledge – whether that be tactics, openings, strategies, or endgame methodology. The second knowledge component would be any information the user has gained from this tutoring system, if they have used it before.
Learning Event: The learning event would be the subsequent chess game, presumably after using this tutoring system and being cognizant of its advice. The user can apply the knowledge component, which is the advice they learned, and apply this knowledge accordingly.
Outer Loop: In this case, the outer loop would make the most sense if it was iterating over a group of chess games player. Perhaps the tutoring system could track the analytics of each game to produce a final “report” or “scorecard” for the user to further use in their training.
Inner Loop: The inner loop would be one chess game. The system will iterate through the game, offering advice, pointing out mistakes and strengths, and suggesting improvements.
Incorrect: This system does not have a clear cut “incorrect” component. Since the game of chess has so many complex pieces, it might be better to have each “incorrect” component be a situation where a user makes the same mistake over multiple games, so the system begins to flag it.
Process:

Now, I'll focus on the technical side of the project, and cover what I did to implement the psychologies I talked about in the previous page. I will share my technical processes and methods in this page, and expand on results and future changes I will make in the next page.

First, the dataset. The dataset I used was pulled from Kaggle (https://www.kaggle.com/datasets/datasnaek/chess/data). It contained over 10,000 chess games played on Lichess. The dataset contained different features, but most notable was player rating, the moves that each player played, the number of turns, the victory status, and different details regarding the opening that was played. In terms of cleaning the dataset, I used the Python library, pandas, to drop any null or blank values, and this ensured my data was usable.

Now, moving onto creating usable data for this assignment. Chess is a complicated game, with many variations. However, as a player progresses, they adapt to certain styles, and the strength of these styles depends on their experience and skill in play. However, most of these styles fall into a select few categories, since there are some guaranteed tactics and strategies that improve one’s game. For this project, given the lack of resources and a shorter timeframe, I decided to look solely at 2 different subsections of play style: one was the specific pieces moved – major pieces, minor pieces, and pawns, while the other was emphasis on the different phases of the game --opening, middlegame, and endgame. I thought these were all traits that could be different in many players, and would provide enough “categories” for them to be clustered into. Using pandas and numpy libraries, I was able to turn the moves into dataframes, and analyzed each game's emphasis on different pieces and game phases.

After generating all of this data, I was left with completely numeric data, which was ready to cluster. Since the goal of this project was to ultimately determine important features in game play throughout different skill levels, I first split the dataset into equal sized samples. Each sample contained a rating range of 200 points, and spanned from a  rating of 1000 to 2400.

For the actual Machine Learning and Clustering I did, I decided to use KMeans clustering, since it is easy to integrate with datasets made by pandas. KMeans clustering using centroids within the datapoints, and rearrages the user inputted number of centroids into the given data until clusters with all similar data are grouped together.

In my case, I used KMeans with both 5 and 10 clusters and analyzed the results. Given the limited scope of the data, the 10 clusters for each rating range was not as different compared to the one with only 5 clusters. In the results section, I will speak more about what I found and how that may be significant.

Overall, with the use of ML, I can figure out what features define increase in skill in chess, and this could be used to create an AI trainer that analyzes chess growth.


Results:

The results of the first 2 steps of the process are contained in the Jupyter Notebook in the submitted Github repository.

Overall, given the categories that were chosen to analyze the games, the results were not as expected. The datum of each game was too naive – in other words, there was no feature that was larger, significant, or variable from rating to rating. When analyzing the average cluster center for each rating category, there was no significant difference (1.1 in Analysis.ipynb). Interestingly, however, the data seemed to follow a pattern where the highest rating and lowest ratings had almost identical cluster centers, while the middle ratings tended to differ from the two.

Additionally, when looking at the average size of the standard deviation of the cluster in each category (1.2 in Analysis.ipynb), they were very similar as well. This alludes to the fact that most rating levels had a very similar spread of data, so the features chosen for clustering analysis were not very good at all.

However, despite all this, I tried using a regression model just out of curiosity. Since the data was very scattered and non-linear, I decided to use a Logistic Regression Model (2.1 in Analysis.ipynb) to predict a player’s rating given the features of their game.. After initializing and fitting the data, I decided to check its accuracy. The Python library for Logistic Regression has a “score” function. Using the score function, I was given an accuracy of just above 4 percent. So, this model was clearly not working for the data at all. However, after both the KMeans analysis and the regression interpretation, there were definitely a few changes I could make to improve this model, although they would take much more time.

Also, just out of curiosity, I decided to make a linear regression model just in case the data somehow followed a linear model (2.2 in Analysis.ipynb). As expected, however, the model was not very accurate. When calculating the average disparity in rating between the predicted and actual data points, the model was off by an average of over 225 rating points.

Reflection:

After all this analysis of results I realized that the main issue of the data I collected and generated was caused by the features I chose. These features were much too simple, and wouldn’t differ much based on the rating of a player. To truly see a much better model with enhanced features, I would have to look at much deeper, complex, and game intensive features.

To do this, I would likely have to use a chess AI, who already has enough knowledge to analyze a game and mistakes a player has made. What first came to mind was Stockfish, the current leading chess AI bot. With Stockfish, I could easily identify occasions where a user made a good move, made a mistake, or made the best move in the position. I could analyze how many times each of these instances occurred, and create some type of formula that could correlate to a rating range. Furthermore, this would allow me to find features of play that are guaranteed to reflect skill level, instead of more abstract ideas that do not add much to the predictive model.

Finally, I could complete this project by adding commonly made mistakes and common improvements and fixes for these mistakes. As a user made these mistakes, the model could detect them, and provide the improvement as feedback to the user. This would finally allow them to improve their game, and as they advanced through the rating ladder, their improvement advice would also constantly be tailored to fit their skill level and opponent difficulty.

However, I still created the “predictor” part of this system, but made it very simplified. Essentially, a user can just input a chess game they played from the website Lichess.org, and the python script will parse through the game, and determine the simple features. After this, the model will look at the clustered categories of the test data, and see which cluster the user best fits into. Obviously, this will not give us any usable results, since the clustered model is the clustering of all datapoints in the set, which is not really optimized for this system. However, the main.py file and the index.html files still demonstrate how a final product of this system could look like, and shows the UI of the project as well.
References

Fagen, W., & Flanagan, K. (n.d.). Clustering. Data Science Discovery. https://discovery.cs.illinois.edu/learn/Towards-Machine-Learning/Clustering/ 
Princeton Review. (n.d.). Intelligent tutoring systems: Enhancing learning through AI. Intelligent Tutoring Systems: Enhancing Learning through AI | The Princeton Review. https://www.princetonreview.com/ai-education/intelligent-tutoring-systems 
VanLehn, K. (2006). The behavior of tutoring systems. International Journal of Artificial Intelligence in Education, 16, 227–265.

VanLehn, K. (2006). The behavior of tutoring systems. International Journal of Artificial Intelligence in Education, 16, Table 1, 227–265.

