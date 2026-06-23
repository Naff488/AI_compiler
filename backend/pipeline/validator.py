def validate_system(system_design, generated_schema):

    errors = []

    pages = system_design["pages"]

    entities = system_design["entities"]

    ui_pages = [

        page["name"]

        for page in generated_schema["ui_schema"]["pages"]

    ]

    db_tables = [

        table["name"]

        for table in generated_schema["db_schema"]["tables"]

    ]

    api_paths = [

        endpoint["path"]

        for endpoint in generated_schema["api_schema"]["endpoints"]

    ]

    # UI validation

    for page in pages:

        if page not in ui_pages:

            errors.append(

                f"Missing UI page: {page}"

            )

    # DB validation

    for entity in entities:

        table = f"{entity}s"

        if table not in db_tables:

            errors.append(

                f"Missing DB table: {table}"

            )

    # API validation

    for entity in entities:

        path = f"/{entity}s"

        if path not in api_paths:

            errors.append(

                f"Missing API endpoint: {path}"

            )

    return errors