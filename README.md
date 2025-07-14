# Guidance for Task

This repository contains the foundational code for a FastAPI microservice that allows instructors to schedule future delivery of course announcements to students via email (simulated delivery). The code structure is modular and production-like, and you are required to complete its intermediate-level implementation.

## What You Must Do
- **Implement/finish a FastAPI POST endpoint** at `/announcements` to allow scheduling course announcements for future delivery.
- **Input requirements:** A title, body, list of recipient emails, and a scheduled UTC time. You must validate:
  - Title and body (non-empty, reasonable length)
  - Each email is valid
  - Scheduled time is strictly in the future
- **Persistence:** Store all scheduled announcements in the database with all necessary fields.
- **Delivery Simulation:** Use async background tasks to log simulated "deliveries" to each provided email at the correct future time. (No real emails are sent; use Python logging.)
- **Modular code:** Ensure routers, models, and schemas are separated.
- **Robust error handling:** Return helpful HTTP error codes and detail for invalid or conflicting requests (e.g., duplicate announcements).
- **OpenAPI Documentation:** Ensure the endpoint is fully self-documented, including example schema, field types, and all relevant responses.
- **Confirmation:** Return a clear confirmation response when an announcement is scheduled.

## Constraints & Tech
- Use FastAPI, SQLAlchemy/SQLite, Pydantic
- Log simulated delivery via Python logging
- Input validation must be robust (see requirements above)
- Keep everything within the provided modular structure
- Ensure OpenAPI docs clearly show request and response shape with examples

## Verifying Your Solution
- Submitting a valid JSON body to the `/announcements` endpoint with all required fields should schedule the announcement and return confirmation (and be persisted).
- Background logging of simulated delivery for each user email should occur at the provided scheduled time (check logs).
- Invalid requests (bad emails, missing fields, scheduled time in past) should return appropriate HTTP errors.
- The OpenAPI docs (Swagger UI) must include clear documentation for all fields with realistic examples.

---
Work within the existing file/module structure and avoid unnecessary complexity. Focus on robust input validation, database persistence, future delivery simulation, structured error handling, and excellent OpenAPI docs.