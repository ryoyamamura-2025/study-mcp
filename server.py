import asyncio
import logging
import os

from fastmcp import FastMCP

logger = logging.getLogger(__name__)
logging.basicConfig(format="[%(levelname)s]: %(message)s", level=logging.INFO)

mcp = FastMCP("MCP Server on Cloud run")

@mcp.tool()
def add(a: int, b: int) -> int:
   """これを使用して、2 つの数値を加算します。
   
   引数:
       a: 最初の数値。
       b: 2 番目の数値。
   
   戻り値:
       2 つの数値の合計。
   """
   logger.info(f">>> Tool: 'add' called with numbers '{a}' and '{b}'")
   return a + b

@mcp.tool()
def subtract(a: int, b: int) -> int:
   """これを使用して、2 つの数値を減算します。
   
   引数:
       a: 最初の数値。
       b: 2 番目の数値。
   
   戻り値:
       2 つの数値の差。
   """
   logger.info(f">>> Tool: 'subtract' called with numbers '{a}' and '{b}'")
   return a - b

if __name__ == "__main__":
   logger.info(f" MCP server started on port {os.getenv('PORT', 8080)}")
   # Cloud Run では、'sse' トランスポート、host="0.0.0.0" も使用できます。
   asyncio.run(
       mcp.run_async(
           transport="streamable-http",
           host="0.0.0.0",
           port=os.getenv("PORT", 8080),
       )
   )