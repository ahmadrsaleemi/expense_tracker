from app.models.users import Users

from werkzeug.security import generate_password_hash, check_password_hash

class UserService:
    @staticmethod
    def create_user(username, email, password):
        from app import db
        user_exist = Users.query.filter(
            (Users.username == username) | (Users.email == email)
        ).first()

        if(user_exist):
            return None, "User already exists"
        
        hashed_password = generate_password_hash(password)

        user = Users(
            username = username,
            email = email,
            password = hashed_password
        )

        db.session.add(user)
        db.session.commit()

        return user, None
    
    @staticmethod
    def get_by_email(email):
        from app import db
        if not email:
            return None
        
        user_exist = Users.query.filter(
            (Users.email == email)
        ).first()

        return user_exist