"""Main script to run the RAG system."""
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
    # Define document folders
    core_docs_path = "../../Core Documents"
    modules_path = "../../Modules"

    # Check if folders exist
    if not os.path.exists(core_docs_path):
        print(f"Error: {core_docs_path} not found")
        return
    if not os.path.exists(modules_path):
        print(f"Error: {modules_path} not found")
        return

    # Step 1: Process PDFs
    print("=" * 60)
    print("STEP 1: Processing PDFs")
    print("=" * 60)
    processor = PDFProcessor(chunk_size=1000, chunk_overlap=200)
    documents = processor.extract_pdfs([core_docs_path, modules_path])
    chunks = processor.chunk_documents(documents)

    # Step 2: Build RAG System
    print("\n" + "=" * 60)
    print("STEP 2: Building RAG System")
    print("=" * 60)
    rag = RAGSystem(use_openai=False)  # Set to True if you have OpenAI API key
    rag.build_vector_store(chunks)

    # Step 3: Save vector store for future use
    print("\n" + "=" * 60)
    print("STEP 3: Saving Vector Store")
    print("=" * 60)
    vector_store_path = "./data/faiss_index"
    os.makedirs(vector_store_path, exist_ok=True)
    rag.save_vector_store(vector_store_path)

    # Step 4: Interactive query loop
    print("\n" + "=" * 60)
    print("STEP 4: Ready to Query")
    print("=" * 60)
    print("\nYour RAG system is ready! Ask questions about the DoD MPP documents.")
    print("Type 'quit' or 'exit' to exit.\n")

    while True:
        try:
            question = input("Question: ").strip()
            if question.lower() in ['quit', 'exit']:
                print("Exiting RAG system. Goodbye!")
                break
            if not question:
                continue

            rag.query(question, verbose=True)
        except KeyboardInterrupt:
            print("\n\nExiting RAG system. Goodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
