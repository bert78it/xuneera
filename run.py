from fastapi import FastAPI, Response
from mediaflow_proxy.main import app as mediaflow_app  # Import mediaflow app
import httpx
import re
import string

# Initialize the main FastAPI application
main_app = FastAPI()

# Add HEAD and GET handlers for root path
@main_app.head("/")
async def head_root():
    return Response(status_code=200)

@main_app.get("/")
async def get_root():
    return Response(status_code=200)

# Manually add only non-static routes from mediaflow_app
for route in mediaflow_app.routes:
    if route.path != "/":  # Exclude the static file path
        main_app.router.routes.append(route)

# Run the main app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(main_app, host="0.0.0.0", port=8080)
