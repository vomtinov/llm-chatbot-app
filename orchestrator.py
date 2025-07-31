import os
import signal
import sys
import time
import subprocess
from dotenv import load_dotenv

def main():
    # Load .env (for local dev) if present
    load_dotenv(override=False)

    # Ports
    api_port = int(os.getenv("API_PORT", "8000"))
    # Azure App Service sets PORT for the single public port; we bind Streamlit to it if present
    public_port = int(os.getenv("PORT", os.getenv("STREAMLIT_PORT", "8501")))

    env = os.environ.copy()

    # Start FastAPI (uvicorn) as a child process
    api_cmd = [sys.executable, "-m", "uvicorn", "app.api:app",
               "--host", "0.0.0.0", "--port", str(api_port)]
    api_proc = subprocess.Popen(api_cmd, env=env)

    # Start Streamlit as a child process
    st_cmd = ["streamlit", "run", "app/streamlit_app.py",
              "--server.address=0.0.0.0", "--server.port", str(public_port)]
    st_proc = subprocess.Popen(st_cmd, env=env)

    def shutdown(signum, frame):
        for p in [st_proc, api_proc]:
            try:
                p.terminate()
            except Exception:
                pass
        # Give them a moment to exit
        time.sleep(2)
        for p in [st_proc, api_proc]:
            try:
                p.kill()
            except Exception:
                pass
        sys.exit(0)

    signal.signal(signal.SIGINT, shutdown)
    signal.signal(signal.SIGTERM, shutdown)

    # Wait for either to exit; if one dies, stop the other
    while True:
        st_ret = st_proc.poll()
        api_ret = api_proc.poll()
        if st_ret is not None or api_ret is not None:
            shutdown(None, None)
        time.sleep(1)

if __name__ == "__main__":
    main()
