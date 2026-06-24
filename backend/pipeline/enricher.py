def enrich_intent(intent):

    features = intent["features"]

    roles = intent["roles"]

    business_rules = intent["business_rules"]

    # subscriptions -> payments

    if (
        "subscriptions" in features
        and "payments" not in features
    ):

        features.append(

            "payments"

        )

    # analytics -> admin

    analytics_exists = any(

        "analytics" in feature.lower()

        for feature in features

    )

    if (

        analytics_exists

        and "admin" not in roles

    ):

        roles.append(

            "admin"

        )

    intent["features"] = list(

        set(features)

    )

    intent["roles"] = list(

        set(roles)

    )

    intent["business_rules"] = business_rules

    return intent