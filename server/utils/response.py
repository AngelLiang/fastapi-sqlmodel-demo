
def make_response(data=dict(), message='操作成功', code=200):
    return {
        'code': code,
        'message': message,
        'data': data
    }


def make_records_response(
    records,
    total: int | None = None,
    page: int | None = None,
    size: int | None = None
):
    return make_response(data={
        'records': records,
        'total': total,
        'page': page,
        'size': size
    })
