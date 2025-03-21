FROM python:3.11

# 设置工作目录
WORKDIR /app

# 安装依赖工具（curl 用于下载 uv 安装脚本）
RUN apt-get update && apt-get install -y curl

# 下载并安装 uv
RUN curl -Ls https://astral.sh/uv/install.sh | bash

# 将 uv 添加到 PATH（默认安装在 ~/.local/bin）
ENV PATH="/root/.local/bin:$PATH"

# 复制代码
COPY . /app

# 使用 uv 安装项目依赖
RUN uv pip install --system --no-cache -r requirements.txt

# 启动 FastAPI 应用
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
