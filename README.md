
# Pakistan SIM Network Checker 🇵🇰

A Python web application that identifies the likely Pakistani
mobile network associated with a phone number prefix.

## Features

- Detects likely Jazz, Zong, Ufone, and Telenor prefixes.
- Supports Pakistani mobile number formats.
- Validates user input.
- Streamlit user interface.
- Optional Gemini AI explanation.
- Simple and beginner-friendly project.

## Technologies

- Python
- Streamlit
- Google Gemini API
- GitHub

## Project Structure

```text
pakistan-sim-network-checker/
├── app.py
├── requirements.txt
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/pakistan-sim-network-checker.git
```

Navigate into the project:

```bash
cd pakistan-sim-network-checker
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## Gemini API Setup

1. Get an API key from Google AI Studio.
2. Configure GEMINI_API_KEY in Streamlit Secrets.
3. Enable the optional AI explanation in the app.

## Important Disclaimer

This application identifies the likely original network
using mobile number prefixes.

Mobile Number Portability (MNP) allows users to change
networks while keeping their phone numbers.

Therefore, the detected network may not be the user's
current SIM provider.

## Author

Your Name
