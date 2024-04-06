# Django Project: Catalyst_count

## Overview

Catalyst_count is a Django web application designed to upload the data using csv or xlsx file format and vies that records. It utilizes the Django framework for the backend and Bootstrap 4 for the frontend. The project includes functionality for user authentication, uploading CSV or Excel files, viewing records via REST API, and managing user accounts.

## Features

- **User Authentication**: Allows users to register, log in, and log out securely.
- **CSV/Excel File Upload**: Enables users to upload CSV or Excel files to add records to the database.
- **View Records**: Provides an interface to view records from the database via REST API.
- **User Management**: Allows administrators to manage user accounts, including creation, viewing, updating, and deletion.

## Technologies Used

- Django: A high-level Python web framework for rapid development.
- Bootstrap 4: A popular CSS framework for building responsive and mobile-first websites.
- PostgreSQL: An open-source relational database management system.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your_username/your_project.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd your_project
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the PostgreSQL database:**

    - Install PostgreSQL and create a database.
    - Update the database configuration in `settings.py` to match your PostgreSQL configuration.

5. **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

6. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

7. **Access the application:**

    Open your web browser and navigate to `http://localhost:8000`.

## Usage

1. **Login:**
   - Access the login page (`/login`) and enter your credentials to log in.

2. **Upload CSV or Excel files:**
   - Navigate to the upload page (`/upload`) and upload CSV or Excel files to add records to the database.

3. **View records:**
   - Access the view records page (`/records`) to view records from the database via REST API.

4. **User management:**
   - Access the user management page (`/users`) to manage user accounts, including creation, viewing, updating, and deletion.

## Configuration

- **Database:** Modify database settings in `settings.py` to match your PostgreSQL configuration.
- **Static files:** Customize static files (CSS, JavaScript) in the `static` directory.
- **Templates:** Customize HTML templates in the `templates` directory.

## Testing

- Describe how to run tests and any testing frameworks used.

## Contributing

- Guidelines for contributing to the project (e.g., reporting bugs, suggesting improvements, coding standards).

## License

- Specify the project's license.

## Credits

- Acknowledge any contributors, libraries, or resources used in the project.

## Contact

- Provide contact information for questions or feedback about the project.
# catalyst_count
# catalyst_count
