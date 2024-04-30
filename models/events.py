# from pydantic import BaseModel
from sqlmodel import JSON, SQLModel, Field, Column
from typing import Optional


class Event(SQLModel, table=True):
  id: Optional[int] = Field(default=None, primary_key=True)
  title: str
  image: str
  description: str
  tags: list[str] = Field(sa_column=Column(JSON))
  locaiton: str

  model_config = {
    "json_schema_extra": {
      "example": {
        "title": "이벤트의 제목입니다",
        "image": "이벤트의 이미지로 .png 와 같은 이미지 링크가 옵니다",
        "description": "이벤트에 대한 설명입니다",
        "tags": ["이곳엔", "이벤트에", "대한", "Tag가", "옵니다"],
        "locaiton": "장소를 가리킵니다"
      }
    }
  }

class EventUpdate(SQLModel):
  title: Optional[str]
  image: Optional[str]
  description: Optional[str]
  tags: Optional[list[str]]
  location: Optional[str]

  model_config = {
    "json_schema_extra": {
      "example": {
        "title": "이벤트의 제목입니다",
        "image": "이벤트의 이미지로 .png 와 같은 이미지 링크가 옵니다",
        "description": "이벤트에 대한 설명입니다",
        "tags": ["이곳엔", "이벤트에", "대한", "Tag가", "옵니다"],
        "locaiton": "장소를 가리킵니다"
      }
    }
  }