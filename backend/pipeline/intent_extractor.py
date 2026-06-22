import os
import json

import google.generativeai as genai

from dotenv import load_dotenv

from schemas.intent_schema import IntentSchema


load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def extract_intent(user_prompt: str):

    prompt = f"""
You are an AI compiler intent extraction engine.

Your task:

Extract application requirements from the user request.

Rules:

1. Return ONLY valid JSON.
2. Never omit implicit roles.
3. If admin exists, automatically include user.
4. If role-based access exists, include roles.
5. Be deterministic.
6. Do not invent unnecessary features.

Output schema:

{{
 "app_type":"",
 "features":[],
 "roles":[],
 "business_rules":[]
}}

User Request:

{user_prompt}
"""

    response = model.generate_content(prompt)

    text = response.text.strip()

    if text.startswith("```"):
        text = text.replace("```json", "")
        text = text.replace("```", "")
        text = text.strip()

    data = json.loads(text)

    return IntentSchema(**data)