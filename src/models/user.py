from utils import db

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    favorites = db.relationship('Favorites', backref='user', lazy=True)
    
    def serialize(self):
        return {
            self.id : id,
            self.nickname : nickname,
            self.email : email
        }
        
    def __repr__(self):
        return '<User %r>' % self.id