import re
import pandas as pd
import json
import whisper
import youtube_dl

class LucidateTextSplitter:
    def __init__(self, text, n):
        self.text = text
        self.n = n

    def split_into_sentences_with_prompts(self):
        print(self.text)
        print(type(self.text))
        if self.text == "":
            raise ValueError("Input text cannot be empty.")
        if self.n <= 0:
            raise ValueError("n must be a positive integer.")
        sentences = re.split("(?<=[.!?]) +", self.text['text'])
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

class LucidateTranscriber:
    def __init__(self, model_path):
        self.model = whisper.load_model(model_path)

    def save_to_mp3(self, url):
        options = {'format': 'bestaudio/best', 'postprocessors': [{'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3', 'preferredquality': '192'}]}
        with youtube_dl.YoutubeDL(options) as downloader:
            downloader.download([url])

        return downloader.prepare_filename(downloader.extract_info(url, download=False)).replace(".m4a", ".mp3")

    def transcribe_youtube_video(self, url, fp16=False, n=5, op_name='transcribe'):
        filename = self.save_to_mp3(url)
        text = self.model.transcribe(filename, fp16=fp16)
        splitter = LucidateTextSplitter(text, n)
        splitter.save_as_excel(f'{op_name}.xlsx')

        return splitter.split_into_sentences_with_prompts()

