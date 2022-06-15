# 8NEWS
## CS50 Web Programming with Python and JavaScript - Final project

### Technologies:
- Python (Django framework)
- Javascript
- HTML
- CSS

### Distinctiveness and complexity:
Keeping carefully the requirements mentioned by CS50, I decided to create a newspaper responsive application. I visited so many real news webpages to get inspiration and finally I decided to add a vintage touch, so I took my phone and called to some of the best journalists from different centuries to create their accounts and post some news happened in the past.
Previous projects was really helpfull to create this. Users can write a feedback of the news, but finally this is not a social network, they can not interact between them. This is not a commerce, but I decided to use a similar way for saving users' favorite news in the database, called  *Readlists*. The buttons to choose news by topic, have a similar functioning of the Mail project. Finally, the login and register functions are the already learned on CS50, just adapted for this app.
I needed several attempts, however I finally got connected the backend and the frontend correctly to publish/edit/delet comments without needing to refresh the page.

**Additional files:**
- forms.py: Stores different ways to create forms using fields from models.py.
- 4 .js files: These files contains functions corresponding to each html document, where is possible to find the operation of the search bar and filter buttons of index.html, the running of comments of news.html and the page effects, used in all pages. 
- 5 .css files: Include the styles of the application, dividing between reset settings and variables, responsiveness, navigation menu, and forms and the general styles.

### Specification:
8News is a web application for desktop and mobile in which users can register as journalists for creating news happened throughout history. All visitors can search by keyword or filter by topic and enjoy the articles written by the registered users. Then, they can get an account to have the possibility of giving their opinion about it and saving thier favorite news at their *Readlists*. If after posting a comment they are not totally sure of the published text, they can edit or delete it with just a click. 

### How it runs:
**General view:**
In this page you can see all news, filter between topic, searching by keywords and save to your Readlist. 
https://dl.dropboxusercontent.com/s/4453qyhujk8kghh/8news_screenshot01.png?dl=0

**News page:**
This page shows the complete content of each news and all comments.
https://dl.dropboxusercontent.com/s/rdy637bs8n7hscz/8news_screenshot02.png?dl=0

**Comments:**
If are a logged user, you can post comments and then edit or delete them.
https://dl.dropboxusercontent.com/s/p5xcbzw4kevfkhm/8news_screenshot03.png?dl=0

**Readlist:**
This page stores your favorite articles, you can access to them whenever you want and delete it by clicking on the button.
https://dl.dropboxusercontent.com/s/1fxug95ayy2rgyq/8news_screenshot04.png?dl=0


### Thanks for your time!
Made by Javier All Varez at June 02, 2022.