"""
JSON Logger Implementation with ISO 8601 timestamps.
"""

import logging
import sys
from typing import Optional
from pythonjsonlogger import jsonlogger
from datetime import datetime, timezone


class ISOJSONFormatter(jsonlogger.JsonFormatter):
    """Custom JSON formatter with ISO 8601 timestamps."""
    
    def add_fields(self, log_record, record, message_dict):
        """Add custom fields to log record."""
        super().add_fields(log_record, record, message_dict)
        
        # Add ISO 8601 timestamp
        if not log_record.get('timestamp'):
            log_record['timestamp'] = datetime.now(timezone.utc).isoformat()
        
        # Add standard fields
        log_record['level'] = record.levelname
        log_record['logger_name'] = record.name
        log_record['module'] = record.module
        log_record['function'] = record.funcName
        log_record['line'] = record.lineno
        
        # Add process/thread info
        log_record['process_id'] = record.process
        log_record['thread_id'] = record.thread
        
        # Add context if available
        if hasattr(record, 'context'):
            log_record['context'] = record.context


class JSONLogger:
    """Wrapper for JSON logger with common configuration."""
    
    def __init__(self, name: str, level: int = logging.INFO, 
                 log_file: Optional[str] = None):
        """
        Initialize JSON logger.
        
        Args:
            name: Logger name
            level: Logging level
            log_file: Optional file path for file logging
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self.logger.propagate = False
        
        # Remove existing handlers
        self.logger.handlers.clear()
        
        # Console handler with JSON formatting
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(level)
        formatter = ISOJSONFormatter(
            '%(timestamp)s %(level)s %(logger_name)s %(message)s'
        )
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)
        
        # File handler if specified
        if log_file:
            file_handler = logging.FileHandler(log_file)
            file_handler.setLevel(level)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)
    
    def get_logger(self):
        """Get the underlying logger instance."""
        return self.logger


# Global logger cache
_loggers = {}


def get_logger(name: str, level: int = logging.INFO, 
               log_file: Optional[str] = None) -> logging.Logger:
    """
    Get or create a JSON logger.
    
    Args:
        name: Logger name
        level: Logging level
        log_file: Optional file path for file logging
        
    Returns:
        Configured logger instance
    """
    cache_key = f"{name}:{level}:{log_file}"
    
    if cache_key not in _loggers:
        json_logger = JSONLogger(name, level, log_file)
        _loggers[cache_key] = json_logger.get_logger()
    
    return _loggers[cache_key]
