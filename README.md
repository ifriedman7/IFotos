# Web Database & Information System Project

## Web Application Development for Online Photo Albums Service

	• Designed a server-side web application to provide users with online photo albums service, including viewing, deleting, editing, and uploading albums and photos using the web interface
	
	• Utilized programming languages and tools including MySQL to build SQL database; Python and Flask framework to build web infrastructure; and Jinja2 as the templating language; also designed front-end website using JavaScript, HTML, and CSS
	
	Originally cloned from StephenWeiXu/Webapp-Online-Album-Service
	Updated by Israel Ike Friedman for Python3 and MySQL 8.4
	
## How to deploy
### Initialize and mount database
Only needed if the database does not yet exist.
1. Mount a storage volume (e.g., EBS volume) to /data on the host
2. Install MySQL server 8.4 on the host.
3. cd db
4. Copy my.cnf to /etc on the host and restart MySQL server.
5. Connect to mysql and create the database and user.
```
mysql -uroot -hlocalhost -p
CREATE DATABASE IF NOT EXISTS IFotos;
CREATE USER IF NOT EXISTS 'ifotos' IDENTIFIED BY 'my_ifotos_password';
GRANT ALL PRIVILEGES ON IFotos.* TO 'ifotos';
source tbl_create.sql;
source load_data.sql;
```
If IFotos database already exists on the volume, just mount the volume to /data.

### Build and run database container
In IFotos/db directory:
```
docker buildx build --network=host --no-cache -t ifotosdb .
docker run -it --name ifotosdb --ipc=host --net=host --pid=host -v /data:/data -d ifotosdb
```
### Build and run webapp container
In IFotos directory:
```
docker buildx build --network=host --no-cache -t ifotos .
docker run -it --name ifotos --ipc=host --net=host --pid=host -d ifotos
```



