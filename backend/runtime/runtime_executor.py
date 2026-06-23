import os
import json


def execute_runtime(schema):

    output_dir = "output"

    os.makedirs(output_dir, exist_ok=True)

    # Save config

    with open(

        f"{output_dir}/config.json",

        "w"

    ) as file:

        json.dump(

            schema,

            file,

            indent=4

        )

    # Generate pages

    pages = schema["ui_schema"]["pages"]

    for page in pages:

        page_name = page["name"]

        with open(

            f"{output_dir}/{page_name}.html",

            "w"

        ) as file:

            file.write(

                f"""

<html>

<head>

<title>{page_name}</title>

</head>

<body>

<h1>{page_name}</h1>

</body>

</html>

"""

            )

    return output_dir