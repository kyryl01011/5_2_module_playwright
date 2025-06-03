from pydantic import BaseModel


class CustomerCreationModel(BaseModel):
    firstname: str
    lastname: str
    zipcode: str
