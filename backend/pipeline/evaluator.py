import json
import time
import sys

from pathlib import Path


# =====================
# Setup paths
# =====================

backend_path = Path(__file__).parent.parent

sys.path.append(str(backend_path))

dataset_path = (

    backend_path

    / "datasets"

    / "test_prompts.json"

)


# =====================
# Import pipeline
# =====================

from pipeline_controller import run_pipeline

from utils.retry_handler import execute_with_retry


# =====================
# Evaluation Function
# =====================

def evaluate_system():

    # Load prompts

    with open(

        dataset_path,

        "r",

        encoding="utf-8"

    ) as file:

        prompts = json.load(file)

    results = []

    total = len(prompts)

    success = 0

    total_latency = 0

    retries_used = 0

    failure_types = {}

    # Run every prompt

    for item in prompts:

        prompt = item["prompt"]

        start = time.time()

        try:

            output, retry_count = execute_with_retry(

                lambda: run_pipeline(prompt)

            )

            latency = round(

                time.time() - start,

                2

            )

            total_latency += latency

            retries_used += retry_count

            errors = output["validation_errors"]

            if len(errors) == 0:

                success += 1

            results.append(

                {

                    "prompt": prompt,

                    "status": "success",

                    "latency": latency,

                    "retries": retry_count,

                    "validation_errors": len(errors)

                }

            )

        except Exception as e:

            latency = round(

                time.time() - start,

                2

            )

            total_latency += latency

            error = str(e)

            # Categorize failures

            if "429" in error:

                failure_name = "api_rate_limit"

            else:

                failure_name = "pipeline_error"

            failure_types[

                failure_name

            ] = failure_types.get(

                failure_name,

                0

            ) + 1

            results.append(

                {

                    "prompt": prompt,

                    "status": "failed",

                    "latency": latency,

                    "retries": 0,

                    "error": error

                }

            )

    # =====================
    # Metrics
    # =====================

    metrics = {

        "total_prompts": total,

        "successful": success,

        "failed": total - success,

        "success_rate": round(

            (success / total) * 100,

            2

        ),

        "average_latency": round(

            total_latency / total,

            2

        ),

        "retries_used": retries_used,

        "failure_types": failure_types,

        "results": results

    }

    return metrics


# =====================
# Run directly
# =====================

if __name__ == "__main__":

    metrics = evaluate_system()

    print("\n===== Evaluation Report =====\n")

    print(

        f"Total Prompts: {metrics['total_prompts']}"

    )

    print(

        f"Successful: {metrics['successful']}"

    )

    print(

        f"Failed: {metrics['failed']}"

    )

    print(

        f"Success Rate: {metrics['success_rate']}%"

    )

    print(

        f"Average Latency: {metrics['average_latency']} sec"

    )

    print(

        f"Retries Used: {metrics['retries_used']}"

    )

    print("\nFailure Types:")

    print(

        metrics["failure_types"]

    )

    print("\n=============================")