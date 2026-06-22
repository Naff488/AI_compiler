FEATURE_MAP = {

    "authentication": "login",

    "contact management": "contacts",

    "contact_management": "contacts",

    "role-based access control": "role_access",

    "role_based_access_control": "role_access",

    "subscription management": "subscriptions",

    "subscription_management": "subscriptions",

    "payment processing": "payments",

    "payment_processing": "payments",

    "dashboard": "dashboard",

    "analytics": "analytics"

}


def normalize_intent(intent):

    normalized_features = []

    for feature in intent["features"]:

        feature = feature.lower().strip()

        normalized_features.append(

            FEATURE_MAP.get(

                feature,

                feature

            )

        )

    normalized_roles = []

    for role in intent["roles"]:

        normalized_roles.append(

            role.lower().strip()

        )

    intent["features"] = normalized_features

    intent["roles"] = normalized_roles

    return intent