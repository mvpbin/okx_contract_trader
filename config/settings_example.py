# config/settings_example.py

# --- API Credentials (Fill these in your actual settings.py) ---
API_KEY = "YOUR_PAPER_TRADING_API_KEY_placeholder"
API_SECRET_KEY = "YOUR_PAPER_TRADING_SECRET_KEY_placeholder"
API_PASSPHRASE = "YOUR_PAPER_TRADING_PASSPHRASE_placeholder"

# --- Trading Mode ---
IS_PAPER_TRADING = True  # True for paper trading, False for live trading

# --- For REST API (flag is used by the SDK) ---
# flag = '1' for Demo Trading, '0' for Live Trading
OKX_API_FLAG = '1' if IS_PAPER_TRADING else '0'
OKX_REST_BASE_URL = "https://www.okx.com"  # Usually the same for live and paper

# --- For WebSocket API (URLs are different) ---
# IMPORTANT: Always verify these URLs with the LATEST OFFICIAL OKX API documentation
OKX_WS_BASE_URL_PAPER_PUBLIC = "wss://wspap.okx.com:8443/ws/v5/public?brokerId=9999"
OKX_WS_BASE_URL_PAPER_PRIVATE = "wss://wspap.okx.com:8443/ws/v5/private?brokerId=9999"
OKX_WS_BASE_URL_LIVE_PUBLIC = "wss://ws.okx.com:8443/ws/v5/public"
OKX_WS_BASE_URL_LIVE_PRIVATE = "wss://ws.okx.com:8443/ws/v5/private"

# --- Selected WebSocket URLs based on IS_PAPER_TRADING ---
OKX_WS_PUBLIC_URL = OKX_WS_BASE_URL_PAPER_PUBLIC if IS_PAPER_TRADING else OKX_WS_BASE_URL_LIVE_PUBLIC
OKX_WS_PRIVATE_URL = OKX_WS_BASE_URL_PAPER_PRIVATE if IS_PAPER_TRADING else OKX_WS_BASE_URL_LIVE_PRIVATE

# --- SDK Debug Mode ---
SDK_DEBUG_MODE = False  # Set to True for more verbose SDK output (e.g., print request/response)

# --- Other Potential Settings ---
# DEFAULT_SYMBOLS = ["BTC-USDT-SWAP", "ETH-USDT-SWAP"]
# LOG_LEVEL = "INFO"
