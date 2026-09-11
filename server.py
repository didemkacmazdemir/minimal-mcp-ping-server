from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Ping Server")


@mcp.tool()
def ping() -> str:
    """Return a pong response."""
    return "pong"


if __name__ == "__main__":
    mcp.run()
