# Stride - A Workout Logger App

Stride is a mobile-responsive web application that was created to assist workout tracking by integrating with the Notion API to manage and retrieve workout videos and logs. Crafted with Flask and Python, styled with Tailwind CSS, and deployed via Fly.io, Stride allow you to randomly select workouts from an existing Notion database, and log sessions.

https://stride.fly.dev

## Features

- Add workout videos to your Notion database.
- Fetch a random workout from the list.
- Log completed workouts with details in Notion.

## Local Development Setup

Before you begin, ensure you have Python and pip installed on your system.

1. **Clone the Repository:**

```bash
git clone https://yourrepository/Stride.git
cd Stride
```

2. **Create and Activate a Virtual Environment:**

For Unix/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

For Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

3. **Install Dependencies:**

```bash
pip install -r requirements.txt
```

4. **Environment Variables:**
   Set the necessary environment variables in your .env file:

makefile

FLASK_APP=app.py
FLASK_ENV=development
NOTION_SECRET=your_notion_secret
DATABASE_ID=your_notion_database_id

5. **Start the Flask Application:**

```bash
flask run
```

Your app should now be running on http://localhost:5000.

## Deploying to Fly.io

1. **Install Fly CLI:**
   Refer to the Fly.io documentation for instructions on installing the Fly CLI.

2. **Create a Fly.io Application:**

```bash
flyctl launch
```

Follow the prompts to set up your new app on Fly.io.

3. **Configure fly.toml:**
   Ensure fly.toml is correctly set up to expose the Flask app on the designated port.

4. **Set Fly.io Secrets:**

```bash
flyctl secrets set NOTION_SECRET=your_notion_secret DATABASE_ID=your_notion_database_id
```

5. **Deploy Your Application:**

```bash
flyctl deploy
```

Monitor the output to ensure your application deploys successfully.

6. **View Your Application:**

```bash
flyctl open
```

This will open your application in a web browser.

## Project Structure

- /templates: HTML templates for the web interface.
- /static: CSS, JavaScript, and other static files.
- app.py: The main Flask application file.
- requirements.txt: Required Python dependencies.
