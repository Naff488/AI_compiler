from pipeline.intent_extractor import extract_intent

from pipeline.normalizer import normalize_intent

from pipeline.system_designer import design_system

from pipeline.schema_generator import generate_schema

from pipeline.validator import validate_system

from pipeline.repair_engine import repair_system

from runtime.runtime_executor import execute_runtime


def run_pipeline(user_prompt):

    intent = extract_intent(user_prompt)

    intent_data = normalize_intent(

        intent.model_dump()

    )

    print("Normalized Intent")

    print(intent_data)

    system_design = design_system(

        intent_data

    )

    generated_schema = generate_schema(

        system_design.model_dump()

    )

    validation_errors = validate_system(

        system_design.model_dump(),

        generated_schema.model_dump()

    )
    repaired_schema = repair_system(

    validation_errors,

    generated_schema.model_dump()

    )
    runtime_output = execute_runtime(

    repaired_schema

    )

    return {

        "intent": intent_data,

        "system_design":

        system_design.model_dump(),

        "generated_schema":

        generated_schema.model_dump(),

        "validation_errors":

        validation_errors,

        "repaired_schema":
        
        repaired_schema,

        "runtime_output":

        runtime_output

    }