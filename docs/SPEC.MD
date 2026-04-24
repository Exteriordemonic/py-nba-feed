# 📋 SPEC — NBA Feed API

## 1. PROJECT GOAL

A REST API built with Django DRF and PostgreSQL that allows users to subscribe to updates about NBA players. Users receive email notifications about any changes to a player's status or when a player makes any activity on social media. In future iterations, we will scrape players' X (Twitter) and Instagram accounts to gather more information.

---

## 2. Technology Stack

| Layer           | Technology                                  |
|-----------------|---------------------------------------------|
| Backend         | Django + Django REST Framework              |
| Database        | PostgreSQL                                  |
| Auth            | JWT (djangorestframework-simplejwt)         |
| Email           | Django email backend (SMTP)                 |
| Internal Events | Django Signals                              |
| Data (phase 1)  | Manual seed                                 |
| Data (phase 2)  | External API (e.g., BallDontLie)            |
| Data (phase 3)  | Scraping                                    |

---

## 3. Entities (models)

### `User`
Built-in Django User + JWT auth.

### `Team`
```
id, name, city, conference, division, logo_url, created_at, updated_at
```

### `Player`
```
id, full_name, display_name, date_of_birth, nationality,
position (ENUM: PG/SG/SF/PF/C), jersey_number,
height_cm, weight_kg, wingspan_cm,
team (FK → Team), experience_years,
draft_year, draft_pick,
contract_type (ENUM), contract_start, contract_end, salary_usd,
availability (ENUM: active/day_to_day/out/suspended/inactive),
injury_note,
created_at, updated_at
```

### `Subscription`
```
id, user (FK → User), player (FK → Player),
created_at
UNIQUE(user, player)
```

### `PlayerChangeLog`
```
id, player (FK → Player),
field_name (e.g., "availability", "team"),
old_value, new_value,
changed_at
```

### `Notification`
```
id, user (FK → User), change_log (FK → PlayerChangeLog),
is_read (bool), sent_at
```

---

## 4. Endpoints

### Auth
```
POST /api/auth/register/
POST /api/auth/login/              → returns access + refresh token
POST /api/auth/token/refresh/
```

### Teams
```
GET  /api/teams/                   → list of teams
GET  /api/teams/{id}/              → team details
```

### Players
```
GET  /api/players/                 → list of players (filter: team, position, availability)
POST /api/players/                 → add player (admin)
GET  /api/players/{id}/            → player details
PUT  /api/players/{id}/            → edit player (admin) → triggers Signal
```

### Subscriptions
```
GET    /api/subscriptions/         → my subscriptions
POST   /api/subscriptions/         → subscribe to player { player_id }
DELETE /api/subscriptions/{id}/    → unsubscribe
```

### Feed (news for logged-in user)
```
GET /api/feed/                     → changes of players I'm subscribed to
                                      (unread first, with filter ?unread=true)
GET /api/feed/{notification_id}/   → notification details → marks as read
```

---

## 5. Signals Logic

```
Player.post_save signal
  → if any tracked field changed (availability, team, contract_*, injury_note)
  → create PlayerChangeLog
  → find all users subscribed to this player
  → create Notification for each
  → send email (Django send_mail)
```

**Tracked fields** (fields that trigger notification):
`availability`, `injury_note`, `team`, `contract_type`, `contract_end`, `salary_usd`, `jersey_number`

---

## 6. Project Phases

| Phase   | What                                                   |
|---------|--------------------------------------------------------|
| **MVP** | Models, Auth, CRUD Players/Teams, Subscriptions, Feed, Signals + Email |
| **v1.1** | External API integration (auto-sync players)          |
| **v1.2** | Scraping (e.g. injury reports)                        |
