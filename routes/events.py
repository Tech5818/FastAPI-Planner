from fastapi import APIRouter, Body, HTTPException, status
from models.events import Event

event_router = APIRouter(
  tags=["Events"]
)

events=[]

@event_router.get("/", response_model=list[Event])
async def retrieve_all_events() -> list[Event]:
  return events

@event_router.get("/{id}", response_model=Event)
async def retrieve_evnet(id: int) -> Event:
  for event in events:
    if event.id == id:
      return event
  raise HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="해당 ID를 가지는 이벤트는 존재하지 않습니다."
  )

@event_router.post("/new")
async def create_event(body: Event = Body(...)) -> dict:
  events.append(body)
  return {
    "message": "성공적으로 이벤트가 생성되었습니다."
  }

@event_router.delete("/{id}")
async def delete_event(id: int) -> dict:
  for event in events:
    if event.id == id:
      events.remove(event)
      return {
        "message": "해당 id를 가지는 이벤트를 성공적으로 삭제했습니다."
      }
  raise HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="해당 id를 가지는 이벤트는 존재하지 않습니다."
  )

@event_router.delete("/")
async def delete_all_event() -> dict:
  events.clear()
  return {
    "message": "이벤트들을 성공적으로 삭제하였습니다."
  }