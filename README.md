# OllamaBOT

OllamaBOT is a simple chatbot powered by the Ollama platform. Follow the steps below to set it up and start using it.

## Prerequisites

1. Download and install [Ollama](https://ollama.com/).
2. Download any model from their repository. You can explore the available models [here](https://ollama.com/search).

---

## Steps to Get Started

### Install Ollama and a Model
1. Open your terminal.
2. To download and use the **Llama 3.1** model, run:
   ```bash
   ollama run llama3.1
   ```

---

### Python Setup

#### Step 1: Create a Virtual Environment
1. Create a virtual environment:
   ```bash
   python -m venv ollama_env
   ```
   On Linux or macOS:
   ```bash
   python3 -m venv ollama_env
   ```
2. Activate the virtual environment:
   - On Windows:
     ```bash
     ollama_env\Scripts\activate
     ```
   - On Linux/macOS:
     ```bash
     source ollama_env/bin/activate
     ```

#### Step 2: Install Required Libraries
Run the following command to install the necessary Python libraries:
```bash
pip install langchain langchain_ollama ollama
```

#### Step 3: Run the Chatbot
Save your chatbot script as `bot.py` and run it using the following commands:
- On Windows:
  ```bash
  python bot.py
  ```
- On Linux/macOS:
  ```bash
  python3 bot.py
  ```

---

## Additional Information
- Visit [Ollama's website](https://ollama.com/) for more details on using the platform.
- For issues or contributions, refer to the [Ollama GitHub repository](https://github.com/ollama).

---

Enjoy building and interacting with your chatbot using OllamaBOT!
