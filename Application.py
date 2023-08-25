import streamlit as st
from LangChainAPi import return_proposal
import time

def main():
    st.title(":green[Upwork] :blue[Proposal] Writer")

    st.caption("Seller Details")
    # Adding top Fields
    col1, col2, col3 = st.columns(3, gap="medium")
    with col1:
        name = st.text_input("Your Name", value="")
    with col2:
        experience = st.text_input("Your Experience", value="")
    with col3:
        budget = st.text_input("Offered Budget", value="")
    
    job_description = st.text_area("Job Description", "")

    # Adding Buttons
    btn_1, btn_2 = st.columns(2, gap="medium")
    with btn_1:
        submit_button = st.button("Generate")
    with btn_2:
        refresh_button = st.button("Refresh Page")

    if submit_button:
        proposal = return_proposal(name, experience, job_description, budget).strip()
        my_bar = st.progress(0, text="")
        for percent_complete in range(100):
            time.sleep(0.1)
            my_bar.progress(percent_complete + 1, text="")
        st.text_area("Your Proposal For Submit to Client", proposal, height=500)
    
    if refresh_button:
        st.experimental_rerun()

if __name__ == "__main__":
    main()
