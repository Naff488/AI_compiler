from pipeline.intent_extractor import extract_intent

from pipeline.normalizer import normalize_intent

from pipeline.system_designer import design_system

from pipeline.schema_generator import generate_schema


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

    return {

        "intent": intent_data,

        "system_design": system_design.model_dump(),

        "generated_schema":

        generated_schema.model_dump()

    }