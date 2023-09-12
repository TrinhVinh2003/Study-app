from tkinter.font import Font
from tkinter import *


class ScorePredict:
    def __init__(self, root):
        global diemThuongXuyen, diemGiuaKy
        self.window = root
        self.window.geometry("600x400")
        self.window.title("ScorePredict")
        bg_color = '#42C2FF'
        fg_color = '#EFFFFD'
        input_color = 'black'
        self.window['bg'] = bg_color
        self.diemMin = {
                "A+": 9,
                "A" : 8.5,
                "B+": 8,
                "B" : 7,
                "C+": 6.5,
                "C" : 5.5,
                "D+": 5,
                "D" : 4
            }
        
        self.duBaoDiemFrame = Frame(master = self.window)
        self.duBaoDiemFrame['bg'] = bg_color
        font25 = Font(self.window, size = 18)
        


        lbl_heading = Label(master = self.duBaoDiemFrame, text = 
        "CHƯƠNG TRÌNH\nTÍNH ĐIỂM THI CUỐI KỲ CẦN ĐẠT", font= Font(self.window, size = 20, weight='bold'), bg=bg_color, fg= 'yellow')
        lbl_heading.grid(row = 0, column = 0, columnspan = 3, sticky = "nsew")

        # chon muc tieu (A, A+, B, B+, ...)
        self.quyDoi = {
            "A+": "4.0/4",
            "A" : "3.7/4",
            "B+": "3.5/4",
            "B" : "3.0/4",
            "C+": "2.5/4",
            "C" : "2.0/4",
            "D+": "1.5/4",
            "D" : "1.0/4"
        }
        lbl_chonMucTieu = Label(master = self.duBaoDiemFrame, text = "Nhập vào mục tiêu của bạn:", font= font25, bg= bg_color, fg= fg_color)
        lbl_chonMucTieu.grid( row= 1, column=0, sticky="w", padx = 5, pady=15)

        self.ent_chonMucTieu = Entry(master = self.duBaoDiemFrame, width = 5, font= font25, fg = input_color)
        self.ent_chonMucTieu.grid(row= 1, column=1, sticky="w",padx = 5, pady=15)

        self.lbl_quyDoiMucTieu = Label(master= self.duBaoDiemFrame, text = "/4", font = font25, bg = bg_color, fg = fg_color)
        self.lbl_quyDoiMucTieu.grid(row = 1, column = 2, sticky = "w", padx = 5, pady = 15)


        self.ent_chonMucTieu.bind("<FocusOut>", self.quyDoiHe)

        # Nhap diem thuong xuyen
        lbl_diemThuongXuyen = Label(master= self.duBaoDiemFrame, text = "Nhập điểm thường xuyên của bạn:", font= font25, bg= bg_color, fg= fg_color, )
        lbl_diemThuongXuyen.grid( row = 2, column = 0, sticky="w", padx = 5, pady = 15)

        self.ent_diemThuongXuyen = Entry(master= self.duBaoDiemFrame, width= 5, font= font25, fg = input_color)
        self.ent_diemThuongXuyen.grid( row = 2, column = 1, sticky="w", padx = 5, pady = 15)

        # Nhap diem giua ky
        lbl_diemGiuaKy = Label(master= self.duBaoDiemFrame, text = "Nhập điểm giữa kỳ của bạn:", font= font25, bg= bg_color, fg= fg_color)
        lbl_diemGiuaKy.grid( row = 3, column = 0, sticky="w", padx = 5, pady = 15)

        self.ent_diemGiuaKy = Entry(master= self.duBaoDiemFrame, width= 5, font= font25, fg = input_color)
        self.ent_diemGiuaKy.grid( row = 3, column = 1, sticky="w", padx = 5, pady = 15)
        
        

        btn_TinhDiem = Button(master = self.duBaoDiemFrame, text = "Tính điểm", command= self.TinhDiem, font = Font(self.window, size = 14), bg= '#85F4FF', relief = "groove")
        btn_TinhDiem.grid(row = 4, column = 1, sticky = "w")

        self.lbl_ketQua = Label(master = self.duBaoDiemFrame, text = "Điểm cuối kỳ cần đạt: ", font= font25, bg= bg_color, fg= fg_color)
        self.lbl_ketQua.grid(row = 5, columnspan = 2,sticky= "nsew")
        
        btn_esc = Button(master= self.duBaoDiemFrame, text = "Thoát", command= self.closeAll, font = Font(self.window, size = 14), bg= '#85F4FF', relief = "groove")
        btn_esc.grid(row = 6, column = 2, sticky = "e")
        
        self.duBaoDiemFrame.grid(row = 0, column = 0, padx = 10)
    def TinhDiem(self):
            self.mucTieu = self.ent_chonMucTieu.get()
            diemThuongXuyen = float(self.ent_diemThuongXuyen.get())
            diemGiuaKy = float (self.ent_diemGiuaKy.get())
            

            duBao = self.duBaoDiem(diemThuongXuyen, diemGiuaKy, self.mucTieu)
            if (duBao == -1):
                self.lbl_ketQua["text"] = "Điểm cuối kỳ cần đạt: Muc tieu khong ton tai"
            elif (duBao > 10):
                self.lbl_ketQua["text"] = "Điểm cuối kỳ cần đạt: Bat kha thi!"
            else:
                self.lbl_ketQua["text"] = f"Điểm cuối kỳ cần đạt: {round(duBao, 2)}"
        

    def duBaoDiem(self, diemThuongXuyen, diemGiuaKy, mucTieu):
        if (self.diemMin.get(self.mucTieu, -1) != -1):
            self.diemCuoiKy = (self.diemMin[self.mucTieu] - (diemThuongXuyen + diemGiuaKy) * 0.2) / 0.6
            return self.diemCuoiKy
        else:
            return -1

    def validate(self, P):
        return len(self.P) < 6

    
    def quyDoiHe(self, event):
        self.mucTieu = self.ent_chonMucTieu.get()
        self.lbl_quyDoiMucTieu["text"] = self.quyDoi.get(self.mucTieu, "/4")


# Tạo nút "Thoat"
    def closeAll(self):
        self.duBaoDiemFrame.destroy()
        self.window.destroy()


if __name__ =='__main__':
    root= Tk()
    application = ScorePredict(root)
    root.mainloop()




    