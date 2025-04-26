# Todo-Application

## Install instructions

Please configure the `sample.env` file before proceeding with the installation. Refer to the detailed configuration
guide in [Configuration](#configuration).

For a quick and efficient setup, it is recommended to use the provided script. Find instructions
in [Script Installation](#script-installation).
> ⚠ **Note:** The script will automatically run the server after setup.

If you prefer a manual setup, follow the steps outlined in [Manual Installation](#manual-installation).

Once installation is complete, see how to launch the project in [How to Run](#how-to-run).

## Configuration

If you're using an online database, ensure that you update the following variable in your `sample.env` file:

- `DATABASE_URL`: Replace this with your own database credentials. Obtain your Neon database URL by following the
  instructions provided in the [Connect with psql guide](https://neon.tech/docs/connect/query-with-psql-editor).

> **Note**:  
> If you try to run the application without setting `DATABASE_URL` or provide an invalid Neon URL, it will automatically **fallback to using a local SQLite3 database** for development purposes.

## Script Installation

1. Clone this repository by running the following command in your terminal:

```
git clone https://github.com/Nantawat6510545543/Todo-Application
```

2. Change your working directory to the project folder:

```
cd Todo-Application
```

3. Execute the setup script based on your operating system:

   for **Mac/Linux**, use this command:
    ```
    chmod +x linux-setup-script.sh
    ./linux-setup-script.sh
    ```

   for **Windows**, use this command:
    ```
    window-setup-script.bat
    ```

## Manual Installation

1. Clone this repository by running the following command in your terminal:

```
git clone https://github.com/Nantawat6510545543/Todo-Application
```

2. Change your working directory to the project folder:

```
cd Todo-Application
```

3. Create and activate a virtual environment:

   for **Mac/Linux**, use this command:
    ```
   python -m venv venv           # Create the virtual environment in "venv/" (only once)
   source ./venv/bin/activate           # Start the virtual environment in bash or zsh
    ```

   for **Windows**, use this command:
    ```
    python -m venv venv
    call  .\venv\Scripts\activate
    ```

4. Create a `.env` file by copying the contents of `sample.env`:

   for **Mac/Linux**, use this command:
    ```
   cp sample.env .env
   ```

   for **Windows**, use this command:
    ```
   copy sample.env .env
   ```

5. Install dependencies by running:

```
pip install -r requirements.txt
```

6. Create a new database by running migrations:

```
python manage.py migrate
```

7. Setup oauth system running setup_oauth:

```
python manage.py setup_oauth
```

## How to run

1. To run the local server

```
python manage.py runserver
```

2. To access the app at http://localhost:8000

3. To deactivate the virtual environment

```
deactivate
```
