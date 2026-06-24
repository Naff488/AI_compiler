from pipeline.intent_extractor import extract_intent

from pipeline.normalizer import normalize_intent

from pipeline.enricher import enrich_intent

from pipeline.failure_handler import handle_failures

from pipeline.system_designer import design_system

from pipeline.schema_generator import generate_schema

from pipeline.validator import validate_system

from pipeline.repair_engine import repair_system

from runtime.runtime_executor import execute_runtime


def run_pipeline(user_prompt):

    # 1. Extract intent

    intent = extract_intent(

        user_prompt

    )

    # 2. Normalize

    intent_data = normalize_intent(

        intent.model_dump()

    )

    # 3. Enrich intent

    intent_data = enrich_intent(

        intent_data

    )

    # 4. Handle failures

    failure_result = handle_failures(

        intent_data

    )

    intent_data = failure_result[

        "intent"

    ]

    # 5. Design system

    system_design = design_system(

        intent_data

    )

    # 6. Generate schema

    generated_schema = generate_schema(

        system_design.model_dump()

    )

    # 7. Validate schema

    validation_errors = validate_system(

        system_design.model_dump(),

        generated_schema.model_dump()

    )

    # 8. Repair schema

    repaired_schema = repair_system(

        validation_errors,

        generated_schema.model_dump()

    )

    # 9. Execute runtime

    runtime_output = execute_runtime(

        repaired_schema

    )

    # 10. Create summary

    summary = {

        "pages": len(

            system_design.pages

        ),

        "entities": len(

            system_design.entities

        ),

        "roles": len(

            system_design.roles

        )

    }

    # 11. Return everything

    return {

        "summary":

        summary,

        "intent":

        intent_data,

        "system_design":

        system_design.model_dump(),

        "generated_schema":

        generated_schema.model_dump(),

        "validation_errors":

        validation_errors,

        "repaired_schema":

        repaired_schema,

        "runtime_output":

        runtime_output,

        "failure_analysis":

        {

            "issues":

            failure_result["issues"],

            "assumptions":

            failure_result["assumptions"]

        }

    }