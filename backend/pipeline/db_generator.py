def generate_db(entities):

    tables = []

    for entity in entities:

        tables.append({

            "name": f"{entity}s"

        })

    return {

        "tables": tables

    }