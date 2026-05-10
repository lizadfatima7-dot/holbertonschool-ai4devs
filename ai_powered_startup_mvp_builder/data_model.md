# Data Model

## Entities

### 1. Project
Represents the main MVP project created by a user.
- `id` (UUID): Unique identifier.
- `name` (String): Project name.
- `description` (Text): Business idea description.
- `created_at` (Timestamp): Creation date.

### 2. SchemaEntity
Represents a database table or entity generated for a project.
- `id` (UUID): Unique identifier.
- `project_id` (FK): Reference to the Project.
- `name` (String): Entity name (e.g., "Users").
- `fields` (JSON): List of attributes and types.

### 3. GeneratedCode
Stores the metadata for the generated codebase.
- `id` (UUID): Unique identifier.
- `project_id` (FK): Reference to the Project.
- `language` (String): The programming language used (e.g., Python).
- `download_url` (String): Path to the generated ZIP file.