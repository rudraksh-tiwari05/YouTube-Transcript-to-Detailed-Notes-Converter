
```markdown
# YouTube Transcript to Detailed Notes Converter

This Streamlit app converts YouTube transcripts into detailed notes using Google Generative AI.

## Features
- Extracts transcript from a YouTube video.
- Summarizes the transcript into detailed notes.
- Displays the video's thumbnail.

## Prerequisites
- Python 3.7+
- Google Generative AI API Key
- YouTube Transcript API

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/youtube-transcript-notes-converter.git
   cd youtube-transcript-notes-converter
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project directory and add your Google API key:
   ```
   Google_api_key=your_google_api_key_here
   ```

## Usage

1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Open your web browser and go to `http://localhost:8501`.

3. Enter the YouTube video link and click "Get Detailed Notes" to retrieve and summarize the transcript.

## File Structure

- `app.py`: Main Streamlit app file.
- `requirements.txt`: List of required Python packages.
- `.env`: Environment file containing API keys (not included in the repository).

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Author

Rudraksh Tiwari

## Acknowledgments

- [Streamlit](https://www.streamlit.io/)
- [YouTube Transcript API](https://github.com/jdepoix/youtube-transcript-api)
- [Google Generative AI](https://developers.generativeai.com/)

---

