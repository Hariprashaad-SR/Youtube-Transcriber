# Tutorial: Creating Environment Files and Executing Streamlit for a YouTube Transcriber Project

In this tutorial, we will guide you through the process of setting up environment files and executing a Streamlit application for a YouTube transcriber project.

## Prerequisites

Before we begin, make sure you have the following installed on your system:

- Python (preferably Python 3.x)
- Pip (Python package manager)

## Step 1: Cloning Repository

1. Open your terminal or command prompt .
2. Move to the desired directory using  ```cd your_path```

3. Clone the repository by typing the below code in the terminal:
    ```
    git clone https://github.com/Hariprashaad-SR/Youtube-Transcriber.git``` 
4. Open this repo on a code editor (eg: VScode) and follow the below steps
## Step 2: Creating Virtual environment

#### For Mac OS
1. Create the virtual environment (venv) by typing the following command on the terminal

        python3 -m venv venv_name

3. Activate the virtual environment by ```source venv_name/bin/activate```

#### For Windows

1. Create the virtual environment (venv) by typing the following command on the terminal

        python3 -m venv venv_name

2. Activate the virtual environment by ```venv_name\Scripts\activate```

 ## Step 3: Installing dependencies

1. Install all dependencies by typing the following command on your terminal

        pip install -r requirements.txt


## Step 4: Setting up the Environment File

1. Create a new file named `.env` in your project directory.

7. Define the following environment variables in the `.env` file:
    ```
    GOOGLE_API_KEY = your_google_api_key
    ```

Replace `your_youtube_api_key` with your actual YouTube API key, which you can obtain from the [Google developers](https://console.developers.google.com/).


## Step 5: Running the Streamlit Application

1. Open your terminal or command prompt.


3. Run the following command to start the Streamlit application:
    ```
    streamlit run src/web.py
    ```

4. Visit `http://localhost:8501` in your web browser to view your Streamlit application.

5. Enter a YouTube video URL in the input field and click Enter. The transcribed text of the video should appear on the page. You can even download it !!!

That's it! You've successfully set up environment files and executed a Streamlit application for your YouTube transcriber project.
