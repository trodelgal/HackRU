import os.path

from src.db_inserter import insert_data
from src.video_analyzer import analyze_video


if __name__ == '__main__':
    video_absolute_path: str = os.path.abspath("resource/video.mp4")
    analyze_video(video_absolute_path)
    insert_data()