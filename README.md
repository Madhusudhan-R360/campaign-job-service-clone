# Campaign Job Service Clone

A simplified clone of an enterprise Campaign Job Service built using FastAPI, MongoDB, and Redis.

This project is designed to replicate the core automation and maintenance responsibilities of a production Campaign Job Service. The service focuses on executing background business operations such as analytics generation, user lifecycle management, order reconciliation, monitoring, and reporting.

---

# Project Overview

The Campaign Job Service acts as the operational backbone of the campaign ecosystem.

Unlike customer-facing services, this service performs internal jobs that automate maintenance and reporting workflows.

Current implementation:

- FastAPI Foundation
- MongoDB Integration
- Redis Integration
- Environment Configuration
- Health Check Endpoint

Planned implementation:

- Analytics Module
- User Lifecycle Jobs
- Order Reconciliation Jobs
- Reminder Jobs
- Monitoring & Alerting
- Dockerization

---

# Architecture

```text
                     Campaign CMS
                           |
                           |
                           v

                Campaign Job Service Clone
                           |
        -----------------------------------------
        |                |                     |
        v                v                     v

   Analytics      User Lifecycle      Monitoring Jobs
      Jobs             Jobs
                           |
                           |
                           v

                        MongoDB
                           |
                           v

                         Redis
```

---

# Project Structure

```text
campaign-job-service-clone/

├── api/
│
├── db/
│   ├── config.py
│   └── connection.py
│
├── services/
│
├── utils/
│
├── main.py
│
├── requirements.txt
│
├── .env
│
├── .gitignore
│
└── README.md
```

---

# Technologies Used

- FastAPI
- MongoDB
- Motor
- Redis
- Pydantic Settings
- Python Dotenv
- Uvicorn

---

# Features Implemented

## Phase 1 - Foundation Setup

Implemented:

✅ FastAPI Application

✅ MongoDB Connection

✅ Redis Connection

✅ Environment Variables

✅ Health Check Endpoint

✅ Swagger Documentation

✅ Development Project Structure

---

# Environment Variables

Create a `.env` file in the project root.

```env
MONGO_URL=mongodb://localhost:27017

DATABASE_NAME=campaign_job_service

REDIS_HOST=localhost

REDIS_PORT=6379

REDIS_DB=0

ENVIRONMENT=DEV
```

---

# Installation

## Clone Repository

```bash
git clone <repository-url>

cd campaign-job-service-clone
```

---

## Create Virtual Environment

```bash
python3 -m venv venv
```

---

## Activate Virtual Environment

Linux / Mac

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Application Configuration

## db/config.py

The application loads configuration from environment variables using Pydantic Settings.

Configuration includes:

```text
MongoDB Connection

Redis Connection

Environment Configuration
```

---

# Database Connections

## MongoDB

MongoDB is configured through:

```python
AsyncIOMotorClient
```

Database:

```text
campaign_job_service
```

---

## Redis

Redis is configured through:

```python
redis.Redis()
```

and will be used for:

```text
Campaign Cache

Account Cache

Session Storage

Temporary Analytics Data
```

in future phases.

---

# Running The Application

Start the service:

```bash
uvicorn main:app --reload --port 8002
```

Application:

```text
http://localhost:8002
```

Swagger Documentation:

```text
http://localhost:8002/docs
```

---

# Health API

## Endpoint

```http
GET /health
```

Response:

```json
{
  "success": true
}
```

Purpose:

```text
Verify Service Health

Verify FastAPI Startup

Verify Deployment Status
```

---

# Swagger Documentation

Open:

```text
http://localhost:8002/docs
```

Available APIs:

```text
GET /health
```

---

# MongoDB Connection Test

Create:

```python
from db.connection import db

print(db.name)
```

Run:

```bash
python test_mongo.py
```

Expected Output:

```text
campaign_job_service
```

---

# Redis Connection Test

Create:

```python
from db.connection import redis_client

redis_client.set(
    "health",
    "ok"
)

print(
    redis_client.get("health")
)
```

Run:

```bash
python test_redis.py
```

Expected Output:

```text
ok
```

---

# Development Ports

Suggested local setup:

```text
Campaign CMS Clone           → 8000

Campaign Notification Clone  → 8001

Campaign Job Service Clone   → 8002
```

---

# Planned Modules

## Phase 2

Analytics Module

```text
Generate Campaign Analytics

Store Analytics Data

Retrieve Analytics Reports
```

Endpoints:

```http
POST /analytics/generate

GET /analytics

GET /analytics/{campaign_id}
```

---

## Phase 3

User Lifecycle Module

```text
Expire Users

Disable Users

Manage User Status
```

---

## Phase 4

Order Reconciliation Module

```text
Order Status Processing

Mock ERP Integration

Voucher Status Updates
```

---

## Phase 5

Reminder Module

```text
Expiry Reminder Jobs

Notification Triggers
```

---

## Phase 6

Monitoring Module

```text
Pending Order Alerts

Duplicate Claim Code Alerts

Operational Monitoring
```

---

## Phase 7

Dockerization & Final Verification

```text
Docker

Docker Compose

Mongo Container

Redis Container

Final Testing
```

---

# Project Progress

```text
✅ Phase 1 - Foundation Setup

⬜ Phase 2 - Analytics Module

⬜ Phase 3 - User Lifecycle Module

⬜ Phase 4 - Order Reconciliation Module

⬜ Phase 5 - Reminder Module

⬜ Phase 6 - Monitoring Module

⬜ Phase 7 - Dockerization & Final Verification
```

---

# Learning Outcomes

This project demonstrates:

- FastAPI Development
- MongoDB Integration
- Redis Integration
- Environment Configuration
- REST API Design
- Microservice Architecture
- Campaign Operations Automation
- Analytics Processing
- Background Job Design

---

# Final Objective

The Campaign Job Service Clone aims to simulate the automation layer of a campaign ecosystem.

```text
Campaign Data
       |
       v
Analytics Jobs
       |
       v
Lifecycle Jobs
       |
       v
Monitoring Jobs
       |
       v
Operational Reports
```

The project will ultimately provide a simplified but realistic implementation of an enterprise Campaign Job Service used for maintenance, analytics, monitoring, and automation workflows.