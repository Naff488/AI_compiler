def generate_ui(pages):

    ui_pages = []

    for page in pages:

        ui_pages.append({

            "name": page,

            "layout": "default"

        })

    return {

        "pages": ui_pages

    }