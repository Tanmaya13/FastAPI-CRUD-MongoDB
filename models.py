"""contains the structure of the collection (or table)"""

from pydantic import BaseModel

class DemoDB(BaseModel):
    name : str
    description : str