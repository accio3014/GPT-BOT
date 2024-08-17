<br>

- [GPT-BOT](#gpt-bot)
  - [Overview](#overview)
    - [Demo Video](#demo-video)
  - [Installation](#installation)
    - [Requirements](#requirements)
  - [Usage](#usage)
- [Author](#author)
  - [accio](#accio)

<br>

# GPT-BOT
"GPT-BOT" is a project that replicates the functionality of a real-time conversational chatbot, one of the features of the Chat GPT mobile app, into a Python program. This project allows you to use a real-time conversational chatbot in the terminal, just like in the mobile app.<br>
<br>
<br>

## Overview
This project has been confirmed to be issue-free as of August 18, 2024. If any issues occur during execution, please refer to the official <a href="https://platform.openai.com/docs/overview" target="_blank">API documentation</a>
<br>
<br>

### Demo Video

<br>
<br>

## Installation
### Requirements
| Python   | Version 3.12.1 or higher  |
|----------|---------------------------|
| Chat GPT | Plus subscription account |

<br>

**#1 Clone the Repository**:
```bash
git clone https://github.com/accio3014/GPT-BOT.git ~/GPT-BOT
```
```bash
cd ~/GPT-BOT
```
<br>

**#2 Set Up a Virtual Environment**:
```bash
python3 -m venv GPT-BOT
```
```bash
source GPT-BOT/bin/activate
```
<br>

**#3 Install the Dependencies**:
```bash
pip3 install -r requirements.txt
```
<br>

**#4 Modify api key, model, voice**:

Modify the information inside the GPT_BOT.py file. There is a reference link for each line.
| Line number | Content    |
|-------------|------------|
| 7           | API key    |
| 42          | Model type |
| 57          | Voice type |

<br>
<br>

## Usage
**#1 Add Permission**:
```bash
chmod +x ~/GPT-BOT/GPT_BOT.py
```
<br>

**#2 Create an Alias**:

Bash shell:
```bash
echo "alias GPT-BOT='python3 ~/GPT-BOT/GPT_BOT.py'" >> ~/.bashrc
```
Zsh shell:
```bash
echo "alias GPT-BOT='python3 ~/GPT-BOT/GPT_BOT.py'" >> ~/.zshrc
```
<br>

**#3 Apply**:

Bash shell:
```bash
source ~/.bashrc
```
Zsh shell:
```bash
source ~/.zshrc
```
<br>

**#4 Run GPT-BOT**:
```bash
GPT-BOT
```
<br>
<br>

# Author
## <a href="https://github.com/accio3014" target="_blank">accio</a>