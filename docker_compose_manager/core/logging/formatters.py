"""
Custom log formatters for various output formats.
"""

from pythonjsonlogger import jsonlogger
from datetime import datetime, timezone


class ISOJSONFormatter(jsonlogger.JsonFormatter):
    """JSON formatter with ISO 8601 timestamps and custom fields."""
    
    def add_fields(self, log_record, record, message_dict):
        """Customize log record fields."""
        super().add_fields(log_record, record, message_dict)
        
        # ISO 8601 timestamp with timezone
        log_record['timestamp'] = datetime.now(timezone.utc).isoformat()
        log_record['level'] = record.levelname
        log_record['logger'] = record.name
        log_record['module'] = record.module
        log_record['function'] = record.funcName
        log_record['line_number'] = record.lineno
        
        # Add exception info if present
        if record.exc_info:
            log_record['exception'] = self.formatException(record.exc_info)
