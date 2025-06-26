# 🏛️ Public Space – Django-Based Social Interaction Platform

A feature-rich Django web application that simulates a public platform where users can follow others, build mutual friendships, and post content — but with **unique rule-based restrictions** to promote mindful social interaction.

## 🚀 Key Features

- ✅ **User Registration & Login** – Secure user authentication system.
- 🔄 **Following System** – Users can follow others and see who follows them back.
- 🧑‍🤝‍🧑 **Mutual Friends Logic** – Automatically detects and counts mutual friendships.
- ⏰ **Time-Based Posting Rules** – Posts allowed only during specific time windows.
- 📊 **Post Limit System** – Daily post limits based on following/friend count.
- 🏠 **Dynamic Homepage** – Displays real-time content and user-specific data.

---

## 🧠 Posting Rules Logic

The platform enforces custom logic based on social activity:

| Condition                              | Daily Post Limit      | Time Restriction             |
|----------------------------------------|------------------------|------------------------------|
| Follows 0 people                       | 1 post/day             | Only between 10:00–10:30 AM IST |
| Follows exactly 2 people               | 2 posts/day            | Anytime                      |
| Has more than 10 mutual friends        | Unlimited              | Anytime                      |

---

## 🛠️ Tech Stack

- **Backend:** Django 5.1.5, Python 3.13.1
- **Database:** SQLite (default), easily upgradable
- **Frontend:** HTML5, CSS3, Bootstrap (optional)
- **Timezone Handling:** IST time logic using `pytz`
- **Authentication:** Django's built-in auth system

---

## 📂 Project Structure

```bash
public_space/
├── space/                  # Core app logic (views, models, templates)
├── templates/              # HTML templates for frontend rendering
├── static/                 # CSS and JavaScript files
├── manage.py               # Django project manager
├── db.sqlite3              # SQLite database
└── requirements.txt        # Python dependencies
