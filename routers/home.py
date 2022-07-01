import sys
sys.path.append("..")
"""Trong routers folder luôn phải thêm line này đầu tiên"""

from fastapi import APIRouter, Depends
import models #da tao module rieng
from database import engine, SessionLocal
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from sqlalchemy.orm import Session


from fastapi import Form
from starlette import status
from starlette.responses import RedirectResponse

# router= APIRouter()
#todo: add tags and prefixes in our responses to our routers
router = APIRouter(
    prefix="/home",
    tags=["Home"],
    responses={401: {"homepage": "nothing"}}
)

models.Base.metadata.create_all(bind=engine)
templates= Jinja2Templates(directory="template")



def get_db(): #Du co access db session dc hay ko, thi cung close de do lai
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

#todo: Create api to mami_web.html
@router.get('/', response_class=HTMLResponse)
def read_home_page(request: Request):
    return templates.TemplateResponse("mami_web.html", {"request": request})

@router.post('/', response_class=HTMLResponse)
def send_message(request: Request, name: str = Form(...),
                 email: str = Form(...),subject: str = Form(...),
                 message: str = Form(...),db: Session = Depends(get_db)):
    content_model = models.ContentTable()
    content_model.hoten = name
    content_model.email = email
    content_model.topic = subject
    content_model.content = message

    db.add(content_model)
    db.commit()

    msg = "Message đã được gửi"
    return templates.TemplateResponse("mami_web.html", {"request": request, "msg": msg})
