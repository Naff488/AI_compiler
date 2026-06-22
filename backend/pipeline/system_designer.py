from schemas.system_design_schema import SystemDesignSchema


def design_system(intent):

    features = intent["features"]

    roles = intent["roles"]

    pages = []

    entities = []

    flows = []

    if "login" in features:

        pages.append("login")

        flows.append("login_flow")

    if "dashboard" in features:

        pages.append("dashboard")

    if "contacts" in features:

        pages.append("contacts")

        entities.append("contact")

        flows.append("contact_flow")

    if "payments" in features:

        pages.append("payments")

        entities.append("subscription")

        flows.append("payment_flow")

    if "subscriptions" in features:

        entities.append("subscription")

    if "analytics" in features:

        pages.append("analytics")

    if roles:

        entities.append("user")

    return SystemDesignSchema(

        pages=list(set(pages)),

        entities=list(set(entities)),

        flows=list(set(flows)),

        roles=roles

    )