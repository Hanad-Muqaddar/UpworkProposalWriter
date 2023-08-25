from langchain import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain
import streamlit as st

def return_prompt():

    prompt_template = PromptTemplate(
        input_variables=["name", "experience", "job_desc", "budget"],

        template = """As an Upwork Expert, and keeping all best tips to write a Job Winning Proposal, Write a Proposal for me
        Seller Details : 
            - Name : {name}
            - Experience : {experience}
        Offering Details:
            - Budget : {budget}
        Job Description : 
            Description : {job_desc}
        Accroding to this seller details, Budget details seller id offerinf, and job description write proposal for this job.
        The way you have to write the proposal is

        1) Use Generic Salutation for the client
        2) Seller Intro and Experience details accroding to job description
        3) Address the Client's Needs
        4) How to solve this problem
        5) Tools and technologies used to solve this
        6) Offering Budget
        7) Ask Relevant Questions if any
        8) At the end add Regard from seller

        Don't leave the whole proposal uncompleted.
        As a professional proposal writer keep it consise and to the point. 
        """
    )
    return prompt_template

def return_proposal(name, experience, job_desc, budget):
    prompt_template = return_prompt()
    chain = LLMChain(
    llm=OpenAI(openai_api_key=st.secrets.OPENAI_API_KEY),
    prompt=prompt_template,
    )
    proposal = chain.run({"name":name, "experience" : f"more than {experience} years", "job_desc" : job_desc, "budget" : f"${budget}"})
    return proposal
