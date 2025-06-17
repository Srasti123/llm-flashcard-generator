# 📚 LLM-Powered Flashcard Generator (Offline + Free)

A fully offline flashcard generator built with Hugging Face's FLAN-T5 and Streamlit.

This tool lets you upload educational text (PDF or TXT) or paste raw content to generate high-quality, multi-question flashcards in strict **Q: / A:** format — no internet or API key required.

---

## 🚀 Features

- ✅ **Runs offline** with Hugging Face `flan-t5-base`
- 📥 Upload `.pdf` or `.txt` files OR paste content directly
- 🔄 Automatically splits long content and generates multiple flashcards
- 🧠 Output in strict `Q:` / `A:` format for easy studying
- 💾 Download flashcards as `.txt`
- ⚙️ Adjustable flashcards per section

---

## 🖼️ Demo

![App Screenshot](https://your-screenshot-or-gif-url.com)

---

## 📁 Project Structure

```

llm-flashcard-generator/
├── app.py                    # Streamlit UI
├── flashcard\_generator.py   # Core logic using FLAN-T5
├── requirements.txt
└── README.md

````

---

## 🛠️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/llm-flashcard-generator.git
cd llm-flashcard-generator
````

### 2. Create and activate a virtual environment

```bash
python -m venv venv
# Windows PowerShell
.\venv\Scripts\Activate.ps1
# OR Windows CMD
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🤖 Download Model (One-Time Only)

You must download the [FLAN-T5 base model](https://huggingface.co/google/flan-t5-base) and place it locally:

```
C:\Users\<YourName>\.cache\huggingface\hub\models--google--flan-t5-base\snapshots\<snapshot-folder>
```

> This project is fully offline after the model is available locally.

---

## 🧪 Run the App

```bash
streamlit run app.py
```

---

## 📥 Sample Flashcard Output

```
Q: What is the function of mitochondria in a cell?
A: It produces energy in the form of ATP through cellular respiration.

Q: What type of cells contain mitochondria?
A: Both plant and animal cells contain mitochondria.
```

---

## 📄 License

This project is open-source and free to use under the [MIT License](LICENSE).

---

## 🙌 Credits

* 🤖 [Hugging Face Transformers](https://huggingface.co)
* ⚡ [Streamlit](https://streamlit.io)
* ✍️ Built with ❤️ by [Vishnu Dubey](https://github.com/<your-username>)

```

---

## ✅ What to Do Next

1. **Copy the markdown above**
2. Go to your GitHub repo
3. Create a new `README.md` or paste into the existing one
4. Commit your changes

---

Let me know if you want:
- A screenshot preview created
- A short demo GIF or video badge added
- Hosting link (Streamlit Cloud or Hugging Face Spaces)

You're almost ready to show this off in your portfolio or resume! 💼
```
