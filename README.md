# Business Card Scanner → WhatsApp (OCR)

A Streamlit web app that extracts text from **front and back images of business cards** using **EasyOCR** (English + Hindi) and lets you share the extracted text directly on **WhatsApp**.

---

## Features

- Upload **Front** and **Back** business card images (JPG/PNG)
- OCR text extraction using **EasyOCR**
- Displays extracted text in the app
- Generates a **WhatsApp share link** with the extracted text

---

## Tech Stack

- **Python**
- **Streamlit** (UI)
- **EasyOCR** (OCR)
- **Pillow** (image handling)
- **NumPy** (array conversion)

---

## Project Structure

- `main.py` — Streamlit application
- `requirements.txt` — Python dependencies

---

## Requirements

1. Install Python 3.9+ (recommended)
2. Ensure you can run Streamlit apps locally

---

## Setup & Installation

### 1) Create a virtual environment (recommended)

```bash
python -m venv venv
```

Activate it:

- **Windows (cmd):**
```bash
venv\Scripts\activate
```

### 2) Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run the App

```bash
streamlit run main.py
```

Open the shown local URL in your browser.

---

## How to Use

1. Upload your **Front** business card image.
2. Optionally upload the **Back** business card image.
3. The app will extract text from the uploaded images.
4. Click **“Share on WhatsApp”** to open WhatsApp with the extracted text prefilled.

---

## Notes / Limitations

- OCR quality depends on image clarity, lighting, and resolution.
- The OCR engine is initialized with languages: **`en` and `hi`**.
- Current implementation runs with `gpu=False`.

---

## License

Add your license information here (e.g., MIT).
