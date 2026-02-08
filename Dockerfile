FROM python:3.11-slim

WORKDIR /app

# Install dependencies first (for layer caching)
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files and install the package
COPY pyproject.toml README.md ./
COPY src/ ./src/
COPY .github/core/ ./.github/core/
RUN pip install --no-cache-dir .

EXPOSE 8000

# Dedalus MCP server (Streamable HTTP on 0.0.0.0:8000/mcp)
CMD ["python", "-m", "alpaca_mcp_server.dedalus_server"]
