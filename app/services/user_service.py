from app.models.user import User

from werkzeug.security import generate_password_hash, check_password_hash

class UserService:
    @staticmethod
    def create_user(username, email, password, fullname):
        from app import db
        user_exist = User.query.filter(
            (User.username == username) | (User.email == email)
        ).first()

        if(user_exist):
            return None, "User already exists"
        
        hashed_password = generate_password_hash(password)

        user = User(
            username = username,
            email = email,
            fullname = fullname,
            password = hashed_password
        )

        db.session.add(user)
        db.session.commit()

        return user, None
