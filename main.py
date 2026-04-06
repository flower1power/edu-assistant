from edu_assistant.config import Config

# Create config file path
config = Config.from_yaml_file("config.yml")
# print("Full config:", config)
# print("LLM model:", config.llms["api"].model)

system_prompt = config.render_system_instructions(role="history_tutor", template="tutor_quick_answer")
print("System prompt:", system_prompt)
