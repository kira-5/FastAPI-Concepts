"""Using External library - cachetools"""
# from fastapi import FastAPI
# from cachetools import TTLCache

# app = FastAPI()

# # Create a cache with a time-to-live (TTL) of 60 seconds.
# cache = TTLCache(maxsize=100, ttl=60)

# @app.get("/cached_endpoint")
# def cached_data():
#     # Check if the data is already in the cache.
#     if "cached_data" in cache:
#         print(True)
#         return cache["cached_data"]

#     # If not in the cache, calculate the data and store it in the cache.
#     data = {"message": "This data is cached."}
#     cache["cached_data"] = data
#     return data

"""Using Custom Middleware"""
# from fastapi import FastAPI, Request, Response
# from starlette.concurrency import iterate_in_threadpool
# import time

# app = FastAPI()

# # Create a cache with a time-to-live (TTL) of 60 seconds
# cache = {}    # cache = TTLCache(maxsize=100, ttl=60)


# @app.middleware("http")
# # Define your custom middleware class
# async def cache_middleware(request: Request, call_next):
#     # You can perform actions before handling the request here.
#     # For example, you could log the incoming request.
#     print(f"Received request: {request.method} {request.url}")
#     print(f"cache-Before: {cache}")
#     if request.method == "GET":
#         url = request.url.path
#         if url in cache:
#             print(True)
#             # If the response is in the cache, return it
#             cached_response = cache[url]
#             response = Response(content=cached_response["content"])
#             response.status_code = cached_response["status_code"]
#             return response

#     # Continue processing the request
#     response = await call_next(request)

#     # For example, you could log the response status code.
#     print(f"Response status code: {response.status_code}")

#     response_body = [chunk async for chunk in response.body_iterator]
#     response.body_iterator = iterate_in_threadpool(iter(response_body))
#     content = response_body[0].decode()
#     print(f"response_body={content}")

#     # Cache the response for GET requests
#     if request.method == "GET":
#         cache[request.url.path] = {
#             "status_code": response.status_code,
#             "content": content,
#         }
#     print(f"cache-After: {cache}")

#     return response


# @app.middleware("http")
# async def add_process_time_header(request: Request, call_next):
#     start_time = time.time()
#     response = await call_next(request)
#     process_time = time.time() - start_time
#     response.headers["X-Process-Time"] = str(process_time)
#     return response


# @app.get("/cached_endpoint")
# async def cache_this():
#     return {"message": "This response will be cached."}


"""Using Custom Dependecy"""
from fastapi import FastAPI, Depends, Request
from cachetools import TTLCache
from typing import Dict

app = FastAPI()

# Create a cache with a time-to-live (TTL) of 60 seconds
cache = TTLCache(maxsize=100, ttl=60)   # cache = {}


def cache_dependency(request: Request) -> Dict:
    # Include request-specific information if needed
    print(f"cache-Before: {cache}")
    url = request.url

    # Create a unique cache key based on the request and additional information
    cache_key = f"{url}"
    print(f"cache_key: {cache_key}")

    # Check if the data is already in the cache
    cached_data = cache.get(cache_key)
    print(cached_data)
    if cached_data:
        return cached_data

    # If not in the cache, calculate the data
    data = {"message": "Stored"}

    # Store the data in the cache for future requests
    cache[cache_key] = data
    print(f"cache-After: {cache}")

    return data


@app.get("/cache-endpoint")
async def cache_endpoint(cached_data: Dict = Depends(cache_dependency)):
    return cached_data


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
