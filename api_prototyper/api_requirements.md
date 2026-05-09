# API Requirements – EduTrack API

## Domain
Academic management platform for managing assignments, grades, and AI study plans.

## Target Users
- **Students**: View assignments, grades, and personalized study plans.
- **Teachers**: Manage assignments, grades, and attendance.
- **Admins**: Manage accounts and institutional reports.

## Core Operations
1. Register user
2. Authenticate user (JWT)
3. Create assignment
4. Submit assignment
5. Update grade
6. Get student grades
7. Mark attendance
8. Get attendance records
9. Generate AI study plan
10. Get GPA summary
11. Delete assignment
12. Search assignments

## Data Rules
- Email must be unique and valid.
- Password must be at least 8 characters.
- Grades must be between 0 and 100.
- Attendance status: present, absent, or late.

## Non-Functional
- Latency: < 300ms.
- Security: HTTPS and JWT required.
- Rate Limit: 100 requests per minute.
- Auth: Passwords hashed with bcrypt.