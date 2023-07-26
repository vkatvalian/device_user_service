# device_user_service

for the subscriptions service :

# create table sub_plan(id INTEGER primary key, currency text, company text);

# insert into sub_plan values (1, 'dollar', 'apple'), (2, 'amd', 'samsung'), (3, 'euro', 'pinephone');

# create table subscriber(sub_id integer not null, user_id integer not null);

for the auth service it will create a table on application level.

uses uvicorn :

``` 
cd subscriptions

uvicorn main:app --host localhost --port 8080
```


```

cd auth

uvicorn main:app

````

### PLEASE NOTE:

1. uses hardcoded subscription plans, uses directories for deciding
2. issue with processing data but its a showcase of how I will manage the connection between the services
3. hardcoded sql queries but works as a showcase of using ORM and raw sql queries + needs to get data through the loop but uses hardcoded indexing
4. all connection/engine parts are global but needs to be wrapped and needs to have a session for the better queries, session management etc
5. several things are broken, f.e. will add several list of users inside the sub_plan table but didn't have time to fix that bug. But it should have NOT NULL fields and needs to use UPDATE when there are already rows for that subscriptions.
6. on production will use another methods for the proxy instead of httpx and hardcoded urls
7. hardcoded urls for the database connections as well, needs to be inside .env variables
