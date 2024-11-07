from flask import *
from .db import get_db

pic = Blueprint('pic', __name__, template_folder='templates')


@pic.route('/pic')
def pic_route():
	db = get_db()
	cur = db.cursor()
	picid = request.args.get('id')
	if not check_pic_id(picid):
		abort(404)

	cur.execute("SELECT format FROM Photo WHERE picid=%s", [picid])
	results = cur.fetchall()
	format = results[0][0]

	cur = db.cursor()
	cur.execute("SELECT albumid FROM Contain WHERE picid=%s", [picid])
	results = cur.fetchall()
	albumid = results[0][0]

	cur = db.cursor()
	cur.execute("SELECT sequencenum FROM Contain WHERE picid=%s", [picid])
	results = cur.fetchall()
	sequencenum = results[0][0]

	if sequencenum > 0:
		cur = db.cursor()
		cur.execute("SELECT picid FROM Contain WHERE albumid=%s AND sequencenum=%s", (albumid, sequencenum-1))
		results = cur.fetchall()
		prev_picid = results[0][0]
	else:
		prev_picid = ""

	cur = db.cursor()
	cur.execute("SELECT picid FROM Contain WHERE albumid=%s AND sequencenum=%s", (albumid, sequencenum+1))
	results = cur.fetchall()
	if results:
		next_picid = results[0][0]
	else:
		next_picid = ""

	options = {
		"picid": picid,
		"format": format,
		"prev_picid": prev_picid,
		"next_picid": next_picid,
		"albumid": albumid
	}

	return render_template("pic.html", **options)


def check_pic_id(picid):
	db = get_db()
	cur = db.cursor()
	cur.execute("SELECT picid FROM Photo WHERE picid=%s", [picid])
	results = cur.fetchall()
	if results:
		return True
	return False

