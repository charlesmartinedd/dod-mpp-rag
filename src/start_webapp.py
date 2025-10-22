"""Simple script to start the web application."""
import os
import subprocess
import sys

def main():
    """Start the Streamlit web application."""
    print("=" * 60)
    print("Starting DoD MPP RAG Web Application")
    print("=" * 60)
    print("\nThe web interface will open in your browser...")
    print("Press Ctrl+C to stop the server\n")

    # Get the directory of this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    web_app_path = os.path.join(script_dir, "web_app.py")

    # Start Streamlit
    try:
        subprocess.run([
            sys.executable, "-m", "streamlit", "run",
            web_app_path,
            "--server.port=8501",
            "--server.address=localhost"
        ])
    except KeyboardInterrupt:
        print("\n\nShutting down web application. Goodbye!")
    except Exception as e:
        print(f"\nError starting web application: {e}")
        print("\nTry running manually:")
        print(f"  streamlit run {web_app_path}")

if __name__ == "__main__":
    main()
