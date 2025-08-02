"""
Transcript Handling Module

This module manages video transcript extraction and processing.
It handles both API-based transcript retrieval and speech-to-text
conversion when needed.
"""

class TranscriptHandler:
    def __init__(self):
        pass
        
    def get_transcript(self, video_id: str) -> str:
        """Retrieve transcript for a given video."""
        raise NotImplementedError
        
    def extract_from_audio(self, audio_path: str) -> str:
        """Extract transcript from video audio using speech-to-text."""
        raise NotImplementedError
