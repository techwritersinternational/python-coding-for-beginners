from openai_client import OpenAIAPI
from anthropic_client import AnthropicAPI

class LLMAPIWrapper:
    def __init__(self):
        self.apis = {
            "openai": OpenAIAPI(),
            "anthropic": AnthropicAPI()
        }

    def call_api(self, api_name, prompt, system_prompt):
        api = self.apis.get(api_name.lower())
        if api is None:
            raise ValueError(f"Unsupported API: {api_name}. The options are openai and anthropic.")
        return api.generate(prompt, system_prompt)
