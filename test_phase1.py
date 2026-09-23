from src.ingestion.linux_auth import LinuxAuthParser
import json

def main():
    parser = LinuxAuthParser()
    log_file = "data/sample_logs/auth_sample.log"
    
    print("--- Procesando archivo de logs ---")
    results = parser.parse_file(log_file)
    
    # Imprimir el resultado estructurado
    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    main()