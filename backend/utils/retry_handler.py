import time


def execute_with_retry(function, retries=3):

    retry_count = 0

    for attempt in range(retries):

        try:

            result = function()

            return result, retry_count

        except Exception as e:

            error = str(e)

            if "429" in error:

                retry_count += 1

                wait = 65

                print(

                    f"Rate limit hit. Waiting {wait} seconds..."

                )

                time.sleep(wait)

            else:

                raise e

    raise Exception(

        "Max retries exceeded"

    )