def adicionar_tarefa(tarefas):
    tarefa = input("Digite a tarefa: ")
    tarefas.append({'tarefa': tarefa, 'concluída': False})
    print("Tarefa adicionada!")


def visualizar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa na lista.")
        return
    for i, t in enumerate(tarefas, start=1):
        status = "Concluída" if t['concluída'] else "Pendente"
        print(f"{i}. {t['tarefa']} ({status})")


def marcar_concluida(tarefas):
    numero = int(input("Digite o número da tarefa para marcar como concluída: ")) - 1
    if 0 <= numero < len(tarefas):
        tarefas[numero]['concluída'] = True
        print("Tarefa marcada como concluída!")
    else:
        print("Número de tarefa inválido.")


def remover_tarefa(tarefas):
    numero = int(input("Digite o número da tarefa para remover: ")) - 1
    if 0 <= numero < len(tarefas):
        tarefas.pop(numero)
        print("Tarefa removida!")
    else:
        print("Número de tarefa inválido.")


def main():
    tarefas = []
    opcoes = {
        '1': adicionar_tarefa,
        '2': visualizar_tarefas,
        '3': marcar_concluida,
        '4': remover_tarefa,
    }

    while True:
        print("\n1. Adicionar Tarefa")
        print("2. Visualizar Tarefas")
        print("3. Marcar Tarefa como Concluída")
        print("4. Remover Tarefa")
        print("0. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha in opcoes:
            opcoes[escolha](tarefas)  # Chama a função correspondente
        elif escolha == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
