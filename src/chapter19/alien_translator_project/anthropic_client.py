from anthropic import Anthropic

client = Anthropic()

class AnthropicAPI():

    def generate(self, prompt, system_prompt):
        message = client.messages.create(
            model="claude-3-7-sonnet-20250219",
            max_tokens=1024,
            system=system_prompt,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return message.content[0].text