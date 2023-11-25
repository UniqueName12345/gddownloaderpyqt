import sys
import os
import requests
import argparse

class GeometryDashDownloader:
    def __init__(self, id_value, name, save_path):
        self.id_value = id_value
        self.name = name
        self.save_path = save_path

    def download_audio(self):
        if self.id_value < 469775:
            raise ValueError("No support for IDs less than 469775. The known name pattern can't be used.")

        if not os.path.exists(self.save_path):
            raise FileNotFoundError(f"The specified save path '{self.save_path}' does not exist.")

        path = os.path.join(self.save_path, f"{self.id_value}.mp3")

        if os.path.exists(path):
            reply = input(f"There's already an audio named '{self.id_value}.mp3'. Overwrite? (yes/no): ")
            if reply.lower() != "yes":
                return

        try:
            response = self.download_file(
                f"http://audio.ngfiles.com/{self.id_value - self.id_value % 1000}/{self.id_value}_{self.name}.mp3",
                path
            )
            if response.status_code == 200:
                print("Audio downloaded successfully.")
            else:
                print("Error downloading audio.")
            response.raise_for_status()
        except Exception as e:
            print(f"Error: {e}")
            if os.path.exists(path):
                os.remove(path)


def parse_arguments():
    parser = argparse.ArgumentParser(description="Geometry Dash Downloader CLI")
    parser.add_argument("id", type=int, help="ID of the audio")
    parser.add_argument("name", type=str, help="Name of the audio")
    parser.add_argument("--save-path", type=str, help="Save path for the downloaded audio")

    return parser.parse_args()


def main():
    args = parse_arguments()
    id_value = args.id
    name = args.name
    save_path = args.save_path

    if not save_path:
        save_path = input("Enter save path (leave blank for default): ") or "C:/"

    downloader = GeometryDashDownloader(id_value, name, save_path)
    downloader.download_audio()


if __name__ == "__main__":
    main()
