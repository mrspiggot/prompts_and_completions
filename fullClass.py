import re
import pandas as pd
import json

class LucidateTextSplitter:
    def __init__(self, text, n):
        self.text = text
        self.n = n

    def split_into_sentences_with_prompts(self):
        if self.text == "":
            raise ValueError("Input text cannot be empty.")
        if self.n <= 0:
            raise ValueError("n must be a positive integer.")
        sentences = re.split("(?<=[.!?]) +", self.text)
        if len(sentences) < self.n:
            raise ValueError("Input text must have at least n sentences.")
        prompts = sentences[::self.n]
        completions = []
        for i in range(len(prompts) - 1):
            completion = " ".join(sentences[self.n * i + 1:self.n * (i + 1)])
            completions.append(completion)
        completions.append(" ".join(sentences[self.n * (len(prompts) - 1) + 1:]))
        data = {'prompt': prompts, 'completion': completions}
        df = pd.DataFrame(data)
        return df

    def save_as_excel(self, filename):
        df = self.split_into_sentences_with_prompts()
        df.to_excel(filename, index=False)
    def save_as_csv(self, filename):
        df = self.split_into_sentences_with_prompts()
        df.to_csv(filename, index=False)
    def save_as_json(self, filename):
        df = self.split_into_sentences_with_prompts()
        data = []
        for i in range(len(df)):
            row = {'prompt': df.iloc[i]['prompt'], 'completion': df.iloc[i]['completion']}
            data.append(row)
        with open(filename, 'w') as f:
            json.dump(data, f)



text = "OpenAI's GPT-3 can be fine-tuned for specialized purposes, opening up a new level of AI for industries. " \
       "Chatbots and assistants can be enhanced to better meet user needs and provide more personalized service. " \
       "Fine-tuning also leads to more accurate and precise natural language processing (NLP), enabling complex human-" \
       "like interactions. The implications for future AI technology are immense, with the potential to open up new " \
       "markets and applications. Fine-tuning also makes machine learning more accessible, democratizing the field " \
       "and making it easier to adopt. All of this adds up to a technological milestone that has the potential to s" \
       "ignificantly impact how we interact with AI in the future. With GPT-3's ability to learn and adapt, the " \
       "future looks bright for those who can harness the power of this impressive technology. The process of " \
       "fine-tuning could help revolutionize industries and create new opportunities for innovation. The potential of " \
       "GPT-3's fine-tuning is limitless, and we are only beginning to scratch the surface of what is possible."
n = 3
splitter = LucidateTextSplitter(text, n)
df = splitter.split_into_sentences_with_prompts()
print(df)
splitter.save_as_json("Split.json")
splitter.save_as_csv("Split.csv")
splitter.save_as_excel("Split.xlsx")