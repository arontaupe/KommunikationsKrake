# Load pandas
import pandas as pd


def make_video_array(titles):
    """
builds a video dict with titles and urls based on the .csv. preserves the order of elements.
    :param titles: array of strings with the video titles
    :return: dict: {'title':'url'}
    """
    # opening the CSV file
    videos = {}

    # Read CSV file into DataFrame df
    df = pd.read_csv('dgs_videos.csv')
    for title in titles:
        videos[title] = df[df["title"] == title].url.values[0]
    return videos
