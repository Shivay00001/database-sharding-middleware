# Database Sharding Middleware

[![Python 3.11](https://img.shields.io/badge/Python-3.11-3776AB.svg)](https://www.python.org/)
[![Architecture](https://img.shields.io/badge/Pattern-Sharding-orange.svg)](https://martinfowler.com/articles/sharding.html)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A **production-grade database middleware** implementation demonstrating horizontal scaling via sharding. This repository features a **Consistent Hashing** router to distribute data across multiple database nodes with minimal rebalancing.

## 🚀 Features

- **Consistent Hashing Router**: Distributes keys evenly across shards using a virtual node ring.
- **Dynamic Scaling**: Supports adding/removing shards with minimal data movement.
- **Fault Tolerance**: mock implementation of failover (routing to next available node).
- **CRUD Operations**: Basic Put/Get interface routed transparently to the correct shard.
- **Replication**: Optional parameter to simulate replication factor.

## 📁 Project Structure

```
database-sharding-middleware/
├── src/
│   ├── router.py         # Consistent Hashing Logic
│   ├── shard_manager.py  # Mock DB Node
│   └── main.py           # CLI Entrypoint
├── requirements.txt
└── Dockerfile
```

## 🛠️ Quick Start

```bash
# Clone
git clone https://github.com/Shivay00001/database-sharding-middleware.git

# Install
pip install -r requirements.txt

# Run Middleware
python src/main.py
```

## 📄 License

MIT License
