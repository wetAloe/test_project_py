from typing_extensions import Self

from pydantic import BaseModel, field_validator, model_validator, ValidationInfo
from fastapi.exceptions import RequestValidationError


class ImageBase(BaseModel):
    data: list[int]


class ImageIn(ImageBase):
    pass


class ImageOut(ImageBase):
    id: int

    model_config = {"from_attributes": True}


class ImagesRange(BaseModel):
    min_depth: int
    max_depth: int

    @model_validator(mode='after')
    def check_passwords_match(self) -> Self:
        if self.min_depth >= self.max_depth:
            raise RequestValidationError('`min_depth` must be less than `max_depth`')
        return self

    @field_validator("min_depth", "max_depth", mode="after")
    @classmethod
    def validate_min_depth(cls, v: int, info: ValidationInfo):
        if v <= 0:
            raise RequestValidationError(f"`{info.field_name}` must be greater than 0")
        return v
