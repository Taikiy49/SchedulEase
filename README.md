<div align="center">
  <h1>SchedulEase</h1>
  <p><strong>React and Flask scheduling-chat prototype powered by Gemini.</strong></p>
  <p>
    <img alt="React" src="https://img.shields.io/badge/React-303840?style=flat-square" />
    <img alt="Flask" src="https://img.shields.io/badge/Flask-303840?style=flat-square" />
    <img alt="Gemini" src="https://img.shields.io/badge/Gemini-303840?style=flat-square" />
  </p>
  <p><a href="#overview">Overview</a> · <a href="#getting-started">Getting started</a> · <a href="#repository-map">Repository map</a></p>
</div>

---

## Overview

An experimental scheduling assistant with a React chat interface and a Flask backend. The model is prompted to turn scheduling requests into structured day, time, name, and activity responses.

## What’s inside

- Conversational scheduling through a browser chat interface.
- A Flask `POST /send-message` endpoint.
- Prompt and generation settings separated from the server.

## Getting started

Use Node.js and Python 3. Start the backend:

```sh
python -m pip install Flask flask-cors google-generativeai
export GEMINI_API_KEY="your-own-api-key"
cd backend
python server.py
```

In another terminal:

```sh
cd frontend
npm ci
npm start
```

The backend uses Flask’s default development port 5000. Review the frontend endpoint configuration for your local environment.

## Repository map

| Location | Purpose |
| --- | --- |
| [`frontend/src/`](./frontend/src/) | Chat interface and side menu |
| [`backend/server.py`](./backend/server.py) | Message endpoint |
| [`backend/chatbot_settings.py`](./backend/chatbot_settings.py) | Gemini initialization |
| [`backend/ai_training.py`](./backend/ai_training.py) | Prompt and generation settings |
| [`backend/google_calendar.py`](./backend/google_calendar.py) | Empty integration placeholder |

## Project status

Prototype. Google Calendar synchronization is not implemented. The backend maintains a shared model session and uses a historical Gemini model identifier. Previously committed credentials require rotation.
