# NBA Feed API — TODO

---

## 🏗️ Milestone 1 — Project Setup

---

#[ ] TASK 01 — Django Project Setup

## Branch
`git flow feature start project-setup`

## Acceptance Criteria
- Django project is initialized with a virtual environment.
- `djangorestframework`, `psycopg2`, `djangorestframework-simplejwt`, `django-environ` are installed and listed in `requirements.txt`.
- PostgreSQL database is configured via environment variables (`.env`).
- Project runs locally with `python manage.py runserver` without errors.
- `.env.example` file exists with all required keys listed.
- `DEBUG=True` only when `ENV=development`.

---

#[ ] TASK 02 — Project Structure Setup

## Branch
`git flow feature start project-structure`

## Acceptance Criteria
- Project is split into Django apps: `players`, `teams`, `subscriptions`, `feed`, `users`.
- Each app has its own `urls.py`, `serializers.py`, `views.py`, `tests/` directory.
- Main `urls.py` includes all app routers under `/api/` prefix.
- `pytest` and `pytest-django` are configured (`pytest.ini` exists).
- Running `pytest` returns 0 errors on empty test suite.

---

## 👤 Milestone 2 — Authentication

---

#[ ] TASK 03 — User Registration Endpoint

## Branch
`git flow feature start user-registration`

## Acceptance Criteria
- `POST /api/auth/register/` accepts `email`, `password`, `username`.
- Returns `201` with user data on success.
- Returns `400` if email is already taken.
- Returns `400` if password is shorter than 8 characters.
- Test: valid registration returns 201.
- Test: duplicate email returns 400.
- Test: short password returns 400.

---

#[ ] TASK 04 — JWT Login & Token Refresh

## Branch
`git flow feature start jwt-auth`

## Acceptance Criteria
- `POST /api/auth/login/` accepts `email` + `password`, returns `access` and `refresh` tokens.
- `POST /api/auth/token/refresh/` accepts `refresh` token, returns new `access` token.
- Expired `access` token returns `401`.
- Test: valid credentials return 200 with both tokens.
- Test: wrong password returns 401.
- Test: token refresh works correctly.
- Test: protected endpoint returns 401 without token.

---

## 🏀 Milestone 3 — Teams

---

#[ ] TASK 05 — Team Model

## Branch
`git flow feature start team-model`

## Acceptance Criteria
- `Team` model exists with fields: `id`, `name`, `city`, `conference`, `division`, `logo_url`, `created_at`, `updated_at`.
- `conference` is limited to `ENUM: East, West`.
- Migration runs without errors.
- Test: Team can be created with valid data.
- Test: `conference` rejects values outside the enum.

---

#[ ] TASK 06 — Teams Endpoints

## Branch
`git flow feature start teams-endpoints`

## Acceptance Criteria
- `GET /api/teams/` returns list of all teams.
- `GET /api/teams/{id}/` returns team details.
- Both endpoints are public (no auth required).
- Returns `404` for non-existent team.
- Test: list returns all seeded teams.
- Test: detail returns correct team by id.
- Test: unknown id returns 404.

---

## 🧑‍💼 Milestone 4 — Players

---

#[ ] TASK 07 — Player Model

## Branch
`git flow feature start player-model`

## Acceptance Criteria
- `Player` model exists with all fields from spec.
- `position` is limited to `ENUM: PG, SG, SF, PF, C`.
- `availability` is limited to `ENUM: active, day_to_day, out, suspended, inactive`.
- `contract_type` is limited to `ENUM: max, supermax, rookie, veteran_min, two_way`.
- `team` is a nullable FK to `Team` (player can be a free agent).
- `updated_at` auto-updates on every save.
- Migration runs without errors.
- Test: Player can be created with valid data.
- Test: Invalid `position` value raises ValidationError.
- Test: Invalid `availability` value raises ValidationError.

---

#[ ] TASK 08 — Player List & Filter Endpoint

## Branch
`git flow feature start player-list-endpoint`

## Acceptance Criteria
- `GET /api/players/` returns paginated list of players (20 per page).
- Supports query filters: `?team={id}`, `?position={pos}`, `?availability={status}`.
- Endpoint is public (no auth required).
- Test: returns all players without filters.
- Test: `?team=` filters correctly.
- Test: `?position=PG` returns only point guards.
- Test: `?availability=out` returns only unavailable players.
- Test: multiple filters combined work correctly.

---

#[ ] TASK 09 — Player Detail Endpoint

## Branch
`git flow feature start player-detail-endpoint`

## Acceptance Criteria
- `GET /api/players/{id}/` returns full player details including team name.
- Returns `404` for non-existent player.
- Endpoint is public (no auth required).
- Test: returns correct player data.
- Test: unknown id returns 404.

---

#[ ] TASK 10 — Player Create & Update Endpoints (Admin)

## Branch
`git flow feature start player-admin-endpoints`

## Acceptance Criteria
- `POST /api/players/` creates a new player (admin only).
- `PUT /api/players/{id}/` updates a player (admin only).
- Both return `403` for non-admin users.
- Both return `401` for unauthenticated requests.
- `PUT` returns `404` for non-existent player.
- Test: admin can create a player.
- Test: admin can update a player.
- Test: non-admin gets 403.
- Test: unauthenticated user gets 401.

---

## 🔔 Milestone 5 — Subscriptions

---

#[ ] TASK 11 — Subscription Model

## Branch
`git flow feature start subscription-model`

## Acceptance Criteria
- `Subscription` model exists with fields: `id`, `user (FK)`, `player (FK)`, `created_at`.
- `UNIQUE` constraint on `(user, player)` pair.
- Migration runs without errors.
- Test: Subscription can be created.
- Test: Duplicate subscription raises IntegrityError.

---

#[ ] TASK 12 — Subscriptions Endpoints

## Branch
`git flow feature start subscriptions-endpoints`

## Acceptance Criteria
- `GET /api/subscriptions/` returns only subscriptions of the authenticated user.
- `POST /api/subscriptions/` creates subscription for `{ player_id }`.
- `DELETE /api/subscriptions/{id}/` removes subscription (only own).
- All endpoints require authentication (401 otherwise).
- Subscribing to the same player twice returns `400`.
- Deleting another user's subscription returns `403`.
- Test: user sees only their own subscriptions.
- Test: subscribe to a player returns 201.
- Test: duplicate subscription returns 400.
- Test: delete own subscription returns 204.
- Test: delete another user's subscription returns 403.

---

## ⚡ Milestone 6 — Signals & Change Tracking

---

#[ ] TASK 13 — PlayerChangeLog Model

## Branch
`git flow feature start player-changelog-model`

## Acceptance Criteria
- `PlayerChangeLog` model exists with fields: `id`, `player (FK)`, `field_name`, `old_value`, `new_value`, `changed_at`.
- Migration runs without errors.
- Test: ChangeLog entry can be created manually.

---

#[ ] TASK 14 — Player Change Detection Signal

## Branch
`git flow feature start player-change-signal`

## Acceptance Criteria
- Django `post_save` signal on `Player` detects changes in tracked fields: `availability`, `injury_note`, `team`, `contract_type`, `contract_end`, `salary_usd`, `jersey_number`.
- For each changed field, a `PlayerChangeLog` entry is created with `old_value` and `new_value`.
- Signal does NOT fire on Player creation (only on update).
- Signal does NOT create a log entry if the value didn't actually change.
- Test: updating `availability` creates a ChangeLog entry.
- Test: updating a non-tracked field does NOT create a ChangeLog entry.
- Test: creating a new player does NOT create a ChangeLog entry.
- Test: value unchanged on save does NOT create a ChangeLog entry.

---

#[ ] TASK 15 — Notification Model

## Branch
`git flow feature start notification-model`

## Acceptance Criteria
- `Notification` model exists with fields: `id`, `user (FK)`, `change_log (FK → PlayerChangeLog)`, `is_read`, `sent_at`.
- `is_read` defaults to `False`.
- Migration runs without errors.
- Test: Notification can be created.
- Test: `is_read` defaults to False.

---

#[ ] TASK 16 — Notification Creation on Player Change

## Branch
`git flow feature start notification-creation`

## Acceptance Criteria
- When a `PlayerChangeLog` entry is created, a `Notification` is created for every user subscribed to that player.
- Users NOT subscribed to the player do NOT receive a notification.
- Test: 3 users subscribed to player → 3 notifications created on change.
- Test: user not subscribed → no notification created.
- Test: one player change creates one notification per user per changed field.

---

#[ ] TASK 17 — Email Notification on Player Change

## Branch
`git flow feature start email-notifications`

## Acceptance Criteria
- When a `Notification` is created, an email is sent to the user.
- Email contains: player name, changed field, old value, new value.
- Email subject format: `[NBA Feed] {Player Name} — {field} updated`.
- In test environment, Django `EMAIL_BACKEND` is set to `locmem` (no real emails sent).
- `sent_at` is populated on the Notification after email is sent.
- Test: email is sent to correct user on player change.
- Test: email contains correct player and field information.
- Test: `sent_at` is set after sending.
- Test: email is NOT sent if user has no subscription.

---

## 📰 Milestone 7 — Feed

---

#[ ] TASK 18 — Feed Endpoints

## Branch
`git flow feature start feed-endpoints`

## Acceptance Criteria
- `GET /api/feed/` returns notifications for the authenticated user, newest first.
- Supports `?unread=true` filter to return only unread notifications.
- `GET /api/feed/{notification_id}/` returns notification detail and marks it as `is_read=True`.
- Returns `404` for notification that doesn't belong to the user.
- All endpoints require authentication (401 otherwise).
- Test: feed returns only current user's notifications.
- Test: `?unread=true` returns only unread notifications.
- Test: accessing detail marks notification as read.
- Test: accessing another user's notification returns 404.

---

## 🌱 Milestone 8 — Seed Data

---

#[ ] TASK 19 — Seed Management Command

## Branch
`git flow feature start seed-data`

## Acceptance Criteria
- Django management command `python manage.py seed_db` exists.
- Seeds at least 5 Teams (covering both conferences).
- Seeds at least 20 Players distributed across teams.
- Command is idempotent (running it twice doesn't create duplicates).
- Test: running seed creates expected number of teams and players.
- Test: running seed twice does not create duplicates.

---