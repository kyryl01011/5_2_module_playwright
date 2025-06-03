from pydantic import BaseModel, Field


class CustomerCreationModel(BaseModel):
    firstname: str
    lastname: str
    zipcode: str
