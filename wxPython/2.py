import wx

class randomName(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Imeto na prozoreca', size=(200,300))
        panel = wx.Panel(self)
        button = wx.Button(panel, label="CLOSE", pos=(20,20), size=(50,20))
    
        status = self.CreateStatusBar()
        question = wx.MessageDialog(None, 'Yes or No?', 'Title', wx.YES_NO) #wx.OK 
        answer = question.ShowModal()
        question.Destroy()
        print answer # yes 5103; no 5104

        txt = wx.TextEntryDialog(None, 'Kak se kazvash?', 'Title', 'test po podrazbirane')
        if txt.ShowModal() == wx.ID_OK:
            answer = txt.GetValue()

        self.Bind(wx.EVT_BUTTON, self.closefuncfrombutton, button)
    
    def closefuncfrombutton(self, event):
        self.Close(True)


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = randomName(parent=None,id=-1)
    frame.Show()
    app.MainLoop()
