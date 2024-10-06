from pathlib import Path

current_path = Path('.').absolute().resolve()

logs_folder_path = current_path / "logs"
logs_folder_path.mkdir(mode=755, parents=True, exist_ok=True)

log_file = logs_folder_path / "log.txt"
log_file.touch(mode=755)