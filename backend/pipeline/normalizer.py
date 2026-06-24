FEATURE_MAP = {

    # Authentication

    "authentication": "login",

    "user authentication": "login",

    "user_authentication": "login",

    "login": "login",

    # Contacts

    "contact management": "contacts",

    "contact_management": "contacts",

    "contacts_management": "contacts",

    "contacts": "contacts",

    # Dashboard

    "dashboard": "dashboard",

    # Role Access

    "role-based access control": "role_access",

    "role_based_access_control": "role_access",

    "role-based access": "role_access",

    "role based access": "role_access",

    # Subscriptions

    "subscription management": "subscriptions",

    "subscription_management": "subscriptions",

    "subscription": "subscriptions",

    "subscriptions": "subscriptions",

    "premium plan": "subscriptions",

    "premium_plan": "subscriptions",

    # Payments

    "payment processing": "payments",

    "payment_processing": "payments",

    "payment": "payments",

    "payments": "payments",

    # Analytics

    "analytics": "analytics",

    "reporting": "analytics",

    "reporting & analytics": "analytics",

    "reporting_and_analytics": "analytics",

    "analytics_viewing": "analytics",

    "analytics reporting": "analytics",

    "analytics_reporting": "analytics",
    
    "analytics reports": "analytics",

    "reporting analytics": "analytics",

    # E-commerce

    # E-commerce

    "shopping cart": "shopping_cart",

    "shopping_cart": "shopping_cart",

    "cart": "shopping_cart",
 
    "checkout process": "checkout_process",

    "checkout_process": "checkout_process",

    "checkout": "checkout_process",

    "payment integration": "payments",

    "admin dashboard": "admin_dashboard",

    "admin_dashboard": "admin_dashboard",

    "product catalog": "product_catalog",

    "product_catalog": "product_catalog",

    "product management (admin)": "product_management",

    "order management (admin)": "order_management",

    "user management (admin)": "user_management",


}


def normalize_intent(intent):

    normalized_features = []

    normalized_roles = []

    # ------------------
    # Normalize features
    # ------------------

    for feature in intent["features"]:

        feature = feature.lower().strip()

        feature = FEATURE_MAP.get(

            feature,

            feature

        )

        if feature not in normalized_features:

            normalized_features.append(

                feature

            )

    # ------------------
    # Normalize roles
    # ------------------

    for role in intent["roles"]:

        role = role.lower().strip()

        role = role.replace(

            " ",

            "_"

        )

        if role not in normalized_roles:

            normalized_roles.append(

                role

            )

    # ------------------
    # Auto rules
    # ------------------

    # subscriptions <-> payments

    if (

        "subscriptions" in normalized_features

        and "payments" not in normalized_features

    ):

        normalized_features.append(

            "payments"

        )

    if (

        "payments" in normalized_features

        and "subscriptions" not in normalized_features

    ):

        normalized_features.append(

            "subscriptions"

        )

    # analytics -> admin

    if (

        "analytics" in normalized_features

        and "admin" not in normalized_roles

    ):

        normalized_roles.append(

            "admin"

        )

    # admin -> user

    if (

        "admin" in normalized_roles

        and "user" not in normalized_roles

    ):

        normalized_roles.append(

            "user"

        )

    # subscriptions -> premium_user

    if (

        "subscriptions" in normalized_features

        and "premium_user" not in normalized_roles

    ):

        normalized_roles.append(

            "premium_user"

        )

    # Update intent

    intent["features"] = normalized_features

    intent["roles"] = normalized_roles

    return intent