from schemas.app_schema import AppSchema

from pipeline.ui_generator import generate_ui

from pipeline.api_generator import generate_api

from pipeline.db_generator import generate_db

from pipeline.auth_generator import generate_auth


def generate_schema(system_design):

    pages = system_design["pages"]

    entities = system_design["entities"]

    roles = system_design["roles"]

    ui_schema = generate_ui(pages)

    api_schema = generate_api(entities)

    db_schema = generate_db(entities)

    auth_schema = generate_auth(

        roles,

        pages

    )

    return AppSchema(

        ui_schema=ui_schema,

        api_schema=api_schema,

        db_schema=db_schema,

        auth_schema=auth_schema

    )