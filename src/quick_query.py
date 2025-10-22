"""Quick query script for RAG system."""
import os
import sys
import io
from pathlib import Path
from pdf_processor import PDFProcessor
from rag_system import RAGSystem

# Fix encoding issues on Windows
if sys.stdout.encoding != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def main():
    question = sys.argv[1] if len(sys.argv) > 1 else "What are some specific oversight duties for Program Managers?"

    # Define paths
    core_docs_path = "../../Core Documents"
    modules_path = "../../Modules"
    vector_store_path = "../data/faiss_index"

    # Initialize RAG system
    rag = RAGSystem(use_openai=False)

    # Check if vector store exists
    if os.path.exists(vector_store_path):
        print("Loading existing vector store...")
        try:
            rag.load_vector_store(vector_store_path)
        except ValueError:
            # Need to update load method
            print("Rebuilding vector store...")
            processor = PDFProcessor(chunk_size=1000, chunk_overlap=200)
            documents = processor.extract_pdfs([core_docs_path, modules_path])
            chunks = processor.chunk_documents(documents)
            rag.build_vector_store(chunks)
            rag.save_vector_store(vector_store_path)
    else:
        print("Building new vector store...")
        processor = PDFProcessor(chunk_size=1000, chunk_overlap=200)
        documents = processor.extract_pdfs([core_docs_path, modules_path])
        chunks = processor.chunk_documents(documents)
        rag.build_vector_store(chunks)
        os.makedirs(vector_store_path, exist_ok=True)
        rag.save_vector_store(vector_store_path)

    # Query
    rag.query(question, verbose=True)

if __name__ == "__main__":
    main()
