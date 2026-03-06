FROM python:3.11-slim

WORKDIR /app

# 复制并安装依赖
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 安装 Gunicorn
RUN pip install gunicorn  # 确保安装 Gunicorn

# 复制应用代码
COPY app.py db.py ./

# 公开容器内的 5001 端口
EXPOSE 5001

# 使用 Gunicorn 启动 Flask 应用，并绑定到 5001 端口
CMD ["gunicorn", "--bind", "0.0.0.0:5001", "app:app"]