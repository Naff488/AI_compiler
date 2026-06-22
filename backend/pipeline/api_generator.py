def generate_api(entities):

    endpoints = []

    methods = [

        "GET",

        "POST",

        "PUT",

        "DELETE"

    ]

    for entity in entities:

        for method in methods:

            endpoints.append({

                "path": f"/{entity}s",

                "method": method

            })

    return {

        "endpoints": endpoints

    }