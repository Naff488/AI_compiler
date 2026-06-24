import os
import json

from google import genai
from dotenv import load_dotenv

from schemas.intent_schema import IntentSchema


load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def extract_intent(user_prompt: str):

    prompt = f"""
You are a STRICT compiler for application generation.

You are NOT a creative assistant.

Your task:

Extract application requirements from the user request.

Rules:

1. Return ONLY valid JSON.
2. Never omit implicit roles.
3. If admin exists, automatically include user.
4. If role-based access exists, include roles.
5. Be deterministic.
6. Do not invent unnecessary features.
7. Do NOT create new roles unless explicitly mentioned.
8. Do NOT create new pages unless explicitly required.
9. Do NOT create new entities unless directly implied.
10. Use the minimum viable architecture.
11. Use ONLY these canonical feature names when applicable:

login
dashboard
contacts
payments
subscriptions
analytics
shopping_cart
product_catalog
checkout_process
admin_dashboard

12. Never invent synonyms such as:
view cart
product browsing
add to cart
manage subscriptions

Convert them to canonical names.

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

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    text = response.text.strip()

    if text.startswith("```"):
        text = text.replace("```json", "")
        text = text.replace("```", "")
        text = text.strip()

    data = json.loads(text)

    return IntentSchema(**data)