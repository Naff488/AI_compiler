import json
import sys
from pathlib import Path

import streamlit as st

# Add backend folder to Python path

backend_path = Path(__file__).parent.parent / "backend"

sys.path.append(str(backend_path))

from pipeline_controller import run_pipeline


st.set_page_config(

    page_title="AI App Compiler",

    page_icon="🤖",

    layout="wide"

)

st.title("🤖 AI App Compiler")

st.write(

    "Natural Language → Structured Application Configuration"

)

user_prompt = st.text_area(

    "Enter your app idea",

    height=150,

    placeholder="Example: Build a CRM with login, contacts, dashboard, role-based access, and premium plan with payments. Admins can see analytics."

)

if st.button("Generate Application"):

    if user_prompt.strip() == "":

        st.warning(

            "Please enter a prompt."

        )

    else:

        with st.spinner(

            "Generating..."

        ):

            try:

                output = run_pipeline(

                    user_prompt

                )

                st.success(

                    "Generation complete!"

                )

                # Metrics

                col1, col2, col3 = st.columns(3)

                col1.metric(

                    "Pages",

                    len(

                        output["system_design"]["pages"]

                    )

                )

                col2.metric(

                    "Entities",

                    len(

                        output["system_design"]["entities"]

                    )

                )

                col3.metric(

                    "Roles",

                    len(

                        output["system_design"]["roles"]

                    )

                )

                # Intent

                st.subheader(

                    "📌 Intent"

                )

                st.json(

                    output["intent"]

                )

                # System Design

                st.subheader(

                    "📐 System Design"

                )

                st.json(

                    output["system_design"]

                )

                # Generated Schema

                st.subheader(

                    "🗄️ Generated Schema"

                )

                st.json(

                    output["generated_schema"]

                )

                # Validation

                st.subheader(

                    "🛠️ Validation Errors"

                )

                st.json(

                    output["validation_errors"]

                )

                # Runtime

                st.subheader(

                    "🔧 Runtime Output"

                )

                st.write(

                    output["runtime_output"]

                )

                # Failure Analysis

                st.subheader(

                    "⚠️ Failure Analysis"

                )

                st.json(

                    output["failure_analysis"]

                )

            except Exception as e:

                st.error(

                    str(e)

                )

