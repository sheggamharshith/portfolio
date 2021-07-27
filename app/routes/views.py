from fastapi import  Request, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

import json 



router = APIRouter()


templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
def read_item(request: Request):

    projects_file = open('app/apis/portfolio/projectsInfo.json')
    company_file = open('app/apis/portfolio/company.json')

    return templates.TemplateResponse(
        "home_page.html",
        {
            "projects": json.load(projects_file),
            'companies': json.load(company_file),
            "request": request,
        },
    )

@router.get("/project/{id}", response_class=HTMLResponse)
def read_item(request: Request,id:int):

    try:
        projects_file = open('app/apis/portfolio/projectsInfo.json')
        project = json.load(projects_file)[id]
        return templates.TemplateResponse(
            "project_info.html",
            {
                "project": project,
                "request": request,
                'id':id
            }
        )
    except IndexError as e:
        return templates.TemplateResponse(
            "project_info.html",
            {
                "request": request,
                "error":"404 Not Found"
            }
        )


