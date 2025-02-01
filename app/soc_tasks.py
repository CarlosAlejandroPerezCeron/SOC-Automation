import subprocess
from app.logging_config import log_security_event

def block_ip(ip_address):
    command = f"iptables -A INPUT -s {ip_address} -j DROP"
    try:
        subprocess.run(command, shell=True, check=True)
        log_security_event("BLOCK_IP", f"IP {ip_address} bloqueada exitosamente.")
        return f"IP {ip_address} bloqueada."
    except subprocess.CalledProcessError:
        log_security_event("BLOCK_IP_FAILURE", f"Error al bloquear IP {ip_address}.")
        return f"Error al bloquear IP {ip_address}."
