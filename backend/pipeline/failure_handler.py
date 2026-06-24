def handle_failures(intent):

    issues = []

    assumptions = []

    features = intent["features"]

    roles = intent["roles"]

    if len(features) < 2:

        issues.append(

            "Prompt is underspecified"

        )

    if "admin" not in roles:

        assumptions.append(

            "Created default admin role"

        )

        roles.append("admin")

    if "payments" in features and "subscriptions" not in features:

        assumptions.append(

            "Added subscriptions because payments exist"

        )

        features.append("subscriptions")

    return {

        "issues": issues,

        "assumptions": assumptions,

        "intent": intent

    }