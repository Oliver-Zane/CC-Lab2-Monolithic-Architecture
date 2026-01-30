# Cloud Computing Lab 2 - Monolithic Architecture

## Student Details
- [cite_start]**Name**: Chetan H S [cite: 3]
- [cite_start]**SRN**: PES1UG23CS161 [cite: 4]
- [cite_start]**Section**: C [cite: 5]

## Lab Overview
This lab demonstrates monolithic architecture concepts including:
- Single point of failure
- Load testing with Locust
- Performance optimization

## Setup Instructions
1. Create virtual environment: `python3 -m venv .venv`
2. Activate: `source .venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Initialize database: `python insert_events.py`
5. Run server: `uvicorn main:app --reload`

## Optimizations Made

### /checkout Route
- **Optimization**: Optimized logic to handle checkout requests more efficiently (demonstrated in SS4/SS5).
- [cite_start]**Performance**: Stable at ~7ms[cite: 99, 158].
- **Note**: The response time did not significantly decrease because the host machine (MacBook Pro) processed the code too quickly for the original inefficiency to be a bottleneck.

### /events Route
- [cite_start]**Optimization**: Removed a wasteful computational loop (`for i in range(3000000): waste += i % 3`) that performed unnecessary modulo operations[cite: 469, 470].
- [cite_start]**Performance**: Changed from ~102ms to ~105ms[cite: 369].
- [cite_start]**Note**: Similar to the checkout route, the powerful hardware of the host machine (MacBook Pro) masked the performance gain, resulting in stable response times despite the optimization[cite: 482].

### /my-events Route
- [cite_start]**Optimization**: Removed a wasteful loop (`for _ in range(1500000): dummy += 1`) that performed unnecessary increment operations[cite: 484, 487].
- [cite_start]**Performance**: Improved from ~50ms to ~47ms (approx. 6% improvement)[cite: 498].

## Screenshots
All screenshots (SS1-SS9) are included in the `screenshots/` folder.