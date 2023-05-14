# 📥 tinyjal

A script to download files on `Just Another Library`

## 📖 How to build and run ?

1. Install the system dependencies
    - `python`
2. Install the Python dependencies

```bash
python -m pip install -r requirements.txt
```

## 📜 Usage example

```bash
python tinyjal.py <url>/archives/art/Animal/birds/ ./birds
```

## ℹ️ Tor controller

To trigger a new Tor circuit, we are using the Tor controller with environment variables:

- **`TOR_CONTROLLER_PORT`**: Represents the Tor controller port
- **`TOR_CONTROLLER_PASSWORD`** Represents the Tor controller password as plaintext
  