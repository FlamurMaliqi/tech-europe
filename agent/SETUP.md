# Agent Setup Instructions

## Quick Start

### 1. Set up your environment

Create a `.env` file in the `agent/` directory:

```bash
cd agent
cp env.example .env
```

Then edit `.env` and add your API keys:
```bash
OPENAI_API_KEY=sk-your-openai-api-key-here
DATABASE_URL=sqlite:///./drive_thru.db
```

### 2. Run the Agent

Simply run:
```bash
./run_agent.sh
```

Or manually:
```bash
uv run python -m drive_thru.agent console
```

The agent will start in console mode for interactive testing.

## Alternative: Development Mode

For development with file watching:
```bash
python3 scripts/run_agent.py dev
```

## User Profile System

The agent has access to 20 pre-generated user profiles stored in the Kontext vector database.

### Test with User Profiles

When running the agent, customers can identify themselves by:
- **User ID**: "Hi, my user ID is 2"
- **Name**: "Hi, I'm Avery"

The agent will:
- Look up their profile
- Welcome them personally
- Show their dietary preferences
- Suggest items based on order history
- Display available coupons

### Sample User IDs

- User ID 1: Phoenix Thomas (Keto diet)
- User ID 2: Avery Anderson (Vegetarian)  
- User ID 3: Riley Taylor (Gluten-free)
- User ID 5: Emery King (No special diet)
- User ID 10: Blake Martinez (No special diet)

## Regenerating User Profiles

To regenerate the fake user profiles:

```bash
cd agent
python3 scripts/generate_fake_user_profiles.py
```

This will create 20 new user profiles and store them in the Kontext vector database.

