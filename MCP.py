from mcp.server.fastmcp import FastMCP
mcp=FastMCP("Calculator")
@mcp.tool()
def add(a: int, b: int):
    return a+b
@mcp.tool()
def subtract(a: int, b: int):
    return a-b
@mcp.tool()
def multiply(a: int, b: int):
    return a*b
@mcp.tool()
def divide(a: int, b:int):
    return a//b