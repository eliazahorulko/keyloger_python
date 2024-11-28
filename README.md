Disclaimer

Important Notice:

This project is intended solely for educational purposes and is designed to demonstrate the functionality of a keylogger program in a controlled, ethical, and legal environment. By using or reviewing this code, you agree to the following conditions:

Ethical Use Only: The keylogger code must not be used for any malicious purposes or deployed on any device without the explicit consent of the owner. Unauthorized access to computer systems, networks, or data is illegal and unethical. Using this code without permission can result in legal consequences.

Educational Intent: This project was developed to provide insight into how keyloggers work and to help security professionals understand how malicious actors may exploit such software to compromise user data. It is intended as a learning tool to support the development of defensive cybersecurity strategies, particularly for ethical hacking and penetration testing in authorized environments.

Controlled Environment: This code should only be run in a safe, controlled environment (such as a personal lab or sandbox) where you have explicit permission to do so. Any unauthorized use of this code could lead to significant legal and ethical issues.

No Unauthorized Deployment: Do not deploy or use this keylogger on any system without proper authorization. The creator of this project takes no responsibility for any unlawful, unauthorized, or unethical use of this code.

Respect Privacy: Always respect privacy and follow ethical guidelines in cybersecurity. Any activity that involves unauthorized surveillance or data collection is a violation of privacy rights.

Liability: The creator of this project does not take responsibility for any damage, loss of data, or any other consequences that may arise from the use of this code.
By proceeding with the use or study of this project, you acknowledge and agree to the terms set forth in this disclaimer.


-------------------------------
Keylogger with Telegram Integration

Overview
This project implements a keylogger that captures keystrokes and provides periodic reports. Reports can be:
- Sent to a Telegram chat via a bot.
- Saved as text files on the local system.

Users can control the keylogger through a Telegram bot with an interactive inline keyboard.


Features
- **Keystroke Logging**: Captures all keypresses, including special keys (e.g., Enter, Space).
- **Reporting Options**:
  - Send logs to Telegram.
  - Save logs to local files.
- Interactive Telegram Bot: Allows users to select the reporting method through an inline keyboard.
- Periodic Reports: Generates reports every 5 seconds (configurable).
- Timestamped Logs: Saves logs with unique filenames based on timestamps.

---
Requirements
- Python 3.7 or higher
- Libraries:
  - `keyboard` (for capturing keystrokes)
  - `pyTelegramBotAPI` (for Telegram bot functionality)

---

Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/keylogger-telegram.git
   cd keylogger-telegram
