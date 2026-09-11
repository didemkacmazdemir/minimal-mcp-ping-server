# Minimal MCP Ping Server

A tiny [Model Context Protocol](https://modelcontextprotocol.io/) server built with Python, UV, and FastMCP.

## Requirements

- Python 3.10+
- [UV](https://docs.astral.sh/uv/)

## Run

```sh
uv run server.py
```

The server communicates over stdio. It exposes one tool:

- `ping` returns `pong`

To inspect it interactively:

```sh
uv run mcp dev server.py
```

## References

- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [FastMCP documentation](https://py.sdk.modelcontextprotocol.io/)
