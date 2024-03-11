from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

NOTION_TOKEN = os.environ.get('NOTION_SECRET')
DATABASE_ID_FOR_VIDEOS = os.environ.get('VIDEO_DB')
DATABASE_ID_FOR_LOGGING = os.environ.get('LOGGED_DB')

from functions import fetch_random_workout_from_videos_database, add_workout_to_database, log_completed_workout

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/random-workout')
def random_workout():
    random_workout = fetch_random_workout_from_videos_database(NOTION_TOKEN, DATABASE_ID_FOR_VIDEOS)
    # Extract the necessary details, for example, the URL, to pass to the template
    video_url = random_workout.get('properties', {}).get('URL', {}).get('url', 'No URL Found')
    return render_template('random_workout.html', video_url=video_url)



@app.route('/log-workout', methods=['GET', 'POST'])
def log_workout_route():
    if request.method == 'POST':
        try:
            # Extract data from the form
            name = request.form['name']
            tags = request.form.getlist('tags')  # Assuming this is a list of tags
            date = request.form['date']
            heaviest_weight = request.form.get('heaviest_weight', type=int)

            # Assuming the function is updated to handle all necessary fields
            response = log_completed_workout(NOTION_TOKEN, DATABASE_ID_FOR_LOGGING, name, tags, date, heaviest_weight)
            
            # Check if the response from the function is what you expect
            if response is not None:
                return render_template('success.html')
            else:
                return "Failed to log workout", 500
        except Exception as e:
            print(f"An error occurred: {e}")
            # In a production app, you would log this to a file or error tracking service
            return "An error occurred while trying to log the workout", 500
    return render_template('log_workout.html')

@app.route('/add-workout', methods=['GET', 'POST'])
def add_workout():
    if request.method == 'POST':
        workout_name = request.form['name']
        workout_url = request.form['url']
        workout_equipment = request.form['equipment']
        
        result = add_workout_to_database(NOTION_TOKEN, DATABASE_ID_FOR_VIDEOS, workout_name, workout_url, workout_equipment)
        if result:
            return render_template('success.html', message="Workout added successfully!")
        else:
            return render_template('error.html', message="Failed to add workout.")
    return render_template('add_workout_form.html')




