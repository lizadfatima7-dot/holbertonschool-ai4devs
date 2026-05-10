# System Architecture

## High-Level Overview
The AI-Powered Startup MVP Builder follows a classic Client-Server architecture with an integrated AI Processing Layer.

### Components:
- **Frontend (Client)**: A React-based web interface where users input requirements.
- **API Gateway**: Handles requests and routes them to the appropriate services.
- **AI Engine (LLM)**: Processes natural language descriptions to generate code and schemas.
- **Code Generator Service**: Orchestrates the assembly of the final project files.
- **Database**: Stores user project metadata and generated schemas (PostgreSQL).



### Workflow:
1. User submits business description via Frontend.
2. API Gateway sends data to the AI Engine.
3. AI Engine returns structured JSON representing the app logic.
4. Code Generator creates files and provides a download link.