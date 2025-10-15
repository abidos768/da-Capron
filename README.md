\# Local AI Assistant with RAG



A text-based AI assistant that runs locally using Ollama and supports RAG (Retrieval-Augmented Generation).



\## Features

\- 🤖 Runs completely offline using Ollama

\- 📚 RAG support for document search

\- 💬 Conversational memory

\- 🚀 Fast inference with local LLMs



\## Requirements

\- Python 3.8+

\- Ollama installed

\- 16GB RAM recommended

\- GPU optional (but recommended)



\## Installation



\### 1. Clone the repository

```bash

git clone https://github.com/YOUR\_USERNAME/ai-assistant.git

cd ai-assistant

```



\### 2. Create virtual environment

```bash

python -m venv venv



\# Windows

venv\\Scripts\\activate



\# Mac/Linux

source venv/bin/activate

```



\### 3. Install dependencies

```bash

pip install -r requirements.txt

```



\### 4. Install Ollama

Download from: https://ollama.com



\### 5. Download a model

```bash

ollama pull llama3.2:3b

```



\## Usage



\### Basic Assistant

```bash

python assistant.py

```



\### RAG Assistant (with document search)

```bash

python rag\_assistant.py

```



Then type `add docs` to load example documents.



\## Adding Your Own Documents



1\. Place text files in the `documents/` folder

2\. Modify `rag\_assistant.py` to load your files

3\. Run the assistant and ask questions about your documents!



\## Project Structure

```

ai-assistant/

├── venv/              # Virtual environment (not in git)

├── assistant.py       # Basic chat assistant

├── rag\_assistant.py   # RAG-enabled assistant

├── requirements.txt   # Python dependencies

├── documents/         # Your documents (not in git)

└── README.md         # This file

```



\## Contributing

Feel free to fork and submit PRs!



\## License

MIT

