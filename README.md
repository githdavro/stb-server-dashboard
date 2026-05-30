<div align="center">

# STB Server Dashboard

Modern web dashboard for monitoring CPU, RAM, storage, temperature, and uptime on low-cost Armbian STB servers.

<img src="./preview.png" alt="Preview" width="100%">

</div>

---

## Overview

STB Server Dashboard is a lightweight monitoring interface built for Armbian-powered set-top-box servers.

The dashboard provides realtime hardware statistics through a simple Python API and a modern single-page web interface.

---

## Features

* Realtime CPU monitoring
* RAM usage statistics
* Storage monitoring
* Temperature tracking
* System uptime information
* Responsive layout
* Material Design-inspired interface
* Lightweight deployment

---

## Stack

| Component | Technology          |
| --------- | ------------------- |
| Frontend  | HTML + Tailwind CSS |
| Backend   | Python              |
| Platform  | Armbian Linux       |

---

## Files

```text
.
├── app.py
└── index.html
```

---

## Run

```bash
python app.py
```

Then open:

```text
http://localhost:5000
```

---

## Purpose

Built for monitoring low-cost Armbian STB servers without requiring constant SSH access.

A simple dashboard for checking system health directly from a browser.

```
```
