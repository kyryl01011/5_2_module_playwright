# Automated UI Tests for Sauce Demo

## 📝 Project Description

This repository contains a suite of automated UI tests developed to verify the core end-to-end (E2E) user scenario on the **Sauce Demo** e-commerce emulator ([https://www.saucedemo.com/](https://www.saucedemo.com/)).

The tests are written in **Python** using the **Pytest** testing framework and **Playwright** for browser automation.

The primary goal of this project is to cover a smoke E2E scenario, ensuring critical user flows from login to order completion are functional.

## 🚀 Requirements

To successfully run these automated UI tests on your local machine, please ensure you have the following tools installed:

  * **Python 3.9+** (latest stable version is recommended)
  * **Git** (for cloning the repository)
  * **Node.js** and **npm** (required for Playwright Browser Drivers installation; Playwright CLI usually handles this, but Node.js is necessary)

## 🛠️ Installation and Setup

Follow these step-by-step instructions to prepare your environment and install the necessary dependencies.

### 1\. Clone the Repository

Open your terminal or command prompt and execute the following command:

```bash
git clone https://github.com/kyryl01011/your-saucedemo-repo.git # Replace with your actual repo link if different
cd your-saucedemo-repo
```

### 2\. Create and Activate a Virtual Environment

It is highly recommended to use a virtual environment to manage project dependencies and avoid conflicts with other Python projects.

```bash
python3 -m venv venv
```

After creating the virtual environment, activate it:

  * **For macOS / Linux:**
    ```bash
    source venv/bin/activate
    ```
  * **For Windows (PowerShell):**
    ```powershell
    .\venv\Scripts\Activate.ps1
    ```
  * **For Windows (Command Prompt / CMD):**
    ```cmd
    .\venv\Scripts\activate.bat
    ```

### 3\. Install Python Dependencies

Install all required Python libraries listed in the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 4\. Install Playwright Browser Drivers

Playwright needs to download and install browser drivers for Chromium, Firefox, and WebKit.

```bash
playwright install
```

## 🚀 Running Tests

Once the installation and setup are complete, you are ready to run the tests.

### Run All Tests

This command will execute all tests discovered by Pytest.

```bash
python -m pytest
```
