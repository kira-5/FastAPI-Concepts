# FastAPI EnvManager

FastAPI EnvManager is a Python web application built with FastAPI that helps manage different environments, including development and production. It provides a convenient way to switch between configurations and settings for various deployment scenarios.


## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [License](#license)
- [Acknowledgments](#acknowledgments)


## Installation

To get started with FastAPI EnvManager, follow these installation steps:

1. Clone the repository:

   ```shell
   git clone https://github.com/yourusername/fastapi-envmanager.git

2. Navigate to the project directory:
    ```shell
   cd fastapi-envmanager

3. Install dependencies using pip:
    ```shell
   pip install -r requirements.txt

4. Set up your environment variables as described in the Configuration section.

5. Start the FastAPI application:
   - To start the FastAPI application, use the following commands depending on your environment:
    - ### Development Environment
        ```shell
        APP_ENV=development uvicorn main:app
    - ### Production Environment
        ```shell
        APP_ENV=production uvicorn main:app


## Usage

FastAPI EnvManager provides a web-based interface for managing your application's environment settings. Follow these steps to use it:

1. **Access the Web Interface**:

   - Open your web browser and navigate to [http://localhost:8000](http://localhost:8000) (or use the appropriate URL if hosted elsewhere).

3. **Switch Between Environments**:

   - Once logged in, you'll see an interface that allows you to switch between different environment configurations.
   - Select the environment you want to configure, such as "Development" or "Production."

4. **Customize Configuration Settings**:

   - After selecting an environment, you can customize configuration settings specific to that environment.
   - Modify settings such as database connections, API keys, and feature toggles according to your requirements.

5. **Save Changes**:

   - Be sure to save your changes after customizing the configuration.
   - The application will update the settings for the selected environment.

FastAPI EnvManager simplifies the process of managing environment-specific configurations, making it easier to switch between development and production settings as needed for your project.


## Configuration

FastAPI EnvManager uses environment variables to configure the application. Below are the available environment variables:

- **APP_ENV**: Set this variable to either "development" or "production" to specify the active environment for your application.

- Here's an example of how to set the environment variable for a development environment:
    ```shell
    export APP_ENV=development

Before running the FastAPI EnvManager application, ensure that you have the necessary environment variables correctly set according to your deployment needs. The value of `APP_ENV` determines which environment configuration the application will use. For example, set it to "development" for local development and testing, and "production" when deploying to a live production server.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


## Acknowledgments

- Thanks to the FastAPI community for their excellent documentation and contributions.
- Special thanks to Abhishek Singh.
