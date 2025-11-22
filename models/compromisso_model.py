compromissos = []
contador_id = 1

def adicionar_compromisso(titulo, data, hora, descricao):
    global contador_id
    compromisso = {
        'id': contador_id,
        'titulo': titulo,
        'data': data,
        'hora': hora,
        'descricao': descricao,
        'concluido': False     
    }
    compromissos.append(compromisso)
    contador_id += 1

def listar_compromissos():
    return compromissos

def buscar_compromisso(id):
    for c in compromissos:
        if c['id'] == id:
            return c
    return None

def editar_compromisso(id, titulo, data, hora, descricao):
    compromisso = buscar_compromisso(id)
    if compromisso:
        compromisso['titulo'] = titulo
        compromisso['data'] = data
        compromisso['hora'] = hora
        compromisso['descricao'] = descricao

def excluir_compromisso(id):
    global compromissos
    compromissos = [c for c in compromissos if c['id'] != id]

def marcar_concluido(id):
    compromisso = buscar_compromisso(id)
    if compromisso:
        compromisso['concluido'] = True

def desmarcar_concluido(id):
    compromisso = buscar_compromisso(id)
    if compromisso:
        compromisso['concluido'] = False
