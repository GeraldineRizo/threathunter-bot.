from abc import ABC, abstractmethod
from typing import List, Dict, Any

class BaseLogParser(ABC):
    """Clase base para todos los parsers de logs del sistema."""

    @abstractmethod
    def parse_line(self, line: str) -> Dict[str, Any]:
        """Procesa una sola línea de log y devuelve un diccionario estructurado."""
        pass

    def parse_file(self, file_path: str) -> List[Dict[str, Any]]:
        """Lee un archivo de logs y procesa cada línea."""
        parsed_events = []
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line:
                    parsed = self.parse_line(line)
                    if parsed:
                        parsed_events.append(parsed)
        return parsed_events