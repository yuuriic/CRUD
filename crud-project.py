##################################################
#                                                #
# Aluno: Yuri de França Cordeiro                 #
# Curso: Análise e Desenvolvimento de Sistemas   #
#                                                #
##################################################

import json

# Listas para amazenar nomes e disciplinas
nomes = []
disciplinas = []

# Dicionário que mapeia as opções do menu principal
opcoes_menu_principal = {
                1: 'Estudantes',
                2: 'Disciplinas',
                3: 'Professores',
                4: 'Turmas',
                5: 'Matriculas',
                0: 'sair'
}

# Dicionário que mapeia as opções do menu de operações
opcoes_menu_operacoes = {
                1: 'Incluir',
                2: 'Listar',
                3: 'Atualizar',
                4: 'Excluir',
                0: 'Voltar ao menu principal'
}

# Função para exibir o menu principal
def menu_principal():
    print(' ----- Menu Principal ----- \n')
    # Percorre o dicionário de opções do menu principal e imprime cada opção
    for numero, opcao in opcoes_menu_principal.items():
        print(f'{numero}. {opcao}')
    print()
    
# Função para exibir o menu de operações
def menu_operacoes():
    # Percorre o dicionário de opções do menu de operações e imprime cada opção
    for numero, opcao in opcoes_menu_operacoes.items():
        print(f'{numero}. {opcao}')

# Função para carregar dados de um arquivo JSON
def carregar_dados(arquivo):
    try:
        with open(arquivo, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Função para salvar dados em um arquivo JSON
def salvar_dados(dados, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)

# Função para carregar dados de um arquivo JSON
def carregar_dados_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            dados = json.load(arquivo)
            return dados
    except FileNotFoundError:
        return []    
    
# Função para obter o nome de um item a partir de um código
def obter_nome_por_codigo(lista, codigo):
    for item in lista:
        if item['codigo'] == codigo:
            return item['nome']
    return 'Nome não encontrado'

# Função para verificar a existência de um código nos dados
def verificar_existencia_codigo(codigo, dados):
    for cadastro in dados:
        if 'codigo' in cadastro and cadastro['codigo'] == codigo:
            return True
    return False

# Função para verificar se um valor é único em uma lista de dados
def verificar_valor_unico(valor, dados, chave):
    for cadastro in dados:
        if chave in cadastro and cadastro[chave] == valor:
            return True
    return False

# Função para verificar se um CPF é único em uma lista de dados
def verificar_cpf_unico(cpf, dados, tipo_cadastro):
    return verificar_valor_unico(cpf, dados, 'cpf')

# Função para validar cpf (somente CPF's que existem..)
''' def validar_cpf(cpf):
    # Remove os caracteres "." e "-" do CPF
    cpf = cpf.replace(".", "").replace("-", "")
    # Verifica se o CPF tem 11 dígitos e consiste apenas de dígitos numéricos
    if len(cpf) != 11 or not cpf.isdigit():
        return False

    soma = 0
    # Realiza o cálculo do primeiro dígito verificador
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    
    digito1 = 11 - (soma % 11)
    # Se o resultado for maior que 9, o dígito verificador é 0
    if digito1 > 9:
        digito1 = 0

    # Verifica se o primeiro dígito verificador é igual ao valor fornecido no CPF
    if int(cpf[9]) != digito1:
        return False

    soma = 0
    # Realiza o cálculo do segundo dígito verificador
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    
    digito2 = 11 - (soma % 11)
    # Se o resultado for maior que 9, o dígito verificador é 0
    if digito2 > 9:
        digito2 = 0

    # Verifica se o segundo dígito verificador é igual ao valor fornecido no CPF
    if int(cpf[10]) != digito2:
        return False

    # Se todas as verificações passarem, o CPF é considerado válido
    return True '''

# Função para incluir um cadastro
def incluir_cadastro(tipo_cadastro, nome_arquivo):
    print(f' ----- Incluir {tipo_cadastro} ----- \n')

    # Carrega os dados dos arquivos correspondentes aos tipos de cadastro existentes
    dados_alunos = carregar_dados_arquivo('alunos.json')
    dados_professores = carregar_dados_arquivo('professores.json')
    dados_disciplina = carregar_dados_arquivo('disciplinas.json')

    while True:
        try:
            novo_codigo = int(input('Digite um novo código: '))
            break 
        except ValueError:
            print(' ----- VALOR INVÁLIDO ----- \n')
            continue

    # Verifica se o código já existe nos dados existentes
    while verificar_existencia_codigo(novo_codigo, dados_alunos) or verificar_existencia_codigo(novo_codigo, dados_professores) or verificar_existencia_codigo(novo_codigo, dados_disciplina):
        print(' ----- Esse código já existe. Por favor, insira um novo código. ----- \n')
        novo_codigo = int(input('Digite um novo código: '))

    # Verifica o tipo de cadastro para tomar ações específicas
    if tipo_cadastro == "Disciplina":
        novo_nome = input('Digite o nome da disciplina: ')

        # Salva os dados no arquivo correspondente
        novo_cadastro = {"codigo": novo_codigo, "nome": novo_nome}
        dados_disciplina.append(novo_cadastro)
        salvar_dados(dados_disciplina, 'disciplinas.json')

    elif tipo_cadastro == "Estudante":
        while True:
            novo_nome = input('Digite o novo nome: ')
            novo_cpf = input('Digite o novo CPF: ')
            novo_cpf = ''.join(filter(str.isdigit, novo_cpf))

            ''' if novo_cpf != '' and not validar_cpf(novo_cpf.zfill(11)):
                print(' ----- CPF inválido. Por favor, insira um CPF válido. ----- \n')
                continue '''

            if verificar_cpf_unico(novo_cpf, dados_alunos, tipo_cadastro):
                print(' ----- Esse CPF já existe como aluno. Por favor, insira um novo CPF. ----- \n')
            elif verificar_cpf_unico(novo_cpf, dados_professores, tipo_cadastro):
                print(' ----- Esse CPF já existe como professor. Por favor, insira um novo CPF. ----- \n')
            else:
                break
            
        # Salva os dados no arquivo correspondente
        novo_cadastro = {"codigo": novo_codigo, "nome": novo_nome, "cpf": novo_cpf}
        dados_alunos.append(novo_cadastro)
        salvar_dados(dados_alunos, 'alunos.json')

    elif tipo_cadastro == "Professor":
        while True:
            novo_nome = input('Digite o novo nome: ')
            novo_cpf = input('Digite o novo CPF: ')
            novo_cpf = ''.join(filter(str.isdigit, novo_cpf))

            ''' if novo_cpf != '' and not validar_cpf(novo_cpf.zfill(11)):
                print(' ----- CPF inválido. Por favor, insira um CPF válido. ----- \n')
                continue '''

            if verificar_cpf_unico(novo_cpf, dados_professores, tipo_cadastro):
                print(' ----- Esse CPF já existe como professor. Por favor, insira um novo CPF. ----- \n')
            elif verificar_cpf_unico(novo_cpf, dados_alunos, tipo_cadastro):
                print(' ----- Esse CPF já existe como aluno. Por favor, insira um novo CPF. ----- \n')
            else:
                break

        # Salva os dados no arquivo correspondente
        novo_cadastro = {"codigo": novo_codigo, "nome": novo_nome, "cpf": novo_cpf, "cpf_professor": novo_cpf}
        dados_professores.append(novo_cadastro)
        salvar_dados(dados_professores, 'professores.json')

    print(f'\n{tipo_cadastro} incluído com sucesso!\n')
    input('Tecle ENTER para continuar.')

# Função para listar cadastros
def listar_cadastro(tipo_cadastro, nome_arquivo):
    print(f' ----- Listar {tipo_cadastro} -----\n')

    # Carrega os dados do arquivo correspondente
    dados = carregar_dados_arquivo(nome_arquivo)

    # Verifica se há dados cadastrados
    if not dados:
        print(f'Não há {tipo_cadastro} cadastrados.')
    else:
        for cadastro in dados:
            print(f'Código: {cadastro["codigo"]}, Nome: {cadastro["nome"]}', end="")
            if tipo_cadastro.lower() != "disciplina" and "cpf" in cadastro:
                print(f', CPF: {cadastro["cpf"]}')
            else:
                print()
    input('\Tecle ENTER para continuar.')

# Função para atualizar um cadastro
def atualizar_cadastro(tipo_cadastro, nome_arquivo):
    print(f'----- Atualizar {tipo_cadastro} -----\n')

    # Carrega os dados do arquivo correspondente e outros arquivos necessários
    dados = carregar_dados_arquivo(nome_arquivo)
    dados_alunos = carregar_dados_arquivo('alunos.json')
    dados_professores = carregar_dados_arquivo('professores.json')
    dados_disciplinas = carregar_dados_arquivo('disciplinas.json')

    codigo_cadastro = int(input(f'Digite o código do(a) {tipo_cadastro} a ser atualizado: '))
    cadastro_encontrado = False

    # Itera sobre os cadastros para encontrar o código especificado
    for cadastro in dados:
        if cadastro['codigo'] == codigo_cadastro:
            cadastro_encontrado = True

            if tipo_cadastro == "Estudante":
                novo_codigo = int(input('Digite um novo código: '))
                while verificar_existencia_codigo(novo_codigo, dados_alunos) or verificar_existencia_codigo(novo_codigo, dados_professores) or verificar_existencia_codigo(novo_codigo, dados_disciplinas):
                    print(' ----- Esse código já existe. Por favor, insira um novo código. ----- \n')
                    novo_codigo = int(input('Digite um novo código: '))
                
                novo_nome = input('Digite o novo nome: ')

                while True:
                    novo_cpf = input('Digite o novo CPF: ')
                    novo_cpf = ''.join(filter(str.isdigit, novo_cpf))

                    if verificar_cpf_unico(novo_cpf, dados_alunos, tipo_cadastro):
                        print(' ----- Esse CPF já existe como aluno. Por favor, insira um novo CPF. ----- \n')
                    elif verificar_cpf_unico(novo_cpf, dados_professores, tipo_cadastro):
                        print(' ----- Esse CPF já existe como professor. Por favor, insira um novo CPF. ----- \n')
                    else:
                        # Atualiza os dados do cadastro
                        cadastro["codigo"] = novo_codigo
                        cadastro["nome"] = novo_nome
                        cadastro["cpf"] = novo_cpf
                        break
            elif tipo_cadastro == "Professor":
                novo_codigo = int(input('Digite um novo código: '))
                while verificar_existencia_codigo(novo_codigo, dados_alunos) or verificar_existencia_codigo(novo_codigo, dados_professores) or verificar_existencia_codigo(novo_codigo, dados_disciplinas):
                    print(' ----- Esse código já existe. Por favor, insira um novo código. ----- \n')
                    novo_codigo = int(input('Digite um novo código: '))

                novo_nome = input('Digite o novo nome: ')
                while True:
                    novo_cpf = input('Digite o novo CPF: ')
                    novo_cpf = ''.join(filter(str.isdigit, novo_cpf))

                    if verificar_cpf_unico(novo_cpf, dados_alunos, tipo_cadastro) or verificar_cpf_unico(novo_cpf, dados_professores, tipo_cadastro):
                        print(' ----- Esse CPF já existe. Por favor, insira um novo CPF. ----- \n')
                    else:
                        # Atualiza os dados do cadastro
                        cadastro["codigo"] = novo_codigo
                        cadastro["nome"] = novo_nome
                        cadastro["cpf"] = novo_cpf
                        break
            elif tipo_cadastro == "Disciplina":
                novo_codigo = int(input('Digite um novo código: '))
                while verificar_existencia_codigo(novo_codigo, dados_alunos) or verificar_existencia_codigo(novo_codigo, dados_professores) or verificar_existencia_codigo(novo_codigo, dados_disciplinas):
                    print(' ----- Esse código já existe. Por favor, insira um novo código. ----- \n')
                    novo_codigo = int(input('Digite um novo código: '))

                novo_nome = input('Digite o novo nome: ')
                
                cadastro["codigo"] = novo_codigo
                cadastro["nome"] = novo_nome

    # Verifica se o cadastro foi encontrado
    if cadastro_encontrado:
        salvar_dados(dados, nome_arquivo)
        print(f'\n{tipo_cadastro} atualizado com sucesso!\n')
    else:
        print(f'{tipo_cadastro} não encontrado.\n')

    input('Tecle ENTER para continuar.')

# Função para remover um cadastro
def remover_cadastro(tipo_cadastro, nome_arquivo):
    print(f' ----- Remover {tipo_cadastro} ----- \n')

    # Carrega os dados do arquivo correspondente e outros arquivos necessários
    dados = carregar_dados_arquivo(nome_arquivo)
    codigo_cadastro = int(input(f'Digite o código do {tipo_cadastro} a ser removido: '))
    cadastro_encontrado = False
     
    # Itera sobre os cadastros para encontrar o código especificado
    for cadastro in dados:
        if cadastro["codigo"] == codigo_cadastro:
            cadastro_encontrado = True
            dados.remove(cadastro)
    
    if cadastro_encontrado:
        salvar_dados(dados, nome_arquivo)
        print(f'\n{tipo_cadastro} removido com sucesso!\n')
    else:
        print(f'\n{tipo_cadastro} não encontrada.\n')
    
    input('Tecle ENTER para continuar.')

# Função para incluir uma turma
def incluir_turma():
    # Carrega os dados das turmas, alunos, professores e disciplinas a partir dos arquivos correspondentes
    turmas = carregar_dados('turmas.json')
    dados_alunos = carregar_dados_arquivo('alunos.json')
    dados_professores = carregar_dados_arquivo('professores.json')
    dados_disciplinas = carregar_dados_arquivo('disciplinas.json')
    
    print(' ----- INCLUIR TURMA ----- \n')

    while True:
        try:
            novo_codigo = int(input('Digite um novo código: '))
            break 
        except ValueError:
            print('\n ----- VALOR INVÁLIDO ----- \n')

    # Verifica se o código já existe em algum dos cadastros existentes
    while verificar_existencia_codigo(novo_codigo, dados_alunos) or verificar_existencia_codigo(novo_codigo, dados_professores) or verificar_existencia_codigo(novo_codigo, dados_disciplinas):
        print(' ----- Esse código já existe. Por favor, insira um novo código. ----- \n')
        novo_codigo = int(input('Digite um novo código: '))

    novo_nome = input('Digite o nome da turma: ')

    # Carrega os dados de alunos, professores e disciplinas
    alunos = carregar_dados('alunos.json') 
    professores = carregar_dados('professores.json')  
    disciplinas = carregar_dados('disciplinas.json')

    # Exibe os dados disponíveis
    print('\n ----- Professores disponíveis -----')
    for professor in professores:
        print(f"Código: {professor['codigo']}, Nome: {professor['nome']}")
    codigo_professor = int(input('\nDigite o código do professor: '))

    # Exibe os dados disponíveis
    print('\n ----- Disciplinas disponíveis ----- ')
    for disciplina in disciplinas:
        print(f"Código: {disciplina['codigo']}, Nome: {disciplina['nome']}")
    codigo_disciplina = int(input('\nDigite o código da disciplina: '))

    # Exibe os dados disponíveis
    print('\n ----- Alunos disponíveis ----- ')
    for aluno in alunos:
        print(f"Código: {aluno['codigo']}, Nome: {aluno['nome']}")
    codigo_alunos = input('\nDigite os códigos dos alunos (separados por vírgula): ').split(',')
    codigo_alunos = [int(codigo.strip()) for codigo in codigo_alunos]

    # Cria um dicionário com os dados da nova turma
    nova_turma = {
        "codigo": novo_codigo,
        "nome": novo_nome,
        "professor": codigo_professor,
        "disciplina": codigo_disciplina,
        "alunos": codigo_alunos
    }

    # Salva os dados atualizados das turmas no arquivo correspondente
    turmas.append(nova_turma)
    salvar_dados(turmas, 'turmas.json')

    print('\n----------------------------')
    print('Turma incluída com sucesso!')
    print('----------------------------\n')
    input('Tecle ENTER para continuar.')

# Função para listar as turmas existentes
def listar_turmas():
    # Carrega os dados das turmas, professores, disciplinas e alunos a partir dos arquivos correspondentes
    turmas = carregar_dados('turmas.json')
    professores = carregar_dados('professores.json')
    disciplinas = carregar_dados('disciplinas.json')
    alunos = carregar_dados('alunos.json')
    
    print(' ----- LISTAR TURMAS ----- \n')

    if not turmas:
        print('Não há turmas cadastradas.\n')
    else:
        for turma in turmas:
            print(f'Código: {turma["codigo"]}')
            print(f'Nome: {turma["nome"]}')
            
            # Obtém o nome do professor e da disciplina usando os respectivos códigos
            nome_professor = obter_nome_por_codigo(professores, turma["professor"])
            nome_disciplina = obter_nome_por_codigo(disciplinas, turma["disciplina"])

            print(f'Professor: {nome_professor}')
            print(f'Disciplina: {nome_disciplina}')
            print('Alunos:')
            
            for codigo_aluno in turma['alunos']:
                # Obtém o nome de cada aluno usando o código
                nome_aluno = obter_nome_por_codigo(alunos, codigo_aluno)
                print(nome_aluno)
            
            print()
    
    input('Tecle ENTER para continuar.')

# Função para atualizar os dados de uma turma
def atualizar_dados_turma():
    # Carrega os dados das turmas, professores, disciplinas e alunos a partir dos arquivos correspondentes
    turmas = carregar_dados('turmas.json')
    professores = carregar_dados('professores.json')
    disciplinas = carregar_dados('disciplinas.json')
    alunos = carregar_dados('alunos.json')

    print(' ----- Atualizar dados da turma ----- \n')
    codigo_turma = int(input('Digite o código da turma a ser atualizada: '))
    turma_encontrada = False

    # Percorre todas as turmas existentes
    for turma in turmas:
        if turma['codigo'] == codigo_turma:     # Verifica se o código da turma atual é igual ao código informado pelo usuário
            turma_encontrada = True     # Marca que a turma foi encontrada

            print('\n ----- Opções de atualização: -----\n')
            print('1. Atualizar nome da turma')
            print('2. Atualizar professor')
            print('3. Atualizar disciplina')
            print('4. Atualizar alunos')
            print('0. Voltar ao menu principal\n')

            opcao_atualizacao = int(input('Digite o número da opção desejada: '))

            # Atualizar os dados cadastrados na turma
            if opcao_atualizacao == 1:
                novo_nome = input('\nDigite o novo nome da turma: ')
                turma['nome'] = novo_nome
                print('Nome da turma atualizado com sucesso!\n')

            elif opcao_atualizacao == 2:
                print('\nProfessores disponíveis:')
                for professor in professores:
                    print(f'Código: {professor["codigo"]}, Nome: {professor["nome"]}')
                novo_codigo_professor = int(input('\nDigite o novo código do professor: '))
                turma['professor'] = novo_codigo_professor
                print('Professor da turma atualizado com sucesso!\n')

            elif opcao_atualizacao == 3:
                print('\nDisciplinas disponíveis:')
                for disciplina in disciplinas:
                    print(f'Código: {disciplina["codigo"]}, Nome: {disciplina["nome"]}')
                novo_codigo_disciplina = int(input('\nDigite o novo código da disciplina: '))
                turma['disciplina'] = novo_codigo_disciplina
                print('Disciplina da turma atualizada com sucesso!\n')

            elif opcao_atualizacao == 4:
                print('\nAlunos disponíveis:')
                for aluno in alunos:
                    print(f'Código: {aluno["codigo"]}, Nome: {aluno["nome"]}')
                codigo_alunos = input('\nDigite os códigos dos alunos (separados por vírgula): ').split(',')
                codigo_alunos = [int(codigo.strip()) for codigo in codigo_alunos]

                turma['alunos'] = codigo_alunos
                print('\n------------------------------------------')
                print('Alunos da turma atualizados com sucesso!\n')
                print('------------------------------------------\n')

            elif opcao_atualizacao == 0:
                print('\n------------------------------')
                print('Voltando ao menu principal...')
                print('------------------------------\n')
                break
            else:
                print('\n----------------')
                print('Opção inválida!\n')
                print('----------------\n')

            salvar_dados(turmas, 'turmas.json')
            break

    if not turma_encontrada:
        print('----------------------------\n')
        print('Turma não encontrada.\n')
        print('----------------------------\n')

    input('Tecle ENTER para continuar')

# Função para remover uma turma
def remover_turma():
    turmas = carregar_dados('turmas.json')
    
    print('--- REMOVER TURMA ---\n')
    codigo_turma = int(input('Digite o código da turma a ser removida: '))
    turma_encontrada = False
    
    # Percorre todas as turmas existentes
    for turma in turmas:
        if turma['codigo'] == codigo_turma:
            turma_encontrada = True
            turmas.remove(turma)        # Remove a turma da lista de turmas
    
    if turma_encontrada:
        salvar_dados(turmas, 'turmas.json')
        print('\n----------------------------')
        print('Turma removida com sucesso!')
        print('----------------------------\n')
    else:
        print('\n-----------------------')
        print('Turma não encontrada.')
        print('-----------------------\n')

    input('Tecle ENTER para continuar')

# Função para incluir matrículas
def incluir_matricula():
    # Carrega os dados das turmas, matrículas e alunos a partir dos arquivos correspondentes
    matriculas = carregar_dados('matriculas.json')
    turmas = carregar_dados('turmas.json')
    alunos = carregar_dados('alunos.json')

    print(' ----- Incluir Matrícula ----- ')

    # Exibe as informações das turmas disponíveis
    print('\nTurmas disponíveis:')
    for turma in turmas:
        print(f"Código: {turma['codigo']}, Nome: {turma['nome']}\n")
    codigo_turma = int(input('Digite o código da turma: '))

    # Exibe as informações dos alunos disponíveis
    print('\nAlunos disponíveis:')
    for aluno in alunos:
        print(f"Código: {aluno['codigo']}, Nome: {aluno['nome']} \n")
    codigo_alunos = input('Digite os códigos dos alunos (separados por vírgula): ').split(',')
    codigo_alunos = [int(codigo.strip()) for codigo in codigo_alunos]

    nova_matricula = {
        "turma": codigo_turma,
        "alunos": codigo_alunos
    }

    # Salva os dados atualizados no arquivo 'matriculas.json'
    matriculas.append(nova_matricula)
    salvar_dados(matriculas, 'matriculas.json')

    print('\n--------------------------------')
    print('Matrícula incluída com sucesso!')
    print('--------------------------------\n')
    input('Tecle ENTER para continuar.')
     
# Função para listar matrículas
def listar_matriculas():
    # Carrega os dados das turmas, matrículas e alunos a partir dos arquivos correspondentes
    matriculas = carregar_dados('matriculas.json')
    turmas = carregar_dados('turmas.json')
    alunos = carregar_dados('alunos.json')

    print('----- LISTAR MATRICULAS -----\n')

    if not matriculas:
        print('Não há matrículas cadastradas.\n')
    else:
        # Obtém o nome da turma com base no código
        for matricula in matriculas:
            codigo_turma = matricula['turma']
            codigo_alunos = matricula['alunos']
            nome_turma = obter_nome_por_codigo(turmas, codigo_turma)
            
            print(f'Código da turma: {codigo_turma}')
            print(f'Nome da turma: {nome_turma}')

            if codigo_alunos:
                # Obtém o nome do aluno com base no código
                print('Código dos alunos:')
                for codigo_aluno in codigo_alunos:
                    nome_aluno = obter_nome_por_codigo(alunos, codigo_aluno)
                    if nome_aluno:
                        print(f'Código: {codigo_aluno}, Nome: {nome_aluno}')
                    else:
                        print(f'Código: {codigo_aluno}, Nome: Nome não encontrado')
                print()
            else:
                print('\n----------------------------------------')
                print('Não há alunos matriculados nessa turma.')
                print('----------------------------------------\n')
    input('Tecle ENTER para continuar.')

# Função para atualizar dados da matrícula
def atualizar_matricula():
    # Carrega os dados das turmas, matrículas e alunos a partir dos arquivos correspondentes
    matriculas = carregar_dados('matriculas.json')
    alunos = carregar_dados('alunos.json')
    turmas = carregar_dados('turmas.json')

    print(' ----- Atualizar Matrícula -----\n')

    # Exibe o código e o nome da turma da matrícula
    for matricula in matriculas:
        turma = next((turma for turma in turmas if turma['codigo'] == matricula['turma']), None)
        
        print('Matrículas disponíveis:')
        print(f"Código da Turma: {matricula['turma']}, Nome da Turma: {turma['nome']}\n")

    codigo_matricula = int(input('Digite o código da turma matriculada: '))

    for matricula in matriculas:
        if matricula['turma'] == codigo_matricula:
            print('\n ----- Opções de atualização: -----\n')
            print('1. Atualizar turma')
            print('2. Atualizar alunos')
            print('0. Voltar ao menu principal\n')

            opcao_atualizacao = int(input('Digite o número da opção desejada: '))

            if opcao_atualizacao == 1:
                 # Obtém o nome das turmas com base no código
                print('\nTurmas disponíveis:')
                for turma in turmas:
                    print(f"Código: {turma['codigo']}, Nome: {turma['nome']}")
                novo_codigo_turma = int(input('Digite o novo código da turma: '))
                matricula['turma'] = novo_codigo_turma
                print('Turma da matrícula atualizada com sucesso!\n')

            elif opcao_atualizacao == 2:
                 # Obtém o nome dos alunos com base no código
                print('\nAlunos disponíveis:')
                for aluno in alunos:
                    print(f'Código: {aluno["codigo"]}, Nome: {aluno["nome"]}')
                codigo_alunos = input('\nDigite os códigos dos alunos (separados por vírgula): ').split(',')
                codigo_alunos = [int(codigo.strip()) for codigo in codigo_alunos]

                matricula['alunos'] = codigo_alunos
                print('\n---------------------------------------------')
                print('Alunos da matrícula atualizados com sucesso\n')
                print('---------------------------------------------\n')

            elif opcao_atualizacao == 0:
                print('Voltando ao menu principal...\n')
                break

    # Salva os dados atualizados no arquivo
    salvar_dados(matriculas, 'matriculas.json')
    input('Tecle ENTER para continuar.')

# Função para excluir uma matrícula
def excluir_matricula():
    # Carrega os dados das turmas e matrículas a partir dos arquivos correspondentes
    matriculas = carregar_dados('matriculas.json')
    turmas = carregar_dados('turmas.json')

    print(' ----- Excluir Matrícula -----\n')
    
    # Exibe o código e o nome da turma para cada matrícula
    print('Turmas disponíveis para exclusão de matrícula:')
    for matricula in matriculas:
        turma = next((turma for turma in turmas if turma['codigo'] == matricula['turma']), None)
        print(f"Código da Turma: {matricula['turma']}, Nome da Turma: {turma['nome']}\n")

    codigo_turma = int(input('Digite o código da turma: '))

    # Verifica se o código da turma da matrícula é igual ao código digitado
    for i, matricula in enumerate(matriculas):
        if matricula['turma'] == codigo_turma:
            del matriculas[i]
            salvar_dados(matriculas, 'matriculas.json')
            print('\n---------------------------------')
            print('Matrícula excluída com sucesso!')
            print('---------------------------------\n')
            break
    else:
        print('\n--------------------------')
        print('Matrícula não encontrada.')
        print('--------------------------\n')

    input('Tecle ENTER para continuar.')

# Bloco para encerrar o programa
def encerrar():
    print('Encerrando o programa... \n')
    input('Tecle ENTER para continuar.\n')
    print('Programa encerrado.\n')
    print('Thank you! \nDeveloper >>> Yuri de França Cordeiro <<< \n')


# Este bloco inicia um loop infinito que exibe o menu principal e solicita ao usuário que escolha uma opção.
while True:
    menu_principal()
    
    try:
        opcao = int(input('Digite o numero da opcao desejada: '))
    except ValueError:
        print('\n----------------------------')
        print(' ----- VALOR INVÁLIDO -----')
        print('----------------------------\n')
        input('Tecle ENTER para continuar.')
        continue

    nome_opcao_menu_principal = opcoes_menu_principal.get(opcao, 'OPÇÃO INVÁLIDA')
    print(f'A opção escolhida foi {opcao} - {nome_opcao_menu_principal} \n')
        
    while True:
        
        '''
        Este bloco aninhado verifica se a opção escolhida no menu principal é igual aos numeros relacionados. 
        Se for o caso, exibe o menu de operações relacionadas a opção e solicita ao usuário que escolha uma opção. 
        '''    
        if opcao == 1:
            # Operações relacionadas a Alunos
            print(f' ----- {nome_opcao_menu_principal} --- Menu de Operações ----- \n')
            menu_operacoes()

            try:
                opcao_entrada = int(input('\nDigite o numero da opcao desejada: '))
            except ValueError:
                print('\n----------------------------')
                print(' ----- OPÇÃO INVÁLIDA -----')
                print('----------------------------\n')
                input('Tecle ENTER para continuar.')
                continue

            nome_opcao_menu_operacoes = opcoes_menu_operacoes.get(opcao_entrada, 'OPÇÃO INVÁLIDA')
            print(f'A opção escolhida foi {opcao_entrada} - {nome_opcao_menu_operacoes}\n')

            if opcao_entrada == 1:
               incluir_cadastro('Estudante', 'alunos.json')

            if opcao_entrada == 2:
                listar_cadastro('Estudante', 'alunos.json')

            if opcao_entrada == 3:
                atualizar_cadastro('Estudante', 'alunos.json')

            if opcao_entrada == 4:            
                remover_cadastro('Estudante', 'alunos.json')

            if opcao_entrada == 0:
                print('\n--------------------------')
                print(' ----- ATUALIZAÇÃO ----- ')
                print('--------------------------\n')
                input('Tecle ENTER para continuar.')
                break
        
        elif opcao == 2:
            # Operações relacionadas a Disciplinas
            print(f'--- {nome_opcao_menu_principal} - Menu de Operações --- \n')
            menu_operacoes()

            try:
                opcao_entrada = int(input('\nDigite o numero da opcao desejada: '))
            except ValueError:
                print('\n----------------------------')
                print(' ----- OPÇÃO INVÁLIDA -----')
                print('----------------------------\n')
                input('Tecle ENTER para continuar.')
                continue

            nome_opcao_menu_operacoes = opcoes_menu_operacoes.get(opcao_entrada, 'OPÇÃO INVÁLIDA')
            print(f'A opção escolhida foi {opcao_entrada} - {nome_opcao_menu_operacoes}\n')

            if opcao_entrada == 1:
               incluir_cadastro('Disciplina', 'disciplinas.json')

            if opcao_entrada == 2:
                listar_cadastro('Disciplina', 'disciplinas.json')

            if opcao_entrada == 3:
                atualizar_cadastro('Disciplina', 'disciplinas.json')

            if opcao_entrada == 4:
                remover_cadastro('Disciplina', 'disciplinas.json')

            if opcao_entrada == 0:
                print('\n--------------------------')
                print(' ----- ATUALIZAÇÃO ----- ')
                print('--------------------------\n')
                input('Tecle ENTER para continuar.')
                break
        
        elif opcao == 3:
            # Operações relacionadas a Professores
            print(f'--- {nome_opcao_menu_principal} - Menu de Operações --- \n')
            menu_operacoes()

            try:
                opcao_entrada = int(input('\nDigite o numero da opcao desejada: '))
            except ValueError:
                print('\n----------------------------')
                print(' ----- OPÇÃO INVÁLIDA -----')
                print('----------------------------\n')
                input('Tecle ENTER para continuar.')
                break

            nome_opcao_menu_operacoes = opcoes_menu_operacoes.get(opcao_entrada, 'OPÇÃO INVÁLIDA')
            print(f'A opção escolhida foi {opcao_entrada} - {nome_opcao_menu_operacoes}\n')

            if opcao_entrada == 1:
               incluir_cadastro('Professor', 'professores.json')

            if opcao_entrada == 2:
                listar_cadastro('Professor', 'professores.json')

            if opcao_entrada == 3:
                atualizar_cadastro('Professor', 'professores.json')

            if opcao_entrada == 4:
                remover_cadastro('Professor', 'professores.json')

            if opcao_entrada == 0:
                print('\n--------------------------')
                print(' ----- ATUALIZAÇÃO ----- ')
                print('--------------------------\n')
                input('Tecle ENTER para continuar.')
                break

        elif opcao == 4:
            # Operações relacionadas a Turmas
            print(f'--- {nome_opcao_menu_principal} - Menu de Operações --- \n')
            menu_operacoes()

            try:
                opcao_entrada = int(input('\nDigite o numero da opcao desejada: '))
            except ValueError:
                print('\n----------------------------')
                print(' ----- OPÇÃO INVÁLIDA -----')
                print('----------------------------\n')
                input('Tecle ENTER para continuar.')
                break

            nome_opcao_menu_operacoes = opcoes_menu_operacoes.get(opcao_entrada, 'OPÇÃO INVÁLIDA')
            print(f'A opção escolhida foi {opcao_entrada} - {nome_opcao_menu_operacoes}\n')

            if opcao_entrada == 1:
               incluir_turma()

            if opcao_entrada == 2:
                listar_turmas()

            if opcao_entrada == 3:
               atualizar_dados_turma()

            if opcao_entrada == 4:
                remover_turma()

            if opcao_entrada == 0:
                print('\n--------------------------')
                print(' ----- ATUALIZAÇÃO ----- ')
                print('--------------------------\n')
                input('Tecle ENTER para continuar.')
                break
        elif opcao == 5:
            # Operações relacionadas a Matrículas
            print(f'--- {nome_opcao_menu_principal} - Menu de Operações --- \n')
            menu_operacoes()

            try:
                opcao_entrada = int(input('\nDigite o numero da opcao desejada: '))
            except ValueError:
                print('\n----------------------------')
                print(' ----- OPÇÃO INVÁLIDA -----')
                print('----------------------------\n')
                input('Tecle ENTER para continuar.')
                break

            nome_opcao_menu_operacoes = opcoes_menu_operacoes.get(opcao_entrada, 'OPÇÃO INVÁLIDA')
            print(f'A opção escolhida foi {opcao_entrada} - {nome_opcao_menu_operacoes}\n')

            if opcao_entrada == 1:
                incluir_matricula()

            if opcao_entrada == 2:
                listar_matriculas()

            if opcao_entrada == 3:
                atualizar_matricula()

            if opcao_entrada == 4:
                excluir_matricula()

            if opcao_entrada == 0:
                print('\n--------------------------')
                print(' ----- ATUALIZAÇÃO ----- ')
                print('--------------------------\n')
                input('Tecle ENTER para continuar.')
                break
    
        # Operações relacionadas a finalização do programa
        elif opcao == "0":
            break
        else:
            print('\n-----------------------------')
            print(' ----- TENTE NOVAMENTE ----- ')
            print('-----------------------------\n')
            input('Tecle ENTER para continuar.')
            break
    if opcao == 0:
        encerrar()
        break