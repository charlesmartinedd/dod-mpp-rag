# Setting Up Documents

This RAG system requires PDF documents to be placed in specific directories.

## Directory Structure

```
rag/
├── src/              # RAG application code
├── data/             # Generated vector store (auto-created)
└── [Parent Directory]/
    ├── Core Documents/    # Place core PDF documents here
    └── Modules/           # Place module PDF documents here
```

## How to Add Your Documents

1. **Create the document folders** in the parent directory (one level up from `rag/`):
   ```bash
   cd ..
   mkdir "Core Documents"
   mkdir "Modules"
   ```

2. **Add your PDF files**:
   - Place core document PDFs in the `Core Documents/` folder
   - Place module PDFs in the `Modules/` folder

3. **Run the RAG system**:
   ```bash
   cd rag/src
   python main.py
   ```
   Or start the web interface:
   ```bash
   python start_webapp.py
   ```

## Note

The PDF documents are not included in this repository to:
- Avoid copyright/licensing issues
- Keep repository size manageable
- Allow users to add their own document collections

The system will automatically:
- Process all PDFs in both directories
- Create semantic chunks
- Build and cache the FAISS vector index
- Save the index for faster subsequent runs
