import streamlit as st
import requests

API_URL = "https://groundwater-contamination-api.onrender.com"

st.set_page_config(
    page_title="Groundwater Risk Intelligence",
    page_icon="💧",
    layout="wide"
)

# ----------------------------
# Custom CSS
# ----------------------------
st.markdown("""
<style>
.main-title{
    font-size:32px;
    font-weight:700;
}
.card{
    padding:20px;
    border-radius:12px;
    background:#111827;
    border:1px solid #374151;
    text-align:center;
}
.risk-high{
    background:#dc2626;
    color:white;
    padding:6px 14px;
    border-radius:8px;
}
.risk-medium{
    background:#f59e0b;
    color:white;
    padding:6px 14px;
    border-radius:8px;
}
.risk-low{
    background:#10b981;
    color:white;
    padding:6px 14px;
    border-radius:8px;
}
</style>
""", unsafe_allow_html=True)

# ----------------------------
# Header
# ----------------------------
st.markdown(
    "<div class='main-title'>💧 Groundwater Contamination Risk Intelligence</div>",
    unsafe_allow_html=True
)

st.caption("AI Powered Water Risk Detection System")

st.divider()

# ----------------------------
# Sidebar Controls
# ----------------------------
st.sidebar.title("Controls")

# fetch example villages
try:
    examples = requests.get(f"{API_URL}/examples").json()
    villages = examples["example_villages"]
except:
    villages = []

selected = st.sidebar.selectbox(
    "Example Villages",
    [""] + villages
)

village = st.sidebar.text_input(
    "Enter Village Name",
    value=selected
)

predict_btn = st.sidebar.button("Predict Risk")

st.sidebar.divider()
st.sidebar.info("Powered by FastAPI + Clustering + Risk Ranking")

# ----------------------------
# Prediction
# ----------------------------
if predict_btn and village:

    with st.spinner("Analyzing groundwater contamination..."):

        try:
            response = requests.get(
                f"{API_URL}/predict",
                params={"village": village}
            )

            data = response.json()

        except:
            st.error("API connection failed")
            st.stop()

    # ----------------------------
    # Error handling
    # ----------------------------
    if "error" in data:
        st.error(data["error"])
        st.write("Try:")
        st.write(data.get("examples", []))
        st.stop()

    result = data["data"]

    # ----------------------------
    # Top Metrics
    # ----------------------------
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### Village")
        st.markdown(f"### {result['village']}")

    with col2:
        st.markdown("### Risk Level")

        risk = result["risk_level"]

        if "High" in risk:
            badge = "risk-high"
        elif "Medium" in risk:
            badge = "risk-medium"
        else:
            badge = "risk-low"

        st.markdown(
            f"<span class='{badge}'>{risk}</span>",
            unsafe_allow_html=True
        )

    with col3:
        st.markdown("### Cluster")
        st.markdown(f"### {result['cluster']}")

    st.divider()

    # ----------------------------
    # Contaminants
    # ----------------------------
    st.markdown("## Top Contaminants")

    contaminants = result["top_contaminants"]

    c1, c2, c3 = st.columns(3)

    def card(title, value):
        st.markdown(
            f"""
            <div class="card">
                <h4>{title}</h4>
                <h2>{value}</h2>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c1:
        card("Primary", contaminants[0])

    with c2:
        card("Secondary", contaminants[1])

    with c3:
        card("Tertiary", contaminants[2])

    st.divider()

    # ----------------------------
    # Risk Insight
    # ----------------------------
    st.markdown("## Risk Insight")

    if "High" in risk:
        st.error("Water unsafe for drinking. Immediate treatment required.")
    elif "Medium" in risk:
        st.warning("Moderate contamination detected. Use filtration.")
    else:
        st.success("Water quality within acceptable limits.")

# ----------------------------
# Footer
# ----------------------------
st.divider()
st.caption("Groundwater Risk Intelligence Platform • Production Deployment")