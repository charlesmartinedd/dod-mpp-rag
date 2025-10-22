"""PDF processing and text extraction module."""
import os
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

class PDFProcessor:
    def __init__(self, chunk_size=1000, chunk_overlap=200):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=["\n\n", "\n", " ", ""]
        )

    def extract_pdfs(self, folder_paths):
        """Extract text from all PDFs in given folders."""
        documents = []

        for folder_path in folder_paths:
            if not os.path.exists(folder_path):
                print(f"Warning: Folder not found: {folder_path}")
                continue

            pdf_files = list(Path(folder_path).glob("*.pdf"))
            print(f"Found {len(pdf_files)} PDFs in {folder_path}")

            for pdf_file in pdf_files:
                try:
                    print(f"  Processing: {pdf_file.name}")
                    loader = PyPDFLoader(str(pdf_file))
                    pdf_docs = loader.load()

                    # Add source metadata
                    for doc in pdf_docs:
                        doc.metadata["source_file"] = pdf_file.name

                    documents.extend(pdf_docs)
                except Exception as e:
                    print(f"    Error processing {pdf_file.name}: {e}")

        print(f"\nTotal pages extracted: {len(documents)}")
        return documents

    def chunk_documents(self, documents):
        """Split documents into chunks."""
        chunks = self.text_splitter.split_documents(documents)
        print(f"Created {len(chunks)} chunks")
        return chunks
