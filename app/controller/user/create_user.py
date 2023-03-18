from app.dao.user import repository, model
from werkzeug.security import generate_password_hash


def handle(name, avatar, username, password, user_role):
    user = model.User(name=name, avatar=avatar, username=username,
                      password=generate_password_hash(password), user_role=user_role)
    return repository.create(user)
