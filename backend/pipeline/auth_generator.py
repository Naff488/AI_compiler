def generate_auth(roles, pages):

    permissions = {}

    for role in roles:

        # ----------------
        # Admin
        # ----------------

        if role == "admin":

            permissions[role] = pages.copy()

        # ----------------
        # Premium User
        # ----------------

        elif role == "premium_user":

            permissions[role] = [

                page

                for page in pages

                if page not in [

                    "analytics",

                    "admin_dashboard"

                ]

            ]

            if (

                "subscriptions" in pages

                and "subscriptions"

                not in permissions[role]

            ):

                permissions[role].append(

                    "subscriptions"

                )

        # ----------------
        # Normal User
        # ----------------

        else:

            permissions[role] = [

                page

                for page in pages

                if page not in [

                    "analytics",

                    "subscriptions",

                    "admin_dashboard"

                ]

            ]

    return {

        "permissions": permissions

    }