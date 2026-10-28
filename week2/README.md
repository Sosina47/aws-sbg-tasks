# Mini Semantic Search

## Overview

This project is a simple FAQ semantic search system built with Python, Pandas, Sentence Transformers, and ChromaDB. It allows users to search frequently asked questions (FAQs) by meaning rather than relying only on exact keyword matches.

## How It Works

1. **Load the data:** Create a small FAQ dataset containing questions and answers using Pandas.
2. **Clean the text:** Convert text to lowercase, remove punctuation, trim extra spaces, and normalize whitespace.
3. **Create chunks:** Combine each question and its answer into one searchable text chunk.
4. **Generate embeddings:** Use the `all-MiniLM-L6-v2` model to convert each chunk into a numerical vector representing its meaning.
5. **Store the data:** Save the FAQ text, IDs, and embeddings in a ChromaDB collection.
6. **Search:** Convert a user's query into an embedding and retrieve the three most similar FAQ chunks from ChromaDB.

## Technologies Used

- **Python** — Main programming language
- **Pandas** — Data preparation and text cleaning
- **Sentence Transformers** — Text embedding generation
- **ChromaDB** — Vector storage and similarity search
- **Google Colab** — Development and execution environment

## Example

**Search query:**

"I forgot my password. How can I get back into my account?"

The system retrieves the three closest FAQ matches, including questions related to resetting a password or recovering account access.

## Purpose

This project demonstrates the basic workflow of semantic search: data preparation, chunking, embedding generation, vector storage, and similarity-based retrieval. It is a beginner-friendly introduction to techniques also used in retrieval-augmented generation (RAG) systems.

## Note

The project uses a small sample FAQ dataset and an in-memory ChromaDB collection. The stored data is temporary and may be lost when the runtime resets.
