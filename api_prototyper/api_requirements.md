# API Requirements - TaskMaster API

## Domain
AI-powered project and task management platform that allows developers and team leads to create, assign, track, and manage tasks and projects through a RESTful API.

## Target Users
- **Developers**: create and manage personal tasks, update task status, and track daily progress through API integrations.
- **Team Leads**: assign tasks to team members, monitor project progress, and generate reports through automated workflows.

## Core Operations
1. Create a new task with title, description, deadline, priority, and assignee
2. Get a task by ID
3. Update task details including status, priority, and assignee
4. Delete a task by ID
5. List all tasks with optional filters by status, priority, and assignee
6. Create a new project with name, description, and deadline
7. Get a project by ID with all associated tasks
8. Update project details
9. Delete a project by ID
10. List all projects with optional filters by status and owner
11. Assign a task to a team member by user ID
12. Get all tasks assigned to a specific user
13. Update task status from To Do to In Progress or Done
14. Search tasks by keyword in title or description

## Data Rules
- Task title must not be empty and must be between 3 and 100 characters
- Task priority must be one of: low, medium, high, or critical
- Task status must be one of: todo, in_progress, or done
- Deadline must be a valid ISO 8601 date and must not be in the past
- Project name must be unique per user account
- User ID must reference an existing user in the system
- Description field is optional but must not exceed 1000 characters
- Assignee must be a valid registered user

## Non-Functional
- Response time must be under 200ms for all read operations
- JWT authentication required for all endpoints
- Rate limiting of 100 requests per minute per authenticated user
- API must support pagination for list endpoints with default page size of 20
- All responses must return JSON format with consistent error structure
- API versioning required using URL prefix such as /api/v1
- HTTPS required for all endpoints in production