from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from observer import db, app
from observer.api.users.model.user_role import user_role
from observer.api.users.model.role import Role

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    name = db.Column(db.String(255))
    avatar = db.Column(db.String(255))
    introduction = db.Column(db.String(255))
    email = db.Column(db.String(255))
    phone = db.Column(db.String(255))
    salt = db.Column(db.String(5))
    roles = db.relationship('Role', secondary=user_role, backref=db.backref('users', lazy='dynamic'))

    # 获取token，有效时间30min
    def generate_auth_token(self, expiration=1800):
        s = Serializer(app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'id': self.id})

    def serialize(self):
        roles = []
        if None != self.roles:
            for role in self.roles:
                roles.append(role.role_name)
        
        return {
            'id'          : self.id,
            'username'    : self.username,
            'name'        : self.name,
            'avatar'      : self.avatar,
            'introduction': self.introduction,
            'email'       : self.email,
            'phone'       : self.phone,
            'roles'       : roles
        }