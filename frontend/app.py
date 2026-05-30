import streamlit as st
import requests

API_BASE_URL = "http://localhost:8000"

st.set_page_config(page_title="Academic Agent System", page_icon="📄", layout="wide")

st.title(" Academic Agent System: RAG & Document Review")

# Sidebar for PDF Upload
with st.sidebar:
    st.header("Upload Document")
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    if uploaded_file is not None:
        if st.button("Process Document"):
            with st.spinner("Uploading and processing..."):
                files = {"file": (uploaded_file.name, uploaded_file.getvalue(), "application/pdf")}
                response = requests.post(f"{API_BASE_URL}/upload", files=files)
                if response.status_code == 200:
                    st.success(f"Successfully processed {uploaded_file.name}!")
                    st.json(response.json())
                else:
                    st.error("Failed to process document.")

# Main Tabs
tab1, tab2 = st.tabs(["💬 Q&A (RAG)", "🔎 Document Review Analysis"])

with tab1:
    st.subheader("Ask questions about the document")
    user_query = st.text_input("Enter your question:")
    if st.button("Ask"):
        if user_query:
            with st.spinner("Generating answer..."):
                response = requests.post(f"{API_BASE_URL}/ask", params={"question": user_query})
                if response.status_code == 200:
                    answer = response.json().get("answer", "No answer found.")
                    st.markdown("### Answer")
                    st.info(answer)
                else:
                    st.error("Failed to get an answer.")
        else:
            st.warning("Please enter a question.")

with tab2:
    st.subheader("Generate Technical Review Report")
    st.markdown("Analyze the uploaded document for unsupported claims, missing assumptions, weak evidence, and overgeneralization.")
    if st.button("Generate Review"):
        with st.spinner("Analyzing document and generating report... (this might take a minute)"):
            response = requests.post(f"{API_BASE_URL}/review")
            if response.status_code == 200:
                report = response.json().get("review_report", "Failed to generate report.")
                st.markdown("### Technical Review Report")
                st.markdown(report)
            else:
                st.error("Failed to generate review report.")
