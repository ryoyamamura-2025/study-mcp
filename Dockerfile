# Python の公式の軽量イメージを使用します
FROM python:3.13-slim

# uv をインストールします
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# プロジェクトを /app にインストールします
COPY . /app
WORKDIR /app

# ステートメントとログメッセージがログにすぐに表示されるようにします
ENV PYTHONUNBUFFERED=1

# 依存関係をインストールします
RUN uv sync

EXPOSE $PORT

# FastMCP サーバーを実行します
CMD ["uv", "run", "python", "server.py"]