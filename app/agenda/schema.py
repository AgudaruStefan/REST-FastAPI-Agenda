from pydantic import BaseModel, constr, validator


class AddContactSchema(BaseModel):
    name : constr(max_length=255, min_length=2)
    phone : constr(max_length=255, min_length=2)
    email : str

    @validator("email")
    def email_must_be_yonder(cls, value):
        if "@tss-yonder.com" not in value:
            raise ValueError("Only Yonder emails are allowed!")
        return value
    
    class Config:
        orm_mode = True

class UpdateContactSchema(BaseModel):
    name : constr(max_length=255, min_length=2)
    phone : constr(max_length=255, min_length=2)
    email : str

    @validator("email")
    def email_must_be_yonder(cls, value):
        if "@tss-yonder.com" not in value:
            raise ValueError("Only Yonder emails are allowed!")
        return value
    
    class Config:
        orm_mode = True