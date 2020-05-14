import cv2,time

first_frame=None   #as i have to store my first frame so i need to make a variable and also assign it with null values

video= cv2.VideoCapture(0)

while True:
    check,frame=video.read()
    
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(21,21),0)
    
    if first_frame is None:
        first_frame= gray   #stored the first captured image in frame
        continue # come out of the if loop

    #for calculate the difference between first frame and it's subsequent frame
    diff_frame = cv2.absdiff(first_frame,gray)
    
    #provides a threshold value,such that it will convert the pixels if difference value with less than 30 to black and greater than 30 to to white
    thr_val=cv2.threshold(diff_frame,30,225, cv2.THRESH_BINARY)[1]
    thr_val=cv2.dilate(thr_val,None, iterations=0)
    
    #define the counetr area (or) basically add the boarders
    cnts=cv2.findContours(thr_val.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    
    #REMOVE noises and shadows.Basically,it will keep only that part white,whch has area greater than 1000 pixels
    
    for contour in cnts:
        if cv2.contourArea(contour) < 1000:
            continue
        #create rectangular box around the object in the frame
        (x ,y ,w ,h)=cv2.boundingRect(contour)
        cv2.rectangle(frame , (x,y) , (x+w,y+h) ,(0,255,0),3)
        
        cv2.imshow("frame",frame)
        cv2.imshow("capturing",gray)
        cv2.imshow("c",diff_frame)
        cv2.imshow("thresh",thr_val)
        
        key=cv2.waitKey(1) # frame will change in 1 milli seconds
        
        if key == ord('q'):
            break
video.release()

cv2.destroyAllWindows()


##########################

import  pandas as pd
from datatime import datatime
#calculating the time for which the object was in front of the camera

first_frame=None
status_list=[None,None]
timees=[]
#dataframe to store the time values during which object daetection and movement appears
df=pandas.DataFrame(columns=["Start","End"])
video=cv2.VideoCapture(0)



while True:
    check,frame=video.read()
    status=0   #istatus is zero as the object is not visible
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(21,21,0))
     #define the counetr area (or) basically add the boarders
    (_,cnts,_)=cv2.findContours(th_value.copy(),cv2.RETR.EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in cnts:
        if cv2.contourArea(contour) < 10000:
            continue
        status=1  #change in status when object is detected
        (x ,y ,w ,h)=cv2.boundingRect(contour)
        cv2.rectangle(frame , (x,y) , (x+w,y+h) ,(0,255,0),3)
status_list.append(status)
status_list=status_list[-2:]
    
    
if status_list[-1]==1 and status_list[-2]==0:
    times.append(datetime.now())
  
if status_list[-1]==0 and status_list[-2]==1:
    times.append(datetime.now())
    
print(status_list)
print(times)

for i in range(0,len(times),2):
    df=df.append({"Start":times[i],"End":times[i+1]},ignore_index=True)
df.to_csv("Time.csv")

video.release()
cvv2.destroyAllWindows()



#plotting the motion detection graph

from motion_detector import df
from bokeh.plottting import figure,show,output_file
from bokeh.models import HoverTool,ColumnDataSource

df["Start_string"]=df["Start"].dt.strftime("%Y-%m-%d  %H:%M:%S")
df["End_string"]=df["End"].dt.strftime("%Y-%m-%d  %H:%M:%S")

cds=ColumnDataSource(df)

p=figure(x_axis_type='datetime',height=100,width=500,responsive=True,title='Motion Graph')
p.yaxis.minor_tick_line_color=None
p.ygrid[0].ticker.desired_num_ticket=1

hover=HoverTool(tooltips=[("Start","@Start_string"),("End","@End_string")])
p.add_tools(hover)

q=p.quad(left="Start",right="End",bottom=0,top=1,color="red",source=cds)

output_file("Graph1.html")
show(p)
