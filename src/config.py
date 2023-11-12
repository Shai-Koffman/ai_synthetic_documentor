import autogen
# gpt-3.5-turbo will default to OPENAI_API_KEY
config_list = autogen.config_list_from_dotenv(
    dotenv_file_path='.env', # If None the function will try to find in the working directory
    model_api_key_map={
        "gpt-4": "OPENAI_API_KEY", 
        "gpt-3.5-turbo": "OPENAI_API_KEY",
    },
    filter_dict={
        "model": {
            "gpt-4",
            "gpt-3.5-turbo",
        }
    }
)

