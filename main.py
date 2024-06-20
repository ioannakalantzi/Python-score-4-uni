from functions import *
import time

quit = False
pl1_sym = "O"
pl2_sym = "X"
score_pl1 = 0
score_pl2 = 0

#New or old game
print("Καλωσήλθατε στο παιχνίδι!")
game_status = input("Επιθυμείτε νέο παιχνίδι (Ν) ή φόρτωση του παιχνιδιού από αρχείο (S); ")
if game_status == "S":
    file_name = input("Δώσε όνομα αρχείου: ")
    lista = from_file(file_name)
    columns = len(lista[0]) -1 
    scores = lista.pop()
    score_pl1 = int(scores[0])
    score_pl2 = int(scores[1])

else:
    columns = input_column("Δώστε αριθμό στηλών παιχνιδιού (5-10) :")
    while columns < 4 or columns > 9:
        print("Το παιχνίδι δεν μπορεί να πραγματοποιηθεί με τον επιλεγμένο αριθμό στηλών.")
        columns = input_column("Δώστε αριθμό στηλών παιχνιδιού (5-10) :")
    #Creation of board
    lista = create_board(columns)

check_for_wrong_value = board(lista)
    

while not quit :
    #emfanisei tablo
    print_board(lista,columns)

    #epilogh sthlhs 1os paixths
    choice_pl1 = input_column("Παίκτης 1: Επέλεξε στήλη για το πιόνι: ")
    if not_inside_border(lista,choice_pl1):
        choice_pl1 = check_for_wrong_value(2, not_inside_border)

    #Code for move
    if not is_full(lista,choice_pl1):
        cords = perform_move(lista,choice_pl1,pl1_sym)
    else:
        choice_pl1 = check_for_wrong_value(1,is_full)
        cords = perform_move(lista,choice_pl1,pl1_sym)
    
    #emfanisei tablo
    print_board(lista,columns)
    
    #Code for Searches

    Winning_posses = check_win_cond(lista,columns,cords,pl1_sym)
    if check_for_one_cond(Winning_posses) == True:
        time.sleep(2)
        mark_winning_symbols(lista,Winning_posses)

        #emfanisei tablo
        print_board(lista,columns)
        time.sleep(2)
        #olis8ish
        drop_down(lista,Winning_posses)
        
        #emfanisei tablo
        print_board(lista,columns)

        score_pl1 += len(Winning_posses)
    
    if board_is_full(lista,columns):
        if score_pl1 > score_pl2:
            print("Παίκτη 1 νίκησες!")
        elif score_pl1 < score_pl2:
            print("Παίκτη 2 νίκησες!")
        else:
            print("Iσοπαλία")
        quit = True
        print("H Βαθμολογία")
        print("Παίκτης 1: ",score_pl1,end="        ")
        print("Παίκτης 2: ",score_pl2)
        continue


    #epilogh sthlhs 2os paixths
    choice_pl2 = input_column("Παίκτης 2: Επέλεξε στήλη για το πιόνι: ")
    if not_inside_border(lista,choice_pl2):
        choice_pl2 = check_for_wrong_value(2, not_inside_border)

    #Code for move
    if not is_full(lista,choice_pl2):
        cords = perform_move(lista,choice_pl2,pl2_sym)
    else:
        choice_pl2 = check_for_wrong_value(1,is_full)
        cords = perform_move(lista,choice_pl2,pl2_sym)
    
    #emfanisei tablo
    print_board(lista,columns)
        
    #Code for Searches
    
    Winning_posses = check_win_cond(lista,columns,cords,pl2_sym)
    if check_for_one_cond(Winning_posses) == True:
        time.sleep(2)
        mark_winning_symbols(lista,Winning_posses)

        #emfanisei tablo
        print_board(lista,columns)
        time.sleep(2)
        #olis8ish
        drop_down(lista,Winning_posses)

        #emfanisei tablo
        print_board(lista,columns)

        score_pl2 += len(Winning_posses)

    
    if board_is_full(lista,columns):
        if score_pl1 > score_pl2:
            print("Παίκτη 1 νίκησες!")
        elif score_pl1 < score_pl2:
            print("Παίκτη 2 νίκησες!")
        else:
            print("Iσοπαλία")
        quit = True
        print("H Βαθμολογία")
        print("Παίκτης 1: ",score_pl1,end="        ")
        print("Παίκτης 2: ",score_pl2)

        
    print("Πατήστε oποιoδήποτε πλήκτρο για να συνεχίσετε.")
    exit = input("Για παύση του παιχνιδιού και αποθήκευση σε αρχείο επιλέξτε΄s': ")
    if exit == "s":
        quit = True
        file_name = input("Δώστε όνομα αρχείου:")
        to_file(file_name, columns, lista,[score_pl1,score_pl2])
        print("To παιχνίδι αποθηκεύτηκε!")
