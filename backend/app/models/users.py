from app.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

class Users(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(100), unique = True, nullable = False)
	email = db.Column(db.String(120), unique = True, nullable = False)
	password = db.Column(db.String(255), nullable = False)
	fullname = db.Column(db.String(80), nullable = False)

	def check_password(self, password):
		return check_password_hash(self.password, password)
	
	def verify_password(user, password):
		if not user:
			return False
		
		return user.check_password(password)