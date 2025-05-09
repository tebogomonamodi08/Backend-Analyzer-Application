from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import FastAPI, Header
from starlette.requests import Request 
from starlette.responses import Response
import time

class LogMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        #Preprocessing
        start_time = time.perf_counter()
        log = {'method':request.method,
               'url':str(request.url)
               }
    
        response = await call_next(request)
        #post processing
        duration = round(time.perf_counter()-start_time,3)
        log['duration'] = duration
        print(log)
        return response

app = FastAPI()

@app.get('/')
async def get_this(token: str = Header(...)):
    return {token}


