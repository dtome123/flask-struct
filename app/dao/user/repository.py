from app.dao.user.model import User, session


def get_by_id(id):
    return session.query(User) \
        .filter(User.id == id) \
        .one()


def get_by_username(username):
    user = session.query(User) \
        .filter(User.username == username) \
        .first()

    return user


def create(user: User):
    session.add(user)
    session.commit()
    return user


def update(id, name, avatar, username, user_role):
    user = get_by_id(id)
    user.name = name
    user.avatar = avatar
    user.username = username
    user.user_role = user_role
    session.commit()

    return user


def list():
    return session.query(User).all()
