import autogen
import dotenv

dotenv.load_dotenv()

config_list = autogen.config_list_from_dotenv(
    ".env",
    {"mistralai/Mistral-7B-Instruct-v0.2"}
)

llm_config = {
    "cache_seed":41,
    "temperature": 0,
    config_list: config_list,
    "timeout": 120,
}

user_proxy = autogen.UserProxyAgent(
    name="Admin",
    system_message="A human admin. Intgeract with the planner to discuss the plan. Plan execution needs to be approved by this admin.",
    code_execution_config={
        "work_dir": "code",
        "use_docker": False,
    },
    human_input_mode="TERMINATE",
)

# TODO: Complete group engineer agent
engineer = autogen.AssistantAgent(
)