from client import OpenSourceVoiceAiAgentInfrastructureBuilderClient

def main():
    client = OpenSourceVoiceAiAgentInfrastructureBuilderClient()
    res = client.build_pipeline("outbound", {"name": "Nova", "tone": "professional", "language": "en-US"})
    cfg = res["agent_pipeline_config"]
    print(f"Voice Agent: {cfg['persona_name']} ({cfg['call_type']} calls)")
    print(f"STT: {cfg['stt_engine']} | TTS: {cfg['tts_engine']}")
    print(f"LLM Router: {cfg['llm_router']}")
    print(f"Estimated Latency: {res['estimated_latency_ms']}ms | Cost: ${res['cost_per_minute_usd']}/min")

if __name__ == "__main__":
    main()
