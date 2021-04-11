from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import PlainTextResponse

from ..dependencies import get_token_header

router = APIRouter(
    prefix="/config", prefix,
    tags=["config"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found."}},
)

@router.get("/git-pull", response_class=PlainTextResponse)
def git_pull():
    t1 = subprocess.Popen("git --git-dir=/var/www/fastapi/.git --work-tree=/var/www/fastapi/ checkout -- /var/www/fastapi", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    t2 = subprocess.Popen("git --git-dir=/var/www/fastapi/.git --work-tree=/var/www/fastapi/ pull",stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    
    task_msg = {
        "task1": t1.communicate()[0],
        "task2": t2.communicate()[1]
    }
    return task_msg