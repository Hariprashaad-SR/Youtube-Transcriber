from youtube_transcript_api import YouTubeTranscriptApi
from logger import logging
from exception import CustomException
import sys

class Transcribe:
    def __init__(self, url):
        self.url = url
        self.transcribeText = ''

    def InitiateTranscribe(self):
        try:
            logging.info('Transcription Started')
            self.video_id = self.url.split('=')[1]
            responses = YouTubeTranscriptApi.get_transcript(self.video_id)

            for response in responses:
                self.transcribeText += (' ' + response['text'])
            logging.info('Trasncription Ended Successfully')

            return (self.video_id, self.transcribeText)

        except Exception as e:
            logging.info('Exception occured during Transcription')
            raise CustomException(e, sys)