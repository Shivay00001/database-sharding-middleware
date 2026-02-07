from typing import Dict, Any

class MockShard:
    def __init__(self, shard_id: str):
        self.id = shard_id
        self.data: Dict[str, Any] = {}

    def put(self, key: str, value: Any):
        print(f"[{self.id}] WRITE {key} = {value}")
        self.data[key] = value

    def get(self, key: str) -> Any:
        val = self.data.get(key)
        print(f"[{self.id}] READ {key} -> {val}")
        return val

    def __repr__(self):
        return f"Shard({self.id}, items={len(self.data)})"
