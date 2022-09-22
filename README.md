# API_portfolio_project

Endpoints:  

/users  
GET : Get single user's information  : /users/id  
GET : Get all users and their information  : /users  
PATCH/PUT : Update user info (One or all of the following :password, username, email)  : /users/id  
DELETE : Delete user  : /users/id  
POST : Create new user  : /users  
  
/stocks  
POST : add new stock  : /stocks  
PUT : update stock information by web scraping  : /stocks/id  
DELETE : delete stock  : /stocks/id  
GET : get single stock's information  : /stocks/id  
GET : get all stocks' information  : /stocks  

/portfolios  
DELETE : delete portfolio  : /portfolios/id
POST : add new portfolio  : /portfolios
GET : get single portfolio  : /portfolios/id
GET : get all portfolios  : /portfolios

