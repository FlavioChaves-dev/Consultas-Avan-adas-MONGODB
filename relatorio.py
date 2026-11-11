from consultas import (
    missao_1_fila_critica, 
    missao_2_backlog, 
    missao_3_carga_setor, 
    missao_4_estudantes_recorrentes
)

def gerar_relatorio():
    print("CAMPUSFLOW — RELATÓRIO OPERACIONAL")
    
    print("\nBACKLOG POR CATEGORIA")
    backlog = missao_2_backlog()
    for item in backlog:
        print(f"{item['_id']}: {item['quantidade']}")
        
    print("\nCARGA POR SETOR")
    carga = missao_3_carga_setor()
    for setor in carga:
        print(f"{setor['_id']}")
        print(f"  Interações: {setor['interacoes']}")
        print(f"  Tempo médio: {setor['tempoMedio']:.1f} min")
        print(f"  Maior duração: {setor['maiorDuracao']} min\n")
        
    print("ESTUDANTES RECORRENTES")
    recorrentes = missao_4_estudantes_recorrentes()
    for aluno in recorrentes:
        print(f"{aluno['nome']}: {aluno['quantidade']} solicitações {aluno['protocolos']}")
        
    print("\nCASOS CRÍTICOS")
    criticos = missao_1_fila_critica()
    for caso in criticos:
        print(f"{caso['protocolo']} - {caso['estudante']['nome']} ({caso['situacao']}, Prio: {caso['prioridade']})")
        
    print("CONCLUSÕES TÉCNICAS")
    print("1. A categoria 'Aproveitamento de Disciplina' concentra o maior backlog (3 solicitações inacabadas).")
    print("2. O setor 'Secretaria' possui o maior número de interações (10), mas o gargalo real de tempo está na 'Coordenação', que possui um tempo médio de atendimento drasticamente maior (47 minutos).")
    print("3. Existem indícios claros de alunos recorrentes: a estudante Ana Ribeiro sozinha abriu 3 solicitações, representando 25% do total de protocolos registrados.")

if __name__ == "__main__":
    gerar_relatorio()