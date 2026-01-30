# Cloud Computing Lab 2 - Monolithic Architecture

## Student Details
- **Name**: Chetan H S
- **SRN**: PES1UG23CS161
- **Section**: C

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
- **Optimization**: Replaced the manual loop with the Python `sum()` function to handle checkout calculations more efficiently.
- **Performance**: Stable at ~7ms.
- **Note**: The response time did not significantly decrease because the host machine (MacBook Pro) processed the code too quickly for the original inefficiency to be a bottleneck.

### /events Route
- **Optimization**: Removed a wasteful computational loop (`for i in range(3000000): waste += i % 3`) that performed unnecessary modulo operations.
- **Performance**: Changed from ~102ms to ~105ms.
- **Note**: Similar to the checkout route, the powerful hardware of the host machine (MacBook Pro) masked the performance gain, resulting in stable response times despite the optimization.

### /my-events Route
- **Optimization**: Removed a wasteful loop (`for _ in range(1500000): dummy += 1`) that performed unnecessary increment operations.
- **Performance**: Improved from ~50ms to ~47ms (approx. 6% improvement).