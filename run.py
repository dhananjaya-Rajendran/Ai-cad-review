"""Application Startup Script for AI CAD Review Server"""
import sys
import uvicorn

from app.config import APP_ENV, HOST, PORT

if __name__ == "__main__":
    port = PORT
    host = HOST
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            pass
    print(f"Starting AI CAD Review server on http://{host}:{port} ...")
    uvicorn.run(
        "app.main:app",
        host=host,
        port=port,
        log_level="info",
        reload=APP_ENV.lower() == "development",
    )
