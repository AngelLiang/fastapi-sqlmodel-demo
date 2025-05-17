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

## 流程

1、在数据库中设计好数据表后，使用sqlacodegen工具导出sqlmodel模型，然后放到server目录里，引入这个模型。

sqlacodegen示例：

```
uv run sqlacodegen --generator sqlmodels  mysql+pymysql://root:root@127.0.0.1:3306/fastapi_sqlmodel_demo?charset=utf8 > models.py
```

之后就可以对这些模型编写schema，再使用这些schema编写相关的接口。

## 注意

- 返回给前端的字段使用驼峰风格
- 如果报错需要抛出自定义错误
