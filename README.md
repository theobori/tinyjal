# 📥 tinyjal

A script to download files on `Just Another Library`

## 📖 How to build and run ?

1. Install the system dependencies
    - `python`
2. Install the Python dependencies

```bash
python -m pip install -r requirements.txt
```

## ℹ️ Tor controller

To trigger a new Tor circuit, we are using the Tor controller with environment variables:

- **`TOR_CONTROLLER_PORT`**: Represents the Tor controller port
- **`TOR_CONTROLLER_PASSWORD`** Represents the Tor controller password as plaintext

## 📜 Usage example

```bash
CONTROLLER_PORT="9051" \
CONTROLLER_PASSWORD="password" \
python tinyjal.py "<url>/archives/art/Animal/birds/" "./random_birds"
```

#### Output example

```bash
[+] Tor new circuit
[Cache]    ./random_birds/archives/art/Animal/birds/birds_photo_01.jpg
[Cache]    ./random_birds/archives/art/Animal/birds/birds_photo_02.jpg
[Cache]    ./random_birds/archives/art/Animal/birds/birds_photo_03.jpg
[Cache]    ./random_birds/archives/art/Animal/birds/birds_photo_04.jpg
[Cache]    ./random_birds/archives/art/Animal/birds/birds_photo_05.jpg
[Cache]    ./random_birds/archives/art/Animal/birds/birds_photo_06.jpg
[Cache]    ./random_birds/archives/art/Animal/birds/birds_photo_07.jpg
[Cache]    ./random_birds/archives/art/Animal/birds/birds_photo_08.jpg
[Cache]    ./random_birds/archives/art/Animal/birds/birds_photo_09.jpg
[Cache]    ./random_birds/archives/art/Animal/birds/birds_photo_10.jpg
[Cache]    ./random_birds/archives/art/Animal/birds/birds_photo_11.jpg
[Cache]    ./random_birds/archives/art/Animal/birds/birds_photo_12.jpg
[Cache]    ./random_birds/archives/art/Animal/birds/birds_photo_13.jpg
[Cache]    ./random_birds/archives/art/Animal/birds/birds_photo_14.jpg
[+]    archives/art/Animal/birds/    birds_photo_15.jpg    65.4 KiB
[+]    archives/art/Animal/birds/    birds_photo_16.jpg    82.0 KiB
[+]    archives/art/Animal/birds/    birds_photo_17.jpg    253.0 KiB
[+]    archives/art/Animal/birds/    birds_photo_18.jpg    60.9 KiB
[+]    archives/art/Animal/birds/    birds_photo_19.jpg    79.4 KiB
[+]    archives/art/Animal/birds/    birds_photo_20.jpg    113.1 KiB
[+]    archives/art/Animal/birds/    birds_photo_21.jpg    84.1 KiB
[+]    archives/art/Animal/birds/    birds_photo_22.jpg    102.6 KiB
[+]    archives/art/Animal/birds/    birds_photo_23.jpg    80.1 KiB
[+]    archives/art/Animal/birds/    birds_photo_24.jpg    142.5 KiB
[+]    archives/art/Animal/birds/    birds_photo_25.jpg    150.8 KiB
[+]    archives/art/Animal/birds/    birds_photo_26.jpg    40.2 KiB
[+]    archives/art/Animal/birds/    birds_photo_27.jpg    66.3 KiB
[+]    archives/art/Animal/birds/    birds_photo_28.jpg    99.0 KiB
[+]    archives/art/Animal/birds/    birds_photo_29.jpg    131.8 KiB
[+]    archives/art/Animal/birds/    birds_photo_30.jpg    97.6 KiB
[+]    archives/art/Animal/birds/    birds_photo_31.jpg    229.0 KiB
[+]    archives/art/Animal/birds/    birds_photo_32.jpg    71.7 KiB
[+]    archives/art/Animal/birds/    birds_photo_33.jpg    43.9 KiB
[+]    archives/art/Animal/birds/    birds_photo_34.jpg    62.5 KiB
[+]    archives/art/Animal/birds/    birds_photo_35.jpg    49.9 KiB
```
  