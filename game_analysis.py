import pandas as pd

def OpeningMove(df, side):
   move_rank = {
    "e5": 1,
    "c5": 2,
    "e6": 3,
    "c6": 4,
    "d5": 5,
    "g6": 6,
    "d6": 7,
    "Nf6": 8,
    "b6": 9,
    "f5": 10,
    "g5": 11,
    "Nc6": 12,
    "b5": 13,
    "a6": 14,
    "h6": 15,
    "Na6": 16,
    "Nh6": 17,
    "h5": 18,
    "a5": 19,
    "Na4": 20,
    "e4": 1,
    "d4": 2,
    "Nf3": 3,
    "c4": 4,
    "g3": 5,
    "f4": 6,
    "b3": 7,
    "Nc3": 8,
    "e3": 9,
    "d3": 10,
    "g4": 11,
    "h3": 12,
    "a4": 13,
    "h4": 14,
    "b4": 15,
    "a3": 16,
    "Nh3": 17,
    "f3": 18,
    "Na3": 19,
    "c3": 20
    }
   move = df[side].iloc[0]
   rank = move_rank[move]
   return rank

def Captures(df, side):
  dfa = df["White"]
  dfb = df["Black"]
  c = 0
  d = 0
  for i in dfa:
    if "x" in i:
      c = c + 1
  for i in dfb:
    if "x" in i:
      d = d + 1
  if (side == "Black"):
    analyze = d
    opp = c
  else:
    analyze = c
    opp = d

  if (analyze > opp):
    analyze = analyze + 0.5 * (analyze - opp)
  elif (opp > analyze):
     analyze = analyze - 0.5 * (analyze - opp)
     if (analyze < 0):
        analyze = 0
  return analyze/len(dfb)
     
def Endgame(df, side):
  dfa = df[side]
  c = 0
  d = 0
  for i in range(len(dfa)):
    if "x" in dfa.iloc[i]:
      c = c + 1
    if (c == 9):
      d = i
      break;
  if (d == 0):
    return 0
  else:
    return 1 - i/len(dfa)
  
def Castling(df, side):
    dfa = df[side]
    for i in range(len(dfa)):
        if (dfa.iloc[i].strip() == "O-O-O"):
            return -1
        elif (dfa.iloc[i].strip() == "O-O"):
            return 1
    return 0

def Major_Pieces(df, side):
  dfa = df[side]
  c = 0
  for i in range(len(dfa)):
    if "Q" in dfa.iloc[i]:
      c = c + 1
    if "R" in dfa.iloc[i]:
      c = c + 1
  return c/len(dfa)

def Minor_Pieces(df, side):
  dfa = df[side]
  c = 0
  for i in range(len(dfa)):
    if "N" in dfa.iloc[i]:
      c = c + 1
    if "B" in dfa.iloc[i]:
      c = c + 1
  return c/len(dfa)

def Pawn(df, side):
  dfa = df[side]
  c = 0
  for i in range(len(dfa)):
    if (("N" not in dfa.iloc[i]) & ("B" not in dfa.iloc[i]) & ("K" not in dfa.iloc[i]) & ("Q" not in dfa.iloc[i]) & ("R" not in dfa.iloc[i])):
      c = c+ 1
  return c/(len(dfa))

def Middlegame(df, side):
  dfa = df[side]
  c = 0
  d = 0
  for i in range(len(dfa)):
    if "x" in dfa.iloc[i]:
      c = c + 1
    if (c == 2):
      d = i
      break;
  begin = d


  f = 0
  g = 0
  for j in range(len(dfa)):
    if "x" in dfa.iloc[j]:
      f = f + 1
    if (f == 9):
      g = j
      break;
  if (g == 0):
    end = len(dfa)
  else:
    end = g

  return (end - begin)/len(dfa)

def GameData(df_data, df, side, player):
  b = Captures(df, side)
  c = Endgame(df, side)
  e = Middlegame(df, side)
  f = Major_Pieces(df, side)
  g = Minor_Pieces(df, side)
  h = Pawn(df, side)

  data = []
  d = {"Player":player,"Captures":b, "Endgame":c, "Middlegame":e, "Major Pieces":f, "Minor Pieces":g, "Pawn":h}
  data.append(d)
  df_game = pd.DataFrame(data)
  df_data = pd.concat([df_game, df_data], ignore_index=True)
  return df_data

def UserGM(df_data, df, side):
  b = Captures(df, side)
  c = Endgame(df, side)
  e = Middlegame(df, side)
  f = Major_Pieces(df, side)
  g = Minor_Pieces(df, side)
  h = Pawn(df, side)

  data = []
  d = {"Captures":b, "Endgame":c, "Middlegame":e, "Major Pieces":f, "Minor Pieces":g, "Pawn":h}
  data.append(d)
  df_game = pd.DataFrame(data)
  df_data = pd.concat([df_game, df_data], ignore_index=True)
  return df_data