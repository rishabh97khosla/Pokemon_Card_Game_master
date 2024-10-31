# Round_four
class round_four :
    
    def __init__(self , player_total_score , computer_total_score):
        
        from tkinter import PhotoImage, font ,  Frame , Tk , Button , Label , Text, messagebox , Entry , StringVar , Radiobutton , IntVar , ttk
        from pandastable import Table, TableModel
        import random
        import pandas as pd
        import Round_five
        
        df = pd.read_csv('cards.csv')
        player_cards = df.sample(n=6)
        player   = player_cards[:3] 
        computer = player_cards[3:]
        
        self.player_total_score = player_total_score
        self.computer_total_score = computer_total_score
        
        def next_round():
            game_window.destroy()
            round_5 = Round_five.round_five(self.player_total_score , self.computer_total_score)

        def play() :
            
            player_round4_score = 0
            computer_round4_score = 0

            
            player_pokemon = poke_name_var.get() # name of the pokemon of the player 
            computer_pokemon = computer['Name'].sample(n=1).values[0] # name of the pokemon by computer randomly 
            computer_power   = random.choice([1,2,3,4]) # power choosen 
                    
            if computer_power == 1 :
                messagebox.showinfo('HP' , 'your pokemon is '+ player_pokemon )
                # player score
                player_score = int(player['HP'][player['Name']==player_pokemon].values)
                # Computer score  
                computer_score = int(computer['HP'][computer['Name']==computer_pokemon].values)
                
                if player_score > computer_score :
                    player_round4_score += 1 
                    fontStyle = font.Font( size=12)
                    label_player = Label(   game_window , font = fontStyle , text = 'Player\'s card -> {} HP : {}'.format(player_pokemon , player_score))
                    label_computer = Label( game_window , font = fontStyle , text = 'Computer\'s card -> {} HP : {}'.format( computer_pokemon , computer_score))
                    label_player.place( x = 650 , y = 350 )
                    label_computer.place( x = 650 , y = 400 )
                    
                elif computer_score > player_score :
                    computer_round4_score += 1 
                    fontStyle = font.Font( size=12)
                    label_player = Label(   game_window , font = fontStyle , text = 'Player\'s card -> {} HP : {}'.format(player_pokemon , player_score))
                    label_computer = Label( game_window , font = fontStyle , text = 'Computer\'s card -> {} HP : {}'.format( computer_pokemon , computer_score))
                    label_player.place( x = 650 , y = 350 )
                    label_computer.place( x = 650 , y = 400 )
                    
                else :
                    fontStyle = font.Font( size=12)
                    label_player = Label(   game_window , font = fontStyle , text = 'Player\'s card -> {} HP : {}'.format(player_pokemon , player_score))
                    label_computer = Label( game_window , font = fontStyle , text = 'Computer\'s card -> {} HP : {}'.format( computer_pokemon , computer_score))
                    label_player.place( x = 650 , y = 350 )
                    label_computer.place( x = 650 , y = 400 )
                    

            if computer_power == 2 :
                messagebox.showinfo('Attack' , 'your pokemon is '+ player_pokemon)
                # player score
                player_score = int(player['Attack'][player['Name']==player_pokemon].values)
                # Computer score 
                computer_score = int(computer['Attack'][computer['Name']==computer_pokemon].values)
                
                if player_score > computer_score :
                    player_round4_score += 1 
                    fontStyle = font.Font( size=12)
                    label_player = Label(   game_window , font = fontStyle , text = 'Player\'s card -> {} Attack : {}'.format(player_pokemon , player_score))
                    label_computer = Label( game_window , font = fontStyle , text = 'Computer\'s card -> {} Attack : {}'.format( computer_pokemon , computer_score))
                    label_player.place( x = 650 , y = 350 )
                    label_computer.place( x = 650 , y = 400 )
                    
                elif computer_score > player_score :
                    computer_round4_score += 1 
                    fontStyle = font.Font( size=12)
                    label_player = Label(   game_window , font = fontStyle , text = 'Player\'s card -> {} Attack : {}'.format(player_pokemon , player_score))
                    label_computer = Label( game_window , font = fontStyle , text = 'Computer\'s card -> {} Attack : {}'.format( computer_pokemon , computer_score))
                    label_player.place( x = 650 , y = 350 )
                    label_computer.place( x = 650 , y = 400 )
                    
                else :
                    fontStyle = font.Font( size=12)
                    label_player = Label(   game_window , font = fontStyle , text = 'Player\'s card -> {} Attack : {}'.format(player_pokemon , player_score))
                    label_computer = Label( game_window , font = fontStyle , text = 'Computer\'s card -> {} Attack : {}'.format( computer_pokemon , computer_score))
                    label_player.place( x = 650 , y = 350 )
                    label_computer.place( x = 650 , y = 400 )
                    
                  
            if computer_power == 3 :
                messagebox.showinfo('Defense' , 'your pokemon is '+ player_pokemon )
                # player score
                player_score = int(player['Defense'][player['Name']==player_pokemon].values)
                # Computer score 
                computer_score = int(computer['Defense'][computer['Name']==computer_pokemon].values)
                
                if player_score > computer_score :
                    player_round4_score += 1 
                    fontStyle = font.Font( size=12)
                    label_player = Label(   game_window , font = fontStyle , text = 'Player\'s card -> {} Defense : {}'.format(player_pokemon , player_score))
                    label_computer = Label( game_window , font = fontStyle , text = 'Computer\'s card -> {} Defense : {}'.format( computer_pokemon , computer_score))
                    label_player.place( x = 650 , y = 350 )
                    label_computer.place( x = 650 , y = 400 )
                    
                elif computer_score > player_score :
                    computer_round4_score += 1 
                    fontStyle = font.Font( size=12)
                    label_player = Label(   game_window , font = fontStyle , text = 'Player\'s card -> {} Defense : {}'.format(player_pokemon , player_score))
                    label_computer = Label( game_window , font = fontStyle , text = 'Computer\'s card -> {} Defense : {}'.format( computer_pokemon , computer_score))
                    label_player.place( x = 650 , y = 350 )
                    label_computer.place( x = 650 , y = 400 )
                    
                else :
                    fontStyle = font.Font( size=12)
                    label_player = Label(   game_window , font = fontStyle , text = 'Player\'s card -> {} Defense : {}'.format(player_pokemon , player_score))
                    label_computer = Label( game_window , font = fontStyle , text = 'Computer\'s card -> {} Defense : {}'.format( computer_pokemon , computer_score))
                    label_player.place( x = 650 , y = 350 )
                    label_computer.place( x = 650 , y = 400 )
                    
            if computer_power == 4 :
                messagebox.showinfo('Speed' , 'your pokemon is '+ player_pokemon)
                # player score
                player_score = int(player['Speed'][player['Name']==player_pokemon].values)
                # Computer score 
                computer_score = int(computer['Speed'][computer['Name']==computer_pokemon].values)
                
                if player_score > computer_score :
                    player_round4_score += 1 
                    fontStyle = font.Font( size=12)
                    label_player = Label(   game_window , font = fontStyle , text = 'Player\'s card -> {} Speed : {}'.format(player_pokemon , player_score))
                    label_computer = Label( game_window , font = fontStyle , text = 'Computer\'s card -> {} Speed : {}'.format( computer_pokemon , computer_score))
                    label_player.place( x = 650 , y = 350 )
                    label_computer.place( x = 650 , y = 400 )
                    
                elif computer_score > player_score :
                    computer_round4_score += 1 
                    fontStyle = font.Font( size=12)
                    label_player = Label(   game_window , font = fontStyle , text = 'Player\'s card -> {} Speed : {}'.format(player_pokemon , player_score))
                    label_computer = Label( game_window , font = fontStyle , text = 'Computer\'s card -> {} Speed : {}'.format( computer_pokemon , computer_score))
                    label_player.place( x = 650 , y = 350 )
                    label_computer.place( x = 650 , y = 400 )
                    
                else :
                    fontStyle = font.Font( size=12)
                    label_player = Label(   game_window , font = fontStyle , text = 'Player\'s card -> {} Speed : {}'.format(player_pokemon , player_score))
                    label_computer = Label( game_window , font = fontStyle , text = 'Computer\'s card -> {} Speed : {}'.format( computer_pokemon , computer_score))
                    label_player.place( x = 650 , y = 350 )
                    label_computer.place( x = 650 , y = 400 )                       
                    
            if player_round4_score > computer_round4_score :
                messagebox.showinfo('result' , 'Player wins the round')
                self.player_total_score += 1
            elif computer_round4_score > player_round4_score :
                messagebox.showinfo('result' , 'Computer wins the round')
                self.computer_total_score += 1
            else :
                messagebox.showinfo('result' , 'No one wins the round its a tie')
          
            
            
    
   
        
        
        game_window = Tk()
        game_window.geometry('1075x500')
        game_window.title('Round 4')
        
        deal_message =  messagebox.showinfo('Dealt' , 'Cards have been dealt')
        
        # cards that are dealt for player one 
        f = Frame(game_window)
        f.place(x = 25 , y = 25)
        player_data = player
        table = pt = Table(f, dataframe=player_data)
        pt.show()
        
        # drop down pokemon names
        poke_name_var = StringVar() 
        fontStyle = font.Font( size=10)
        pokemon_name_frame = Frame(game_window).place(x = 25 , y = 350 )
        poke_name_drop = ttk.Combobox(pokemon_name_frame, width = 27, textvariable = poke_name_var , font = fontStyle)
        poke_name_drop['values'] = list(player['Name'])
        poke_name_drop.current(1)
        poke_name_drop.place(x = 25 , y = 350 )
        
        #play button 
        play_button = Button(game_window , text = 'Play' , width = 25 , command = play).place(x = 300 , y = 350 )
        
        # next round button 
        next_button = Button(game_window , text = 'Next round' ,  command = next_round , width = 25).place(x = 50 , y = 400)
        
        # image tile 
        Image_tile = PhotoImage(file ='pokemon.png')
        image_label = Label(game_window , image = Image_tile).place(x = 600, y = 25)

        
        game_window.mainloop()