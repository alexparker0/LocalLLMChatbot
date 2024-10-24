from gpt4all import GPT4All
model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf") # downloads / loads a 1.98GB LLM
with model.chat_session():
    print(model.generate("What genes are present in cancerous cells?", max_tokens=512))