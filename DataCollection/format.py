import pandas as pd
import re

def MovesListData(moves):
    simplified_moves = re.sub(r'{.*?}', '', moves)
    cleaned_moves = re.sub(r"\(.*?\)","", moves)
    cleaned_moves = cleaned_moves.replace("..", "")
    final_moves = cleaned_moves.replace("?", "")
    final_moves = final_moves.replace("!", "")
    return final_moves

def MovesList(moves):
    simplified_moves = re.sub(r'{.*?}', '', moves)
    idx = simplified_moves.index('.org"]')
    moves = simplified_moves[idx + 8:]
    cleaned_moves = re.sub(r"\(.*?\)","", moves)
    cleaned_moves = cleaned_moves.replace("..", "")
    final_moves = cleaned_moves.replace("?", "")
    final_moves = final_moves.replace("!", "")
    return final_moves

def ListOfMoves(final_moves):
    list = final_moves.split(" ")
    for i in range(len(list)):
        list[i] = list[i].strip().split(' ')[-1]
        
    cleaned_list = []

    for i in range(0, len(list)):
        if ("O-O" in list[i]):
            cleaned_list.append(list[i])
            continue
        if ((list[i] == " ") | (list[i] == '') | ("." in list[i]) | ("-" in list[i])):
            continue
        else:
            cleaned_list.append(list[i])
    
    return cleaned_list

def MovesToDf(cleaned_list):
    iter = []
    for i in range(len(cleaned_list)):
        if (i % 2 == 0):
            iter.append(i)
    
    data = []
    for i in iter:
        if (i + 1 < len(cleaned_list)):
            d = {"White": cleaned_list[i], "Black": cleaned_list[i + 1]}
        else:
            d = {"White": cleaned_list[i], "Black": ""}
        data.append(d)
    
    df = pd.DataFrame(data)
    return df

def PGNtoDF(moves):
    final_moves = MovesList(moves)
    list = ListOfMoves(final_moves)
    df = MovesToDf(list)
    return df

def PGNtoData(moves):
    final_moves = MovesListData(moves)
    list = ListOfMoves(final_moves)
    df = MovesToDf(list)
    return df