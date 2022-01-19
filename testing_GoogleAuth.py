# Google OAuth 2.0 and OAuth consent screen

# authetication to google api services
# create oauth client secret file

# https://console.cloud.google.com/

# pip install pydrive2

import mimetypes
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
import pandas as pd


gauth = GoogleAuth()
gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.
drive = GoogleDrive(gauth)

File_ID = '1889-jt2vo4C71-tE2MGhQezCGguGWqmdRt6mMrClXlk' # Drive Excel File ID
Folder_ID = '16p2Fcoe7JSQlX8S5YM4sSR7nR-HM15Yw' # Drive Folder ID for Excel File
File_Name = 'Test Copy of BudgetForLife' # Using existing drive file name, could use a new one if I would like
File_List = drive.ListFile({'q': "'16p2Fcoe7JSQlX8S5YM4sSR7nR-HM15Yw' in parents"}).GetList() #Get list of files in a given folder
for Item in File_List:
    print(Item['title']) #Title of item in the folder
    #This should tell you which mimetype the file you're trying to download
    print('title: %s, mimeType: %s' % (Item['title'], Item['mimeType']))
    mimetypes = { 
        # Drive Sheets files as MS Excel files.
        'application/vnd.google-apps.spreadsheet': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'}
    # See https://developers.google.com/drive/v3/web/mime-types
    File = drive.CreateFile({'id': File_ID}) # Initialize GoogleDrive instance w/ File ID
    print(File['title'])
    print(File['mimeType'])
    
    download_mimetype = None
    
    if File['mimeType'] in mimetypes:
            download_mimetype = mimetypes[File['mimeType']]
            print('Downloading file %s from Google Drive' % File['title'])
            File.GetContentFile(File_Name, mimetype=download_mimetype) #Download file as File Title and mimetype
            #Item.GetContentFile(r'C:\Users\charl\Desktop\\' + Item['title'], mimetype=download_mimetype)
    else: 
        print('Could not download file %s from Google Drive' % File['title'])
        #Item.GetContentFile(r'C:\Users\charl\Desktop\googledrive\\' + Item['title'], mimetype=download_mimetype)

#downloaded = drive.CreateFile({'id': File_ID})
#downloaded.GetContentFile(File_Name)


#df = pd.read_excel(File_Name, sheet_name=2, header=4, usecols=None) #Reading the dictionary keys & values of my File_Name, specifying the sheet I want to read & the header/row I want to start reading from

#print(df)

