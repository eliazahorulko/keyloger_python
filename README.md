Keylogger with Telegram Integration

Overvieц
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
