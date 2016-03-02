class State(object):

    def __init__(self, name):
        self.name = name

    def add_actions(self, actions):
        self.actions = actions

    def __repr__(self):
            return self.name


class NodeSearch(object):

    def __init__(self, state):
        self.state = state

    def set_parent(self, parent):
        self.parent = parent

    def __repr__(self):
        return self.state.name


class Search(object):

    def __init__(self, initial_state, goal):
        self.initial_state = NodeSearch(initial_state)
        self.initial_state.parent = None
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
            explored.add(new_state.state)

            if new_state.state == self.goal:
                return new_state

            #print "Estado escolhido: ",new_state
            #print "Estados da fronteira: ",frontier
            #print "Estados explorados: ",explored

            for state in new_state.state.actions:
                if state not in explored:
                    aux_state = NodeSearch(state)
                    frontier.append(aux_state)
                    aux_state.set_parent(new_state)

joao_pessoa = State("joao pessoa")
itabaiana = State("itabaiana")
campina_grande = State("campina grande")
santa_rita = State("santa rita")
mamanguape = State("mamanguape")
guarabira = State("guarabira")
areia = State("areia")
coxixola = State("coxixola")
soledade = State("soledade")
picui = State("picui")
monteiro = State("monteiro")
patos = State("patos")
pombal = State("pombal")
itaporanga = State("itaporanga")
catole_do_rocha = State("catole do rocha")
sousa = State("sousa")
cajazeiras = State("cajazeiras")

joao_pessoa.add_actions([itabaiana, campina_grande, santa_rita])
itabaiana.add_actions([joao_pessoa, campina_grande])
santa_rita.add_actions([joao_pessoa, mamanguape])
mamanguape.add_actions([santa_rita, guarabira])
guarabira.add_actions([mamanguape, areia])
areia.add_actions([guarabira, campina_grande])
campina_grande.add_actions([itabaiana, areia, soledade, coxixola, joao_pessoa])

soledade.add_actions([campina_grande, patos, picui])
picui.add_actions([soledade])
coxixola.add_actions([campina_grande, monteiro])
patos.add_actions([soledade, itaporanga, pombal])
monteiro.add_actions([coxixola, itaporanga])
catole_do_rocha.add_actions([pombal])
pombal.add_actions([patos, catole_do_rocha, sousa])
itaporanga.add_actions([patos, cajazeiras, monteiro])
sousa.add_actions([pombal, cajazeiras])
cajazeiras.add_actions([sousa, itaporanga])


search = Search(joao_pessoa, cajazeiras)
result = search.search();

def print_path(state):
    state_parent = state.parent
    print state

    while state_parent:
        print state_parent
        state_parent = state_parent.parent


print_path(result)








