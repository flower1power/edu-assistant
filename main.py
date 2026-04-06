from dotenv import load_dotenv

from edu_assistant.config import Config
from edu_assistant.llm_client import get_llm_client

load_dotenv()

INPUT_PROMPT = "Кто ты?"

config = Config.from_yaml_file("config.yml")
llm_config = config.llms["ollama"]

llm_client = get_llm_client(llm_config)

response = llm_client.responses.create(
    model=llm_config.model,
    max_output_tokens=llm_config.max_output_tokens,
    input=INPUT_PROMPT
)

print(response.output_text)
