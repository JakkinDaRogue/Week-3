import wx

class Example(wx.Frame):
    num = ""

    def add(self, a, b):
        pass
        c = a + b
        c = str(c)
        self.display.WriteText(c)

    def sub(self, a, b):
        pass
        c = a - b
        c = str(c)
        self.display.WriteText(c)

    def mult(self, a, b):
        pass
        d=0
        c=0
        while d < b:
            c = c + a
            d = d + 1
        c = str(c)
        self.display.WriteText(c)

    def div(self, a, b):
        pass
        c=0
        while a>=b:
            a = a - b
            c = c + 1
        c = str(c)
        self.display.WriteText(c)

    def pow(self, a, b):
        pass
        d=1
        c=0
        while d < b:
            a = a * a
            c = a
            d = d + 1
        c = str(c)
        self.display.WriteText(c)

    def rem(self, a, b):
        pass
        c=0
        while a>=b:
            a = a - b
            c = c + 1
        a = str(a)
        self.display.WriteText(a)

    def BtD(self, binary):
        count = 0
        ans = 0
        binary_str = str(binary)
        while count <= len(binary_str):
            rem = binary % 2
            ans = rem*2**count + ans
            binary = int(binary / 10)
            count = count + 1
        ans = str(ans)
        self.display.WriteText(ans)

    def BtO(self, binary):
        output1 = ""
        output2 = ""
        count = 0
        [side_a, side_b] = str(binary).split(".")

        if len(side_a) % 3 == 1:
                side_a = "00" + side_a
        elif len(side_a) % 3 == 2:
                side_a = "0" + side_a

        if len(side_b) % 3 == 1:
                    side_b = side_b + "00"
        elif len(side_b) % 3 == 2:
                    side_b = side_b + "0"

        for index in range(0, len(side_a), 3):
            cur_group = side_a[index: index+3]
            if cur_group == "000":
                output1 = output1 + "0"
            elif cur_group == "001":
                output1 = output1 + "1"
            elif cur_group == "010":
                output1 = output1 + "2"
            elif cur_group == "011":
                output1 = output1 + "3"
            elif cur_group == "100":
                output1 = output1 + "4"
            elif cur_group == "101":
                output1 = output1 + "5"
            elif cur_group == "110":
                output1 = output1 + "6"
            elif cur_group == "111":
                output1 = output1 + "7"

        for index in range(0, len(side_b), 3):
            cur_group = side_b[index: index+3]
            if cur_group == "000":
                output2 = output2 + "0"
            elif cur_group == "001":
                output2 = output2 + "1"
            elif cur_group == "010":
                output2 = output2 + "2"
            elif cur_group == "011":
                output2 = output2 + "3"
            elif cur_group == "100":
                output2 = output2 + "4"
            elif cur_group == "101":
                output2 = output2 + "5"
            elif cur_group == "110":
                output2 = output2 + "6"
            elif cur_group == "111":
                output2 = output2 + "7"
        self.display.WriteText(output1 + "." + output2)

    def BtH (self, binary):
        binary = str(binary)
        [num_bef_dec, num_after_dec] = binary.split(".")
        print (num_bef_dec)
        print (num_after_dec)
        output = ""
        output_1 = ""
        count = 0
        side_a = len(num_bef_dec)
        print (side_a)
        side_b = len(num_after_dec)
        print (side_b)

        if side_a % 4 == 1:
            num_bef_dec = num_bef_dec[::-1] + "000"
            num_bef_dec = num_bef_dec[::-1]
            print (num_bef_dec)
        elif side_a % 4 == 2:
            num_bef_dec = num_bef_dec[::-1] + "00"
            num_bef_dec = num_bef_dec[::-1]
        elif side_a % 4 == 3:
            num_bef_dec = num_bef_dec[::-1] + "0"
            num_bef_dec = num_bef_dec[::-1]

        if side_b % 4 == 1:
            num_after_dec = num_after_dec + "000"

        elif side_b % 4 == 2:
            num_after_dec = num_after_dec + "00"

        elif side_b % 4 == 3:
            num_after_dec = num_after_dec + "0"


        for index in range(0, side_a, 4):
            cur_group = num_bef_dec[index:index+4]

            if cur_group == "0000":
                output = output + "0"
            elif cur_group == "0001":
                output = output + "1"
            elif cur_group == "0010":
                output = output + "2"
            elif cur_group == "0011":
                output = output + "3"
            elif cur_group == "0100":
                output = output + "4"
            elif cur_group == "0101":
                output = output + "5"
            elif cur_group == "0110":
                output = output + "6"
            elif cur_group == "0111":
                output = output + "7"
            elif cur_group == "1000":
                output =output + "8"
            elif cur_group == "1001":
                output = ouput + "9"
            elif cur_group == "1010":
                output = output + "A"
            elif cur_group == "1011":
                output = output + "B"
            elif cur_group == "1100":
                output = output + "C"
            elif cur_group == "1101":
                output = output + "D"
            elif cur_group == "1110":
                output = output + "E"
            elif cur_group == "1111":
                output = output + 'F'

        for index in range(0, side_b, 4):
            cur_group = num_after_dec[index:index+4]

            if cur_group == "0000":
                output_1 = output_1 + "0"
            elif cur_group == "0001":
                output_1 = output_1 + "1"
            elif cur_group == "0010":
                output_1 = output_1 + "2"
            elif cur_group == "0011":
                output_1 = output_1 + "3"
            elif cur_group == "0100":
                output_1 = output_1 + "4"
            elif cur_group == "0101":
                output_1 = output_1 + "5"
            elif cur_group == "0110":
                output_1 = output_1 + "6"
            elif cur_group == "0111":
                output_1 = output_1 + "7"
            elif cur_group == "1000":
                output_1 =output_1 + "8"
            elif cur_group == "1001":
                output_1 = output_1 + "9"
            elif cur_group == "1010":
                output_1 = output_1 + "A"
            elif cur_group == "1011":
                output_1 = output_1 + "B"
            elif cur_group == "1100":
                output_1 = output_1 + "C"
            elif cur_group == "1101":
                output_1 = output_1 + "D"
            elif cur_group == "1110":
                output_1 = output_1 + "E"
            elif cur_group == "1111":
                output_1 = output_1 + 'F'
        total = output + '.' + output_1
        self.display.WriteText(total)

    def Operations(self, array):
        if "+" in self.num:
            self.num = self.num.split("+")
            self.add(float(self.num[0]), float(self.num[-1]))

        if "-" in self.num:
            self.num = self.num.split("-")
            self.sub(float(self.num[0]), float(self.num[-1]))

        if "*" in self.num:
            self.num = self.num.split("*")
            self.mult(float(self.num[0]), float(self.num[-1]))

        if "/" in self.num:
            self.num = self.num.split("/")
            self.div(float(self.num[0]), float(self.num[-1]))

        if "^" in self.num:
            self.num = self.num.split("^")
            self.pow(float(self.num[0]), float(self.num[-1]))

        if "%" in self.num:
            self.num = self.num.split("%")
            self.rem(float(self.num[0]), float(self.num[-1]))

        if "BtD" in self.num:
            self.num = self.num.replace("BtD", " ")
            self.BtD(float(self.num))

        if "BtO" in self.num:
            self.num = self.num.replace("BtO", " ")
            self.BtD(float(self.num))

        if "BtH" in self.num:
            self.num = self.num.replace("BtH", " ")
            self.BtH(float(self.num))

    def OnClicked(self, event):
        btn = event.GetEventObject().GetLabel()
        print("6")

    def OnQuit(self, e):
        self.Close()

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        self.InitUI()
        self.Centre()

    def InitUI(self):


        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        fileItem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)

        def main():

            app = wx.App()
            ex = Example(None, title='Calculator')
            ex.Show()
            app.MainLoop()

        vbox = wx.BoxSizer(wx.VERTICAL)
        self.display = wx.TextCtrl(self, style=wx.TE_RIGHT)
        vbox.Add(self.display, flag=wx.EXPAND|wx.TOP|wx.BOTTOM, border=4)
        gs = wx.GridSizer(6, 4, 5, 5)

        self.btn_c = wx.Button(self, label='C')
        self.btn_rem = wx.Button(self, label='%')
        self.btn_7 = wx.Button(self, label='7')
        self.btn_8 = wx.Button(self, label='8')
        self.btn_9 = wx.Button(self, label='9')
        self.btn_div = wx.Button(self, label='/')
        self.btn_4 = wx.Button(self, label='4')
        self.btn_5 = wx.Button(self, label='5')
        self.btn_6 = wx.Button(self, label='6')
        self.btn_mult = wx.Button(self, label='*')
        self.btn_1 = wx.Button(self, label='1')
        self.btn_2 = wx.Button(self, label='2')
        self.btn_3 = wx.Button(self, label='3')
        self.btn_min = wx.Button(self, label='-')
        self.btn_0 = wx.Button(self, label='0')
        self.btn_dec = wx.Button(self, label='.')
        self.btn_eql = wx.Button(self, label='=')
        self.btn_add = wx.Button(self, label='+')
        self.btn_pow = wx.Button(self, label='^')
        self.btn_BtD = wx.Button(self, label='Bin to Dec')
        self.btn_DtO = wx.Button(self, label='Bin to Oct')
        self.btn_DtH = wx.Button(self, label='Bin to Hex')

        self.btn_c.Bind(wx.EVT_BUTTON,self.OnClicked_c)
        self.btn_rem.Bind(wx.EVT_BUTTON,self.OnClicked_rem)
        self.btn_7.Bind(wx.EVT_BUTTON,self.OnClicked7)
        self.btn_8.Bind(wx.EVT_BUTTON,self.OnClicked8)
        self.btn_9.Bind(wx.EVT_BUTTON,self.OnClicked9)
        self.btn_div.Bind(wx.EVT_BUTTON,self.OnClicked_div)
        self.btn_4.Bind(wx.EVT_BUTTON,self.OnClicked4)
        self.btn_5.Bind(wx.EVT_BUTTON,self.OnClicked5)
        self.btn_6.Bind(wx.EVT_BUTTON,self.OnClicked6)
        self.btn_mult.Bind(wx.EVT_BUTTON,self.OnClicked_mult)
        self.btn_1.Bind(wx.EVT_BUTTON,self.OnClicked1)
        self.btn_2.Bind(wx.EVT_BUTTON,self.OnClicked2)
        self.btn_3.Bind(wx.EVT_BUTTON,self.OnClicked3)
        self.btn_min.Bind(wx.EVT_BUTTON,self.OnClicked_min)
        self.btn_0.Bind(wx.EVT_BUTTON,self.OnClicked0)
        self.btn_dec.Bind(wx.EVT_BUTTON,self.OnClicked_dec)
        self.btn_eql.Bind(wx.EVT_BUTTON,self.OnClicked_eql)
        self.btn_add.Bind(wx.EVT_BUTTON,self.OnClicked_add)
        self.btn_pow.Bind(wx.EVT_BUTTON,self.OnClicked_pow)
        self.btn_BtD.Bind(wx.EVT_BUTTON,self.OnClicked_BtD)
        self.btn_DtO.Bind(wx.EVT_BUTTON,self.OnClicked_DtO)
        self.btn_DtH.Bind(wx.EVT_BUTTON,self.OnClicked_DtH)

        gs.AddMany( [(self.btn_c, 0, wx.EXPAND),
            (wx.StaticText(self), wx.EXPAND),
            (wx.StaticText(self), wx.EXPAND),
            (self.btn_rem, 0, wx.EXPAND),
            (self.btn_7, 0, wx.EXPAND),
            (self.btn_8, 0, wx.EXPAND),
            (self.btn_9, 0, wx.EXPAND),
            (self.btn_div, 0, wx.EXPAND),
            (self.btn_4, 0, wx.EXPAND),
            (self.btn_5, 0, wx.EXPAND),
            (self.btn_6, 0, wx.EXPAND),
            (self.btn_mult, 0, wx.EXPAND),
            (self.btn_1, 0, wx.EXPAND),
            (self.btn_2, 0, wx.EXPAND),
            (self.btn_3, 0, wx.EXPAND),
            (self.btn_min, 0, wx.EXPAND),
            (self.btn_0, 0, wx.EXPAND),
            (self.btn_dec, 0, wx.EXPAND),
            (self.btn_eql, 0, wx.EXPAND),
            (self.btn_add, 0, wx.EXPAND),
            (self.btn_pow, 0, wx.EXPAND),
            (self.btn_BtD, 0, wx.EXPAND),
            (self.btn_DtO, 0, wx.EXPAND),
            (self.btn_DtH, 0, wx.EXPAND) ])

        vbox.Add(gs, proportion=1, flag=wx.EXPAND)
        self.SetSizer(vbox)

        self.Bind(wx.EVT_MENU, self.OnQuit, fileItem)

    def OnClicked_c(self, event):
        self.display.Clear()
        self.num = ""

    def OnClicked_rem(self, event):
        self.display.WriteText("%")
        self.num += ("%")

    def OnClicked7(self, event):
        self.display.WriteText("7")
        self.num += ("7")

    def OnClicked8(self, event):
        self.display.WriteText("8")
        self.num += ("8")

    def OnClicked9(self, event):
        self.display.WriteText("9")
        self.num += ('9')

    def OnClicked_div(self, event):
        self.display.WriteText("/")
        self.num += ('/')

    def OnClicked4(self, event):
        self.display.WriteText("4")
        self.num += ('4')

    def OnClicked5(self, event):
        self.display.WriteText("5")
        self.num += ('5')

    def OnClicked6(self, event):
        self.display.WriteText("6")
        self.num += ('6')

    def OnClicked_mult(self, event):
        self.display.WriteText("*")
        self.num += ('*')

    def OnClicked1(self, event):
        self.display.WriteText("1")
        self.num += ('1')

    def OnClicked2(self, event):
        self.display.WriteText("2")
        self.num += ('2')

    def OnClicked3(self, event):
        self.display.WriteText("3")
        self.num += ('3')

    def OnClicked_min(self, event):
        self.display.WriteText("-")
        self.num += ('-')

    def OnClicked0(self, event):
        self.display.WriteText("0")
        self.num += (0)

    def OnClicked_dec(self, event):
        self.display.WriteText(".")
        self.num += ('.')

    def OnClicked_eql(self, event):
        self.display.WriteText("=")
        self.Operations(self.num)

    def OnClicked_add(self, event):
        self.display.WriteText("+")
        self.num += ('+')

    def OnClicked_pow(self, event):
        self.display.WriteText("^")
        self.num += ('^')

    def OnClicked_BtD(self, event):
        self.num += ("BtD")

    def OnClicked_DtO(self, event):
        self.num += ("BtO")

    def OnClicked_DtH(self, event):
        self.num += ("BtH")

def main():

    app = wx.App()
    ex = Example(None, title='Calculator')
    ex.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
