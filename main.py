from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

folder = '1jssIFkeWWQmToMZkTvmRkUbrw07ErDBd'

file1 = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : 'hello.txt'})
file1.SetContentString('Hello world!')
file1.Upload()