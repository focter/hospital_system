# 医院管理系统

这是一个基于 Flask 开发的简单医院管理示例程序，提供医生登录、病人管理、医生管理、病房管理和科室管理等功能。

## 环境准备

1. **Python 版本**：建议使用 Python 3.8 及以上。
2. **依赖安装**：

```bash
python3 -m venv venv
source venv/bin/activate
pip install Flask Flask-SQLAlchemy PyMySQL
```

3. **数据库**：需要本地安装 MySQL，并创建名为 `hospital_db` 的数据库。默认连接配置在 `app.py` 中：

```
mysql+pymysql://root:123456@localhost/hospital_db
```

如需修改用户名或密码，可编辑 `app.py` 中的 `SQLALCHEMY_DATABASE_URI`。

## 运行方式

1. 在项目根目录执行：

```bash
python app.py
```

2. 首次运行时会自动在数据库中创建所需的表。
3. 打开浏览器访问 [http://localhost:5000](http://localhost:5000)，进入医生登录界面。

## 功能简介

- **医生登录/登出**：`login.py`
- **病人管理**：`patient_routes.py`
- **医生管理**：`doctor_routes.py`
- **病房管理**：`room_routes.py`
- **科室管理**：`department_routes.py`

各功能的页面模板位于 `templates/` 目录，界面语言为中文。

## 目录结构

```
app.py                # 应用入口
models.py             # 数据库模型
login.py              # 登录相关路由
patient_routes.py     # 病人相关路由
doctor_routes.py      # 医生相关路由
room_routes.py        # 病房相关路由
department_routes.py  # 科室相关路由
templates/            # HTML 模板
```

启动后即可在浏览器中进行相应的增删改查操作。
