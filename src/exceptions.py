from fastapi import status
from fastapi.exceptions import HTTPException


class EntityDoesNotExistException(HTTPException):
    def __init__(self, detail: str = "Entity does not exist."):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail)
