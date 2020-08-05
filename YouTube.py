from pytube import YouTube
from tkinter.filedialog import *
from tkinter.messagebox import *
from threading import *
import PIL.Image

vSize=0

#pasting url
def paste():
	cliptext = main.clipboard_get()
	url_field.insert(0,cliptext)


#threading
def kashifThread():
	kThread=Thread(target=YD)
	kThread.start()
	
#download progress
def progresss(chunk, file_handle, bytes_remaining):
	vDownloaded=(vSize-bytes_remaining)
	print("r: ",bytes_remaining)
	print("v: ",vDownloaded)
	#file size
	aSize=(vSize/(1024*1024))
	print(aSize)
	fSize.config(text="Video Size: {:.2f} MB".format(aSize))
	fSize.pack(side=TOP, pady=5)
	
	sizeD=(vDownloaded/(1024*1024))
	fDSize.config(text="Downloading: {:.2f} MB".format(sizeD))
	fDSize.pack(side=TOP,pady=5)
	
	per=(vDownloaded/vSize)*100
	dBtn.config(text="{:00.2f} % Downloaded".format(per))
	



def YD():
	global vSize
	try:
		url=url_field.get()
		print(url)
		
		#changing button text
		dBtn.config(text="Please Wait...")
		dBtn.config(state=DISABLED)
		cURL.pack_forget()
		save=askdirectory()
		print(save)
		if save is None:
			return
		kash=YouTube(url, on_progress_callback=progresss)
		
		video=kash.streams.first()
		vTitle.config(text=video.title)
		vTitle.pack(side=TOP, pady=10)
		vSize=video.filesize
		
		
		
	#	vs=(video.filesize)/(1024*1024)
#		print("File Size:  {:.2f}".format((video.filesize)/(1024*1024)),"MB")
#		
#		fSize.config(text="{:00.2f} % MB".format(vs))
#	
		
	
#	fSize.pack(side=TOP, pady=5)
		
		#to save video
		video.download(save)
		print("Downloaded")
		dBtn.config(text="Start Download")
		dBtn.config(state=NORMAL)
		showinfo("Video Downloader by Kashif","Downloaded")
		url_field.delete(0,END)
		vTitle.pack_forget()
		fSize.pack_forget()
		fDSize.pack_forget()
		
		
	except Exception as e:
		print(e)
		print("Error")
		cURL.pack(side=TOP, pady=5)
		dBtn.config(text="Start Download")
		dBtn.config(state=NORMAL)
		
		
		
		
#Creating GUI
main=Tk()

#title
main.title("YouTube Downloader by Kashif")

#icon
#main.iconbitmap('icon.ico)

#mainicon
file=PhotoImage(file='yi.png') 
mainicon=Label(main,image=file)
mainicon.pack(side=TOP, pady=50)

#text to say put url
url_info=Label(main,text='Enter URL from YouTube', font='normal 10 bold underline',justify=CENTER)
url_info.pack(side=TOP,pady=0.01)


#Url field
url_field=Entry(main,font=("Square Sans Serif",18), justify=CENTER)
url_field.pack(side=TOP,fill=X, padx=80)

#button to paste

pBtn=Button(main,text="Paste", font='calibri 5 bold',bg='violet',fg='blue',bd=20,relief=GROOVE, command=paste, justify=CENTER)
pBtn.place(x=120,y=150)
pBtn.pack(pady=13)


#button to download

dBtn=Button(main,text="Start Download", font='calibri 15 bold',bd=20,relief=RAISED, command=kashifThread, justify=CENTER)
dBtn.pack(side=TOP, pady=20)



#creating File Size
fSize=Label(main,text="")
fDSize=Label(main,text="")

#creating Title
vTitle=Label(main,text='')



#creating footer
subscribe=Label(main,text="FEATURED: youmehackers.com and pubglites.com")
subscribe.pack(side=BOTTOM,pady=20)

footer=Label(main,text="This App is created by Kashif")
footer.pack(side=BOTTOM,pady=10)

#currect URL information cURL
cURL=Label(main,text="Plz Enter correct URL", font='calibri 15 bold', fg='red')

#picturebabu
file=PhotoImage(file='pic.png') 
file=file.subsample(3)
babu=Label(main,image=file)
babu.pack(side=BOTTOM, pady=50)

main.geometry("600x700")
main.mainloop()