from re import sub

from pydantic import BaseModel


def to_camel(string):
    s = sub(r'([_\-])+', " ", string).title().replace(" ", "")
    return ''.join([s[0].lower(), s[1:]])


class BaseModelo(BaseModel):
    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True
