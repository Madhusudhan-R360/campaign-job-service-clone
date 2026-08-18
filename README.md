# Campaign Job Service Clone

A simplified clone of an enterprise Campaign Job Service built using FastAPI, MongoDB, and Redis.

This service represents the operational automation layer of a campaign ecosystem. It focuses on analytics generation, campaign maintenance, lifecycle automation, monitoring, and reporting jobs.

---

# Project Overview

The Campaign Job Service is an internal service responsible for:

- Campaign Analytics
- User Lifecycle Jobs
- Order Processing Jobs
- Reminder Jobs
- Monitoring & Alerting
- Operational Reporting

This project recreates those concepts in a simplified and learning-focused implementation.

---

# Current Progress

## ✅ Phase 1 - Foundation Setup

Implemented:

- FastAPI Application
- MongoDB Integration
- Redis Integration
- Environment Configuration
- Health Check API
- Swagger Documentation

---

## ✅ Phase 2 - Analytics Module

Implemented:

- Campaign Analytics Collection
- Generate Analytics API
- Get Analytics API
- Campaign Analytics Lookup
- MongoDB Persistence

---

# Project Structure

```text
campaign-job-service-clone/

├── api/
│   └── analytics/
│       ├── app.py
│       ├── schema.py
│       └── utility.py
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

# Architecture

```text
                     Campaign CMS
                           |
                           |
                           v

               Campaign Job Service Clone
                           |
      -----------------------------------------
      |                 |                     |
      v                 v                     v

 Analytics      Lifecycle Jobs      Monitoring
    Jobs

                           |
                           v

                        MongoDB
                           |
                           v

                         Redis
```

---

# Tech Stack

- FastAPI
- Python 3.12
- MongoDB
- Motor (Async MongoDB Driver)
- Redis
- Pydantic
- Uvicorn

---

# Environment Configuration

Create a `.env` file:

```env
MONGO_URL=mongodb://localhost:27018

DATABASE_NAME=campaign_job_service

REDIS_HOST=localhost

REDIS_PORT=6379

REDIS_DB=0

ENVIRONMENT=DEV
```

> Update the MongoDB port if your MongoDB container uses a different mapping.

---

# Installation

## Clone Repository

```bash
git clone https://github.com/<your-username>/campaign-job-service-clone.git

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

# Running the Application

```bash
uvicorn main:app --reload --port 8002
```

Application:

```text
http://localhost:8002
```

Swagger UI:

```text
http://localhost:8002/docs
```

---

# Health Check API

## Endpoint

```http
GET /health
```

### Response

```json
{
  "success": true
}
```

Purpose:

- Verify API availability
- Verify application startup
- Verify deployment health

---

# Analytics Module

The Analytics Module simulates campaign analytics generation similar to the production Campaign Job Service.

---

## Generate Analytics

### Endpoint

```http
POST /analytics/generate
```

### Request Body

```json
{
  "campaign_id": "CMP001",
  "campaign_name": "Summer Rewards",
  "active_users": 120,
  "expired_users": 10,
  "total_orders": 75,
  "transaction_volume": 125000
}
```

### Response

```json
{
  "success": true,
  "analytics_id": "689f123abc"
}
```

---

## Get All Analytics

### Endpoint

```http
GET /analytics
```

### Response

```json
[
  {
    "_id": "689f123abc",
    "campaign_id": "CMP001",
    "campaign_name": "Summer Rewards",
    "active_users": 120,
    "expired_users": 10,
    "total_orders": 75,
    "transaction_volume": 125000,
    "generated_at": "2025-08-18T10:30:00"
  }
]
```

---

## Get Analytics By Campaign

### Endpoint

```http
GET /analytics/{campaign_id}
```

### Example

```http
GET /analytics/CMP001
```

### Response

```json
[
  {
    "_id": "689f123abc",
    "campaign_id": "CMP001",
    "campaign_name": "Summer Rewards",
    "active_users": 120,
    "expired_users": 10,
    "total_orders": 75,
    "transaction_volume": 125000,
    "generated_at": "2025-08-18T10:30:00"
  }
]
```

---

# MongoDB Collection

## campaign_analytics

Example Document:

```json
{
  "campaign_id": "CMP001",
  "campaign_name": "Summer Rewards",
  "active_users": 120,
  "expired_users": 10,
  "total_orders": 75,
  "transaction_volume": 125000,
  "generated_at": "2025-08-18T10:30:00"
}
```

---

# Local Development Ports

Recommended setup:

```text
Campaign CMS Clone            -> 8000

Campaign Notification Clone   -> 8001

Campaign Job Service Clone    -> 8002
```

---

# Completed Phases

```text
✅ Phase 1 - Foundation Setup

✅ Phase 2 - Analytics Module

⬜ Phase 3 - User Lifecycle Module

⬜ Phase 4 - Order Reconciliation Module

⬜ Phase 5 - Reminder Module

⬜ Phase 6 - Monitoring Module

⬜ Phase 7 - Dockerization
```

---

# Upcoming Phase

## Phase 3 - User Lifecycle Module

Planned APIs:

```http
POST /jobs/user-expire

POST /jobs/user-disable

GET /jobs/users
```

Features:

- Active Users
- Expired Users
- Disabled Users
- User Status Tracking

---

# Learning Outcomes

This project demonstrates:

- FastAPI Development
- MongoDB CRUD Operations
- Redis Integration
- REST API Design
- Analytics Processing
- Backend Service Architecture
- Campaign Automation Concepts
- Microservice Design Patterns

---

# Final Goal

The Campaign Job Service Clone aims to replicate the operational automation layer used in campaign platforms.

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

By the end of the project, the service will support analytics, user lifecycle management, order automation, monitoring, reminders, and reporting workflows similar to an enterprise Campaign Job Service.