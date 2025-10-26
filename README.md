# 🍟 McDonald's Drive-Thru AI Agent

<div align="center">

**Built for Tech Europe Munich Hackathon | {Tech: Europe} Munich**

An intelligent voice-powered drive-thru ordering system with real-time analytics and conversation insights.

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![Next.js](https://img.shields.io/badge/Next.js-16-black.svg)](https://nextjs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104-green.svg)](https://fastapi.tiangolo.com/)
[![LiveKit](https://img.shields.io/badge/LiveKit-0.10-red.svg)](https://livekit.io/)

</div>

## 📋 Overview

This project is an end-to-end AI-powered drive-thru ordering system that combines voice agents with comprehensive analytics. The system enables natural conversation ordering at McDonald's drive-thrus while providing restaurant staff with real-time insights into customer interactions and order processing.

### Key Features

- 🎤 **Voice Agent**: LiveKit-powered conversational AI for natural drive-thru interactions
- 📊 **Real-Time Dashboard**: Next.js web interface for monitoring orders and conversations
- 📈 **Analytics Engine**: Sentiment analysis, conversation metrics, and business intelligence
- 🎟️ **Coupon System**: Smart coupon and promotion handling
- 🗄️ **Data Pipeline**: Automated conversation analysis and order tracking
- 🔄 **REST API**: FastAPI backend for dashboard and integrations

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         Voice Agent Layer                         │
│  (LiveKit + OpenAI STT/TTS + Conversational AI + Menu Logic)    │
└────────────────────────────┬────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      Data Pipeline Layer                          │
│  (Conversation Analysis + Sentiment Scoring + Order Processing)  │
└────────────────────────────┬────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                         Database Layer                            │
│            (PostgreSQL/SQLite with SQLAlchemy ORM)               │
└────────────────────────────┬────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      API & Dashboard Layer                        │
│  (FastAPI REST API + Next.js Dashboard with Real-time Updates)  │
└─────────────────────────────────────────────────────────────────┘
```

## 📁 Project Structure

```
tech-europe/
├── agent/                          # Backend services
│   ├── drive_thru/                # Core application
│   │   ├── agent.py               # LiveKit voice agent
│   │   ├── api.py                 # FastAPI REST API
│   │   ├── database.py            # Menu and database operations
│   │   ├── database_config.py     # Database configuration
│   │   ├── models.py              # SQLAlchemy models
│   │   ├── order.py               # Order state management
│   │   ├── data_pipeline.py       # Data processing pipeline
│   │   ├── conversation_analyzer.py  # AI analysis tools
│   │   └── data_validator.py      # Data validation
│   ├── scripts/                   # Utility scripts
│   │   ├── init_database.py       # Database initialization
│   │   ├── run_agent.py           # Agent runner
│   │   └── run_api.py             # API server
│   ├── tests/                     # Test suite
│   └── docs/                      # Documentation
├── dashboard/                      # Frontend dashboard
│   ├── src/
│   │   ├── app/                   # Next.js app router pages
│   │   │   ├── page.tsx           # Main dashboard
│   │   │   ├── orders/            # Orders page
│   │   │   └── metrics/           # Analytics page
│   │   ├── components/            # React components
│   │   │   ├── orders-table.tsx   # Order display
│   │   │   ├── conversation-list.tsx  # Conversation viewer
│   │   │   ├── analytics-chart.tsx    # Charts and graphs
│   │   │   └── metrics-card.tsx       # Metrics cards
│   │   └── lib/
│   │       ├── api.ts             # API client
│   │       └── utils.ts           # Utilities
│   └── package.json
└── README.md
```

## 🚀 Quick Start

### Prerequisites

- **Python 3.12+** with `uv` package manager ([install uv](https://docs.astral.sh/uv/))
- **Node.js 18+** and npm
- **OpenAI API Key** (for voice processing)
- **PostgreSQL** (optional, SQLite works by default)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd tech-europe
   ```

2. **Set up the backend agent**
   ```bash
   cd agent
   
   # Install Python dependencies
   uv pip install -e .
   
   # Create .env file with your API keys
   cp .env.example .env
   # Edit .env and add: OPENAI_API_KEY=your-key-here
   
   # Initialize the database
   python scripts/init_database.py
   ```

3. **Set up the frontend dashboard**
   ```bash
   cd ../dashboard
   
   # Install Node dependencies
   npm install
   ```

### Running the System

**Terminal 1: Start the voice agent**
```bash
cd agent
uv run python scripts/run_agent.py
```

**Terminal 2: Start the API server**
```bash
cd agent
uv run python scripts/run_api.py
```

**Terminal 3: Start the dashboard**
```bash
cd dashboard
npm run dev
```

Open your browser to [http://localhost:3000](http://localhost:3000) to see the dashboard!

## 🎯 Usage

### Using the Voice Agent

The agent runs in console mode for easy testing. Simply start it and interact naturally:

```bash
cd agent
uv run python -m drive_thru.agent console
```

Example conversation:
```
Agent: "Welcome to McDonald's! What can I get for you today?"
Customer: "I'd like a Big Mac combo with medium fries and a Coke"
Agent: "Got it! A Big Mac combo with medium fries and Coca-Cola. Anything else?"
Customer: "That's all, thanks"
Agent: "Your total is $12.99. Please pull forward to the first window."
```

### Dashboard Features

The dashboard provides real-time monitoring of:

- 📦 **Incoming Orders**: Live order display with details
- 💬 **Conversation Transcripts**: Full conversation history
- 📊 **Analytics**: Sentiment analysis, success rates, and metrics
- 📈 **Trends**: Popular items, revenue, and performance over time

### API Endpoints

The FastAPI server exposes several endpoints:

- `GET /health` - Health check
- `GET /conversations` - List conversations
- `GET /orders` - List orders
- `GET /metrics/summary` - Business metrics
- `GET /items/popular` - Popular items

See [docs/API.md](agent/docs/API.md) for full API documentation.

## 🧪 Testing

Run the test suite:

```bash
cd agent
python -m pytest tests/
```

Key test files:
- `test_complete_flow.py` - End-to-end workflow tests
- `test_conversation_analysis.py` - Conversation analytics tests
- `test_natural_completion.py` - Natural language handling tests
- `test_simple_conversation.py` - Basic conversation tests

## 📊 Data Points Captured

The system tracks comprehensive metrics:

### Order Metrics
- Order details (items, quantities, sizes)
- Order success rate
- Total price and discounts
- Applied coupons
- Timestamps

### Conversation Metrics
- Full transcript with turn-by-turn dialogue
- Conversation duration
- Total turns (agent + customer)
- Sentiment score (-1.0 to 1.0)
- Success status
- Customer satisfaction rating (1-5)
- Customer feedback

### Business Intelligence
- Popular items and combos
- Revenue tracking
- Daily summaries
- Error rates
- Tool call success rates

## 🎁 Bonus Features

- ✅ **Observability**: Comprehensive logging and metrics collection
- ✅ **Error Handling**: Robust error recovery and graceful degradation
- ✅ **Customer Feedback**: End-of-conversation feedback collection
- ✅ **Coupon Support**: Smart handling of BOGO deals and promotions
- ✅ **Scalability**: Designed for multi-location deployment

## 🌐 Deployment

For production deployment, see [docs/DEPLOYMENT.md](agent/docs/DEPLOYMENT.md).

Key deployment options:
- **Docker**: Containerized deployment with Docker Compose
- **PostgreSQL**: Production-grade database
- **Redis**: Session management and caching
- **LiveKit Cloud**: Managed voice infrastructure

## 🤝 Contributing

This project was built for the Tech Europe Munich Hackathon. Contributions and improvements are welcome!

## 📝 License

This project is part of the Tech Europe Munich Hackathon.

## 🙏 Acknowledgments

- **LiveKit** for the powerful voice agent framework
- **OpenAI** for speech-to-text and conversation AI
- **FastAPI** for the high-performance API framework
- **Next.js** for the modern dashboard framework
- **McDonald's** for the use case inspiration

---

<div align="center">
  
**Built with ❤️ at Tech Europe Munich Hackathon**

{Tech: Europe} Munich | 2025

</div>
