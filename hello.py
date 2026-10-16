import json
from pathlib import Path

CASES_PATH = Path(__file__).parent / "data" / "cases.jsonl"


def fake_agent(prompt: str) -> str:
    """假 agent：不调用任何模型，只按规则返回答案。之后换成真 LLM 时，只改这个函数。"""
    if "1+1" in prompt:
        return "2"
    return "I don't know"


def load_cases(path: Path = CASES_PATH) -> list[dict]:
    """读取 JSONL 用例文件，每行一个用例，跳过空行。"""
    with path.open(encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


if __name__ == "__main__":
    for case in load_cases():
        print(f"[{case['id']}] {case['utterance']}  → 期望 {len(case['expected_tasks'])} 个任务")
