from typing import List

from pydantic import BaseModel, create_model, ConfigDict


class ResponseOut(BaseModel):
    code: int
    message: str
    data: dict


def make_response_schema(data_schema: object, class_name: str = None):
    if not class_name:
        class_name = data_schema.__name__ + 'Response'
    response_schema_fields = {
        'code': (int, 0),
        'message': (str, 'success'),
        'data': (data_schema, None)
    }
    response_schema = create_model(
        class_name,
        __config__=None,
        __base__=BaseModel,
        __module__=BaseModel.__module__,
        __validators__={},
        **response_schema_fields
    )
    return response_schema


def make_records_response_schema(model_schema: object, class_name: str = None):
    """
    创建一个如下的类

    from ninja import Schema

    class UserListOut(Schema):
        class UserListOutData(Schema):
            records: List[UserSchema]
            total: int
            current: int
            size: int

        code :int = 0
        message: str = 'success'
        data: Data

    """
    if not class_name:
        class_name = model_schema.__name__ + 'ListResponse'
    data_schema_fields = {
        'records': (List[model_schema], None),
        'total': (int | None, None),
        'page': (int | None, None),
        'size': (int | None, None),
    }
    data_schema_name = class_name + 'Data'
    data_schema = create_model(
        data_schema_name,
        __config__=ConfigDict(arbitrary_types_allowed=True),
        __base__=BaseModel,
        __module__=BaseModel.__module__,
        __validators__={},
        **data_schema_fields,
    )
    response_schema = make_response_schema(data_schema, class_name)

    return response_schema


def to_camel_case(x):
    return ''.join(word.capitalize() if i > 0 else word.lower()
                   for i, word in enumerate(x.split('_')))
