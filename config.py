from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN: str = os.environ["BOT_TOKEN"]
USER_TOKEN: str = os.environ["USER_TOKEN"]
GROUP_ID: int = int(os.environ["GROUP_ID"])

_conv_ids = os.getenv("CONVERSATION_IDS", "")
CONVERSATION_IDS: list[int] = [int(x) for x in _conv_ids.split(",") if x.strip()]

CLIP_NAME: str = os.getenv("CLIP_NAME", "")
CLIP_DESCRIPTION: str = os.getenv("CLIP_DESCRIPTION", "")
CLIPS_DIR: str = os.getenv("CLIPS_DIR", "clips")

START_HOUR: int = int(os.getenv("START_HOUR", "21"))
START_MINUTE: int = int(os.getenv("START_MINUTE", "0"))
START: str = f"{START_HOUR}:{START_MINUTE}"
END_HOUR: int = int(os.getenv("END_HOUR", "23"))
END_MINUTE: int = int(os.getenv("END_MINUTE", "59"))
END: str = f"{END_HOUR}:{END_MINUTE}"
POSTING_INTERVAL: int = int(os.getenv("POSTING_INTERVAL", "1"))
CLEANUP_INTERVAL_HOURS: int = int(os.getenv("CLEANUP_INTERVAL_HOURS", "24"))

LAST_TIME_POST: datetime = datetime.strptime(
    os.getenv("LAST_TIME_POST", "2025-06-16 21:25:30"), "%Y-%m-%d %H:%M:%S"
)

LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
LOG_FORMAT: str = os.getenv("LOG_FORMAT", "%(asctime)s - %(name)s - %(levelname)s - %(message)s")

USE_YTDLP: bool = os.getenv("USE_YTDLP", "true").lower() == "true"
YTDLP_PATH: str = os.getenv("YTDLP_PATH", "yt-dlp")
