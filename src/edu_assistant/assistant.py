from dotenv import load_dotenv
from loguru import logger

from edu_assistant.config import RoleType, TemplateType, Config
from edu_assistant.llm_client import get_llm_client

load_dotenv()


def create_response(llm_key: str, role: RoleType, template: TemplateType, prompt: str) -> str:
    config = Config.from_yaml_file("config.yml")
    llm_config = config.llms[llm_key]
    llm_client = get_llm_client(llm_config)
    instructions = config.render_system_instructions(role=role, template=template)
    logger.debug(f"LLM instructions: {instructions}")

    response = llm_client.responses.create(
        model=llm_config.model,
        max_output_tokens=llm_config.max_output_tokens,
        instructions=instructions,
        input=prompt
    )

    return response.output_text
