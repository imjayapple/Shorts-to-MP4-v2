# YouTube Shorts to MP4 - Downloader

This program utilizes the `yt-dlp` library to download YouTube Shorts and save them as `.mp4` files with user-specified titles. The program features a simple user interface (UI) that accepts YouTube Shorts links and titles, storing them in a `.CSV` file for batch processing.

## Features

- Accepts YouTube Shorts URLs and desired titles via a user-friendly UI.
- Stores the URLs and titles in a `.CSV` file.
- Automatically downloads the videos and saves them with the specified titles.

## Requirements

- Python 3.x
- `yt-dlp` library

You can install `yt-dlp` using pip:

```bash
pip install yt-dlp
```
## Usage

1. Run the program to open the UI.
2. Enter the YouTube Shorts URL and the desired title in the provided fields.
3. Submit the details to add them to the .CSV file.
4. Run the program again to process the .CSV file and download all listed URLs with the specified titles.

## Example

1. Open the program:
    ```bash
    python your_program.py
    ```
2. Enter the YouTube Shorts URL and the desired title in the UI.

3. Submit the details. They will be added to videos.csv.

4. Run the program to start downloading:
    ```bash
    python your_program.py
    ```

The program will read the videos.csv file and download each YouTube Short, saving them with the specified titles.

## License

This project is licensed under the MIT License.

## Acknowledgments

- yt-dlp - The library used for downloading YouTube Shorts.