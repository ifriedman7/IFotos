from flask import Flask, render_template

from extensions import mysql
import controllers

# Initialize Flask app with the template folder address
app = Flask(__name__, template_folder='templates')

# Initialize MySQL database connector
#app.config['MYSQL_HOST'] = 'localhost'
#app.config['MYSQL_USER'] = 'root'
#app.config['MYSQL_PASSWORD'] = 'IFotos12#'
#app.config['MYSQL_DB'] = 'IFotos'
#app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

#https://flask-mysql.readthedocs.io/en/latest/
#app.config['MYSQL_DATABASE_HOST'] = 'ifotos-deployer.servebeer.com'
#default host is localhost
app.config['MYSQL_DATABASE_PORT'] = 3306
#default port is 3306
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'IFotos12#'
app.config['MYSQL_DATABASE_DB'] = 'IFotos'
mysql.init_app(app)

# Register the controllers
app.register_blueprint(controllers.album)
app.register_blueprint(controllers.albums)
app.register_blueprint(controllers.pic)
app.register_blueprint(controllers.main)

# Listen on external IPs
# For us, listen to port 3000 so you can just run 'python app.py' to start the server
if __name__ == '__main__':
    # listen on external IPs
    app.run(host='0.0.0.0', port=3000, debug=True)
