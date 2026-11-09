# sanctuary-companion
A local-first, privacy-focused terminal companion combining trauma-informed AI support (via local Ollama) with box breathing pacers, grounding routines, and dream recall tracking.
# Sanctuary & Support Companion

A local-first, privacy-focused terminal application combining **trauma-informed AI support** (powered by local Ollama models) with **grounding routines, box breathing pacers, and dream recall tracking**.

## Key Features
* **Local Trauma-Informed AI Chat:** Connects privately to a local Ollama instance (`http://localhost:11434`) with zero chat history saved to disk.
* **Verified Support Directories:** Built-in offline access to U.S. national, state, and international crisis, housing, and medical financial aid resources.
* **Evening Anchor & Box Breathing Pacer:** Guided 4-cycle box breathing countdown paired with a calming terminal visual landscape and customizable focus intentions.
* **Morning Dream Recall Tracker:** Offline logger for tracking dream narratives and detachment/observer metrics.
* **Text Sanitizer:** Local utility to strip formatting noise and hash intrusive text inputs.

## Prerequisites
* **Python 3.8+** (Uses standard Python library modules only—no external `pip` packages required).
* **Ollama** *(Optional, required only for Option 1 AI chat)*: [Install Ollama](https://ollama.com) and run `ollama serve` in the background.

## Quick Start
1. Clone or download this repository:
   ```bash
   git clone https://github.com
   cd sanctuary-companion
   ```
2. Run the application:
   ```bash
   python3 sanctuary_companion.py
   ```

## Customizing the Local AI Model
By default, Option 1 looks for an Ollama model named `support-assistant`. You can build your own custom model in Ollama using a `Modelfile`, or edit `MODEL_NAME` at the top of `sanctuary_companion.py` to use any installed model (such as `llama3.2` or `mistral`).

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Disclaimer
This software is a personal grounding and informational utility. It is not a medical device, clinical therapy replacement, or emergency response service. If you are in crisis, call or text **988** (U.S. & Canada) or visit [findahelpline.com](https://findahelpline.com).
