from fastapi import APIRouter, HTTPException, status
from models.users import User, UserSignIn

user_router = APIRouter(
  tags=["User"]
)

users = {}

@user_router.post("/signup")
async def sign_new_user(data: User) -> dict:
  if data.email in users:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail="해당 이메일을 가진 유저는 존재합니다."
    )
  users[data.email] = data
  return {
    "message": "유저가 성공적으로 생성되었습니다."
  }

@user_router.post("/signin")
async def sign_user_in(user: UserSignIn) -> dict:
  if user.email not in users:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail="해당 이메일을 가지는 유저는 존재하지 않습니다."
    )
  if users[user.email].password != user.password:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail="잘못된 비밀번호 입니다."
    )
  
  return {
    "message": "로그인이 성공적으로 되었습니다."
  }