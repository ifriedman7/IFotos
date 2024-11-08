from flask import Flask, render_template
import controllers
import os

# https://flask-mysql.readthedocs.io/en/latest/
# Initialize Flask app with the template folder address
app = Flask(__name__, template_folder='templates')

# Configure MySQL database connector
app.config['MYSQL_DATABASE_HOST'] = 'ifotosdb'
# default host is localhost
app.config['MYSQL_DATABASE_PORT'] = 3306
# default port is 3306
app.config['MYSQL_DATABASE_USER'] = 'ifotos'
app.config['MYSQL_DATABASE_PASSWORD'] = os.getenv('MYSQL_PASSWORD', '')
app.config['MYSQL_DATABASE_DB'] = 'IFotos'

# Register the controllers
app.register_blueprint(controllers.album)
app.register_blueprint(controllers.albums)
app.register_blueprint(controllers.pic)
app.register_blueprint(controllers.main)

# Listen on external IPs
# Listen to port 3000 so you can just run 'python app.py' to start the server
# For uwsgi, dont app.run or init_app. Comment out next 3 lines.
# mysql.init_app(app)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)

