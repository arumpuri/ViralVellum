# ViralVellum

## Overview

ViralVellum is an open-source multi-agent system powered by crewAI that automates the creation of engaging history scripts for YouTube channels. Tired of dry timelines and boring lectures? This AI "crew" researches forgotten facts, weaves them into gripping narratives, boosts them with hooks and SEO magic, and polishes them for prime-time virality.

## Why ViralVellum?

✅ **Viral Potential**: Agents optimize for YouTube's algorithm—think surprise twists, humor, and shareable moments.

🔄 **Modular & Extensible**: Configurable via YAML for easy tweaks; add agents or tools as your channel grows.

🔍 **Fact-First Fun**: Built-in research and fact-checking to keep history accurate (and you lawsuit-free).

## Features

- **Agent Crew**: 6 specialized agents (Researcher, Storyteller, SEO Optimizer, Engagement Booster, Visual Suggestor, Editor)
- **Tool Integration**: Web search via Serper for real-time facts and trends
- **Sequential Workflow**: Research → Narrate → Optimize → Engage → Visualize → Polish
- **Customizable**: Edit `config/agents.yaml` and `config/tasks.yaml` to fit your style
- **Output**: Full script with embedded notes for production (aims for 10-15 min videos)

## Quick Start

### Prerequisites

- Python 3.8+
- **API Keys**:
  - OpenAI (for LLM): Set `OPENAI_API_KEY` env var
  - Serper (for web search): Set `SERPER_API_KEY` env var (free tier at [serper.dev](https://serper.dev))

### Installation

```
git clone https://github.com/yourusername/ViralVellum.git
cd ViralVellum
pip install -r requirements.txt
```
### Usage
```
python main.py
```

## Project Structure
```text
ViralVellum/
├── config/
│   ├── agents.yaml     # Agent definitions (roles, goals, tools)
│   └── tasks.yaml      # Task workflows
├── main.py             # Core script: Loads YAML, builds crew, runs
├── requirements.txt    # Dependencies
└── README.md           # You're reading it!
