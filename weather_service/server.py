from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")


@mcp.tool()
async def get_weather(city: str) -> str:
    """Получить погоду для города."""
    return f"Погода в {city} всегда отличная!"


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
