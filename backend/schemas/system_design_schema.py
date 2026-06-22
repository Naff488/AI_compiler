from pydantic import BaseModel
from typing import List


class SystemDesignSchema(BaseModel):

    pages: List[str]

    entities: List[str]

    flows: List[str]

    roles: List[str]