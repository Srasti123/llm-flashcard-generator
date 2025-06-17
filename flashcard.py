from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

# Path to your locally downloaded FLAN-T5 model
model_path = r"C:\Users\vishn\.cache\huggingface\hub\models--google--flan-t5-base\snapshots\7bcac572ce56db69c1ea7c8af255c5d7c9672fc2"

# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSeq2SeqLM.from_pretrained(model_path)

# Split long text into chunks (400 words each)
def chunk_text(text, max_words=400):
    words = text.split()
    return [" ".join(words[i:i + max_words]) for i in range(0, len(words), max_words)]

# Generate multiple flashcards in strict Q&A format
def generate_flashcards(text, subject=None, cards_per_chunk=5):
    chunks = chunk_text(text)
    all_flashcards = []

    for chunk_index, chunk in enumerate(chunks):
        for card_index in range(cards_per_chunk):
            prompt = f"""
            Generate one unique, high-quality educational flashcard from the content below.
            Respond strictly in the following format:
            Q: <question>
            A: <answer>

            {f'Subject: {subject}' if subject else ''}

            Content:
            {chunk}
            """

            inputs = tokenizer(prompt, return_tensors="pt", max_length=512, truncation=True)
            outputs = model.generate(**inputs, max_new_tokens=256, temperature=0.7)
            flashcard_raw = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

            # Fallback postprocessing to ensure Q/A format
            if "Q:" not in flashcard_raw:
                question_part = flashcard_raw.split('?')[0] + "?"
                answer_part = flashcard_raw.split('?')[-1].strip()
                flashcard_raw = f"Q: {question_part}\nA: {answer_part}"

            all_flashcards.append(flashcard_raw)

    return "\n\n".join(all_flashcards)
