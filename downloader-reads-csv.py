import csv
import os
import yt_dlp  

#Commenting on the code below for future reference

#   create_csv_if_not_exists()
#check 'if' the file named 'videos.csv' exists, if not, create it
#either way, proceed, open the CSV file
#'w' = write mode
#newline='' prevents blank lines between rows
#'with' statement ensures the file is properly closed after we're complete
#'writer' creates the CSV writer object (allows us to write data in CSV format)
#'writer.writerow' writes the header row to define our columns

def create_csv_if_not_exists():
    if not os.path.exists('videos.csv'):
        with open('videos.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['url', 'title', 'status'])

#   download_videos()
#open and read the CSV file
#'r' = read mode
#again, newline='' handles line endings (no blank lines)
#'reader' create a dictionary reader that reads the CSV and creates dictionaries where the keys are the column headers
#... so each row becomes {'url': 'http://...', 'title': 'My Video', 'status': 'pending'}
#'rows' converts it to a list so that we can modify it later

def download_videos():
    """Download videos from CSV and update their status"""
    with open('videos.csv', 'r', newline='') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
    
    #checks 'if' downloads folder exists, if not, create one

    if not os.path.exists('downloads'):
        os.makedirs('downloads')
    
    # Configure yt-dlp options
    ydl_opts = {
        'format': 'best',  # Get best quality
        'outtmpl': 'downloads/%(title)s.%(ext)s',  # Output template
        'quiet': False,  # Show progress
        'no_warnings': False,
        'ignoreerrors': True  # Continue on error
    }
    
    for row in rows:
        if row['status'] != 'completed':
            try:
                print(f"\nAttempting to download: {row['title']}")
                
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([row['url']])
                
                row['status'] = 'completed'
                print(f"Successfully downloaded: {row['title']}")
                
            except Exception as e:
                row['status'] = 'failed'
                print(f"Error downloading {row['title']}: {str(e)}")
    
    # Write updated statuses back to CSV
    with open('videos.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['url', 'title', 'status'])
        writer.writeheader()
        writer.writerows(rows)

def main():
    """Main function to run the program"""
    print("YouTube Shorts Downloader Starting...")
    create_csv_if_not_exists()
    download_videos()
    print("\nDownload process completed!")

if __name__ == "__main__":
    main()