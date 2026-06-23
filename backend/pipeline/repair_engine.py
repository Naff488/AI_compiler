def repair_system(

    validation_errors,

    generated_schema

):

    repaired = generated_schema.copy()

    for error in validation_errors:

        if "Missing API endpoint:" in error:

            path = error.split(": ")[1]

            repaired["api_schema"]["endpoints"].append(

                {

                    "path": path,

                    "method": "GET"

                }

            )

        if "Missing DB table:" in error:

            table = error.split(": ")[1]

            repaired["db_schema"]["tables"].append(

                {

                    "name": table

                }

            )

    return repaired