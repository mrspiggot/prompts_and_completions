import re
import pandas as pd

class TextSplitter:
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


text = "This is sentence 1. This is sentence 2. This is sentence 3. This is sentence 4. This is sentence 5. This is sentence 6. This is sentence 7. This is sentence 8. This is sentence 9. This is sentence 10. This is sentence 11. This is sentence 12. This is sentence 13. This is sentence 14. This is sentence 15. This is sentence 16. This is sentence 17. This is sentence 18. This is sentence 19. This is sentence 20. This is sentence 21. This is sentence 22. This is sentence 23. This is sentence 24. This is sentence 25. This is sentence 26. This is sentence 27. This is sentence 28. This is sentence 29. This is sentence 30. This is sentence 31. This is sentence 32. This is sentence 33. This is sentence 34. This is sentence 35. This is sentence 36. This is sentence 37. This is sentence 38. This is sentence 39. This is sentence 40. This is sentence 41. This is sentence 42. This is sentence 43. This is sentence 44. This is sentence 45. This is sentence 46. This is sentence 47. This is sentence 48. This is sentence 49. This is sentence 50."
n = 5
splitter = TextSplitter(text, n)
df = splitter.split_into_sentences_with_prompts()
print(df)
