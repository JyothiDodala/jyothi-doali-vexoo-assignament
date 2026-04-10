import streamlit as st
from bonus_router import detect_query_type, math_module, legal_module, medical_module, general_module

# =========================
# ROUTER FUNCTION
# =========================
def route_query(query):
    module, confidence = detect_query_type(query)

    if "Math" in module:
        response = math_module(query)
    elif "Legal" in module:
        response = legal_module(query)
    elif "Medical" in module:
        response = medical_module(query)
    else:
        response = general_module(query)

    return module, confidence, response


# =========================
# STREAMLIT UI
# =========================

st.set_page_config(page_title="Smart Query Router", layout="centered")

st.title("🤖 Smart Query Router")
st.markdown("### AI-based Reasoning-Aware System")

query = st.text_input("💬 Enter your query:")

if st.button("Submit"):

    if query:
        module, confidence, response = route_query(query)

        st.divider()

        # RESULT SECTION
        st.subheader("📊 Result")

        col1, col2 = st.columns(2)

        with col1:
            st.info(f"**Module:** {module}")
        with col2:
            st.success(f"**Confidence:** {int(confidence * 100)}%")

        st.write(f"**Query:** {query}")

        st.subheader("💡 Response")
        st.write(response)

    else:
        st.warning("Please enter a query!")