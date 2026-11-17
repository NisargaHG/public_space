# Public Space – Rule-Based Social Interaction Platform

**Connect Meaningfully. Interact Mindfully.**

Public Space is a Django-based social interaction platform that introduces custom, rule-based restrictions to encourage meaningful online engagement.

Unlike conventional social networking platforms, Public Space incorporates relationship-based posting limits and time-dependent posting rules. Users can register, follow other users, establish mutual friendships and share posts according to predefined social activity conditions.

---

## Project Overview

Most social media platforms encourage frequent posting and continuous engagement.

Public Space explores an alternative approach by introducing structured posting restrictions based on user relationships and social activity.

The application evaluates a user's following count and mutual friendship count to determine their posting eligibility.

The main objective is to demonstrate how custom business rules can be implemented in a web application using Django, relational database models and backend validation.

## Key Features

### 1. User Authentication

- User registration and login.
- Account-based access to platform functionality.
- Django's built-in authentication system.

### 2. Following System

- Users can follow other registered users.
- Users can identify their followers.
- Following relationships are used to determine posting eligibility.

### 3. Mutual Friendship Management

- Identifies mutual relationships between users.
- Calculates mutual friendship counts.
- Uses mutual friendship information in posting-rule evaluation.

### 4. Rule-Based Posting Restrictions

The platform applies custom posting limits based on social relationships.

| User Condition | Daily Posting Limit | Time Restriction |
|---|---|---|
| Follows 0 people | 1 post per day | 10:00–10:30 AM IST |
| Follows exactly 2 people | 2 posts per day | No time restriction |
| More than 10 mutual friends | Unlimited | No time restriction |

These rules are designed to encourage users to build meaningful social connections rather than focusing only on posting frequency.

### 5. Dynamic Homepage

- Displays platform content.
- Presents user-specific information.
- Supports dynamic content rendering based on application data.

---

## Application Workflow

```text
             USER REGISTRATION
                    |
                    v
              USER LOGIN
                    |
                    v
          SOCIAL RELATIONSHIPS
                    |
          +---------+---------+
          |                   |
          v                   v
      FOLLOWING          MUTUAL FRIENDS
          |                   |
          +---------+---------+
                    |
                    v
           POSTING RULE ENGINE
                    |
          +---------+----------+
          |         |          |
          v         v          v
       Follow 0  Follow 2   Mutual Friends
          |         |       Greater than 10
          v         v          v
       1 Post    2 Posts    Unlimited
       Daily     Daily        Posts
          |         |          |
          +---------+----------+
                    |
                    v
           POST ELIGIBILITY
                    |
                    v
             POST CREATION
                    |
                    v
            DYNAMIC HOMEPAGE
```

---

## Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python 3.13.1 |
| Backend Framework | Django 5.1.5 |
| Database | SQLite |
| Frontend | HTML5, CSS3 |
| UI Framework | Bootstrap (where configured) |
| Authentication | Django Built-in Authentication |
| Timezone Management | pytz |
| Development Environment | VS Code |
| Version Control | Git and GitHub |

## Database and Backend Design

The application uses Django's database models and SQLite for persistent data storage.

The backend manages the following application responsibilities:

- User account management.
- Following relationships.
- Mutual friendship identification.
- Post creation and management.
- Daily posting-limit evaluation.
- Time-based posting restrictions.
- User-specific homepage content.

The relationship data is used by the application's business logic to determine whether a user is eligible to create a post.

---

## Project Structure

```text
public_space/
│
├── public_space/
│   └── Django project configuration
│
├── space/
│   └── Core application logic
│
├── staticfiles/
│   └── Collected static assets
│
├── templates/
│   └── HTML templates (if configured)
│
├── manage.py
├── requirements.txt
├── db.sqlite3
└── README.md
```

---

## Getting Started

### Prerequisites

Make sure you have installed:

- Python 3.13.1
- pip
- Git
- VS Code or another Python IDE

### Step 1: Clone the Repository

```bash
git clone https://github.com/NisargaHG/public_space.git

cd public_space
```

### Step 2: Create a Virtual Environment

```bash
python -m venv venv
```

### Step 3: Activate the Virtual Environment

For Windows:

```powershell
.\venv\Scripts\activate
```

For Linux/macOS:

```bash
source venv/bin/activate
```

### Step 4: Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 5: Apply Database Migrations

```bash
python manage.py migrate
```

### Step 6: Start the Development Server

```bash
python manage.py runserver
```

Open the following address in your browser:

```text
http://127.0.0.1:8000/
```

**Note:** The default Django development server is intended for local development. Database migrations and application configuration should be checked before running the application in a fresh environment.

---

## Core Business Logic

The distinguishing feature of Public Space is its relationship-based posting restriction mechanism.

The platform evaluates:

1. Number of users followed.
2. Number of mutual friendships.
3. Daily posting activity.
4. Current IST time.
5. Posting eligibility under the configured rules.

This demonstrates the implementation of conditional business logic within a Django web application.

**Example scenarios:**

- A user who follows nobody is restricted to one post per day during the specified 30-minute time window.
- A user who follows exactly two people can publish up to two posts per day.
- A user with more than ten mutual friends is eligible for unlimited posting under the documented rules.

---

## Future Enhancements

Potential improvements include:

- Notifications for new followers and social interactions.
- Improved user profile management.
- Advanced content discovery.
- Post engagement analytics.
- REST API integration.
- Automated testing of posting restrictions.
- Enhanced database optimization.
- Deployment to a cloud hosting platform.

## Learning Outcomes

This project demonstrates practical implementation of:

- Django application development.
- User authentication and authorization concepts.
- Relational database management.
- Social relationship modelling.
- Conditional business logic.
- Timezone-aware application logic.
- Dynamic server-rendered web applications.

---



*Public Space – Building a more meaningful approach to social interaction through rule-based application design.*
