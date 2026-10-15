def fake_agent(prompt: str) -> str:
    """假 agent：不调用任何模型，只按规则返回答案。之后换成真 LLM 时，只改这个函数。"""
    if "1+1" in prompt:
        return "2"
    return "I don't know"


if __name__ == "__main__":
    for q in ["What is 1+1?", "What is the capital of France?"]:
        print(f"Q: {q}\nA: {fake_agent(q)}\n")
