def generate_auth(roles, pages):

    permissions = {}

    for role in roles:

        if role == "admin":

            permissions[role] = pages

        else:

            permissions[role] = [

                page

                for page in pages

                if page != "analytics"

            ]

    return {

        "permissions": permissions

    }