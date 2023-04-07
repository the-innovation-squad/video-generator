import os
import yaml
from video import create_segment, concatenate_segments
from narration import create_narration

def generate():
    # Read the YAML file
    with open("input/video_script.yml", "r") as file:
        video_script = yaml.safe_load(file)

    # Iterate through the timeline of content items and stock video clips to create video segments
    for index, item in enumerate(video_script["timeline"]):
        content = item["content"]
        options = item["options"]
        clip = item["clip"]

        output_dir = "output/" + str(index)
        os.mkdir(output_dir)

        audio_path = create_narration(content, options, output_dir)
        create_segment(audio_path, clip, output_dir)

    # Stitch the video segments together
    segment_paths = [os.path.join("output", str(index), "video_processed.mp4") for index, item in enumerate(video_script["timeline"])]
    concatenate_segments(segment_paths, "output/final.mp4")

    # TODO: add watermark at the end if one is provided

