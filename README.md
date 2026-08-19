# Campaign Job Service Clone

A simplified clone of an enterprise Campaign Job Service built using FastAPI, MongoDB, and Redis.

This project simulates the operational automation layer of a campaign ecosystem. The service is responsible for analytics generation, user lifecycle processing, order reconciliation, reminder processing, monitoring, and reporting workflows.

---

# Project Overview

In a production campaign platform, the Job Service executes scheduled and operational jobs that maintain system health and automate business workflows.

Responsibilities include:

- Campaign Analytics
- User Lifecycle Management
- Voucher Processing
- Order Reconciliation
- Reminder Management
- Monitoring & Alerting
- Operational Reporting

This project recreates those concepts using FastAPI and MongoDB.

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
- Get Analytics API
- Campaign Analytics API
- MongoDB Persistence

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
- Get Order API
- Reconcile Orders Job
- Voucher Assignment Workflow

---

## ✅ Phase 5 - Reminder Module

Implemented:

- Reminders Collection
- Create Reminder API
- Get Reminders API
- Send Reminders Job
- Expiry Detection Logic
- Reminder Tracking
- Reminder History

---

# Architecture

```text
                    Campaign CMS
                          |
                          |
                          v

              Campaign Job Service Clone
                          |
 -------------------------------------------------------------------
 |                |                |               |               |
 v                v                v               v               v

Analytics     User Jobs      Order Jobs     Reminder Jobs    Monitoring

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
│   ├── orders/
│   │   ├── app.py
│   │   ├── schema.py
│   │   └── utility.py
│   │
│   └── reminders/
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

## Activate Environment

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

Swagger Documentation:

```text
http://localhost:8002/docs
```

---

# Health Module

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

---

# Analytics Module

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

```http
GET /analytics
```

---

## Get Analytics By Campaign

```http
GET /analytics/{campaign_id}
```

### Collection

```text
campaign_analytics
```

---

# User Lifecycle Module

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

```http
POST /users
```

---

## Get Users

```http
GET /users
```

---

## Expire Users Job

```http
POST /jobs/user-expire
```

### Status Change

```text
ACTIVE → EXPIRED
```

---

## Disable Users Job

```http
POST /jobs/user-disable
```

### Status Change

```text
EXPIRED → DISABLED
```

### Collection

```text
users
```

---

# Order Reconciliation Module

Simulates production ERP-based voucher reconciliation.

---

## Order Flow

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

```http
POST /orders
```

---

## Get Orders

```http
GET /orders
```

---

## Get Order

```http
GET /orders/{order_id}
```

---

## Reconcile Orders

```http
POST /jobs/reconcile-orders
```

### Collections

```text
orders

vouchers
```

---

# Reminder Module

Simulates expiry reminder workflows.

---

## Reminder Flow

```text
User Expiry Approaching
          |
          v

/jobs/send-reminders
          |
          v

Reminder Generated
          |
          v

Reminder Stored
```

---

## Create Reminder

### Endpoint

```http
POST /reminders
```

### Request

```json
{
  "user_id": "USR001",
  "campaign_id": "CMP001",
  "message": "Reward expires soon."
}
```

---

## Get Reminders

### Endpoint

```http
GET /reminders
```

---

## Send Reminders Job

### Endpoint

```http
POST /jobs/send-reminders
```

### Logic

```text
Find ACTIVE Users

Expiry Within 7 Days

Create Reminder Record

Mark Reminder As SENT
```

### Sample Response

```json
{
  "success": true,
  "reminders_sent": 3
}
```

### Collection

```text
reminders
```

### Example Document

```json
{
  "user_id": "USR001",
  "campaign_id": "CMP001",
  "message": "Your campaign benefit expires soon.",
  "status": "SENT",
  "created_at": "2026-08-19T12:00:00"
}
```

---

# MongoDB Collections

Implemented Collections:

```text
campaign_analytics

users

orders

vouchers

reminders
```

Planned Collections:

```text
monitoring_logs

notifications
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

✅ Phase 5 - Reminder Module

⬜ Phase 6 - Monitoring Module

⬜ Phase 7 - Dockerization & Deployment
```

---

# Upcoming Phase

## Phase 6 - Monitoring Module

Features:

```text
Pending Order Alerts

Duplicate Voucher Detection

Monitoring Logs

Operational Metrics

Health Monitoring
```

Planned APIs:

```http
POST /jobs/monitor-system

GET /monitoring

GET /monitoring/orders

GET /monitoring/users
```

---

# Learning Outcomes

This project demonstrates:

- FastAPI Development
- MongoDB CRUD Operations
- Redis Integration
- Analytics Processing
- User Lifecycle Automation
- Order Reconciliation
- Voucher Management
- Reminder Processing
- Background Job Design
- Microservice Architecture

---

# Final Goal

The Campaign Job Service Clone aims to replicate the automation backbone of an enterprise campaign platform.

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
Reminder Jobs
       |
       v
Monitoring Jobs
       |
       v
Operational Reports
```

By the end of the project, the service will support analytics, lifecycle management, order processing, reminders, monitoring, reporting, and operational automation similar to a real production Campaign Job Service.