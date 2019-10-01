#!/usr/bin/env python
# -*- coding: utf-8 -*-
# AGT
# Copyright 2019 Ariel H Garcia Traba <ariel.garcia.traba@gmail.com>


print ("https://www.youtube.com/watch?v=eZpSGS7vF5Y")
print ("""
			pip3 install sklearn
			pip3 install bokeh
""")
def limpiar():
    import os
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
options = ["piedra", "tijeras", "papel"]
def search_winner(p1, p2):
    if p1 == p2:
        result = 0
    
    elif p1 == "piedra" and p2 == "tijeras":
        result = 1
    elif p1 == "piedra" and p2 == "papel":
        result = 2
    elif p1 == "tijeras" and p2 == "piedra":
        result = 2
    elif p1 == "tijeras" and p2 == "papel":
        result = 1
    elif p1 == "papel" and p2 == "piedra":
        result = 1
    elif p1 == "papel" and p2 == "tijeras":
        result = 2
    return result

search_winner("papel", "tijeras")

test = [
    ["piedra", "piedra", 0],
    ["piedra", "tijeras", 1],
    ["piedra", "papel", 2]
]

for partida in test:
    print("player1: %s player2: %s Winner: %s Validation: %s" % (
        partida[0], partida[1], search_winner(partida[0], partida[1]), partida[2]
    ))


from random import choice
def get_choice():
	return choice(options)

for i in range(10):
	player1 = get_choice()
	player2 = get_choice()
	print("player1: %s player2: %s Winner: %s " % (
		player1, player2, search_winner(player1, player2)
	))
def str_to_list(option):
    if option=="piedra":
        res = [1,0,0]
    elif option=="tijeras":
        res = [0,1,0]
    else:
        res = [0,0,1]
    return res

data_X = list(map(str_to_list, ["piedra", "tijeras", "papel"]))
data_y = list(map(str_to_list, ["papel", "piedra", "tijeras"]))

print(data_X)
print(data_y)


#-------------Prueba----------------------------
from sklearn.neural_network import MLPClassifier

clf = MLPClassifier(verbose=False, warm_start=True)

model = clf.fit([data_X[0]], [data_y[0]])
print(model)

def play_and_learn(iters=10, debug=False):
    score = {"win": 0, "loose": 0}
    
    data_X = []
    data_y = []
    
    for i in range(iters):
        player1 = get_choice()
        
        predict = model.predict_proba([str_to_list(player1)])[0]
        
        if predict[0] >= 0.95:
            player2 = options[0]
        elif predict[1] >= 0.95:
            player2 = options[1]
        elif predict[2] >= 0.95:
            player2 = options[2]
        else:
            player2 = get_choice()
            
        if debug==True:
            print("Player1: %s Player2 (modelo): %s --> %s" % (player1, predict, player2))
        
        winner = search_winner(player1, player2)
        if debug==True:
            print("Comprobamos: p1 VS p2: %s" % winner)
        
        if winner==2:
            data_X.append(str_to_list(player1))
            data_y.append(str_to_list(player2))
            
            score["win"]+=1
        else:
            score["loose"]+=1
        
    return score, data_X, data_y
    
#-------------Entrenamiento---------------------
score, data_X, data_y = play_and_learn(1, debug=True)
print(data_X)
print(data_y)
print("Score: %s %s %%" % (score, (score["win"]*100/(score["win"]+score["loose"]))))
if len(data_X):
    model = model.partial_fit(data_X, data_y)
i = 0
historic_pct = []
while True:#entrenamiento con 1000 juegos
    i+=1
    score, data_X, data_y = play_and_learn(1000, debug=True)#debug=False)
    pct = (score["win"]*100/(score["win"]+score["loose"]))
    historic_pct.append(pct)
    print("Iter: %s - score: %s %s %%" % (i, score, pct))
    
    if len(data_X):
        model = model.partial_fit(data_X, data_y)
    
    if sum(historic_pct[-9:])==900:# su en la suma de las ultimas 9 es un 100% (900% sumadas) es que aprendio
        break

#-------------Grafica de aprendisaje------------
from bokeh.plotting import figure, show
from bokeh.io import push_notebook, show, output_notebook
output_notebook()
x = range(len(historic_pct))
y = historic_pct

p = figure(
    title="Porcetaje de aprendizaje en cada iteración",
    x_axis_label="Iter", y_axis_label="%", width=900)

p.line(x, y, legend=None, line_width=1)
show(p)
model.predict_proba([str_to_list("piedra")])
