"""Streamlit Web Application for DoD MPP RAG System."""
import streamlit as st
import os
import sys
from pathlib import Path
from rag_system import RAGSystem
from pdf_processor import PDFProcessor
import tempfile

# Page configuration
st.set_page_config(
    page_title="DoD MPP Assistant",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #555;
        text-align: center;
        margin-bottom: 2rem;
    }
    .source-box {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
    .chat-message {
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    .user-message {
        background-color: #e3f2fd;
    }
    .assistant-message {
        background-color: #f5f5f5;
    }
</style>
""", unsafe_allow_html=True)

def initialize_rag_system():
    """Initialize or load the RAG system."""
    vector_store_path = "./data/faiss_index"

    # Check if vector store exists
    if os.path.exists(vector_store_path):
        st.info("📦 Loading existing vector store...")
        rag = RAGSystem(use_openai=st.session_state.get('use_openai', False))
        rag.load_vector_store(vector_store_path)
        return rag
    else:
        st.warning("🔨 No vector store found. Building from PDFs...")

        # Define document folders
        core_docs_path = "../../Core Documents"
        modules_path = "../../Modules"

        if not os.path.exists(core_docs_path) or not os.path.exists(modules_path):
            st.error("❌ Error: Core Documents or Modules folder not found!")
            return None

        # Process PDFs
        with st.spinner("Processing PDFs..."):
            processor = PDFProcessor(chunk_size=1000, chunk_overlap=200)
            documents = processor.extract_pdfs([core_docs_path, modules_path])
            chunks = processor.chunk_documents(documents)

        # Build vector store
        with st.spinner("Building vector store..."):
            rag = RAGSystem(use_openai=st.session_state.get('use_openai', False))
            rag.build_vector_store(chunks)
            os.makedirs(vector_store_path, exist_ok=True)
            rag.save_vector_store(vector_store_path)

        st.success("✅ Vector store built successfully!")
        return rag

def process_uploaded_files(uploaded_files):
    """Process uploaded PDF files and add to vector store."""
    if not uploaded_files:
        return []

    temp_dir = tempfile.mkdtemp()
    temp_files = []

    for uploaded_file in uploaded_files:
        temp_path = os.path.join(temp_dir, uploaded_file.name)
        with open(temp_path, 'wb') as f:
            f.write(uploaded_file.getbuffer())
        temp_files.append(temp_path)

    # Process new PDFs
    processor = PDFProcessor(chunk_size=1000, chunk_overlap=200)
    documents = processor.extract_pdfs([temp_dir])
    chunks = processor.chunk_documents(documents)

    return chunks

def display_chat_message(role, content, sources=None):
    """Display a chat message with optional sources."""
    message_class = "user-message" if role == "user" else "assistant-message"

    with st.container():
        st.markdown(f'<div class="chat-message {message_class}">', unsafe_allow_html=True)

        if role == "user":
            st.markdown(f"**You:** {content}")
        else:
            st.markdown(f"**Assistant:** {content}")

            if sources:
                with st.expander("📄 View Sources"):
                    for i, source in enumerate(sources, 1):
                        st.markdown(f"""
                        <div class="source-box">
                            <strong>[{i}] {source['file']} (Page {source['page']})</strong><br>
                            {source['content'][:300]}...
                        </div>
                        """, unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

def main():
    """Main application."""

    # Header
    st.markdown('<div class="main-header">📚 DoD Mentor-Protégé Program Assistant</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Ask questions about the DoD MPP documents</div>', unsafe_allow_html=True)

    # Sidebar
    with st.sidebar:
        st.header("⚙️ Settings")

        # OpenAI settings
        use_openai = st.checkbox("Use OpenAI GPT for answers", value=False)
        api_key = None

        if use_openai:
            api_key = st.text_input("OpenAI API Key", type="password")
            st.info("💡 Using GPT will provide more comprehensive answers")

        st.session_state.use_openai = use_openai and api_key

        st.divider()

        # File upload
        st.header("📤 Upload Documents")
        uploaded_files = st.file_uploader(
            "Add new PDF documents",
            type=['pdf'],
            accept_multiple_files=True
        )

        if uploaded_files:
            if st.button("Process Uploaded Files"):
                with st.spinner("Processing uploaded PDFs..."):
                    new_chunks = process_uploaded_files(uploaded_files)
                    if new_chunks and 'rag_system' in st.session_state:
                        st.session_state.rag_system.build_vector_store(new_chunks)
                        st.success(f"✅ Added {len(new_chunks)} chunks from {len(uploaded_files)} files")

        st.divider()

        # Clear chat history
        if st.button("🗑️ Clear Chat History"):
            st.session_state.messages = []
            st.rerun()

        st.divider()

        # Info
        st.header("ℹ️ About")
        st.markdown("""
        This RAG system provides instant access to:
        - **Core Documents**: MPP SOP, Appendix I
        - **10 Training Modules**: All MPP topics

        **Features:**
        - Semantic search across all documents
        - Source citations for transparency
        - Upload custom PDFs
        - Optional GPT integration
        """)

    # Initialize session state
    if 'messages' not in st.session_state:
        st.session_state.messages = []

    if 'rag_system' not in st.session_state:
        st.session_state.rag_system = initialize_rag_system()

    # Update OpenAI settings if changed
    if st.session_state.rag_system and st.session_state.use_openai and api_key:
        os.environ["OPENAI_API_KEY"] = api_key

    # Display chat history
    for message in st.session_state.messages:
        display_chat_message(
            message["role"],
            message["content"],
            message.get("sources")
        )

    # Chat input
    question = st.chat_input("Ask a question about the DoD MPP...")

    if question:
        # Add user message
        st.session_state.messages.append({"role": "user", "content": question})
        display_chat_message("user", question)

        # Get answer from RAG system
        if st.session_state.rag_system:
            with st.spinner("Searching documents..."):
                # Get retrieved documents
                retrieved_docs = st.session_state.rag_system.vector_store.similarity_search(question, k=4)

                # Prepare sources
                sources = []
                for doc in retrieved_docs:
                    sources.append({
                        "file": doc.metadata.get("source_file", "unknown"),
                        "page": doc.metadata.get("page", "?"),
                        "content": doc.page_content
                    })

                # Generate answer
                context = "\n\n".join([doc.page_content for doc in retrieved_docs])

                if st.session_state.use_openai:
                    # Use OpenAI for better answers
                    try:
                        from langchain_openai import ChatOpenAI
                        from langchain.chains import LLMChain
                        from langchain.prompts import PromptTemplate

                        llm = ChatOpenAI(model="gpt-4", temperature=0)
                        prompt = PromptTemplate(
                            template="""You are a helpful assistant for the DoD Mentor-Protégé Program.
                            Use the following context to answer the question. Be specific and cite relevant details.

                            Context:
                            {context}

                            Question: {question}

                            Answer:""",
                            input_variables=["context", "question"]
                        )

                        chain = LLMChain(llm=llm, prompt=prompt)
                        answer = chain.run(context=context, question=question)
                    except Exception as e:
                        answer = f"Error using OpenAI: {e}\n\nFalling back to context:\n{context[:500]}..."
                else:
                    # Use simple context-based answer
                    answer = f"""Based on the retrieved documents:\n\n{context[:800]}...\n\n💡 **Tip**: Enable OpenAI in the sidebar for AI-powered comprehensive answers."""

                # Add assistant message
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer,
                    "sources": sources
                })

                # Display answer
                display_chat_message("assistant", answer, sources)
        else:
            st.error("RAG system not initialized. Please check your document folders.")

    # Example questions
    if len(st.session_state.messages) == 0:
        st.markdown("### 💭 Try asking:")
        example_questions = [
            "What are the eligibility requirements for mentors?",
            "How do I report financial data?",
            "What are the roles and responsibilities?",
            "Tell me about subcontracting requirements",
            "What is the agreement approval process?"
        ]

        cols = st.columns(2)
        for i, eq in enumerate(example_questions):
            with cols[i % 2]:
                if st.button(eq, key=f"example_{i}"):
                    # Trigger query with example question
                    st.session_state.trigger_question = eq
                    st.rerun()

    # Handle triggered example questions
    if hasattr(st.session_state, 'trigger_question'):
        question = st.session_state.trigger_question
        delattr(st.session_state, 'trigger_question')
        st.rerun()

if __name__ == "__main__":
    main()
