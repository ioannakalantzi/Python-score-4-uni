def pos(x,y):
    """
    Επιστρέφει τις συντεταγμένες του πιονιού πάνω στο ταμπλό, σε μορφή λίστας.

    >>> pos(6,2)
    [6,2]

    """
    return [x,y]
    
def get_row(l):
    """
    Επιστρέφει την γραμμή στην οποία βρίσκεται το πιόνι, παίρνοντας
    το πρώτο αντικείμενο από την λίστα συντεταγμένων της συνάρτησης pos().

    l= pos(6,2)

    >>> get_row(l)
    6

    """

    return l[0]

def get_column(l):
    """
    Επιστρέφει την στήλη στην οποία βρίσκεται το πιόνι, παίρνοντας
    το δεύτερο αντικείμενο από την λίστα συντεταγμένων της συνάρτησης pos().
    
    l= pos(6,2)

    >>> get_column(l)
    2

    """

    return l[1]

def create_board(columns):
    """
    Δημιουργεί το ταμπλό, φτιάχνοντας μια κενή λίστα, 
    στην οποία προσθέτει 8 επιπλέον λίστες (γραμμές του ταμπλό), που 
    περιέχουν πλήθος αντικειμένων ίσο με τον αριθμό στηλών που εισήγαγε ο παίκτης.

    >>> create_board(6)
    [
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    ]
    """

    list = []
    for i in range(8):
        temp_list = []
        for j in range(columns + 1):
            temp_list.append(0)
        list.append(temp_list)
    return list

def input_column(mes):
    """
    Δέχεται την επιλογή στήλης του παίκτη αφού εμφανίσει το κατάλληλο μήνυμα, και την μειώνει κατά μία μονάδα, 
    έτσι ώστε όταν χρησιμοποιηθεί ως δείκτης σε λίστα, να δώσει το επιθυμητό αποτέλεσμα.

    >>> input_column(5)
    4

    """
    column = int(input(mes))
    column -= 1
    return column
  
def board(list):
    def check_value(periptwsh, term = None):
        """ 
        Δέχεται την επιλογή στήλης του παίκτη, μόνο εάν είναι λανθασμένη, και ελέγχει σε ποια από τις 
        2 περιπτώσεις λάθους ανήκει, αφού εμφανίσει το κατάλληλο ενημερωτικό μήνυμα.
        Έπειτα ζητάει εκ νέου την τιμή μέσω της συνάρτησης give_correct_value().
        Περιπτώσεις :
        
        1. Η στήλη που επέλεξε ο παίκτης για να τοποθετήσει το πιόνι του είναι γεμάτη.
        2. Η στήλη που επέλεξε ο παίκτης για να τοποθετήσει το πιόνι του είναι εκτός των ορίων του ταμπλό.

        """
        if periptwsh == 1:
            prompt_mess = ["Διάλεξε στήλη: ","Η στήλη είναι γεμάτη, διάλεξε άλλη!"]
            value = give_correct_value(is_full,prompt_mess,(list,),input_column)
            return value
        else:
            prompt_mess = ["Διάλεξε στήλη: ","Πρόσεχε! Εκτός Ταμπλό."]
            value = give_correct_value(not_inside_border, prompt_mess,(list,), input_column)

    return check_value

def give_correct_value(term, message, vars = None, input_method = None):
    """
    Πραγματοποιεί έλεγχο εισαγωγής τιμής!
    Σε περίπτωση που ο χρήστης δώσει λάθος τιμή,  ζητάει επαναληπτικά νέα τιμή, 
    μέχρι να δωθεί κάποια αποδεκτή.

    """
    print(message[1])
    while True:
        value = input_column(message[0])
        bool = term(get_row(vars),value)
        if bool == True:
            print(message[1])
        else:
            return value

def not_inside_border(board, choice):
    """
    Δέχεται την επιλογή στήλης του παίκτη, και εάν είναι μέσα στα όρια του ταμπλό
    επιστρέφει False, αντιθέτως, εάν είναι εκτός των ορίων, επιστρέφει True.
    Η συνάρτηση είναι βοηθητική της give_correct_value(). 

    >>> not_inside_border(lista, 4)
    False
    >>> not_inside_border(lista, 11)
    True
    
    """
    if choice < 0:
        return True
    if not(len(board[0]) <= choice):
        return False
    return True


def is_full(board, choice):
    """
    Η συνάρτηση ελέγχει εάν είναι γεμάτη η στήλη που επέλεξε ο παίχτης, 
    ελέγχοντας την πρώτη γραμμή από πάνω.
    Εάν είναι γεμάτη επιστρέφει True, εάν όχι, επιστρέφει False.

    lista = [
    [0,"O",0,0,0,0],
    ["O","O",0,0,0,0],
    ["O","X",0,0,0,0],
    ["O","O",0,0,0,0],
    ["O",,"O",0,0,0],
    ["X","X",0,0,0,0],
    ["X","X",0,0,0,0],
    ["O","X","X","O",0,0],
    ]
    
    >>> is_full(lista, 1)
    False

    >>> is_full(lista, 2)
    True

    """
    if board[0][choice] == 0:
        return False
    return True

def board_is_full(board,limit_columns):
    """
    Ελέγχει εάν το ταμπλό είναι γεμάτο, τρέχοντας την συνάρτηση is_full(),
    για όλες τις στήλες του ταμπλό.

    lista = [
    [0,"O",0,0,0,0],
    ["O","O",0,0,0,0],
    ["O","X",0,0,0,0],
    ["O","O",0,0,0,0],
    ["O",,"O",0,0,0],
    ["X","X",0,0,0,0],
    ["X","X",0,0,0,0],
    ["O","X","X","O",0,0],
    ]
    
    >>> board_is_full(lista, 6)
    False

    """

    for i in range(limit_columns):
        if is_full(board, i) == False:
            return False
    return True

def vertical_run(board, choice):
    """
    Ψάχνει να βρει την τοποθεσία του τελευταίου πιονιού της λίστας.
    Επιστρέφει ένα tuple με τα cords του της τοποθέσεις του νέου πιονιού.

    lista = [
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,"X",0,0],
        [0,0,"O",0,0],
    ]
    >>> vertical_run(lista, 3)
    (3,7)

    """
    i = 0
    while i <= 7:
        if board[i][choice] != 0:
            return ((i-1,choice))
        i += 1
    return (len(board)-1, choice)

def add_sym(board, pos, sym):
    """
    Τοποθετεί στο ταμπλό το νέο πιόνι.

    lista = [
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
    ]

    >>> add_sym(lista, [7,0], "O")
    [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    ["O",0,0,0,0],
    ]

    """
    board[get_row(pos)][get_column(pos)] = sym

def perform_move(board, column, sym):
    """
    Με την βοήθεια των κατάλληλων συναρτήσεων, βρίσκει την γραμμή και την στήλη του νέου πιονιού που 
    τοποθετήθηκε και επιστρέφει μια λίστα με τις συντεταγμένες του.
    
    lista = [
    [0,0,0,0,0,0],
    ["O",0,0,0,0,0],
    ["O",0,0,0,0,0],
    ["O",0,0,0,0,0],
    ["O",0,0,0,0,0],
    ["X",0,0,0,0,0],
    ["X",0,0,0,0,0],
    ["O",0,0,0,0,0],
    ]

    >>> perform_move(lista, 0, "O")
    [0,0]
    
    """
    set_pos = vertical_run(board,column)
    add_sym(board,set_pos,sym)
    return pos(get_row(set_pos),get_column(set_pos))

def search_horizontally(board,limit_column, cords, sym):
    """
    Η συνάρτηση ελέγχει το ταμπλό ανά γραμμή, ξεκινώντας από την πρώτη γραμμή από πάνω που περιέχει
    έστω και ένα πιόνι. Υπάρχει μετρητής που περιέχει τον αριθμό των πιονιών ίδιου τύπου που βρίσκονται
    το ένα δίπλα στο άλλο. Εάν ο μετρητής φτάσει στο 4, σημαίνει ότι υπάρχει νικητήριο πιόνι, και ελέγχει
    για έξτρα πιόνια ίδιου τύπου στις διπλανές θέσεις. Εάν ο μετρητής<4 και το επόμενο πιόνι είναι 
    αντίθετου τύπου ή 0, ο μετρητής μηδενίζεται.

    lista = [
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    ["O",0,0,0,0,0],
    ["O",0,0,0,0,0],
    ["O",0,0,0,0,0],
    ["X",0,0,0,0,0],
    ["X",0,0,0,0,0],
    ["X","X","X","X",0,0],
    ]

    >>> search_horizontally(lista, 6, [7,2], "X")
    [[7,0],[7,1],[7,2],[7,3]]

    """
    symbols = ["O","X"]
    if symbols[0] == sym:
        target_sym = sym
    else:
        target_sym = symbols[1]
    element_list = []
    counter = 0
    column = 0
    row = get_row(cords)
    flag = False
    while column <= limit_column and not flag:
        element = board[row][column]
        if element == target_sym:
            counter += 1
            element_list.append(pos(row,column))
        else:
            counter = 0
            element_list = []
        if counter >= 4:
            if column + 1 <= limit_column:
                if board[row][column + 1] == target_sym:
                    flag = False
                else:
                    flag = True
        column += 1
    return element_list

def search_vertically(board, cords, sym):
    """
    Η συνάρτηση ελέγχει την στήλη που τοποθετήθηκε το τελευταίο πίονι, ξεκινώντας από την γραμμή που τοποθετήθηκε το τελευταίο πιόνι. 
    Υπάρχει μετρητής που περιέχει τον αριθμό των πιονιών ίδιου τύπου που βρίσκονται
    το ένα κάτω από το άλλο. Εάν ο μετρητής φτάσει στο 4, σημαίνει ότι υπάρχει νικητήριο πιόνι, και ελέγχει
    για έξτρα πιόνια ίδιου τύπου στις από κάτω/πάνω θέσεις. Εάν ο μετρητής<4 και το επόμενο πιόνι είναι 
    αντίθετου τύπου ή 0 , ο μετρητής μηδενίζεται.
    
    lista = [
    [0,0,0,0,0,0],
    ["O",0,0,0,0,0],
    ["O",0,0,0,0,0],
    ["O",0,0,0,0,0],
    ["O",0,0,0,0,0],
    ["X",0,0,0,0,0],
    ["X",0,0,0,0,0],
    ["O","X","X","O",0,0],
    ]

    >>> search_vertically(lista, [1,0], "O")
    [[1,0],[2,0],[3,0],[4,0]]
    
    """
    symbols = ["O","X"]
    if symbols[0] == sym:
        target_sym = sym
    else:
        target_sym = symbols[1]
    element_list = []
    counter = 0
    row = get_row(cords)
    column = get_column(cords)
    flag = False
    while row < 8 and not flag:
        element = board[row][column]
        if element == target_sym:
            counter += 1
            element_list.append(pos(row,column))
        else:
            counter = 0
            element_list = []
            flag = True
        if counter >= 4:
            if row + 1 <= 7:
                if board[row + 1][column] == target_sym:
                    flag = False
                else:
                    flag = True
        row += 1
    return element_list

def search_diagonally(board, limit_column, cords, sym):
    """
    Η συνάρτηση παίρνει ως σημείο αναφοράς τις συντεταγμένες του τελευταίου πιονιού που τοποθετήθηκε στο ταμπλό.
    Ελέγχει με σειρά: πάνω αριστερά, κάτω δεξία, πάνω δεξία, και κάτω αριστερά, εάν υπάρχουν πιόνια ίδιου τύπου.
    Εάν υπάρχουν, προσθέτονται σε ξεχωριστές λίστες σύμφωνα με την διαγώνιο οι οποίες εμφανίζονται, εάν πληρούν 
    τα κριτήρια των κανόνων (το μήκος να είναι μεγαλύτερο ή ίσο του 4) όπου και υπάρχει νικητήριο πιόνι.

     lista = [
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    ["O",0,0,0,0,"O"],
    ["O",0,0,0,"O","X"],
    ["O",0,0,"O","O","O"],
    ["X",0,"O","X","O","O"],
    ["X","O","X","O","X","X"],
    ["O","X","X","X","O","O"],
    ]

    >>> search_diagonally(lista, 6, [2,5], "O")
    [[2,5],[3,4],[4,3],[5,2],[6,1],[7,0]]

    """

    symbols = ["O","X"]
    if symbols[0] == sym:
        target_sym = sym
    else:
        target_sym = symbols[1]

    #First Element pos
    row = get_row(cords)
    column = get_column(cords)


    #diadikasia eureshs max left up
    counter_left_right = 1
    element_list_left_right = []
    obstacle_present = False
    i = 1
    while not obstacle_present:
        next_row, next_column = row - i, column - i
        if next_row >= 0 and next_column >= 0:               #an einai mesa sta oria,mas endiaferei mono to left orio
            element = board[next_row][next_column]
            if element == target_sym:
                counter_left_right += 1
                element_list_left_right.append(pos(next_row,next_column))
            else:
                obstacle_present = True
        else:
            obstacle_present = True
        i += 1
    #diadikasia eureshs min right down
    obstacle_present = False
    i = 1
    while not obstacle_present:
        next_row, next_column = row + i, column + i
        if next_row <= 7 and next_column <= limit_column:
            element = board[next_row][next_column]
            if element == target_sym:
                counter_left_right += 1
                element_list_left_right.append(pos(next_row,next_column))
            else:
                obstacle_present = True
        else:
            obstacle_present = True
        i += 1

    #diadikasia eureshs max right up
    element_list_right_left = []
    counter_right_left = 1
    obstacle_present = False
    i = 1
    while not obstacle_present:
        next_row, next_column = row - i, column + i
        if next_row >= 0 and next_column <= limit_column:
            element = board[next_row][next_column]
            if element == target_sym:
                counter_right_left += 1
                element_list_right_left.append(pos(next_row,next_column))
            else:
                obstacle_present = True
        else:
            obstacle_present = True
        i += 1

    #diadikasia eureshs min left down
    obstacle_present = False
    i = 1
    while not obstacle_present:
        next_row, next_column = row + i, column - i
        if next_row <= 7 and next_column >= 0:
            element = board[next_row][next_column]
            if element == target_sym:
                counter_right_left += 1
                element_list_right_left.append(pos(next_row,next_column))
            else:
                obstacle_present = True
        else:
            obstacle_present = True
        i += 1
        

    if counter_left_right < 4 and counter_right_left < 4:
        return []
    elif counter_left_right >= 4 and counter_right_left < 4:
        return element_list_left_right + [cords]
    elif counter_left_right < 4 and counter_right_left >= 4:
        return element_list_right_left + [cords]
    else:
        return element_list_left_right + element_list_right_left + [cords]



def check_for_one_cond(list):
    """
    Δέχεται την λίστα από τις συναρτήσεις search_horizontally(), search_vertically(), και search_diagonally(), 
    και εάν το μήκος της είναι μεγαλύτερο η ίσο του 4, επιστρέφει True, άρα υπάρχει νικητήριο πιόνι,  αλλιώς επιστρέφει False. 

    list = [[7,0], [7,1], [7,2], [7,3]]

    >>> check_for_one_cond(list)
    True

    """
    if len(list) >= 4:
        return True
    return False

def check_win_cond(board, limit_column, cords, sym):
    """
    Ελέγχει εάν υπάρχει κάποια λίστα (οριζόντια, κάθετα ή διαγώνια) που να επιστρέφει True μέσω της συνάρτησης 
    check_for_one_cond(), άρα που να είναι νικητήρια, και την επιστρέφει. Εάν δεν υπάρχει τέτοια λίστα σε αυτόν τον γύρο,
    επιστρέφει μία κενή λίστα.

    lista = [
    [0,0,0,0,0,0],
    ["O",0,0,0,0,0],
    ["O",0,0,0,0,0],
    ["O",0,0,0,0,0],
    ["O",0,0,0,0,0],
    ["X",0,0,0,0,0],
    ["X",0,0,0,0,0],
    ["O","X","X","O",0,0],
    ]

    >>> check_win_cond(lista, 6, [1,0], "O")
    [[1,0],[2,0],[3,0],[4,0]]

    """

    #Horizontal
    hor_res_list = search_horizontally(board, limit_column, cords, sym)
    hor_res = check_for_one_cond(hor_res_list)
    
    #Vertical
    vert_res_list = search_vertically(board, cords, sym)
    vert_res = check_for_one_cond(vert_res_list)
        
    #Diagonal
    diag_res_list = search_diagonally(board, limit_column, cords, sym)
    diag_res = check_for_one_cond(diag_res_list)

    if hor_res == True:
        return hor_res_list
    elif vert_res == True:
        return vert_res_list
    elif diag_res == True:
        return diag_res_list
    else:
        return []

def mark_winning_symbols(board,data):
    """
    Αντικαθιστά τα στοιχεία της νικητήριας λίστας με το σύμβολο "*" πάνω στο ταμπλό.

    lista = [
    [0,0,0,0,0,0],
    ["O",0,0,0,0,0],
    ["O",0,0,0,0,0],
    ["O",0,0,0,0,0],
    ["O",0,0,0,0,0],
    ["X",0,0,0,0,0],
    ["X",0,0,0,0,0],
    ["O","X","X","O",0,0],
    ]

    data = [[1,0],[2,0],[3,0],[4,0]]

    >>> mark_winning_symbols(lista, data)
    [
    [0,0,0,0,0,0],
    ["*",0,0,0,0,0],
    ["*",0,0,0,0,0],
    ["*",0,0,0,0,0],
    ["*",0,0,0,0,0],
    ["X",0,0,0,0,0],
    ["X",0,0,0,0,0],
    ["O","X","X","O",0,0],
    ]
    """

    for cords in data:
        add_sym(board,cords,"*")

def drop_down(board,data):
    """
    Πραγματοποιεί την αφαίρεση των νικητήριων πιονιών από το ταμπλό
    και την ολίσθηση προς τα κάτω των πιονιών που στοιβάζονται πάνω
    από τα αφαιρούμενα πιόνια.

    lista = [
    [0,0,0,0,0,0],
    [0,0,0,0,0,"X"],
    ["O",0,0,0,0,"*"],
    ["O",0,0,0,"*","X"],
    ["O",0,"X","*","O","O"],
    ["X","X","*","X","O","O"],
    ["X","*","X","O","X","X"],
    ["*","X","X","X","O","O"],
    ]

    list = [[2,5],[3,4],[4,3],[5,2],[6,1],[7,0]]

    >>> drop_down(lista, list)
    [
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,"X"],
    ["O",0,0,0,0,"X"],
    ["O",0,0,0,"O","O"],
    ["O",0,"X","X","O","O"],
    ["X","X","X","O","X","X"],
    ["X","X","X","X","O","O"],
    ]
    """

    same_column = False
    if data[0][1] == data[1][1]:
        same_column = True

    if not same_column:
        for cords in data:
            row = get_row(cords)
            column = get_column(cords)

            #sthn column sthlh
            last_element = vertical_run(board, column)
            last_element = get_row(last_element) + 1 
            current = 0
            prev = 1
                    
            #metatheseis
            while row - prev >= last_element:
                board[row - current][column],board[row - prev][column] = board[row - prev][column],board[row - current][column]
                current += 1
                prev += 1
            board[row-current][column] = 0
    else:
        for cords in data:
            add_sym(board,cords,0)

def to_file(file_name, columns , data, scores):
    """
    Καλείται μετά την επιλογή "s" του παίκτη, και αποθηκεύει την κατάσταση του παιχνιδιού σε
    αρχείο CSV, όπου κάθε γραμμή του αρχείου θα αντιστοιχεί
    σε μια γραμμή του ταμπλώ του παιχνιδιού, ξεκινώντας από τη γραμμή Α. Η κωδικοποίηση
    κάθε γραμμής γίνεται αποθηκεύοντας 0 (μηδέν) για τα κενά κελιά, 1 για τα κελιά που υπάρχει
    το σύμβολο "O" του παίκτη 1, και 2 για τα κελιά που υπάρχει το σύμβολο "X" του παίκτη 2.
    Η τελευταία γραμμή του αρχείου καταγράφει το σκορ του κάθε παίκτη. 

    """
    
    f = open(file_name,"w")
    for i in range(8): #for the rows
        for j in range(columns+1): #for the columns
            element = data[i][j]
            if element == "O":
                element = 1
            if element == "X":
                element = 2
            if j == columns:
                f.write(str(element))
            else:
                f.write(str(element)+",")
        f.write("\n")
    f.write(str(scores[0]) + "," + str(scores[1]))
    f.close()

def from_file(name):
    """
    Ανακτά το ταμπλό από το αποθηκευμένο αρχείο που επιλέγει ο παίκτης και το επιστρέφει σε μορφή λίστας,
    αντικαθιστώντας το 1 με το σύμβολο "Ο", και το 2 με το σύμβολο "Χ".

    """

    f = open(name,"r")
    data = [line.strip().split(",") for line in f]
    for i in range(len(data)-1):
        for j in range(len(data[i])):
            element = data[i][j]
            if element == "1":
                element = "O"
            if element == "2":
                element = "X"
            if element == "0":
                element = 0
            data[i][j] = element
    f.close()
    return data

def print_board(data,columns):
    """
    Δημιουργεί το ταμπλό σύμφωνα με την επιλογή στηλών του παίκτη.
    Τοποθετεί τους άξονες των γραμμών (A-H) κάθετα, και των στηλών (1-επιλογή) οριζόντια,
    διαχωρίζοντάς τες με τις κατάλληλες παύλες-σύμβολα. Επίσης, τοποθετεί τα πιόνια των παικτών
    ανάλογα με την κατάσταση του παιχνιδιού, παίρνοντας τις συντεταγμένες τους από την λίστα data.

    data = [
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,"Χ",0,0,0,0,0],
    [0,"Ο",0,"Ο","Χ",0,0],
    ]
    >>> print_board(data, 7)

        1     2     3     4     5     6     7 
    -+-----+-----+-----+-----+-----+-----+-----+
    A|     |     |     |     |     |     |     |
    B|     |     |     |     |     |     |     |
    C|     |     |     |     |     |     |     |
    D|     |     |     |     |     |     |     |
    E|     |     |     |     |     |     |     |
    F|     |     |     |     |     |     |     |
    G|     |    X|     |     |     |     |     |
    H|     |    O|     |    O|    X|     |     |
    -+-----+-----+-----+-----+-----+-----+-----+
    """

    letters = ["A","B","C","D","E","F","G","H"]
    space4 = "    "
    columns = columns + 1
    #print numbers
    for i in range(1,columns+1):
        print(space4 + str(i),end=" ")
    print()

    #top border
    print("-+-----+",end="")
    for i in range(columns-1):
        print("-----+",end="")
    print()

    for i in range(8):
        print(letters[i]+"|",end="")
        for j in range(columns):
            if data[i][j] == 0:
                print(space4 + " |",end="")
            else:
                print(space4 + data[i][j]+"|",end="")
        print()

    #down border
    print("-+-----+",end="")
    for i in range(columns-1):
        print("-----+",end="")
    print()