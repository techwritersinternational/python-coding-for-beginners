from openai import OpenAI

client = OpenAI()

class OpenAIAPI():

    def generate(self, prompt, system_prompt):
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system", 
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        return completion.choices[0].message.content
