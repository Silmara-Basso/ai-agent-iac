# ai-agent-iac
 INITIAL VERSION: Artificial Intelligence agent capable of interacting with users and automating infrastructure provisioning through Infrastructure as Code (IaC) practices with Terraform.


# Case Study - Deploying an App with Docker and an AI Agent for Infrastructure Provisioning with IaC

File Structure:

 ```
 .
 ├── app
 │   ├── iac.py
 │   └── requirements.txt
 ├── .env
 ├── docker-compose.yml
 └── Dockerfile
```

# Configure your OpenAI API Key

- Create a file called .env in the root of your project (at the same level as docker-compose.yml).
- Open the .env file and add your OpenAI API key: OPENAI_API_KEY=your_key
OPENAI_API_KEY=TOKEN_OPENAI_HERE
OPENAI_API_BASE-https://api.openai.com/v1/

# Build and Run the Docker Container

```docker compose -p ai-iac up --build```

# Interact with the Agent

http://localhost:8501


![Application](/images/iac.png)
