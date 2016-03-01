class State(object):

    def __init__(self, name):
        self.name = name

    def addActions(self, actions):
        self.actions = actions

    def __repr__(self):
            return self.name

class Search(object):

    def __init__(self, initial_state, goal):
        self.initial_state = initial_state
        self.goal = goal

    def choose_state(self, frontier):
        return frontier.pop(0)

    def search(self):
        frontier = [self.initial_state]
        explored = set()

        while 1:
            if len(frontier) == 0:
                return False

            new_state = self.choose_state(frontier)
            explored.add(new_state)

            if new_state == self.goal:
                return new_state

            #print "Estado escolhido: ",new_state
            #print "Estados da fronteira: ",frontier
            #print "Estados explorados: ",explored

            for state in new_state.actions:
                if state not in explored and state not in frontier:
                    frontier.append(state)

joao_pessoa = State("joao_pessoa")
santa_rita = State("santa_rita")
itabaiana = State("itabaiana")
mamanguape = State("mamanguape")
guarabira = State("guarabira")
areia = State("areia")
campina_grande = State("campina_grande")

soledade = State("soledade")
coxixola = State("coxixola")
picui = State("picui")
monteiro = State("monteiro")
patos = State("patos")
pombal = State("pombal")
catole_do_rocha = State("catole_do_rocha")
sousa = State("sousa")
itaporanga = State("itaporanga")
cajazeiras = State("cajazeias")


joao_pessoa.addActions([santa_rita,campina_grande,itabaiana])
santa_rita.addActions([mamanguape,joao_pessoa])
itabaiana.addActions([campina_grande,joao_pessoa])
mamanguape.addActions([santa_rita,guarabira])
guarabira.addActions([areia,mamanguape])
areia.addActions([guarabira,campina_grande])
campina_grande.addActions([itabaiana,joao_pessoa,areia,soledade,coxixola])

soledade.addActions([campina_grande,picui,patos])
coxixola.addActions([campina_grande,monteiro])
picui.addActions([soledade])
monteiro.addActions([coxixola,itaporanga])
patos.addActions([soledade,pombal,itaporanga])
pombal.addActions([catole_do_rocha,sousa,patos])
catole_do_rocha.addActions([pombal])
sousa.addActions([pombal,cajazeiras])
itaporanga.addActions([monteiro,patos,cajazeiras])
cajazeiras.addActions([sousa,itaporanga])


print Search(joao_pessoa, cajazeiras).search()









