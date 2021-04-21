from pytube.cli import on_progress
from pytube import YouTube
from time import sleep
print("----------------------- Welecom To YouTuBe Downloader v1.0 : creat by OZX-OG -----------------------\n")

while True:
    
    
    tbUrl = input("Enter URL: ")
    if tbUrl == "" :
        print("\nPlease Enter YouTuBe Link...")
        sleep(1)
        continue
    
    elif tbUrl[:32] == "https://www.youtube.com/watch?" or tbUrl[:19] == "https://youtu.be/" :
        print("\nPlease Enter Correct URL...")
        sleep(1)
        continue
    
    print("\nWait a second...")
    YTvideo = YouTube(tbUrl, on_progress_callback = on_progress)
    

        
    print("\nYou Can Select You form, You can also change location Download(Press: c) ")
    ask_ex = input("(mp3 or mp4 or both, c): ")
        
    def down ():
        while True:
            
            print("****************************** Title ****************************\n")
                
            print(YTvideo.title)
                
            print("\n****************************** Title ****************************")
            print("****************************** thumbnail ************************\n")
                
            print(YTvideo.thumbnail_url)
                
            print("\n****************************** thumbnail ************************\n")
            print("")
            
            i = 1
            for stream in videos:
                print( str(i) + " " + str(stream) )
                i+=1
            
            #fix download number
            try:    
                stream_numb = int(input("\nEnter Numb: "))
                
            except ValueError: #ValueError: hada ila dkhle faragh wela 7orof
                print("Please Enter Numbers If you Can, You can select 1 to " + i)
                sleep(10)
                continue
            
            except IndexError: #IndexError: dekhl ra9em makaynch
                print("Please Don't Enter " + i + "+, ou can select 1 to " + i)
                sleep(10)
                continue
        
            video = videos[stream_numb-1]
            title = str(YTvideo.title)
            
            check_txt = True
            add_sl = ""
            
            
            take_loca = open("Loca.txt","r")
            take_loca_edit = take_loca.readlines()
            
            for x in take_loca_edit:
                loca = x
            
            if loca == "C:\\Download\\":
                check_txt = True
            else:
                check_txt = False
            
            
            if loca == "" :
                loca = "C:\\Download\\"
                
            
            #fix local download
            try:
                take_loca = open("Loca.txt","r")
                
            except FileNotFoundError:
                change_loca = open("Loca.txt","w")
                change_loca.write("C:\\Download\\")
                change_loca.close()
                
            except:
                
                if check_txt == False:
                    add_sl = "\\" + "\\"
                else:
                    add_sl = ""
            
            
            #fix file download title 
            try:
                video.download(loca + add_sl + title.replace("\"", "").replace("\'","") )
            
            
            except OSError:
                print("Downloading...")
                #"C:\Download\"
                video.download(loca + add_sl + title.partition(" ")[0])
                
                thumbnail_url = open(loca + add_sl + title.partition(" ")[0] + "\\" + "( thumbnail )" + title.partition(" ")[0]  + ".txt" ,"w")
                #D:download rico 
                thumbnail_url.write("******** thumbnail ********\n")
                thumbnail_url.write(YTvideo.thumbnail_url)
                thumbnail_url.write("\n******** thumbnail ********")
                thumbnail_url.close()
                break
            
            print("Downloading...")
            #"C:\Download\"
            video.download(loca + add_sl + title.replace("\"", "").replace("\'","") )
            
            thumbnail_url = open(loca + add_sl + title.replace("\"", "").replace("\'","") + "\\" + "( thumbnail )" + title.replace("\"", "").replace("\'","")  + ".txt" ,"w")
            thumbnail_url.write("******** thumbnail ********\n")
            thumbnail_url.write(YTvideo.thumbnail_url)
            thumbnail_url.write("\n******** thumbnail ********")
            thumbnail_url.close()
            break    
      
    #End download
            
    if ask_ex.lower() == "both":
        videos = YTvideo.streams.all()
        down()
                
    elif ask_ex.lower() == "mp4":
        videos = YTvideo.streams.filter(file_extension='mp4').all()
        down()
                    
    elif ask_ex.lower() == "mp3":
        videos = YTvideo.streams.filter(only_audio=True).all()
        down()
    
    elif ask_ex.lower() == "c" or ask_ex.lower() == "change":
        ask_Loca = input("Enter Your new location(Press n to stop - Press r to restart to Deafult): ")
        
        if ask_Loca.lower() == "n":
            continue
        
        elif ask_Loca.lower() == "r" :
            change_loca = open("Loca.txt","w")
            change_loca.write("C:\\Download\\")
            change_loca.close()
            
        else:
            change_loca = open("Loca.txt","w")
            change_loca.write(ask_Loca.replace("\\", "\\" + "\\"))
            change_loca.close()
            continue
    
    else:
        videos = YTvideo.streams.all()
        down()
    
    print("\ngo to C:\\Download To see your videos\n")  
    print("finish")
    
    
    
    end = input("do you want to restart app(y or n): ")
    
    if end.lower() == "y" or end.lower() == "yes": continue
    elif end.lower() == "n" or end.lower() == "no": break
    else: break
