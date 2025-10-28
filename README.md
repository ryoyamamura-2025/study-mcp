# Deploy MCP server on Cloud run
Cloud run にテスト用 MCP サーバーをデプロイする勉強用リポジトリ


このプロジェクトは、FastMCPライブラリを使用して構築されたMCP（Microservice Communication Protocol）サーバーをGoogle Cloud Runにデプロイするためのものです。加算と減算の機能を持つシンプルなマイクロサービスを提供します。


## プロジェクトの構成

- `deploy.sh`: Cloud Runにサービスをデプロイするためのシェルスクリプト。
- `Dockerfile`: FastMCPサーバーのDockerイメージを構築するための設定ファイル。
- `pyproject.toml`: Pythonプロジェクトの依存関係と設定を管理するためのPoetry設定ファイル。
- `server.py`: `fastmcp`ライブラリを使用してMCPサーバーのロジックを実装。`add`と`subtract`ツールを提供します。
- `test_server.py`: `server.py`で定義されたMCPサーバーのテストコード。
- `uv.lock`: プロジェクトの依存関係をロックするためのファイル。

## 環境構築方法
```
git clone XXX
cd XXX
uv sync
```

## デプロイ方法

1. `deploy.sh`内の`PROJECT_ID`, `REGION`, `SERVICE_NAME`, `MEMORY`の変数を環境に合わせて更新します。
2. Google Cloud SDKがインストールされ、認証されていることを確認します。
3. `deploy.sh`スクリプトを実行して、Cloud Runにサービスをデプロイします。

