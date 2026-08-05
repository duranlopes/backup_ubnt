# Backup UBNT Radios

Python utility to back up configuration files from Ubiquiti/UBNT radios over SSH/SCP.

The script connects to each radio listed in `config.py`, downloads the default UBNT configuration file (`/tmp/system.cfg`), and saves a renamed copy under the local `backup/` directory.

## Features

- Back up multiple UBNT radios in one run
- Uses SSH/SCP through `paramiko` and `scp`
- Saves files with friendly device names, for example `backup/station.cfg`
- Simple configuration through `config.py`
- Dependencies updated to patched versions to address known GitHub Dependabot security alerts

## Requirements

- Python 3.11 or newer recommended
- Network access to the radios via SSH
- Valid SSH username/password for each radio

## Installation

Clone the repository and create a virtual environment:

```bash
git clone https://github.com/duranlopes/backup_ubnt.git
cd backup_ubnt
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Configuration

Edit `config.py` before running the script:

```python
# Device name -> IP address
ips = {
    "station": "192.168.15.33",
    "ap": "192.168.15.32",
}

user = "admin"                 # Radio username
password = "yourpassword"      # Radio password
localfile = "/tmp/system.cfg"  # Default UBNT config file path
```

### Configuration fields

| Field | Description |
| --- | --- |
| `ips` | Dictionary where the key is the backup file name and the value is the radio IP address. |
| `user` | SSH username used to connect to the radios. |
| `password` | SSH password used to connect to the radios. |
| `localfile` | Remote file path to download from each radio. UBNT radios commonly expose `/tmp/system.cfg`. |

## Usage

Run:

```bash
python backup_ubiquiti.py
```

For each entry in `ips`, the script will:

1. Connect to the radio via SSH.
2. Download `localfile` using SCP.
3. Save the file in `backup/`.
4. Rename it using the device name from `ips`, for example `backup/ap.cfg`.

## Output

Example output directory:

```text
backup/
|-- ap.cfg
`-- station.cfg
```

## Security notes

- Do not commit real production passwords to `config.py`.
- Restrict repository access if `config.py` contains sensitive device details.
- Keep dependencies updated with Dependabot or `pip-audit`.

## Verify dependencies

To check for known dependency vulnerabilities locally:

```bash
source .venv/bin/activate
pip install pip-audit
pip-audit -r requirements.txt
```

## Troubleshooting

| Symptom | Possible cause | What to check |
| --- | --- | --- |
| `Falha na autenticacao` | Invalid credentials | Confirm `user` and `password` in `config.py`. |
| `Nao foi possivel conectar` | Radio unreachable | Check IP address, routing, firewall, and SSH service. |
| Backup file is missing | Remote file path changed | Confirm `localfile` exists on the radio. |
| Only one file is saved | Duplicate device names or rename failure | Ensure each key in `ips` is unique. |
