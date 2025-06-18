from CCoordinates import CXY,tCXY
from CDesignator import CDesignator
from tkinter import *

class CModDraw():
    def __init__(self,ModName,scale,SizeBoard,side,angle=0):
        self.__side=side
        self.__angle=angle
        self.__ModName=ModName
        self.__scl=scale
        self.__SB=SizeBoard
        #
        self.__root = Tk()
        self.__root.title(self.__ModName)
        self.__root.geometry(self.__SB.size(1.2*self.__scl))
        #
        self.__canvas = Canvas(bg="#53C351", width=round(self.__SB.x*self.__scl), height=round(self.__SB.y*self.__scl))
        self.__canvas.pack(anchor=CENTER, expand=1)
        #
        self.__c=tCXY(self.__scl,self.__SB,self.__side,self.__angle)

    def DzDraw(self,dz,rzm):
        el_fill="#80CBC4"
        el_outline="#004D40"
        match dz.Des[0]:
            case 'R':
                el_fill="#485E5D"
                el_outline="#13453E"
            case 'C':
                el_fill="#757535"
                el_outline="#1B6872"
            case 'L':
                el_fill="#247CF7"
                el_outline="#0A373D"
            case 'D':
                el_fill="#214643"
                el_outline="#13636E"
            case 'V':
                match dz.Des[1]:
                    case 'T':
                        el_fill="#373798"
                        el_outline="#396336"
                        #print(rzm,dz.Angle)
                    case 'D':
                        el_fill="#6E2E1E"
                        el_outline="#3A7981"
        # Рисуем компонент
        vl=self.__c.tr(dz.XY.vl(rzm,dz.Angle))
        np=self.__c.tr(dz.XY.np(rzm,dz.Angle))
        self.__canvas.create_rectangle(vl.x,vl.y,np.x,np.y, fill=el_fill, outline=el_outline)
        # Рисуем ключ
        rz1p=CXY(.2,.2)
        vl1p=self.__c.tr(dz.XY1p.vl(rz1p))
        np1p=self.__c.tr(dz.XY1p.np(rz1p))
        self.__canvas.create_rectangle(vl1p.x,vl1p.y,np1p.x,np1p.y, fill="#F17F7F", outline="#02231D")
        # Печатаем дезигнатор            
        dt=self.__c.tr(dz.XY)
        textID = self.__canvas.create_text(dt.x,dt.y, angle=dz.Angle, fill="#FDFDFD")
        self.__canvas.itemconfig(textID, text = dz.Des)


    def RepDraw(self,dz_rep,rdz):
        # Рисуем внешний круг
        rdz1=CXY(1.,1.)
        vl_rdz1=self.__c.tr(dz_rep.XY.vl(rdz1))
        np_rdz1=self.__c.tr(dz_rep.XY.np(rdz1))
        self.__canvas.create_oval(vl_rdz1.x,vl_rdz1.y,np_rdz1.x,np_rdz1.y, fill="#69CFB0", outline="#031210")
        # Рисуем внутренний круг
        vl_rdz=self.__c.tr(dz_rep.XY.vl(rdz))
        np_rdz=self.__c.tr(dz_rep.XY.np(rdz))
        self.__canvas.create_oval(vl_rdz.x,vl_rdz.y,np_rdz.x,np_rdz.y, fill="#C0E16E", outline="#031210")
        # Подписываем дезигнатор
        dtr=self.__c.tr(dz_rep.XY)
        textIDR = self.__canvas.create_text(dtr.x,dtr.y, angle=dz_rep.Angle, fill="#0B0606")
        self.__canvas.itemconfig(textIDR, text = dz_rep.Des[3])


    def RepFL(self,rzfr,rep0,rep1): 
        # Выводим репер с нулевыми координатами  
        vl_rep0=self.__c.tr(rep0.vl(rzfr))
        np_rep0=self.__c.tr(rep0.np(rzfr))
        self.__canvas.create_oval(vl_rep0.x,vl_rep0.y,np_rep0.x,np_rep0.y,  outline="#E1FC37")
        # Выводим самый дальний репер
        vl_rep1=self.__c.tr(rep1.vl(rzfr))
        np_rep1=self.__c.tr(rep1.np(rzfr))
        self.__canvas.create_oval(vl_rep1.x,vl_rep1.y,np_rep1.x,np_rep1.y,  outline="#291FE7")      

    def RootLoop(self):
        self.__root.mainloop()