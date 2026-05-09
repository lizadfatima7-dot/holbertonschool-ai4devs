# API Requirements – EduTrack API

## Domain
Academic management platform for students and teachers to manage assignments, grades, attendance, and AI-powered study plans.

## Target Users
- **Students**: Access assignments, view grades, and retrieve personalized study plans.
- **Teachers**: Create assignments, update grades, and manage attendance records.
- **Admins**: Manage user accounts and generate institutional reports.

## Core Operations
1.  **Register User**: Create a new account for a student or teacher.
2.  **User Login**: Authenticate user and return a JWT token.
3.  **Create Assignment**: Add a new assignment to a specific class (Teacher).
4.  **Get Assignments**: List all assignments for a class or student.
5.  **Submit Assignment**: Upload or link completed work (Student).
6.  **Update Grade**: Assign or edit a numerical grade for a submission (Teacher).
7.  **Get Student Grades**: Retrieve a comprehensive list of grades for a user.
8.  **Mark Attendance**: Record student presence for a class session (Teacher).
9.  **Get Attendance Records**: Filter attendance by student or date range.
10. **Generate AI Study Plan**: Create a personalized study guide based on performance.
11. **Get Performance Summary**: Retrieve student GPA and academic analytics.
12. **Delete Assignment**: Remove an assignment from the database (Teacher/Admin).

## Data Rules
- **Email**: Must be unique and follow a valid email format.
- **Password**: Minimum 8 characters, including at least one uppercase letter and one number.
- **Grades**: Must be a numeric value between 0 and 100.
- **Dates**: Assignment due dates must be set in the future.
- **Attendance Status**: Must be one of the following: `present`, `absent`, or `late`.
- **Validation**: Student and Class IDs must exist before creating assignment records.
- **AI Logic**: An AI study plan requires at least 3 graded assignments to be generated.

## Non-Functional
- **Latency**: All endpoints must respond in under 300ms under normal load.
- **Security**: JWT authentication required for all endpoints except register and login.
- **Encryption**: Passwords must be hashed using bcrypt before storage.
- **Rate Limiting**: Maximum of 100 requests per minute per user.
- **Protocol**: All data must be transmitted over HTTPS.
- **Versioning**: API versioning must be handled via URL prefix (e.g., `/api/v1/`).