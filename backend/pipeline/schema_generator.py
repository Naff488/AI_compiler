from schemas.app_schema import AppSchema


def generate_schema(system_design):

    pages = system_design["pages"]

    entities = system_design["entities"]

    roles = system_design["roles"]


    ui_schema = {

        "pages": []

    }

    for page in pages:

        ui_schema["pages"].append({

            "name": page

        })


    api_schema = {

        "endpoints": []

    }

    for entity in entities:

        api_schema["endpoints"].append({

            "path": f"/{entity}s",

            "method": "GET"

        })


    db_schema = {

        "tables": []

    }

    for entity in entities:

        db_schema["tables"].append({

            "name": f"{entity}s"

        })


    auth_schema = {

        "permissions": {}

    }

    for role in roles:

        auth_schema["permissions"][role] = pages


    return AppSchema(

        ui_schema=ui_schema,

        api_schema=api_schema,

        db_schema=db_schema,

        auth_schema=auth_schema

    )