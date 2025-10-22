# DoD MPP RAG System - Quick Start

A free, local Retrieval-Augmented Generation system for querying DoD Mentor-Protégé Program documents.

## ✨ Features

- **Free & Local**: No API costs, runs entirely on your machine
- **Fast Search**: FAISS vector database for semantic search
- **Smart Chunking**: Documents split intelligently to preserve context
- **Easy to Use**: Simple command-line interface
- **Persistent**: Saves vector store for reuse without reprocessing

## 📦 Installation

1. **Install Python dependencies:**
   ```bash
   cd rag
   pip install -r requirements.txt
   ```

2. **Set up your documents:**

   **Important**: PDF documents are not included in this repository. You need to add your own documents.

   See [SETUP_DOCUMENTS.md](SETUP_DOCUMENTS.md) for detailed instructions on where to place your PDF files.

   Quick setup:
   ```bash
   cd ..  # Go to parent directory
   mkdir "Core Documents"
   mkdir "Modules"
   # Add your PDF files to these folders
   ```

3. **Run the RAG system:**
   ```bash
   cd src
   python main.py
   ```

The first run will:
- Extract all PDFs from `Core Documents/` and `Modules/` folders
- Process them into semantic chunks
- Build the FAISS vector database
- Save the index for future use

## 💬 Usage Examples

Once running, ask questions like:

```
Question: What are the eligibility requirements for mentors?
Question: How do I report financial data?
Question: What are the roles and responsibilities?
Question: Tell me about subcontracting requirements
Question: What is the agreement approval process?
```

## 🏗️ Architecture

```
PDFs (Core Documents + Modules)
    ↓
PDF Processor (PyPDF)
    ↓
Text Chunking (Semantic splits)
    ↓
Embeddings (HuggingFace all-MiniLM-L6-v2)
    ↓
Vector Store (FAISS - local, fast)
    ↓
Retriever (Similarity search, top 4 results)
    ↓
Answer (Context + question → answer)
```

## 📁 Project Structure

```
rag/
├── requirements.txt          # Python dependencies
├── data/
│   └── faiss_index/         # Vector store (created on first run)
└── src/
    ├── main.py              # Entry point
    ├── pdf_processor.py      # PDF extraction & chunking
    └── rag_system.py        # RAG core logic
```

## ⚙️ Configuration

### Chunk Size
Adjust `chunk_size` and `chunk_overlap` in `pdf_processor.py`:
```python
processor = PDFProcessor(chunk_size=1000, chunk_overlap=200)
```
- **Smaller chunks**: More precise but less context
- **Larger chunks**: More context but less granular

### Search Results
Change number of retrieved documents in `rag_system.py`:
```python
search_kwargs={"k": 4}  # Return top 4 results
```

### Enable OpenAI (Optional)
For better answers with GPT-4, add your API key:
```python
rag = RAGSystem(use_openai=True, api_key="sk-...")
```

## 🚀 Optimization Tips

1. **First run takes time** - Embedding generation is I/O intensive
2. **Subsequent runs are instant** - Vector store is cached
3. **Ask specific questions** - "What are mentor eligibility requirements?" works better than "Tell me about mentors"
4. **Check sources** - System shows which documents/pages were used

## 📊 What Gets Indexed

**Core Documents (3 files):**
- MPP SOP (Standard Operating Procedures)
- Appendix I

**Modules (10 files):**
1. DoD Mentor-Protégé Program overview
2. Roles and responsibilities
3. Agreement types and processes
4. Mentor eligibility and agreement development
5. Financial management and reporting
6. Performance monitoring and compliance
7. Developmental assistance
8. Subcontracting and small business
9. Contract administration
10. Awards and recognition

**Total**: ~150-200 pages of indexed content

## 🔧 Troubleshooting

**"Module not found" error:**
```bash
# Make sure you're in the correct directory
cd C:\Users\MarieLexisDad\claudeflow\rag\src
python main.py
```

**"PDF file not found":**
- Ensure `Core Documents/` and `Modules/` folders are in the parent directory of `rag/`
- Check folder names match exactly (case-sensitive on some systems)

**Slow performance:**
- First run processes all PDFs (normal, takes 2-5 minutes)
- Subsequent runs load from cache instantly
- Reduce `chunk_size` if memory is limited

## 📈 Next Steps

Once comfortable with this basic RAG:

1. **Add more PDFs** - System automatically indexes new files
2. **Upgrade to Production** - Add Streamlit UI, FastAPI backend
3. **Deploy to Cloud** - Share with team (Hugging Face Spaces, Render)
4. **Add OpenAI** - Enable GPT-powered responses

## 📝 Notes

- System uses **sentence-transformers** (free, local embeddings)
- **FAISS** provides fast semantic search without external APIs
- No data leaves your computer - fully private
- Can be used offline once vector store is built

---

**Questions?** Check the code comments or modify `main.py` to adjust behavior.
