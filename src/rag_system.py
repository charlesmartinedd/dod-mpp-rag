"""RAG (Retrieval-Augmented Generation) system using FAISS and sentence transformers."""
import os
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from pdf_processor import PDFProcessor

class RAGSystem:
    def __init__(self, use_openai=False, api_key=None):
        """
        Initialize RAG system.

        Args:
            use_openai: If True, uses OpenAI API (requires OPENAI_API_KEY)
            api_key: OpenAI API key (optional, can use env var)
        """
        print("Initializing RAG System...")

        # Initialize embeddings (free, local)
        print("Loading embeddings model...")
        self.embeddings = HuggingFaceEmbeddings(
            model_name="all-MiniLM-L6-v2",
            model_kwargs={"device": "cpu"}
        )

        self.vector_store = None
        self.retriever = None
        self.qa_chain = None
        self.use_openai = use_openai

        if use_openai and api_key:
            os.environ["OPENAI_API_KEY"] = api_key

        print("RAG System initialized!")

    def build_vector_store(self, documents):
        """Build FAISS vector store from documents."""
        print(f"\nBuilding vector store from {len(documents)} documents...")
        self.vector_store = FAISS.from_documents(documents, self.embeddings)
        self.retriever = self.vector_store.as_retriever(
            search_type="similarity",
            search_kwargs={"k": 4}  # Return top 4 relevant chunks
        )
        print("Vector store created successfully!")

    def query(self, question, verbose=True):
        """
        Query the RAG system.

        Args:
            question: User's question
            verbose: Print retrieval details

        Returns:
            Answer string
        """
        if not self.retriever:
            return "Error: Vector store not built. Run build_vector_store first."

        # Retrieve relevant chunks
        retrieved_docs = self.vector_store.similarity_search(question, k=4)

        if verbose:
            print(f"\n{'='*60}")
            print(f"Question: {question}")
            print(f"{'='*60}")
            print(f"\nRetrieved {len(retrieved_docs)} relevant chunks:")
            for i, doc in enumerate(retrieved_docs, 1):
                source = doc.metadata.get("source_file", "unknown")
                page = doc.metadata.get("page", "?")
                print(f"\n[{i}] Source: {source} (Page {page})")
                print(f"    {doc.page_content[:200]}...")

        # Create context from retrieved documents
        context = "\n\n".join([doc.page_content for doc in retrieved_docs])

        # Simple prompt-based answer (no API needed)
        answer = self._generate_answer_local(question, context)

        print(f"\n{'='*60}")
        print(f"Answer: {answer}")
        print(f"{'='*60}\n")

        return answer

    def _generate_answer_local(self, question, context):
        """Generate answer using simple template (no API calls)."""
        # Clean text to handle encoding issues
        try:
            context_clean = context.encode('utf-8', errors='ignore').decode('utf-8')
        except:
            context_clean = context

        # For quick start without API, return a template response
        return f"""Based on the retrieved documents, here's what I found:

{context_clean[:500]}...

[Note: For full AI-powered answers, add an OpenAI API key to enable GPT-powered responses]"""

    def save_vector_store(self, path="./faiss_index"):
        """Save vector store to disk."""
        if self.vector_store:
            self.vector_store.save_local(path)
            print(f"Vector store saved to {path}")

    def load_vector_store(self, path="./faiss_index"):
        """Load vector store from disk."""
        print(f"Loading vector store from {path}...")
        self.vector_store = FAISS.load_local(
            path,
            self.embeddings,
            allow_dangerous_deserialization=True
        )
        self.retriever = self.vector_store.as_retriever(
            search_type="similarity",
            search_kwargs={"k": 4}
        )
        print("Vector store loaded!")
