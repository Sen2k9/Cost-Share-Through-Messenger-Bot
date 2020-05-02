# Cost-Share-Through-Messenger-Bot
## Calculating the shared cost of a group in messenger bot

## Problem Description
It has seen that close community (i.e. country-based community in LaTech, group of friends) often arrange different program i.e. get together on a community member house, potluck party, trip, organize a national festival, etc. After each program, someone needs to take charge of collecting all the costs, calculating the shared cost, and letting each member about his or her share, which is a tedious and time-consuming job. One option to get rid of this hassle is to use an app that will automatically do all the stuff. However, installing another app, frequently check the update in the apps is also another burdensome job. On the other hand, most of the people (All!) use Facebook and Messenger. If it is possible to make a messenger bot which will do all the above-mentioned job it will be a lot easier to reach all the members of the community (typically closed community are connected through messenger using group).

## Description of Mini world
In the messenger people connected through a group. Group in the database will be identified by a unique name. There will be two types of people in each group member and admin. A person can be a member and/or admin of more than one group on Facebook.
In the database, each person will be identified through Facebook PSID (an id for using the Facebook app). The database also stores the person’s name, address, payment ID (i.e. email for Chase QuickPay).
To keep track of the program, the database will store program date, location, and type of the program (there will be 4 types: tour, get together, festival, potluck), the participator and cost spent on the program. Each program will be organized by a member or admin.
Moreover, the program can be sponsored by a person in the group or an outer member/entity. The database also keeps track of the sponsored name and sponsorship value (in USD).
The database also stores all the dependent name, date of birth, sex of each member to keep track of whether the family member participates in the program.

## Technological Overview

## Phase 1:
 ### A database will have users information (such as, name, address, payment ID, email, sex, DOB etc.)
 ### A user can be a member or Admin
 ### An admin will have previlege to remove or add a member.
 ### App should be able to communicate between messenger and the database
 ### An event or program (hosted only by the admin) should have at least date, location and the type
 ### An event will serve independently. Such as one member/admin can participate in several events.
 ### The automated bot should calculate the total cost and cost per member after the end date of the event.
 
## Phase 2:
 ### An event can have sponsor from a person or agency
 ### An event can have several sponsors and one sponsors can participate in several events (Many to Many relations).
 ### Automated bot will calculate the cost per member after deduction of the sponsored money.
 ### An admin can create a poll/survey in the messenger and the database will serve in the background for the poll decision
 ### A member can upload event photos and the database will save all photos.
 ### After the event the admin can share all saved photos from the database to desired members.
 
## Phase 3:
 ### The database will reset after a month to save memory for every member. ( Premium membership can have one year subscription)
 ### A member having the app can have an analytical and infographic result of his/her cost per month in events. ( Premium membership can have the service for a year).
 
 ## Technology recommended:
 ## Python, JavaScript, Django, React
