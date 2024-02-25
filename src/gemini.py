import google.generativeai as genai
import os
import sys
from logger import logging
from exception import CustomException
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

class GenerateSummary:
    def __init__(self, transcript, prompt = None):

        if prompt == None:
            prompt  =  """
                        You are Yotube video summarizer. You will be taking the transcript text
                        and summarizing the entire video and providing the important summary in points
                        within 250 words. Please provide the summary of the text given here: 
                    """
        
        self.transcript = transcript
        self.prompt = prompt
    
    def summarise(self):
        try:
            logging.info('Summarization starts')
            self.model = genai.GenerativeModel("gemini-pro")
            self.result = self.model.generate_content(self.prompt + self.transcript)
            logging.info('Summarization completed')

            return self.result.text
        
        except Exception as e:
            logging.info('Exception occured during Summarization')
            raise CustomException(e, sys)
