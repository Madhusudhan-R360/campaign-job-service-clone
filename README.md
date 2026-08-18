# Campaign Job Service Clone

A simplified clone of an enterprise Campaign Job Service built using FastAPI, MongoDB, and Redis.

This project recreates the operational automation layer of a campaign ecosystem. The service is responsible for analytics generation, user lifecycle management, order reconciliation, monitoring, reporting, and workflow automation.

---

# Project Overview

In a production campaign platform, the Job Service executes business operations that keep campaigns synchronized and healthy.

Typical responsibilities include:

- Campaign Analytics
- User Lifecycle Management
- Order Processing
- Voucher Assignment
- Reminder Jobs
- Monitoring & Alerting
- Operational Reporting

This clone implements those concepts in a simplified and learning-focused architecture.

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

- Analytics Collection
- Generate Analytics API
- Get All Analytics API
- Get Analytics By Campaign API

---

## ✅ Phase 3 - User Lifecycle Module

Implemented:

- User Collection
- Create User API
- Get Users API
- User Expiry Job
- User Disable Job
- User Status Tracking

---

## ✅ Phase 4 - Order Reconciliation Module

Implemented:

- Orders Collection
- Vouchers Collection
- Create Order API
- Get Orders API
- Get Single Order API
- Reconcile Orders Job
- Voucher Generation
- Order Completion Workflow

---

# Architecture

```text
                    Campaign CMS
                          |
                          |
                          v

              Campaign Job Service Clone
                          |
 ----------------------------------------------------------------
 |                 |                 |               |           |
 v                 v                 v               v           v

Analytics      User Jobs      Order Jobs      Monitoring    Reporting

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
│   ├── users/
│   │   ├── app.py
│   │   ├── schema.py
│   │   └── utility.py
│   │
│   └── orders/
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

Linux / Mac

```bash
source venv/bin/activate
```

Windows

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

Swagger UI:

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

---

# Analytics Module

Simulates campaign analytics generation jobs.

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

---

## Get All Analytics

### Endpoint

```http
GET /analytics
```

---

## Get Analytics By Campaign

### Endpoint

```http
GET /analytics/{campaign_id}
```

---

## Collection

```text
campaign_analytics
```

---

# User Lifecycle Module

Simulates production jobs:

```text
user-expire

user-disable
```

---

## User Lifecycle Flow

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

---

## Get Users

### Endpoint

```http
GET /users
```

---

## Run User Expiry Job

### Endpoint

```http
POST /jobs/user-expire
```

### Status Change

```text
ACTIVE → EXPIRED
```

---

## Run User Disable Job

### Endpoint

```http
POST /jobs/user-disable
```

### Status Change

```text
EXPIRED → DISABLED
```

---

## Collection

```text
users
```

---

# Order Reconciliation Module

Simulates the production ERP synchronization and voucher reconciliation jobs.

---

## Order Lifecycle

```text
ORDER CREATED
       |
       v

PENDING
       |
       v

/jobs/reconcile-orders
       |
       v

COMPLETED
       |
       v

Voucher Assigned
```

---

## Create Order

### Endpoint

```http
POST /orders
```

### Request

```json
{
  "order_id": "ORD001",
  "user_id": "USR001",
  "campaign_id": "CMP001",
  "amount": 5000
}
```

### Response

```json
{
  "success": true,
  "message": "Order Created"
}
```

---

## Get All Orders

### Endpoint

```http
GET /orders
```

---

## Get Order By ID

### Endpoint

```http
GET /orders/{order_id}
```

Example:

```http
GET /orders/ORD001
```

---

## Reconcile Orders Job

### Endpoint

```http
POST /jobs/reconcile-orders
```

### Response

```json
{
  "success": true,
  "processed_orders": 1
}
```

---

## Example Order

```json
{
  "order_id": "ORD001",
  "user_id": "USR001",
  "campaign_id": "CMP001",
  "amount": 5000,
  "status": "COMPLETED",
  "voucher_code": "A7B81D21"
}
```

---

## Example Voucher

```json
{
  "order_id": "ORD001",
  "voucher_code": "A7B81D21",
  "created_at": "2026-08-18T12:00:00"
}
```

---

# MongoDB Collections

Implemented:

```text
campaign_analytics

users

orders

vouchers
```

Planned:

```text
notifications

monitoring_logs

reminders
```

---

# Local Development Ports

```text
Campaign CMS Clone            → 8000

Campaign Notification Clone   → 8001

Campaign Job Service Clone    → 8002
```

---

# Project Progress

```text
✅ Phase 1 - Foundation Setup

✅ Phase 2 - Analytics Module

✅ Phase 3 - User Lifecycle Module

✅ Phase 4 - Order Reconciliation Module

⬜ Phase 5 - Reminder Module

⬜ Phase 6 - Monitoring Module

⬜ Phase 7 - Dockerization & Deployment
```

---

# Upcoming Phase

## Phase 5 - Reminder Module

Inspired by production jobs:

```text
Mail Expiry Reminder

Campaign Reminder Jobs

Notification Triggers
```

Planned APIs:

```http
POST /jobs/send-reminders

GET /reminders

POST /reminders
```

Features:

```text
Reminder Creation

Expiry Detection

Reminder Processing

Reminder History
```

---

# Learning Outcomes

This project demonstrates:

- FastAPI Development
- MongoDB CRUD Operations
- Redis Integration
- REST API Design
- Analytics Processing
- User Lifecycle Management
- Order Reconciliation
- Voucher Processing
- Background Job Design
- Microservice Architecture

---

# Final Goal

The Campaign Job Service Clone aims to simulate the automation backbone of an enterprise campaign platform.

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
Order Reconciliation Jobs
       |
       v
Monitoring Jobs
       |
       v
Operational Reports
```

By the end of the project, the service will support analytics generation, user lifecycle automation, voucher-based order processing, reminders, monitoring, reporting, and operational workflows similar to a real enterprise Campaign Job Service.