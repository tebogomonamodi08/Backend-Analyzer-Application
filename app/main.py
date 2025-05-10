from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from fastapi import FastAPI


class LogMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        #preprocess logic 
        client_ip = request.client.host
        
        response = await call_next(request)
        status_code = response.status_code

        with open('log.txt','a') as file_obj:
            file_obj.write(f'Client IP Adress: {client_ip}, Status code: {status_code}')
        return response
        #postprocess logic


app = FastAPI()
app.add_middleware(LogMiddleware)

@app.get('/')
async def get_this():
    return 'A file should be make'