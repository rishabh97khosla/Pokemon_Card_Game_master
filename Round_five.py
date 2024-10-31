# Round_five
class round_five :
    
    def __init__(self, player_total_score , computer_total_score):
        
        from tkinter import PhotoImage ,font ,  Frame , Tk , Button , Label , Text, messagebox , Entry , StringVar , Radiobutton , IntVar , ttk
        from pandastable import Table, TableModel
        import random
        import pandas as pd
        import pokemon_login
        

        df = pd.read_csv('cards.csv')
        player_cards = df.sample(n=6)
        player   = player_cards[:3] 
        computer = player_cards[3:]
        
        self.player_total_score = player_total_score
        self.computer_total_score = computer_total_score
        
        def next_game():
            game_window.destroy()
            Login = pokemon_login.Welcome()
            

        def play() :
            
            player_round5_score = 0
            computer_round5_score = 0 

            
            player_pokemon = poke_name_var.get() # name of the pokemon 
            player_power   = choice_variable.get() # power choosen  
                    
            if player_power == 1 :
                messagebox.showinfo('HP' , 'your pokemon is '+ player_pokemon + ' and you choose HP')
                # player score
                player_score = int(player['HP'][player['Name']==player_pokemon].values)
                # Computer score 
                computer_pokemon = computer['Name'].sample(n=1).values[0] # random card is selected 
                computer_score = int(computer['HP'][computer['Name']==computer_pokemon].values)
                
                if player_score > computer_score :
                    player_round5_score += 1 
                    fontStyle = font.Font( size=12)
                    label_player = Label(   game_window , font = fontStyle , text = 'Player\'s card -> {} HP : {}'.format(player_pokemon , player_score))
                    label_computer = Label( game_window , font = fontStyle , text = 'Computer\'s card -> {} HP : {}'.format( computer_pokemon , computer_score))
                    label_player.place( x = 650 , y = 350 )
                    label_computer.place( x = 650 , y = 400 )
                    
                elif computer_score > player_score :
                    computer_round5_score += 1 
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

            if player_power == 2 :
                messagebox.showinfo('Attack' , 'your pokemon is '+ player_pokemon + ' and you choose Attack')
                # player score
                player_score = int(player['Attack'][player['Name']==player_pokemon].values)
                # Computer score 
                computer_pokemon = computer['Name'].sample(n=1).values[0] # random card is selected 
                computer_score = int(computer['Attack'][computer['Name']==computer_pokemon].values)
                
                if player_score > computer_score :
                    player_round5_score += 1 
                    fontStyle = font.Font( size=12)
                    label_player = Label(   game_window , font = fontStyle , text = 'Player\'s card -> {} Attack : {}'.format(player_pokemon , player_score))
                    label_computer = Label( game_window , font = fontStyle , text = 'Computer\'s card -> {} Attack : {}'.format( computer_pokemon , computer_score))
                    label_player.place( x = 650 , y = 350 )
                    label_computer.place( x = 650 , y = 400 )
                    
                elif computer_score > player_score :
                    computer_round5_score += 1 
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
                    
                  
            if player_power == 3 :
                messagebox.showinfo('Defense' , 'your pokemon is '+ player_pokemon + ' and you choose Defense')
                # player score
                player_score = int(player['Defense'][player['Name']==player_pokemon].values)
                # Computer score 
                computer_pokemon = computer['Name'].sample(n=1).values[0] # random card is selected 
                computer_score = int(computer['Defense'][computer['Name']==computer_pokemon].values)
                
                if player_score > computer_score :
                    player_round5_score += 1 
                    fontStyle = font.Font( size=12)
                    label_player = Label(   game_window , font = fontStyle , text = 'Player\'s card -> {} Defense : {}'.format(player_pokemon , player_score))
                    label_computer = Label( game_window , font = fontStyle , text = 'Computer\'s card -> {} Defense : {}'.format( computer_pokemon , computer_score))
                    label_player.place( x = 650 , y = 350 )
                    label_computer.place( x = 650 , y = 400 )
                    
                elif computer_score > player_score :
                    computer_round5_score += 1 
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
                    
            if player_power == 4 :
                messagebox.showinfo('Speed' , 'your pokemon is '+ player_pokemon + ' and you choose Speed')
                # player score
                player_score = int(player['Speed'][player['Name']==player_pokemon].values)
                # Computer score 
                computer_pokemon = computer['Name'].sample(n=1).values[0] # random card is selected 
                computer_score = int(computer['Speed'][computer['Name']==computer_pokemon].values)
                
                if player_score > computer_score :
                    player_round5_score += 1 
                    fontStyle = font.Font( size=12)
                    label_player = Label(   game_window , font = fontStyle , text = 'Player\'s card -> {} Speed : {}'.format(player_pokemon , player_score))
                    label_computer = Label( game_window , font = fontStyle , text = 'Computer\'s card -> {} Speed : {}'.format( computer_pokemon , computer_score))
                    label_player.place( x = 650 , y = 350 )
                    label_computer.place( x = 650 , y = 400 )
                    
                elif computer_score > player_score :
                    computer_round5_score += 1 
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
                    
            # round_winner        
            if player_round5_score > computer_round5_score :
                messagebox.showinfo('result' , 'Player wins the round')
                self.player_total_score += 1

            elif computer_round5_score > player_round5_score :
                messagebox.showinfo('result' , 'Computer wins the round')
                self.computer_total_score += 1
               
            else :
                messagebox.showinfo('result' , 'No one wins the round its a tie')
              
            
            
            # game winner
            if self.player_total_score > self.computer_total_score :
                messagebox.showinfo('result' , 'player  wins the game ')
                print(self.player_total_score)
                print(self.computer_total_score)
            elif self.player_total_score < self.computer_total_score :
                messagebox.showinfo('result' , 'computer wins the game ')
                print(self.player_total_score)
                print(self.computer_total_score)
            else :
                messagebox.showinfo('result' , 'the game is tied ')
                print(self.player_total_score)
                print(self.computer_total_score)
                
                
            

               
        
        
          

            
        
        
    
   
        
        
        game_window = Tk()
        game_window.geometry('1075x500')
        game_window.title('Round 5')
        
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
        
        #radio button 
        choice_variable = IntVar()
        power_frame = Frame(game_window).place(x = 250 , y = 350)
        HP        = Radiobutton(power_frame , text = 'Hp'      , value = 1  , variable = choice_variable , font = 5 , command = play ).place(x = 250 , y = 350)
        Attack    = Radiobutton(power_frame , text = 'Attack'  , value = 2  , variable = choice_variable , font = 5 , command = play  ).place(x = 300 , y = 350)
        Defense   = Radiobutton(power_frame , text = 'Defense' , value = 3  , variable = choice_variable , font = 5 , command = play  ).place(x = 380 , y = 350)
        Speed     = Radiobutton(power_frame , text = 'Speed'   , value = 4  , variable = choice_variable , font = 5 , command = play  ).place(x = 475 , y = 350)
    
        # home button 
        Home_button = Button(game_window , text = 'Back to Home' ,  command = next_game , width = 25).place(x = 50 , y = 400)
        
        # image tile 
        Image_tile = PhotoImage(file ='pokemon.png')
        image_label = Label(game_window , image = Image_tile).place(x = 600, y = 25)
        
        game_window.mainloop()