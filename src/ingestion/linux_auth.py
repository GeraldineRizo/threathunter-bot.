import re
from typing import Dict, Any, Optional
from .base import BaseLogParser

class LinuxAuthParser(BaseLogParser):
    """Parser para logs de autenticación de Linux (/var/log/auth.log)."""

    def __init__(self):
        # Patrón para detectar intentos fallidos de SSH
        self.failed_ssh_pattern = re.compile(
            r"(?P<timestamp>\w{3}\s+\d+\s+\d{2}:\d{2}:\d{2})\s+\S+\s+sshd\[\d+\]:\s+Failed password for (?:invalid user )?(?P<user>\S+) from (?P<ip>\S+) port \d+ ssh2"
        )

    def parse_line(self, line: str) -> Optional[Dict[str, Any]]:
        match = self.failed_ssh_pattern.search(line)
        if match:
            data = match.groupdict()
            return {
                "timestamp": data["timestamp"],
                "source_ip": data["ip"],
                "event_type": "FAILED_LOGIN",
                "service": "sshd",
                "user": data["user"],
                "severity": "MEDIUM",
                "raw_log": line
            }
        
        # Estructura por defecto para logs no mapeados
        return {
            "timestamp": "UNKNOWN",
            "source_ip": "N/A",
            "event_type": "GENERAL_EVENT",
            "service": "syslog",
            "user": "N/A",
            "severity": "LOW",
            "raw_log": line
        }