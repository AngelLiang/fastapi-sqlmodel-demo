# fastapi-sqlmodel-demo

## 技术栈

- python
- uv
- fastapi
- sqlmodel
- mysql

## 目录说明

```
.
├── main.py              # 应用程序入口文件
├── pyproject.toml       # 项目依赖配置文件
├── uv.lock             # uv 包管理器锁定文件
├── .flake8             # flake8 代码风格检查配置
├── .python-version     # Python 版本配置文件
├── server/             # 服务器端代码目录
│   ├── __init__.py     # 包初始化文件
│   ├── database.py     # 数据库连接配置
│   ├── errors.py       # 自定义错误处理
│   ├── models.py       # 数据模型定义
│   ├── settings.py     # 项目配置
│   ├── user/           # 用户相关模块
│   └── utils/          # 工具函数目录
└── sh/                 # 脚本文件目录
```

## 开发流程

1、数据库设计 -> 导出模型 -> 实现服务

在数据库中设计好数据表后，使用sqlacodegen工具导出sqlmodel模型，然后放到server目录里，引入这个模型。

sqlacodegen示例：

```
uv run sqlacodegen --generator sqlmodels  mysql+pymysql://root:root@127.0.0.1:3306/fastapi_sqlmodel_demo?charset=utf8 > models.py
```

之后就可以对这些模型编写schema，再使用这些schema编写相关的接口。

## 注意

- 返回给前端的字段使用驼峰风格
- 如果报错需要抛出自定义错误


## 设计

1、HTTP响应需要包装一层，可以使用 utils/response.py中的make_response函数返回。

```
{
    "code": 0,
    "message": "success",
    "data": {}
}
```

2、如果需要配置swagger接口文档的响应数据结构，可以使用 utils/schemas.py中的make_response_schema方法，创建一个Response，然后赋值给路由的response_model参数，swagger接口文档就会显示对应的响应结构。

示例：

```
# schemas.py
class UserOut(User, table=False):
    class Config:
        from_attributes = True
        populate_by_name = True
        # 将下划线命名转换为驼峰命名
        alias_generator = to_camel_case


UserOutResponse = make_response_schema(UserOut)
UserListOutResponse = make_records_response_schema(UserOut)


# apis.py
@router.get('/user-list', response_model=UserListOutResponse)
async def get_user(db: AsyncSession = Depends(get_async_db), filter: UserFilterIn = Query()):
    ...
```
