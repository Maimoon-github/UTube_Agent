"""
Data Schema Module

This module defines the data schemas for storing YouTube video data
including metadata, transcripts, and metrics.
"""

class VideoSchema:
    """Schema for storing video data."""
    
    def __init__(self):
        self.schema = {
            'video_id': str,
            'title': str,
            'description': str,
            'transcript': str,
            'metrics': dict,
            'created_at': str,
            'updated_at': str
        }
        
    def validate(self, data: dict) -> bool:
        """Validate data against schema."""
        raise NotImplementedError
