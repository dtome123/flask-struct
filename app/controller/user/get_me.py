from app.dao.user import repository, model


def handle(id):
    return repository.get_by_id(id)
