from pydantic import BaseModel
from typing import List, Dict


class AppSchema(BaseModel):

    ui_schema: Dict

    api_schema: Dict

    db_schema: Dict

    auth_schema: Dict