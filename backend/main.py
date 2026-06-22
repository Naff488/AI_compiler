from pipeline_controller import run_pipeline


prompt = """
Build a CRM with login,
contacts, dashboard,
role-based access,
premium plan with payments.
Admins can see analytics.
"""


result = run_pipeline(prompt)

print(result)