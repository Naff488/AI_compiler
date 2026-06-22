REQUIRED_KEYS = [
    "app_type",
    "features",
    "roles",
    "business_rules"
]


def validate_intent(data):

    errors = []

    for key in REQUIRED_KEYS:

        if key not in data:

            errors.append(
                f"Missing key: {key}"
            )

    return errors