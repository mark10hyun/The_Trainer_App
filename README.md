# The_Trainer_App
Fitness Tracker Application

### Problem
	With health and fitness growing as an industry, there is a demand for fitness plans and fitness trainers. Our friend, who is a fitness fanatic and loves to train and offers training programs to his friends and created a group chat of all of his friends that wanted to work out with him and get on a training plan. This begged us to ask the question, how does he manage to keep all of his programs, and how does he keep tabs on which and what workout for each of his friends ?  
### Solution
	Build an application that served as a user record database that is specifically geared towards physical trainers. This application adds organization and simplicity for fitness trainers. This application allows physical trainers to add new clients, view and print user records to csv, update user’s and goals, delete users, and search for users. The most prominent feature was the ability to auto assign specific workout plans to the users based off of their inputted fitness goals. 
	For our front end/UI development, we used the tkinter package in python.
 For backend, we created 5 tables (Goals, Plan, Exercises, Users, and Progress) each table consisting of primary and foreign keys, which was crucial to maintaining referential integrity and allowed us to optimize performance, instead of continuously redeclaring the values which may lead to misidentified data. Utilizing referential constraints was extremely important because each user was unique, and had their own unique work out plan
