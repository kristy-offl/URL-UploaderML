class Translation(object):

    START_TEXT = """Hello,

This is a Telegram URL Upload Bot!

<b>Please send me any Direct download URL link, I can upload to telegram as File/Video</b>

/help for more details..

Support Group : @ML_SupportGroup
"""

    HELP_USER = """Hai I'am a URL Uploader bot..
    
⛑️ How To Use Me & More 😉
Uploading Files To Telegram
⇰ Send Me Any Direct Link & Use "|" To Separate Link From New Name For Example https://example.com | newname.extension.

Set Thumbnail
⇰ Send A Photo To Make It As Permanent Thumbnail.

Deleting Thumbnail
⇰ Send /deletethumb To Delete Thumbnail.

Generate Thumbnail
⇰ Send Two Photos In A Media Album.
⇰ Reply To That Photos With /generatecustomthumbnail

Support Group : @ML_SupportGroup
"""

    FORMAT_SELECTION = """Select the desired format: <a href='{}'>file size might be approximate</a>
    
Send your custum thumbnail if required.
You can use /deletethumbnail to delete the auto-generated thumbnail."""
    
    SET_CUSTOM_USERNAME_PASSWORD = """If you want to download premium videos, provide in the following format:
URL | newfilename | username | password"""


    UPGRADE_TEXT = "<b>👉 Create own Clone Bot.. </b>  \n\n<a href='https://github.com/kristy-offl/URL-UploaderML'>Click here, Fork and deploy!!</a>"
    
    DOWNLOAD_START = "Trying to download your file..."
    
    UPLOAD_START = "Uploading now.."
    
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds. \n\nUploaded in {} seconds."

    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.95GB due to Telegram API limitations."

    SAVED_CUSTOM_THUMB_NAIL = "Custom thumbnail saved. This will be permanent.\n\nUse /deletethumbnail to clear it."

    DEL_ETED_CUSTOM_THUMB_NAIL = "Custom thumbnail cleared succesfully."

    CUSTOM_CAPTION_UL_FILE = " "

    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."

    NO_VOID_FORMAT_FOUND = "ERROR...\n<b>YouTubeDL</b> said: {}"
    
    SHOW_THUMB = "Use /deletethumbnail to clear this thumbnail."
    
    NO_THUMB = "No saved thumbnails Found!!\n\nSend an image to save it as your thumbnail permanently."    
