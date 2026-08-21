# genpark-open-source-voice-ai-agent-infrastructure-builder-skill

![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue) ![License MIT](https://img.shields.io/badge/license-MIT-green) ![MCP Compatible](https://img.shields.io/badge/MCP-Compatible-purple) ![GenPark AI](https://img.shields.io/badge/GenPark-AI--Agent--Skill-orange)

> **GenPark AI Agent Skill** -- Self-hosted voice AI agent infrastructure builder for inbound/outbound calling with STT, TTS, LLM routing (Dograh style)

## Quick Start
```python
python example_usage.py
```

## 📊 Agentic Architecture Flowchart
```mermaid
graph LR
  User([User / AI Agent]) -->|JSON Request| Skill[GenPark AI Skill]
  Skill -->|Execution Logic| CoreEngine[Core Processing Engine]
  CoreEngine -->|Structured Output| User
```

## 🔌 MCP Integration
```bash
python mcp_server.py
```
