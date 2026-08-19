# Campaign Job Service Clone

A simplified clone of an enterprise Campaign Job Service built using FastAPI, MongoDB, Redis, and Docker.

This project simulates the operational automation layer of a campaign ecosystem. It includes analytics processing, user lifecycle management, order reconciliation, voucher assignment, reminder processing, monitoring, and containerized deployment.

---

# Project Overview

In large-scale campaign platforms, background services execute scheduled and operational jobs that automate business workflows.

Typical responsibilities include:

- Campaign Analytics
- User Lifecycle Management
- Order Reconciliation
- Voucher Assignment
- Reminder Notifications
- Monitoring & Alerting
- Operational Reporting

This clone recreates those workflows in a simplified microservice architecture using FastAPI.

---

# Features Implemented

## ✅ Phase 1 - Foundation Setup

- FastAPI Application
- MongoDB Integration
- Redis Integration
- Environment Configuration
- Health Check API
- Swagger Documentation

---

## ✅ Phase 2 - Analytics Module

- Generate Analytics API
- Get Analytics API
- Get Analytics By Campaign API
- MongoDB Analytics Collection

---

## ✅ Phase 3 - User Lifecycle Module

- Create User API
- Get Users API
- User Expiry Job
- User Disable Job
- User Status Management

User Lifecycle:

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

## ✅ Phase 4 - Order Reconciliation Module

- Create Order API
- Get Orders API
- Get Order API
- Order Reconciliation Job
- Voucher Assignment

Order Lifecycle:

```text
CREATED
   |
   v
PENDING
   |
   v
RECONCILIATION JOB
   |
   v
COMPLETED
   |
   v
VOUCHER GENERATED
```

---

## ✅ Phase 5 - Reminder Module

- Create Reminder API
- Get Reminders API
- Reminder Processing Job
- Expiry Detection Logic
- Reminder History

Reminder Flow:

```text
User Expiry Approaching
          |
          v
Send Reminder Job
          |
          v
Reminder Created
          |
          v
Status = SENT
```

---

## ✅ Phase 6 - Monitoring Module

- Monitoring Dashboard API
- Monitoring Logs API
- Monitoring Job
- User Metrics Tracking
- Order Metrics Tracking
- Historical Monitoring Logs

Monitoring Flow:

```text
Users
   \
    \
Orders ---> Monitoring Job
    /
   /

      |
      v

Monitoring Dashboard
```

---

## ✅ Phase 7 - Dockerization & Deployment

- Dockerfile
- Docker Compose
- MongoDB Container
- Redis Container
- Environment Variable Support
- Complete Local Deployment

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
├── Dockerfile
│
├── docker-compose.yml
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
- Docker
- Docker Compose

---

# Environment Configuration

Create a `.env` file.

Local Development:

```env
MONGO_URL=mongodb://localhost:27017

DATABASE_NAME=campaign_job_service

REDIS_HOST=localhost

REDIS_PORT=6379

REDIS_DB=0

ENVIRONMENT=LOCAL
```

Docker Deployment:

```env
MONGO_URL=mongodb://mongodb:27017

DATABASE_NAME=campaign_job_service

REDIS_HOST=redis

REDIS_PORT=6379

REDIS_DB=0

ENVIRONMENT=DOCKER
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

# Run Application Locally

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

# Docker Deployment

## Build Containers

```bash
docker compose build
```

## Start Containers

```bash
docker compose up -d
```

## Check Containers

```bash
docker ps
```

Expected:

```text
campaign-job-service
campaign-job-mongo
campaign-job-redis
```

---

# Available APIs

## Health

```http
GET /health
```

---

# Analytics APIs

Generate Analytics:

```http
POST /analytics/generate
```

Get Analytics:

```http
GET /analytics
```

Get Analytics By Campaign:

```http
GET /analytics/{campaign_id}
```

---

# User APIs

Create User:

```http
POST /users
```

Get Users:

```http
GET /users
```

User Expiry Job:

```http
POST /jobs/user-expire
```

User Disable Job:

```http
POST /jobs/user-disable
```

---

# Order APIs

Create Order:

```http
POST /orders
```

Get Orders:

```http
GET /orders
```

Get Order:

```http
GET /orders/{order_id}
```

Reconcile Orders:

```http
POST /jobs/reconcile-orders
```

---

# Reminder APIs

Create Reminder:

```http
POST /reminders
```

Get Reminders:

```http
GET /reminders
```

Send Reminders:

```http
POST /jobs/send-reminders
```

---

# Monitoring APIs

Run Monitoring Job:

```http
POST /jobs/monitor-system
```

Dashboard:

```http
GET /monitoring/dashboard
```

Monitoring Logs:

```http
GET /monitoring/logs
```

---

# MongoDB Collections

```text
campaign_analytics

users

orders

vouchers

reminders

monitoring_logs
```

---

# Testing Checklist

```text
✅ Health API

✅ Analytics Module

✅ User Lifecycle Module

✅ Order Reconciliation Module

✅ Voucher Generation

✅ Reminder Module

✅ Monitoring Dashboard

✅ Monitoring Logs

✅ MongoDB Integration

✅ Redis Integration

✅ Docker Deployment
```

---

# Local Ports

```text
Campaign CMS Clone            → 8000

Campaign Notification Clone   → 8001

Campaign Job Service Clone    → 8002

MongoDB                       → 27017

Redis                         → 6379
```

---

# Future Enhancements

```text
JWT Authentication

Role-Based Access Control

APScheduler Cron Jobs

Email Notifications

Redis Caching

Centralized Logging

Prometheus Metrics

Grafana Dashboard

Unit Tests

GitHub Actions CI/CD

Kubernetes Deployment
```

---

# Learning Outcomes

This project demonstrates:

- FastAPI Development
- MongoDB CRUD Operations
- Redis Integration
- REST API Design
- Background Job Processing
- User Lifecycle Management
- Order Reconciliation
- Voucher Processing
- Reminder Automation
- Monitoring & Reporting
- Dockerization
- Microservice Architecture

---

# Final Workflow

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

The Campaign Job Service Clone provides a complete end-to-end implementation of a production-inspired campaign operations service with analytics, lifecycle automation, vouchers, reminders, monitoring, MongoDB persistence, Redis integration, and Docker deployment.