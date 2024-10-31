# Welcome_page

class Welcome :
    
    def __init__(self):
        
        from tkinter import font , Entry , messagebox , Text , END , Tk , Button , Label , StringVar , PhotoImage
        import Round_one
        
        def enter():
            
            player_name = player_name_value.get()
            messagebox.showinfo('Message' , 'Let\'s catch them All !! ' + player_name )
            welcome_window.destroy()
            round1 = Round_one.round_one()
           
        
        
        
        
        
        welcome_window = Tk()
        welcome_window.geometry('500x300')
        welcome_window.title('Welcome to Pokemon ')
        
        # Logo
        logo = PhotoImage(file = 'main_logo.png')
        logo_label = Label(welcome_window , image = logo).place(x = 45 , y = 10)
        
        fontStyle = font.Font( size=14)
        player_name = Label(welcome_window , text = 'Player\'s name *' , font = fontStyle ).place(x = 200 , y = 175)
        player_name_value = StringVar()
        player_name_textbox = Entry(welcome_window , font = fontStyle , textvariable = player_name_value).place(x = 150 , y = 210)
        
        button_logo = PhotoImage(file = 'login.png')
        enter_button = Button(welcome_window , text = 'Enter'  , command = enter  , image = button_logo ).place(x = 160 , y = 250)
        
        welcome_window.mainloop()
    
    