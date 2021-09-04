docker exec -it mongo-db bash
mongo -u admin -p
use mydb
db.createUser({user: 'apiuser', pwd: 'apipassword', roles: [{role: 'readWrite', db: 'mydb'}]})