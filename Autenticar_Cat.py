from Catalogo_USER import PACIENTES, ADMINS, DOUTORES


def autenticar(role, username, password):
    """
    Retorna um dicionário com dados do usuário se autenticado, ou None.
    role: "Paciente", "Admin", "Doutor"
    """
    username = username.strip()
    if role == "Paciente":
        source = PACIENTES
    elif role == "Admin":
        source = ADMINS
    elif role == "Doutor":
        source = DOUTORES
    else:
        return None

    for entry in source:
        if entry.get("username") == username and entry.get("password") == password:
            # devolve cópia sem a senha por segurança
            result = {k: v for k, v in entry.items() if k != "password"}
            return result
    return None

def criar_conta(role, username, password, extra=None):
    """
    Função simples para adicionar conta nas listas em memória.
    Retorna True se criado, False se já existe.
    """
    username = username.strip()
    if role == "Paciente":
        source = PACIENTES
    elif role == "Admin":
        source = ADMINS
    elif role == "Doutor":
        source = DOUTORES
    else:
        return False

    for entry in source:
        if entry.get("username") == username:
            return False

    new_entry = {"username": username, "password": password}
    if extra:
        new_entry.update(extra)
    source.append(new_entry)
    return True