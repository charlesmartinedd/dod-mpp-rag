# DoD MPP RAG Web Application - User Guide

## 🚀 Quick Start

### Installation

1. **Install dependencies:**
   ```bash
   cd rag/src
   pip install -r requirements_web.txt
   ```

2. **Start the web application:**
   ```bash
   python start_webapp.py
   ```

   Or directly with Streamlit:
   ```bash
   streamlit run web_app.py
   ```

3. **Access the application:**
   - Open your browser to: `http://localhost:8501`
   - The interface will load automatically

## 💡 Features

### 1️⃣ **Chat Interface**
- Ask natural language questions about DoD MPP documents
- View chat history of your session
- Get instant answers with source citations

### 2️⃣ **Source Citations**
- Every answer includes source documents and page numbers
- Click "View Sources" to see exact text excerpts
- Verify information directly from official documents

### 3️⃣ **Document Upload**
- Add new PDF documents on the fly
- System automatically processes and indexes them
- No need to restart the application

### 4️⃣ **OpenAI Integration (Optional)**
- Enable GPT-4 for comprehensive, AI-powered answers
- Simple toggle in the sidebar
- Provide your OpenAI API key securely
- Falls back to context-based answers if disabled

### 5️⃣ **Session Management**
- Clear chat history anytime
- Persistent vector store (no reprocessing on restart)
- Fast loading times after initial setup

## 🎯 Usage Examples

### Basic Query
1. Type your question in the chat input at the bottom
2. Press Enter
3. View the answer with source citations

### Example Questions
- "What are the eligibility requirements for mentors?"
- "How do I report financial data?"
- "What are the roles and responsibilities?"
- "Tell me about subcontracting requirements"
- "What is the agreement approval process?"

### Using OpenAI (Optional)
1. Toggle "Use OpenAI GPT for answers" in sidebar
2. Enter your OpenAI API key
3. Ask questions to get AI-powered comprehensive answers

### Adding New Documents
1. Click "Upload Documents" in sidebar
2. Select one or more PDF files
3. Click "Process Uploaded Files"
4. Documents are immediately searchable

## 🏗️ Architecture

```
User Question
    ↓
Streamlit Web Interface
    ↓
RAG System (rag_system.py)
    ↓
FAISS Vector Search
    ↓
Retrieved Context (Top 4 chunks)
    ↓
Answer Generation:
  - Simple: Context display
  - OpenAI: GPT-4 powered answer
    ↓
Display with Sources
```

## ⚙️ Configuration

### Port Configuration
Default port is `8501`. To change:
```bash
streamlit run web_app.py --server.port=8080
```

### Search Settings
Modify `rag_system.py` to adjust:
- Number of retrieved documents: `search_kwargs={"k": 4}`
- Chunk size: `PDFProcessor(chunk_size=1000)`
- Chunk overlap: `chunk_overlap=200`

### Styling
Custom CSS is in `web_app.py` under `st.markdown()` section.

## 🔧 Troubleshooting

### "Vector store not found"
- First run builds the vector store (takes 2-5 minutes)
- Ensure `Core Documents/` and `Modules/` folders exist
- Check paths in `main.py`

### "Module not found" error
```bash
pip install -r requirements_web.txt
```

### OpenAI errors
- Verify your API key is correct
- Check OpenAI account has credits
- Ensure internet connection is active
- System falls back to context-based answers on error

### Port already in use
```bash
# Use a different port
streamlit run web_app.py --server.port=8502
```

### Slow performance
- First run processes all PDFs (normal)
- Subsequent runs load from cache instantly
- Consider reducing chunk_size if memory is limited

## 📊 System Requirements

- **Python**: 3.8 or higher
- **RAM**: 4GB minimum (8GB recommended)
- **Storage**: 500MB for vector store
- **Browser**: Modern browser (Chrome, Firefox, Safari, Edge)

## 🚀 Deployment Options

### Local Development
```bash
streamlit run web_app.py
```

### Network Access
```bash
streamlit run web_app.py --server.address=0.0.0.0 --server.port=8501
```
Access from other devices: `http://YOUR_IP:8501`

### Cloud Deployment

#### Streamlit Cloud (Free)
1. Push to GitHub
2. Connect at streamlit.io/cloud
3. Deploy in one click

#### Hugging Face Spaces (Free)
1. Create Space at huggingface.co/spaces
2. Upload files
3. Configure as Streamlit app

#### Docker
```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements_web.txt .
RUN pip install -r requirements_web.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "web_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

## 🎨 Customization

### Change Theme
Create `.streamlit/config.toml`:
```toml
[theme]
primaryColor = "#1f77b4"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f0f2f6"
textColor = "#262730"
font = "sans serif"
```

### Modify UI
Edit `web_app.py`:
- Custom CSS in `st.markdown()` section
- Layout changes in `st.set_page_config()`
- Sidebar content in `with st.sidebar:` block

### Add Features
- Chat export: Add button to download chat history
- Analytics: Track most asked questions
- Multi-language: Add translation support
- Audio input: Use speech-to-text API

## 📈 Performance Tips

1. **Vector Store Caching**: Automatically cached after first run
2. **GPU Acceleration**: Use `faiss-gpu` for faster search
3. **Batch Processing**: Upload multiple PDFs at once
4. **OpenAI Caching**: Reuse contexts for similar questions

## 🔒 Security Notes

- API keys are stored in session state (not persisted)
- No data is sent externally (unless OpenAI is enabled)
- Uploaded files are processed in temporary directories
- Vector store is local to your machine

## 📝 Next Steps

1. **Enhance Answers**: Enable OpenAI for better responses
2. **Add Documents**: Upload your own PDFs
3. **Deploy**: Share with team on cloud platform
4. **Customize**: Modify UI to match your branding

## 🆘 Support

- **Issues**: Check console logs for errors
- **Documentation**: See README.md in project root
- **Code**: Review `web_app.py` for implementation details

---

**Enjoy your DoD MPP RAG Assistant! 🎉**
