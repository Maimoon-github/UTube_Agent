"""
YouTube Data Ingestion Module

This module handles the ingestion of YouTube data including video metadata,
transcripts, and engagement metrics.
"""

from .youtube_api import YouTubeAPI
from .transcript import TranscriptHandler
from .metrics import MetricsCollector

__all__ = ['YouTubeAPI', 'TranscriptHandler', 'MetricsCollector']
