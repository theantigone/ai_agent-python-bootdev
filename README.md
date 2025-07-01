# Custom-built Agentic AI using Google Gemini's API
<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [Prerequisites](#prerequisites)
- [Running the Agentic AI](#running-the-agentic-ai)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Prerequisites

1. Open your terminal, then copy-paste this command to clone this project (download this project) to your computer:

```bash
git clone https://github.com/theantigone/bootdev-ai-agent.git
```

2. Change the current directory to the root of this project:

```bash
cd bootdev-ai-agent/
```

3. Create a virtual environment using [`uv`](https://github.com/astral-sh/uv) at the root of this project directory:

```bash
# install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# initialise uv
uv init

# create the virtual environment
uv venv
```

4. Activate the virtual environment:

```bash
source .venv/bin/activate
```

> [!NOTE]
> You should see `(venv)` at the beginning of your terminal prompt:
> ```bash
> (venv) user@host $
> ```

5. Install the necessary Python [`uv`](https://github.com/astral-sh/uv) packages to run the agentic AI:

```bash
uv add -r requirements.txt
```

6. Create a [Gemini API key](https://ai.google.dev/gemini-api/docs/api-key) if you don't already have one.

7. Create a `.env` file at the root of this project, then paste your Gemini API key into it as so:

```
GEMINI_API_KEY="your_api_key_here"
```

Replace `"your_api_key_here"` with your actual Gemini API key.

## Running the Agentic AI

Run:
```bash
uv run main.py
```
to see results.
