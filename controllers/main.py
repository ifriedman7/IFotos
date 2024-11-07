from flask import *
from .db import get_db

main = Blueprint('main', __name__, template_folder='templates')


@main.route('/')
def main_route():
	db = get_db()
	cur = db.cursor()

	query = "SELECT username FROM User"
	cur.execute(query)
	results = cur.fetchall() #results will be a tuple of tuples
	
	usernames = []
	for ele in results:
		usernames.append(ele[0])

	options = {
		"usernames": usernames
	}
	return render_template("index.html", **options)

