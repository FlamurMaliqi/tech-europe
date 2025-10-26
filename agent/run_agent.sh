#!/bin/bash

# Setup script for running the Drive-Thru Agent

echo "🚀 Starting McDonald's Drive-Thru Agent"
echo ""

# Check if .env exists
if [ ! -f .env ]; then
    echo "⚠️  No .env file found. Creating from template..."
    cp env.example .env
    echo ""
    echo "❌ Please edit .env and add your API keys:"
    echo "   - OPENAI_API_KEY (required)"
    echo "   - Optional: Kontext API keys for user profiles"
    echo ""
    echo "Edit .env and run this script again."
    exit 1
fi

# Load environment variables
source .env

# Check if OpenAI API key is set
if [ -z "$OPENAI_API_KEY" ]; then
    echo "❌ OPENAI_API_KEY is not set in .env file"
    echo "Please add your OpenAI API key to the .env file"
    exit 1
fi

echo "✅ Environment loaded"
echo ""

# Run the agent in console mode
echo "Starting agent in console mode..."
echo "Press [Ctrl+B] to toggle between Text/Audio mode, [Q] to quit."
echo ""

uv run python -m drive_thru.agent console

