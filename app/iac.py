# Deploy de App com Docker e Agente de IA Para Provisionamento de Infraestrutura com IaC
#=================================================
# app/iac.py
#=================================================
# Creating the user interface and managing interaction with the AI ​​Agent.
import os
import streamlit as st
from crewai import Agent, Task, Crew
from crewai.process import Process
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# --- Streamlit Page Setup ---
st.set_page_config(
    page_title="AI Agent for Infrastructure Provisioning with IaC",
    page_icon=":100:",
    layout="wide"
)

st.title("🤖 Terraform Script Generator with AI Agent")
st.markdown("""
This tool uses a specialized AI Agent to convert your infrastructure descriptions 
into ready-to-use Terraform (HCL) code.
""")

# --- CrewAI Agent Configuration ---
try:
    openai_llm = ChatOpenAI(
        model="gpt-4-turbo",
        api_key=os.getenv("OPENAI_API_KEY")
    )
except Exception as e:
    st.error(f"Erro ao inicializar o modelo de linguagem: {e}. Verifique se a sua OPENAI_API_KEY está configurada no arquivo .env.")
    openai_llm = None

# Define the AI ​​Agent with a specific role, goal, and backstory to ensure it generates accurate and efficient Terraform scripts based on user requirements.
terraform_expert = Agent(
  role='Senior Infrastructure as Code Specialist',
  goal='Create accurate and efficient Terraform scripts based on user requirements.',
  backstory=(
    "You are a highly experienced DataOps Engineer with a decade of experience in automating "
    "cloud infrastructure provisioning using Terraform. You have a deep understanding "
    "of cloud providers like AWS, Azure and GCP, and are a master at writing clean, modular and reusable HCL (HashiCorp "
    "Configuration Language). Your mission is to translate high-level infrastructure descriptions into ready-to-use Terraform code."
  ),
  verbose=True,
  allow_delegation=False,
  llm=openai_llm
)

# --- User Interface ---
st.header("Describe the Desired Infrastructure")

prompt = st.text_area(
    "Provide a clear and detailed prompt. The more specific you are, the better the result will be.",
    height=150,
    placeholder="Example: Create the IaC code with Terraform to create an S3 bucket on AWS with the name 'basso-appx-12345', with versioning and SSE-S3 encryption enabled."
)

if st.button("Generate Terraform Script", type="primary", disabled=(not openai_llm)):
    if prompt:
        with st.spinner("The AI ​​Agent is working... Please be patient and wait."):
            try:
                # Defines the task for the agent based on the user's prompt.
                terraform_task = Task(
                    description=(
                        f"Based on the following user request, generate a complete and functional Terraform script. "
                        f"The output should be ONLY the HCL code block, without any explanation or additional text. "
                        f"The code should be well-formatted and ready to be saved in a .tf file.\n\n"
                        f"User Request: '{prompt}'"
                    ),
                    expected_output='A code block containing the Terraform script (HCL). The code should be complete and should not contain placeholders like "your_configuration_here".',
                    agent=terraform_expert
                )

                # Creates and manages the team (Crew) to execute the task.
                terraform_crew = Crew(
                    agents=[terraform_expert],
                    tasks=[terraform_task],
                    process=Process.sequential,
                    verbose=True
                )

                # Start the process and get the result.
                result = terraform_crew.kickoff()
                
                st.header("Generated Result")
                st.code(result, language='terraform')
                st.success("Script generated successfully.")

            except Exception as e:
                st.error(f"An error occurred during execution: {e}")
    else:
        st.warning("Please insert a description of the infrastructure to generate the script.")

st.markdown("---")
st.markdown("Built with [Streamlit](https://streamlit.io/) and [CrewAI](https://www.crewai.com/). Developed by Silmara Basso.")
