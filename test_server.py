import asyncio

from fastmcp import Client

async def test_server():
   # streamable-http トランスポートを使用して MCP サーバーをテストします。
   # sse トランスポートを使用する場合は「/sse」エンドポイントを使用します。
   async with Client("https://test-mcp-server-897239585193.us-central1.run.app/mcp") as client:
       # 利用可能なツールをリストします
       tools = await client.list_tools()
       for tool in tools:
           print(f">>> Tool found: {tool.name}")
       # 加算ツールを呼び出します
       print(">>>  Calling add tool for 1 + 2")
       result = await client.call_tool("add", {"a": 1, "b": 2})
       print(f"<<<  Result: {result.content[0].text}")
       # 減算ツールを呼び出します
       print(">>>  Calling subtract tool for 10 - 3")
       result = await client.call_tool("subtract", {"a": 10, "b": 3})
       print(f"<<< Result: {result.content[0].text}")

if __name__ == "__main__":
    asyncio.run(test_server())