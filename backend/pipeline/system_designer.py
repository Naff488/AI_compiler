from schemas.system_design_schema import SystemDesignSchema


def design_system(intent):

    features = intent["features"]

    roles = intent["roles"]

    pages = []

    entities = []

    flows = []

    # ----------------
    # Feature aliases
    # ----------------

    alias_map = {

        # Login

        "authentication": "login",

        "user authentication": "login",

        # Cart

        "shopping cart": "shopping_cart",

        "shopping_cart": "shopping_cart",

        "cart": "shopping_cart",

        "view cart": "shopping_cart",

        "add to cart": "shopping_cart",

        "remove from cart": "shopping_cart",

        # Products

        "product": "product_catalog",

        "products": "product_catalog",

        "product catalog": "product_catalog",

        "product_catalog": "product_catalog",

        "product management": "product_catalog",

        "product_management": "product_catalog",

        "product browsing": "product_catalog",

        # Checkout

        "checkout": "checkout_process",

        "checkout process": "checkout_process",

        "checkout_process": "checkout_process",

        "checkout & payments": "checkout_process",

        "checkout and payment processing": "checkout_process",

        # Payments

        "payment integration": "payments",

        "payment processing": "payments",

        "payments integration": "payments",

        # Subscriptions

        "subscription": "subscriptions",

        "subscriptions management": "subscriptions",

        "subscription management": "subscriptions",

        "manage subscriptions": "subscriptions",

        "manage subscriptions (user)": "subscriptions",

        "subscription management (admin)": "subscriptions",

        # Analytics

        "analytics reporting": "analytics",

        "reporting and analytics": "analytics",

        # Admin

        "admin dashboard": "admin_dashboard",

        "admin_dashboard": "admin_dashboard",

    }

    # ----------------
    # Normalize features
    # ----------------

    normalized_features = []

    for feature in features:

        feature = feature.lower().strip()

        feature = alias_map.get(

            feature,

            feature

        )

        if feature not in normalized_features:

            normalized_features.append(

                feature

            )

    features = normalized_features

    # ----------------
    # Auto rules
    # ----------------

    if (

        "checkout_process" in features

        and "payments" not in features

    ):

        features.append(

            "payments"

        )

    if (

        "shopping_cart" in features

        and "product_catalog" not in features

    ):

        features.append(

            "product_catalog"

        )

    # ----------------
    # Pages
    # ----------------

    feature_page_map = {

        "login": "login",

        "dashboard": "dashboard",

        "contacts": "contacts",

        "payments": "payments",

        "subscriptions": "subscriptions",

        "analytics": "analytics",

        "shopping_cart": "cart",

        "product_catalog": "products",

        "checkout_process": "checkout",

        "admin_dashboard": "admin_dashboard",

    }

    for feature in features:

        if feature in feature_page_map:

            page = feature_page_map[feature]

            if page not in pages:

                pages.append(

                    page

                )

    # ----------------
    # Entities
    # ----------------

    if "contacts" in features:

        entities.append(

            "contact"

        )

    if "shopping_cart" in features:

        entities.append(

            "cart"

        )

    if "product_catalog" in features:

        entities.append(

            "product"

        )

    if "checkout_process" in features:

        entities.append(

            "order"

        )

    if "subscriptions" in features:

        entities.append(

            "subscription"

        )

    # DO NOT ADD ADMIN

    if "user" not in entities:

        entities.append(

            "user"

        )

    # ----------------
    # Flows
    # ----------------

    if "login" in features:

        flows.append(

            "login_flow"

        )

    if "contacts" in features:

        flows.append(

            "contact_flow"

        )

    if "payments" in features:

        flows.append(

            "payment_flow"

        )

    if "checkout_process" in features:

        flows.append(

            "checkout_flow"

        )

    if "shopping_cart" in features:

        flows.append(

            "cart_flow"

        )

    return SystemDesignSchema(

        pages=pages,

        entities=entities,

        flows=flows,

        roles=roles

    )