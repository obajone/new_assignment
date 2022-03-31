from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

folder = '1jssIFkeWWQmToMZkTvmRkUbrw07ErDBd'

directory = 'C:/Users/HP/Desktop/APPLICATIONS/ASABA'
for file in os.listdir(directory):
    file_name = os.path.join(directory, file)
    gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : file})
    gfile.SetContentFile(file_name)
    gfile.Upload()
    # print(file_path)