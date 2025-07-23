# Developer Setup Guide - project-build-a-comprehensive

This guide provides a comprehensive setup for developers working on "project-build-a-comprehensive," a legal case management system.  We recommend using Docker for a consistent and simplified development environment.

## Prerequisites

* **Required Software Versions:**
    * Python 3.9+
    * Node.js 16+
    * PostgreSQL 14+ (or compatible database)
    * Docker Desktop (if using Docker option)
    * Docker Compose (if using Docker option)

* **Development Tools:**
    * Git
    * Text editor or IDE (see recommendations below)

* **IDE Recommendations and Configurations:**
    * **VS Code:** Highly recommended due to its excellent extensions for Python, JavaScript, and debugging. Install extensions like "Python," "Prettier," "ESLint," and "Docker."
    * **PyCharm:** A robust IDE specifically designed for Python development.  Provides excellent debugging and code completion features.
    * **WebStorm:** A powerful IDE for JavaScript development, ideal for the frontend portion.

## Local Development Setup

### Option 1: Docker Development (Recommended)

1. **Clone Repository:**
   ```bash
   git clone <repository_url>
   cd project-build-a-comprehensive
   ```

2. **Docker Setup:** Ensure Docker Desktop and Docker Compose are installed and running.

3. **Development `docker-compose.yml` Configuration:**  This file (located in the root directory) defines the services (database, backend, frontend).  A sample might look like this:

   ```yaml
   version: "3.9"
   services:
     db:
       image: postgres:14
       ports:
         - "5432:5432"
       environment:
         - POSTGRES_USER=your_db_user
         - POSTGRES_PASSWORD=your_db_password
         - POSTGRES_DB=your_db_name
     backend:
       build: ./backend
       ports:
         - "8000:8000"
       depends_on:
         - db
       environment:
         - .env
     frontend:
       build: ./frontend
       ports:
         - "3000:3000"
       depends_on:
         - backend
   ```

4. **Hot Reload Setup:**  The `docker-compose.yml` file should be configured to automatically rebuild and restart the backend and frontend containers upon code changes.  This typically involves using volumes to mount your project directories into the containers.  Consult your framework's documentation for specific hot reload configurations (e.g., using Nodemon for the frontend).


### Option 2: Native Development

1. **Backend Setup:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r backend/requirements.txt
   ```

2. **Frontend Setup:**
   ```bash
   cd frontend
   npm install
   ```

3. **Database Setup:**
   Download and install PostgreSQL. Create a database with the name specified in your `.env` file (see below).  Configure the database user and password accordingly.


## Environment Configuration

* **Required Environment Variables:**  These will vary depending on your application's needs.  Examples:
    * `DATABASE_URL`: Connection string to your database.
    * `SECRET_KEY`:  A secret key for security (backend).
    * `STRIPE_SECRET_KEY`:  Stripe API key for payment processing.
    * `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_USERNAME`, `EMAIL_PASSWORD`:  Email server configuration.


* **Local Development `.env` File Setup:** Create a `.env` file in the root directory and populate it with your local environment variables:

   ```
   DATABASE_URL=postgresql://your_db_user:your_db_password@localhost:5432/your_db_name
   SECRET_KEY=your_secret_key
   # ... other environment variables
   ```

* **Configuration for Different Environments:** Use a configuration management system (e.g., environment variables, configuration files) to manage settings for different environments (development, staging, production).


## Running the Application

* **Start Commands (Docker):**
   ```bash
   docker-compose up -d --build
   ```

* **Start Commands (Native):**
   ```bash
   # Backend:
   cd backend
   python manage.py runserver 8000 # Or your preferred run command

   # Frontend:
   cd frontend
   npm start
   ```

* **Access Frontend and Backend:** The frontend will typically be accessible at `http://localhost:3000` (or the port defined in `docker-compose.yml` or your `package.json`). The backend API will be accessible at `http://localhost:8000` (or the port defined in `docker-compose.yml` or `manage.py`).

* **API Documentation Access:**  Use tools like Swagger or Postman to explore and test your APIs.


## Development Workflow

* **Git Workflow and Branching Strategy:** Use Gitflow or a similar branching strategy (e.g., feature branches for new features, hotfix branches for urgent bug fixes).

* **Code Formatting and Linting Setup:**  Use tools like `black` (Python) and `Prettier` (JavaScript) to enforce consistent code formatting.  Linters like `pylint` (Python) and `ESLint` (JavaScript) help catch potential errors.

* **Testing Procedures:** Write unit tests and integration tests.  Use a testing framework like `pytest` (Python) and `Jest` (JavaScript).

* **Debugging Setup:** Use your IDE's debugger or command-line debuggers (e.g., `pdb` in Python, browser developer tools for JavaScript).


## Database Management

* **Running Migrations:** Use database migration tools (e.g., Alembic for Python, Sequelize migrations for Node.js) to manage database schema changes.

* **Seeding Development Data:** Create scripts to populate your database with sample data for development.

* **Database Reset Procedures:**  Include scripts to easily reset your database to a clean state.


## Testing

* **Running Unit Tests:**  Use your chosen testing framework's command-line interface (e.g., `pytest` or `jest`).

* **Running Integration Tests:**  Similar to unit tests, but focus on interactions between different components.

* **Test Coverage Reports:** Use tools like `coverage.py` (Python) to generate reports on your test coverage.


## Common Development Tasks

* **Adding New API Endpoints:** Follow your framework's guidelines for creating new API endpoints (e.g., Django REST framework, Express.js).

* **Adding New Frontend Components:** Use your chosen frontend framework (e.g., React, Vue, Angular) to create new components.

* **Database Schema Changes:**  Use migrations to manage schema changes.

* **Adding Dependencies:**  Use `pip` (Python) and `npm` (JavaScript) to manage dependencies.


## Troubleshooting

* **Common Setup Issues:** Check your `.env` file for typos and ensure all required services are running.

* **Port Conflicts Resolution:** Change ports in your `docker-compose.yml` or configuration files if there are port conflicts.

* **Dependency Issues:** Use `pip freeze` and `npm ls` to check your dependencies and resolve conflicts.

* **Environment Variable Problems:** Ensure your environment variables are correctly set and accessible to your application.


## Contributing

* **Code Style Guidelines:** Adhere to the style guides for Python and JavaScript (PEP 8, StandardJS/Airbnb).

* **Pull Request Process:** Create clear and concise pull requests with descriptive titles and explanations.

* **Issue Reporting:** Use the issue tracker to report bugs and feature requests.  Provide clear and reproducible steps to reproduce the issue.


This guide provides a foundation for development. Specific details will depend on the chosen frameworks and technologies used in the project. Remember to consult the documentation for those technologies as you progress.
