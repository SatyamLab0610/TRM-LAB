# Install Playwright
!pip install playwright==1.42.0

# Install Chromium for Playwright
!playwright install chromium

# Install required system dependencies
!apt-get update -y
!apt-get install -y \
  libnss3 \
  libatk1.0-0 \
  libatk-bridge2.0-0 \
  libcups2 \
  libxkbcommon0 \
  libxcomposite1 \
  libxrandr2 \
  libgbm1 \
  libasound2 \
  libpangocairo-1.0-0 \
  libxdamage1 \
  libxfixes3 \
  fonts-liberation
