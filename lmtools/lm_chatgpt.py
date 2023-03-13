import time

import openai

from lmtools.lmsampler_baseclass import LMSamplerBaseClass
import numpy as np


class LM_ChatGPT(LMSamplerBaseClass):
    def __init__(self, model_name):
        """
        Supported models: 'gpt-3.5-turbo' must be in name.
        """
        super().__init__(model_name)
        if "gpt3" in model_name:
            # engine is all text after 'gpt3-'
            self.engine = model_name.split("-")[1]
        else:
            self.engine = self.model_name
        # make sure engine is a valid model
        valid_engines = [
            "gpt-3.5-turbo",
        ]
        if self.engine not in valid_engines:
            raise ValueError(f"engine {self.engine} not in {valid_engines}")
        # make sure API key is set
        if openai.api_key is None:
            raise ValueError("OpenAI API key must be set")
    
    def get_completion(self, prompt, args):
        response = openai

    def send_prompt(self, prompt, n_probs=100):
        raise NotImplementedError

    def sample(self, messages):
        # messages is expected to be a list of strings, with the following structure:
        # system, user, assistant, user, assistant, ...
        response = openai.ChatCompletion.create(
            model=self.engine,
            messages=messages,
        )
        return response["choices"][0]["message"]["content"]


if __name__ == "__main__":
    # test LM_GPT2
    lm = LM_ChatGPT("gpt-3.5-turbo")
    text = lm.sample(
        # prompt="What is the capital of France?\nThe capital of France is",
        messages=[
            {"role": "system", "content": "You are an expert, factual chatbot."},
            {"role": "user", "content": "What is the capital of France?"},
        ]
    )
    print(text)
    pass
