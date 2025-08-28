'''The example function below keeps track of the opponent's 
history and plays whatever the opponent played two plays ago.
 It is not a very good player so you will need to change the code to pass the challenge.'''

# to tackle this problem i am going to be need some extra argument and mutable Memory-tied dict.
def player(prev_play, bot_history=[], my_history=[], name_history=[], play_order=[{
              "RR": 0,
              "RP": 0,
              "RS": 0,
              "PR": 0,
              "PP": 0,
              "PS": 0,
              "SR": 0,
              "SP": 0,
              "SS": 0,
          }]):
    guess = "R"
    
    # Append the previous play to the bot's history
    bot_history.append(prev_play)

    
    ideal_play = {'R': 'P', 'P': 'S', 'S': 'R'}
    # defining the number of play for other function utilites
    history_len = len(bot_history)

    # properly cleaning the histories for all the bots to be tackled seamlessly
    if history_len > 1000:
        bot_history.clear()
        bot_history.append(prev_play)
        name_history.clear()
        name_history.append(' ') # to prevent error for instant operations after clearing
        my_history.clear()

    # i need to identify the player, so i'll make 3 rounds of opening moves
    if history_len <= 4:
        if history_len == 1:
            my_history.append("R")
            return "R"
        elif history_len == 2:
            my_history.append("P")
            return "P"
        elif history_len == 3:
            my_history.append("S")
            return "S"
        # from the fourth move on we would have identified the bot and use a particular fallback countter strategy
        else:
            bots_code = "".join(bot_history[-3:])
            '''I logically tried all possible bots result for the opening three moves and came up with a 
            generalize response attahced to each bot'''

            loop_to_bot = {'RPP': 'quincy', 'PPP': 'abbey', 'PPS': 'kris'}
            
            if bots_code in loop_to_bot:
                bot = loop_to_bot[bots_code]
            else:
                bot = "mrugesh"
            name_history.append(bot)
    # am not including mrugesh' full code due to nature of its function

    # counter each bot's strategy

    # for quincy a repeated modular arithmetic pattern
    if name_history[-1] == "quincy":
        choices = ["R", "R", "P", "P", "S"]
        next_move = choices[history_len % len(choices)]
        guess = ideal_play[next_move]

    # for mrugesh a simple frequency analysis
    if name_history[-1] == "mrugesh":
        next_move = max(set(my_history[-10:]), key=my_history[-10:].count)
        guess = ideal_play[ideal_play[next_move]]

    # for kris a counter for pattern recognition
    if name_history[-1] == "kris":
        next_move = ideal_play[my_history[-1]]
        guess = ideal_play[next_move]

    # for abbey a conditional frequency analysis
    if name_history[-1] == "abbey":
        my_last_two = "".join(my_history[-2:])
        if len(my_last_two) == 2:
            play_order[0][my_last_two] += 1

        potential_choices = [
            my_history[-1] + "R",
            my_history[-1] + "P",
            my_history[-1] + "S",
        ]

        sub_order = {
            k: play_order[0][k]
            for k in potential_choices if k in play_order[0]
        }

        if sub_order:
            predicted_play = max(sub_order, key=sub_order.get)[1]
            guess = ideal_play[ideal_play[predicted_play]]

    my_history.append(guess)
    return guess
