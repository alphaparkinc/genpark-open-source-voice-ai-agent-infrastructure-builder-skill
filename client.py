class OpenSourceVoiceAiAgentInfrastructureBuilderClient:
    def build_pipeline(self, call_type: str = "inbound", voice_persona_config: dict = None) -> dict:
        voice_persona_config = voice_persona_config or {}
        persona = voice_persona_config.get("name", "Aria")
        return {
            "agent_pipeline_config": {
                "stt_engine": "whisper-large-v3",
                "llm_router": "claude-3-haiku (fast path) → claude-3-5-sonnet (complex queries)",
                "tts_engine": "cartesia-sonic",
                "vad_model": "silero-vad-v5",
                "persona_name": persona,
                "call_type": call_type,
                "max_concurrent_calls": 200
            },
            "estimated_latency_ms": 680,
            "cost_per_minute_usd": 0.043
        }
