import autogen
# gpt-3.5-turbo will default to OPENAI_API_KEY
config_list = autogen.config_list_from_dotenv(
    dotenv_file_path='.env', # If None the function will try to find in the working directory
    model_api_key_map={
        "gpt-4": "OPENAI_API_KEY", 
        "gpt-3.5-turbo": "OPENAI_API_KEY",
        "gpt-4-1106-preview":"OPENAI_API_KEY",
    },
    filter_dict={
        "model": {
#            "gpt-4",
#            "gpt-3.5-turbo",
            "gpt-4-1106-preview"    
        }
    },
)

llm_config = {
#    "cache_seed": 42,  # change the cache_seed for different trials
    "temperature": 0,
    "config_list": config_list,
    "timeout": 600,
    "max_retry_period" : 300,
    "retry_wait_time" : 60,
}



