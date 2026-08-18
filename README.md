# Campaign Job Service Clone

A simplified clone of an enterprise Campaign Job Service built using FastAPI, MongoDB, and Redis.

This project replicates the operational automation layer of a campaign ecosystem. It focuses on analytics generation, user lifecycle processing, background jobs, monitoring, reporting, and workflow automation.

---

# Project Overview

In a real campaign platform, the Job Service is responsible for executing scheduled operations and maintaining system health.

Typical responsibilities include:

- Campaign Analytics
- User Lifecycle Management
- Voucher Processing
- Order Reconciliation
- Reminder Notifications
- Monitoring & Alerting
- Operational Reporting

This clone recreates those concepts in a simplified and learning-focused manner.

---

# Current Progress

## ✅ Phase 1 - Foundation Setup

Implemented:

- FastAPI Application
- MongoDB Integration
- Redis Integration
- Environment Configuration
- Swagger Documentation
- Health Check API

---

## ✅ Phase 2 - Analytics Module

Implemented:

- Campaign Analytics Collection
- Generate Analytics API
- Get All Analytics API
- Get Campaign Analytics API
- MongoDB Persistence

---

## ✅ Phase 3 - User Lifecycle Module

Implemented:

- User Collection
- Create User API
- Get Users API
- User Expiry Job
- User Disable Job
- User Status Management

---

# Architecture

```text
                    Campaign CMS
                          |
                          |
                          v

              Campaign Job Service Clone
                          |
 ------------------------------------------------
 |                 |               |            |
 v                 v               v            v

Analytics      User Jobs     Monitoring   Order Jobs
   Jobs

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
│   ├── analytics/
│   │   ├── app.py
│   │   ├── schema.py
│   │   └── utility.py
│   │
│   └── users/
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

# Technology Stack

- Python 3.12
- FastAPI
- MongoDB
- Motor
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

---

# Installation

## Clone Repository

```bash
git clone https://github.com/Madhusudhan-R360/campaign-job-service-clone.git

cd campaign-job-service-clone
```

## Create Virtual Environment

```bash
python3 -m venv venv
```

## Activate Virtual Environment

Linux / Mac:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running The Application

```bash
uvicorn main:app --reload --port 8002
```

Application:

```text
http://localhost:8002
```

Swagger:

```text
http://localhost:8002/docs
```

---

# Health Module

## Health Check

### Endpoint

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

- Verify application startup
- Verify service availability
- Verify deployment health

---

# Analytics Module

This module simulates the Analytics Cron functionality of the real Campaign Job Service.

---

## Generate Analytics

### Endpoint

```http
POST /analytics/generate
```

### Request

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

Returns all analytics records.

---

## Get Analytics By Campaign

### Endpoint

```http
GET /analytics/{campaign_id}
```

Example:

```http
GET /analytics/CMP001
```

---

## Analytics Collection

### Collection

```text
campaign_analytics
```

### Example Document

```json
{
  "campaign_id": "CMP001",
  "campaign_name": "Summer Rewards",
  "active_users": 120,
  "expired_users": 10,
  "total_orders": 75,
  "transaction_volume": 125000,
  "generated_at": "2026-08-18T10:30:00"
}
```

---

# User Lifecycle Module

This module simulates the real production jobs:

```text
user-expire

user-disable
```

---

## User Status Flow

```text
ACTIVE
   |
   v
EXPIRED
   |
   v
DISABLED
```

---

## Create User

### Endpoint

```http
POST /users
```

### Request

```json
{
  "user_id": "USR001",
  "name": "John Doe",
  "email": "john@example.com",
  "campaign_id": "CMP001",
  "expiry_date": "2026-08-20T00:00:00"
}
```

### Response

```json
{
  "success": true,
  "user_id": "689f123abc"
}
```

---

## Get All Users

### Endpoint

```http
GET /users
```

Returns all users.

---

## Run User Expiry Job

### Endpoint

```http
POST /jobs/user-expire
```

### Response

```json
{
  "success": true,
  "expired_users": 1
}
```

### Behaviour

```text
ACTIVE → EXPIRED
```

for users whose expiry date has passed.

---

## Run User Disable Job

### Endpoint

```http
POST /jobs/user-disable
```

### Response

```json
{
  "success": true,
  "disabled_users": 1
}
```

### Behaviour

```text
EXPIRED → DISABLED
```

---

## Users Collection

### Collection

```text
users
```

### Example Document

```json
{
  "user_id": "USR001",
  "name": "John Doe",
  "email": "john@example.com",
  "campaign_id": "CMP001",
  "expiry_date": "2026-08-20T00:00:00",
  "status": "ACTIVE",
  "created_at": "2026-08-18T10:00:00"
}
```

---

# MongoDB Collections

Implemented:

```text
campaign_analytics

users
```

Planned:

```text
orders

order_items

voucher_details

monitoring_logs

notifications
```

---

# Local Port Configuration

Recommended local setup:

```text
Campaign CMS Clone            → 8000

Campaign Notification Clone   → 8001

Campaign Job Service Clone    → 8002
```

---

# Completed Phases

```text
✅ Phase 1 - Foundation Setup

✅ Phase 2 - Analytics Module

✅ Phase 3 - User Lifecycle Module

⬜ Phase 4 - Order Reconciliation Module

⬜ Phase 5 - Reminder Module

⬜ Phase 6 - Monitoring Module

⬜ Phase 7 - Dockerization & Deployment
```

---

# Upcoming Phase

## Phase 4 - Order Reconciliation Module

Inspired by the production endpoint:

```http
POST /campaign/jobs/get-order-status
```

Features:

```text
Order Creation

Order Tracking

Mock ERP Integration

Voucher Assignment

Order Reconciliation

Order Status Updates
```

Planned APIs:

```http
POST /orders

GET /orders

GET /orders/{order_id}

POST /jobs/reconcile-orders
```

---

# Learning Outcomes

This project demonstrates:

- FastAPI Development
- MongoDB CRUD Operations
- Redis Integration
- REST API Design
- Analytics Processing
- User Lifecycle Automation
- Background Job Design
- Microservice Architecture
- Campaign Operations Design Patterns

---

# Final Goal

The Campaign Job Service Clone aims to replicate the operational automation backbone of an enterprise campaign platform.

```text
Campaign Data
       |
       v
Analytics Jobs
       |
       v
User Lifecycle Jobs
       |
       v
Order Processing Jobs
       |
       v
Monitoring Jobs
       |
       v
Operational Reports
```

By the end of the project, the service will support analytics generation, lifecycle management, order reconciliation, monitoring, reporting, reminders, and operational automation similar to a real production Campaign Job Service.