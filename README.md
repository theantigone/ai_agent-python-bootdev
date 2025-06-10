# Custom-built Agentic AI using Google Gemini's API

## How to play with Google Gemini's API

1. Open your terminal, then copy-paste this command to clone this project (download this project) to your computer:

```bash
git clone https://github.com/theantigone/bootdev-ai-agent.git
```

2. Change the current directory to the root of this project:

```bash
cd bootdev-ai-agent/
```

3. Create a virtual environment at the root of this project directory:

```bash
python3 -m venv venv
```

4. Activate the virtual environment:

```bash
source venv/bin/activate
```

> [!NOTE]
> You should see `(venv)` at the beginning of your terminal prompt:
> ```bash
> (venv) user@machine $
> ```

5. Install the necessary Python `pip` packages to run the agentic AI:

```bash
pip install -r requirements
```

6. Create a [Gemini API key](https://ai.google.dev/gemini-api/docs/api-key) if you don't already have one.

7. Create a `.env` file at the root of this project, then paste your Gemini API key into it as so:

```
GEMINI_API_KEY="your_api_key_here"
```

Replace `"your_api_key_here"` with your actual Gemini API key.

8. Voila!
