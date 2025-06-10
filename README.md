# Agentic AI using Google's Gemini API

## How to run
1. Change directory to the root of this directory, then initialise the Python virtual environment:
```bash
python3 -m venv venv
```
2. Activate the virtual environment:
```bash
source venv/bin/activate
```
You should see `(venv)` at the beginning of your terminal prompt:
```bash
(venv) user@machine $ 
```
3. Install the necessary Python `pip` packages:
```bash
pip install -r requirements
```
4. Create a [Gemini API key] if you don't already have one
5. Create a `.env` file at the root of this project, then paste your Gemini API key into it as so:
```
GEMINI_API_KEY="your_api_key_here"
```
Replace `"your_api_key_here"` with your actual Gemini API key.

6. Voila!
