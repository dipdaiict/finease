# Print message indicating the start of setting up the initial environment
echo "[$(date)]: Setting up the initial environment for your project..."

# Create virtual environment
echo "[$(date)]: Creating virtual environment..."
python -m venv .venv

# Activate virtual environment
echo "[$(date)]: Activating virtual environment..."
source .venv/Scripts/activate

# Install dependencies
echo "[$(date)]: Installing dependencies..."
pip install --upgrade pip
pip install -r requirements_dev.txt

# Additional setup steps can go here

# Print message indicating successful setup completion
echo "[$(date)]: Setup completed successfully."
