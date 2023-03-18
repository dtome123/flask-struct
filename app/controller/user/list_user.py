from app.dao.user import repository, model


def handle():
    return repository.list()
