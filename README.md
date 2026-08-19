# Campaign Job Service Clone

A simplified clone of an enterprise Campaign Job Service built using FastAPI, MongoDB, and Redis.

This project simulates the operational automation layer of a campaign management ecosystem. The service handles analytics generation, user lifecycle management, order reconciliation, reminder processing, monitoring, and reporting workflows.

---

# Project Overview

In a production campaign platform, background services continuously execute operational jobs such as:

- Analytics Generation
- User Expiry Processing
- User Disable Processing
- Order Reconciliation
- Voucher Assignment
- Reminder Processing
- Monitoring & Alerting
- Operational Reporting

This project recreates those responsibilities using FastAPI and MongoDB in a simplified microservice architecture.

---

# Current Progress

## ✅ Phase 1 - Foundation Setup

Implemented:

- FastAPI Application
- MongoDB Integration
- Redis Integration
- Environment Variables
- Health Check Endpoint
- Swagger Documentation

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

- Users Collection
- Create User API
- Get Users API
- User Expiry Job
- User Disable Job
- User Status Management

---

## ✅ Phase 4 - Order Reconciliation Module

Implemented:

- Orders Collection
- Vouchers Collection
- Create Order API
- Get Orders API
- Get Order API
- Order Reconciliation Job
- Voucher Assignment Workflow

---

## ✅ Phase 5 - Reminder Module

Implemented:

- Reminders Collection
- Create Reminder API
- Get Reminders API
- Reminder Processing Job
- Expiry Detection Logic
- Reminder Tracking

---

## ✅ Phase 6 - Monitoring Module

Implemented:

- Monitoring Logs Collection
- Monitoring Dashboard API
- Monitoring Logs API
- System Monitoring Job
- User Metrics Reporting
- Order Metrics Reporting
- Historical Monitoring Logs

---

# Architecture

```text
                    Campaign CMS
                          |
                          |
                          v

              Campaign Job Service Clone
                          |
 ----------------------------------------------------------------------
 |              |              |             |              |          |
 v              v              v             v              v          v

Analytics    User Jobs     Order Jobs   Reminders   Monitoring   Reports

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
│   ├── reminders/
│   │   ├── app.py
│   │   ├── schema.py
│   │   └── utility.py
│   │
│   └── monitoring/
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

Application URL:

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

```http
GET /health
```

Response:

```json
{
  "success": true
}
```

---

# Analytics Module

## Generate Analytics

```http
POST /analytics/generate
```

## Get All Analytics

```http
GET /analytics
```

## Get Analytics By Campaign

```http
GET /analytics/{campaign_id}
```

Collection:

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

### Create User

```http
POST /users
```

### Get Users

```http
GET /users
```

### Expire Users

```http
POST /jobs/user-expire
```

### Disable Users

```http
POST /jobs/user-disable
```

Collection:

```text
users
```

---

# Order Reconciliation Module

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

### Create Order

```http
POST /orders
```

### Get Orders

```http
GET /orders
```

### Get Single Order

```http
GET /orders/{order_id}
```

### Reconcile Orders

```http
POST /jobs/reconcile-orders
```

Collections:

```text
orders

vouchers
```

---

# Reminder Module

## Reminder Flow

```text
Expiry Approaching
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

### Create Reminder

```http
POST /reminders
```

### Get Reminders

```http
GET /reminders
```

### Send Reminders

```http
POST /jobs/send-reminders
```

Collection:

```text
reminders
```

---

# Monitoring Module

The Monitoring Module simulates operational dashboards and health reporting.

---

## System Monitoring Flow

```text
Users
     \
      \
Orders ---> Monitoring Job
      /
     /

        |
        v

Monitoring Metrics
        |
        v

Dashboard
```

---

## Run Monitoring Job

```http
POST /jobs/monitor-system
```

Example Response:

```json
{
  "success": true,
  "data": {
    "active_users": 5,
    "expired_users": 1,
    "disabled_users": 2,
    "pending_orders": 3,
    "completed_orders": 15
  }
}
```

---

## Monitoring Dashboard

```http
GET /monitoring/dashboard
```

Example Response:

```json
{
  "active_users": 5,
  "expired_users": 1,
  "disabled_users": 2,
  "pending_orders": 3,
  "completed_orders": 15
}
```

---

## Monitoring Logs

```http
GET /monitoring/logs
```

Example Response:

```json
[
  {
    "_id": "68a4abcd1234",
    "active_users": 5,
    "expired_users": 1,
    "disabled_users": 2,
    "pending_orders": 3,
    "completed_orders": 15,
    "generated_at": "2026-08-19T12:00:00"
  }
]
```

Collection:

```text
monitoring_logs
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

monitoring_logs
```

Future Collections:

```text
notifications

audit_logs
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

✅ Phase 6 - Monitoring Module

⬜ Phase 7 - Dockerization & Deployment
```

---

# Upcoming Phase

## Phase 7 - Dockerization & Deployment

Planned Deliverables:

- Dockerfile
- Docker Compose
- MongoDB Container
- Redis Container
- Environment Configuration
- One Command Startup
- Production-style Local Deployment

---

# Learning Outcomes

This project demonstrates:

- FastAPI Development
- MongoDB CRUD Operations
- Redis Integration
- Analytics Processing
- User Lifecycle Automation
- Voucher Processing
- Order Reconciliation
- Reminder Management
- Monitoring & Reporting
- Microservice Architecture

---

# Final Goal

The Campaign Job Service Clone aims to replicate the automation backbone of a campaign platform.

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

By the end of the project, the service will provide a production-style implementation of analytics, lifecycle management, order processing, reminders, monitoring, and reporting workflows similar to a real enterprise Campaign Job Service.