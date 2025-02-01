import ansible_runner
from app.logging_config import log_security_event
from app.database import insert_log

def execute_playbook(playbook_path):
    log_security_event("PLAYBOOK_EXECUTION", f"Ejecutando {playbook_path}")
    insert_log("PLAYBOOK_EXECUTION", f"Ejecutando {playbook_path}")

    r = ansible_runner.run(private_data_dir='.', playbook=playbook_path)
    
    if r.status == "successful":
        log_security_event("PLAYBOOK_SUCCESS", f"Ejecutado correctamente: {playbook_path}")
        insert_log("PLAYBOOK_SUCCESS", f"Ejecutado correctamente: {playbook_path}")
    else:
        log_security_event("PLAYBOOK_FAILURE", f"Error en {playbook_path}: {r.rc}")
        insert_log("PLAYBOOK_FAILURE", f"Error en {playbook_path}: {r.rc}")

    return r.status
