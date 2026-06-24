import json

from pipeline.evaluator import evaluate_system


metrics = evaluate_system()

with open(

    "metrics/evaluation_results.json",

    "w"

) as file:

    json.dump(

        metrics,

        file,

        indent=4

    )

print(metrics)