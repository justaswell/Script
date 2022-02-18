import pyautogui
import time

def QJZ():
    yuyue="yuyue.png"
    shuaxin="shuaxin.png"
    huadong="huadong.png"
    locationyy = pyautogui.locateCenterOnScreen(yuyue, confidence=0.9)

    if locationyy is not None:
        pyautogui.click(locationyy.x, locationyy.y, clicks=1, interval=0.2, duration=0.2, button='left')

        locationhd=pyautogui.locateCenterOnScreen(huadong, confidence=0.9)
        while locationhd is None:
            locationhd = pyautogui.locateCenterOnScreen(huadong, confidence=0.9)
        pyautogui.moveTo(locationhd)
        pyautogui.dragRel(300, 0, duration=0.5)
        print("Done.")
        return 1
    else:
        time.sleep(2)
        locationsx=pyautogui.locateCenterOnScreen(shuaxin, confidence=0.9)
        pyautogui.click(locationsx.x, locationsx.y, clicks=1, interval=0.2, duration=0.2, button='left')
        locationyy = pyautogui.locateCenterOnScreen(yuyue, confidence=0.9)
        while locationyy is None:
            locationyy = pyautogui.locateCenterOnScreen(yuyue, confidence=0.9)
            if locationyy is not None:
                break
            else:
                print("the website has not shown completely.")
                time.sleep(5)
        #print("找不到按钮，刷新界面。")
        return 0


if __name__ == '__main__':
    key=input("start? y or n\n")
    succeed=0
    count=0
    if key=='y':
        while succeed==0 and count!=2:
            if(time.localtime().tm_hour==19):
                succeed=QJZ()
                count+=1
            else:
                print("the time is",time.localtime())
                hour=time.localtime().tm_hour
                min=time.localtime().tm_min
                sec=time.localtime().tm_sec
                wait=(18-hour)*60*60+(59-min)*60+(60-sec)
                print(wait)
                time.sleep(wait)


