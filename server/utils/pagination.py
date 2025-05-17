from sqlalchemy import Select


def paginate(query: Select, page: int | None, size: int | None) -> Select:
    if size:
        query = query.limit(size)
        if page:
            query = query.offset((page - 1) * size)
    return query
