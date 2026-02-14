# AI ChatBot Project

A conversational AI chatbot built with LangChain and Chroma vector database, designed to provide intelligent responses based on restaurant reviews and customer data.

## Project Overview

This project implements an AI-powered chatbot that leverages:
- **LangChain** for orchestrating language model interactions
- **Chroma** vector database for semantic search and retrieval
- **Vector embeddings** for intelligent context understanding
- **Restaurant reviews dataset** for knowledge base

## Tech Stack

- **Python 3.x**
- **LangChain** - LLM orchestration framework
- **Chroma** - Vector database for semantic search
- **FastAPI/Flask** - Web framework (if applicable)
- **OpenAI/Hugging Face** - Language models

## Project Structure

```
.
├── main.py                          # Main entry point
├── ChatBotUi.py                     # UI component for the chatbot
├── vector.py                        # Vector embedding and management
├── realistic_restaurant_reviews.csv # Restaurant reviews dataset
├── chrome_langchain_db/             # Chroma vector database storage
├── requirements.txt                 # Project dependencies
├── .gitignore                       # Git ignore rules
└── README.md                        # This file
```

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd AI_Agent
   ```

2. **Create and activate virtual environment**
   ```bash
   # Windows
   python -m venv myenv
   myenv\Scripts\activate

   # Linux/Mac
   python3 -m venv myenv
   source myenv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Chatbot

```bash
python main.py
```

### Starting the UI

```bash
python ChatBotUi.py
```

## File Descriptions

- **main.py** - Core application logic and initialization
- **ChatBotUi.py** - User interface for interacting with the chatbot
- **vector.py** - Handles vector embeddings and similarity search
- **realistic_restaurant_reviews.csv** - Dataset containing restaurant reviews used for training/context
- **chrome_langchain_db/** - Persisted Chroma vector database with embeddings

## Configuration

Before running the project, ensure you have:
- API keys for LLM services (if applicable) in environment variables
- Proper Python version installed
- All dependencies from `requirements.txt`

## Features

- Semantic search using vector embeddings
- Context-aware responses based on restaurant reviews
- Interactive chatbot interface
- Persistent vector database storage

## Contributing

1. Create a feature branch
2. Make your changes
3. Commit with clear messages
4. Push to the repository

## License

[Add license information here]

## Support

For issues or questions, please create an issue in the repository.
