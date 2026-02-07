from src.router import ConsistentHashRouter
from src.shard_manager import MockShard
import time

def main():
    print("--- Database Sharding Middleware Demo ---")
    
    # Initialize Shards
    shard_names = ["shard-us-east", "shard-us-west", "shard-eu-central"]
    shards = {name: MockShard(name) for name in shard_names}
    
    # Initialize Router
    router = ConsistentHashRouter(nodes=shard_names, replicas=5)
    print(f"Initialized Router with {len(shard_names)} shards.")

    # Write Data
    users = ["user_123", "user_456", "user_789", "user_abc", "user_xyz", "admin_001"]
    print("\n--- Distributing Data ---")
    for user_id in users:
        target_shard_id = router.get_node(user_id)
        target_shard = shards[target_shard_id]
        target_shard.put(user_id, {"name": f"Name_{user_id}", "active": True})

    # Verify Distribution
    print("\n--- Shard Distribution ---")
    for s in shards.values():
        print(s)

    # Read Data
    print("\n--- Reading Data ---")
    query_id = "user_456"
    target = router.get_node(query_id)
    print(f"Router says {query_id} is on {target}")
    shards[target].get(query_id)

    # Simulation Node Failure
    print("\n--- Simulating Node Failure (shard-us-east) ---")
    router.remove_node("shard-us-east")
    failures_moved = 0
    # In a real system we would need to migrate data. 
    # Here we show where the router *now* points for the same keys.
    for user_id in users:
        target_shard_id = router.get_node(user_id)
        if target_shard_id != "shard-us-east":
             # If it originally mapped to east, now it maps somewhere else
             pass
        print(f"Key {user_id} now maps to -> {target_shard_id}")

if __name__ == "__main__":
    main()
