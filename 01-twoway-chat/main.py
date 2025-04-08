import autogen

def main():
    config_list = autogen.config_list_from_json(
        "OAI_CONFIG_LIST.json",
        filter_dict={
            "model": ["mistralai/Mistral-7B-Instruct-v0.2"]
        }
    )

    assistant = autogen.AssistantAgent(
        name="Assistant",
        llm_config={
            "config_list": config_list,
            "timeout": 120,
            "temperature": 0.7
        }
    )

    user_proxy = autogen.UserProxyAgent(
        name="user",
        human_input_mode="NEVER",
        code_execution_config={
            "work_dir": "coding",
            "use_docker": False 
        }
    )

    user_proxy.initiate_chat(
        assistant,
        message="Plot META vs AAPL prices using yfinance. First install required packages."
    )

if __name__ == "__main__":
    main()