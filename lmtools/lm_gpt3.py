import time

import openai

from lmtools.lmsampler_baseclass import LMSamplerBaseClass


class LM_GPT3(LMSamplerBaseClass):
    def __init__(self, model_name):
        """
        Supported models: 'ada', 'babbage', 'curie', 'davinci', 'gpt3-ada', gpt3-babbage', gpt3-curie', gpt3-davinci', 'text-ada-001', 'text-babbage-001', 'text-curie-001', 'text-davinci-001', 'text-davinci-002'
        """
        super().__init__(model_name)
        if "gpt3" in model_name:
            # engine is all text after 'gpt3-'
            self.engine = model_name.split("-")[1]
        else:
            self.engine = self.model_name
        # make sure engine is a valid model
        valid_engines = [
            "ada",
            "babbage",
            "curie",
            "davinci",
            "text-ada-001",
            "text-babbage-001",
            "text-curie-001",
            "text-davinci-001",
            "text-davinci-002",
        ]
        if self.engine not in valid_engines:
            raise ValueError(f"engine {self.engine} not in {valid_engines}")
        # make sure API key is set
        if openai.api_key is None:
            raise ValueError("OpenAI API key must be set")

    def send_prompt(self, prompt, n_probs=100):
        start_time = time.time()
        response = openai.Completion.create(
            engine=self.engine,
            prompt=prompt,
            max_tokens=1,
            logprobs=n_probs,
        )
        logprobs = response["choices"][0]["logprobs"]["top_logprobs"][0]
        # sort dictionary by values
        sorted_logprobs = dict(
            sorted(logprobs.items(), key=lambda x: x[1], reverse=True)
        )
        # TODO - automate this?
        now = time.time()
        min_time = 0.1
        if now - start_time < min_time:
            wait_time = min_time - (now - start_time)
            wait_time = max(wait_time, 0)
            time.sleep(wait_time)
        return sorted_logprobs

    def sample_several(self, prompt, temperature=0, n_tokens=10):
        response = openai.Completion.create(
            engine=self.engine,
            prompt=prompt,
            max_tokens=n_tokens,
            temperature=temperature,
        )
        return response["choices"][0]["text"]


if __name__ == "__main__":
    # test LM_GPT2
    lm = LM_GPT3("gpt3-ada")
    text = lm.sample_several(
        prompt="What is the capital of France?\nThe capital of France is",
        temperature=0,
        n_tokens=50,
    )
    print(text)
    pass
