# da-Capron - Local AI Assistant

Local AI assistant using Ollama + RAG. Built by friends, for learning.

## What It Does
- Chat with AI locally (no internet needed)
- Search through documents (RAG)
- Remembers conversation context

## Quick Start

### Setup (Do this once)
```bash
# 1. Clone
git clone https://github.com/abidos768/da-Capron.git
cd da-Capron

# 2. Install Python stuff
python -m venv venv
venv\Scripts\activate          # Windows
pip install -r requirements.txt

# 3. Install Ollama from https://ollama.com

# 4. Download model
ollama pull llama3.2:3b
```

### Run It
```bash
# Basic chat
python assistant.py

# With document search
python rag_assistant.py
```

## Files
- `assistant.py` - Simple chatbot
- `rag_assistant.py` - Chatbot + document search
- `requirements.txt` - Python packages needed
- `documents/` - Put your docs here (for RAG)

## Future Improvements & Ideas

### 🔮 Planned Features

#### 1. **Enhanced RAG System** 📚
- [ ] PDF file support
- [ ] Word document (.docx) support
- [ ] Batch folder loading
- [ ] Better document chunking strategies
- [ ] Multiple knowledge bases

#### 2. **User Interface Options** 🎨
- [ ] **Gradio Web UI** - Simple browser-based chat interface
- [ ] **Streamlit Dashboard** - Interactive data visualization
- [ ] **Flask Web App** - Custom web interface
- [ ] **Rich Terminal UI** - Colored and formatted terminal output

#### 3. **Additional Features** ✨
- [ ] Conversation history save/load
- [ ] Export chats to text/markdown
- [ ] Multiple AI personalities (system prompts)
- [ ] Voice input/output (TTS/STT)
- [ ] Web search integration
- [ ] Multi-language support

#### 4. **Model Improvements** 🧠
- [ ] Support for larger models (8B, 13B+)
- [ ] Model switching on-the-fly
- [ ] Specialized models (coding, math, creative writing)
- [ ] Model comparison tools

#### 5. **Performance Optimizations** ⚡
- [ ] GPU acceleration optimization
- [ ] Response caching
- [ ] Faster embedding models
- [ ] Batch processing for RAG queries
- [ ] Streaming responses

#### 6. **Developer Tools** 🛠️
- [ ] API endpoint creation
- [ ] Docker containerization
- [ ] Automated testing
- [ ] Performance benchmarking
- [ ] Logging and debugging tools

### 🎯 Quick Wins (Easy to Implement)

**Want to contribute? Start here:**

1. **Add Gradio Web UI** (30 minutes)
   ```bash
   pip install gradio
   ```
   Create a simple web interface for easier interaction

2. **PDF Support** (1 hour)
   ```bash
   pip install PyPDF2
   ```
   Load and process PDF documents

3. **Conversation History** (45 minutes)
   Save and load previous conversations

4. **System Prompts** (30 minutes)
   Add different personalities (helpful, creative, technical, etc.)

## Contributing

We welcome contributions! Here's how:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Setup
```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/da-Capron.git

# Add upstream remote
git remote add upstream https://github.com/abidos768/da-Capron.git

# Create feature branch
git checkout -b feature/your-feature-name

# Make changes, commit, and push
git add .
git commit -m "Description of changes"
git push origin feature/your-feature-name
```

## Known Issues
- ChromaDB may take time to initialize on first run
- Large documents may cause memory issues
- GPU detection may fail on some systems

## Troubleshooting

**Ollama not found:**
```bash
# Check if Ollama is installed
ollama --version

# Make sure Ollama service is running
ollama serve
```

**Import errors:**
```bash
# Reinstall dependencies
pip install -r requirements.txt --upgrade
```

**GPU not detected:**
```bash
# Check CUDA availability (NVIDIA)
nvidia-smi

# Ollama will automatically use CPU if GPU unavailable
```

## Resources
- [Ollama Documentation](https://github.com/ollama/ollama)
- [ChromaDB Documentation](https://docs.trychroma.com/)
- [LangChain RAG Tutorial](https://python.langchain.com/docs/use_cases/question_answering/)

## License
MIT

## Authors
- [@abidos768](https://github.com/abidos768)

---

**⭐ Star this repo if you find it useful!**
