# YouTube-Mass-Uploader
Quickly upload all files in a folder to YouTube

### THE MAX NUMBER OF VIDEOS YOU CAN UPLOAD USING THIS PER DAY IS 6. This is because of the YouTube Data API Quota.

Take a look at this:
https://developers.google.com/youtube/v3/guides/uploading_a_video

`uploader.py` is a copy of the script shown there, but converted to python 3.

## How to Use
1. Download the files
2. Find your client secrets file by going to [Google Cloud Console](https://console.cloud.google.com) and creating an OAuth 2.0 Client ID. Once this has been created, enable the [YouTube Data API v3](https://console.cloud.google.com/apis/library/youtube.googleapis.com?project=learned-house-346312). Go back to credentials and download the client ID using the download button next to Actions. Rename the file as `client_secrets.json` and put it in the same folder as the downloaded files.
3. Edit `loopthroughvideos.py`. Enter the directory containing the video files and set the file extensions of the files you want to upload.
4. Run by going into the directory containing the downloaded files and entering the command `python loopthroughvideos.py`.

## Additional Settings
As seen in the Google Developers link, you can modify the `os.system` statement with the following parameters:
```
--title="Enter title here"

--description="Add a description"

--keywords="Put keywords here"

--category="Add category here"

--privacyStatus="Set privacy"
```
The privacy options are public, private, and unlisted.

For more information: [Setting Script Parameters](https://developers.google.com/youtube/v3/guides/uploading_a_video#Calling)