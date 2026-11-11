from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["campusflow_a12"]
solicitacoes = db["solicitacoes"]

def missao_1_fila_critica():
    consulta = {
        "situacao": {"$in": ["ABERTA", "EM_ANALISE"]},
        "prioridade": {"$gte": 4}
    }
    projecao = {
        "protocolo": 1, 
        "estudante.nome": 1, 
        "categoria.nome": 1, 
        "situacao": 1, 
        "prioridade": 1, 
        "_id": 0
    }
    ordenacao = [("prioridade", -1), ("criadoEm", 1)]
    
    return list(solicitacoes.find(consulta, projecao).sort(ordenacao))

def missao_2_backlog():
    pipeline = [
        {"$match": {"situacao": {"$ne": "CONCLUIDA"}}},
        {"$group": {
            "_id": "$categoria.nome",
            "quantidade": {"$sum": 1}
        }},
        {"$sort": {"quantidade": -1}}
    ]
    return list(solicitacoes.aggregate(pipeline))

def missao_3_carga_setor():
    pipeline = [
        {"$unwind": "$atendimentos"},
        {"$group": {
            "_id": "$atendimentos.setor",
            "interacoes": {"$sum": 1},
            "tempoMedio": {"$avg": "$atendimentos.duracaoMin"},
            "maiorDuracao": {"$max": "$atendimentos.duracaoMin"}
        }},
        {"$sort": {"interacoes": -1}}
    ]
    return list(solicitacoes.aggregate(pipeline))

def missao_4_estudantes_recorrentes():
    pipeline = [
        {"$group": {
            "_id": "$estudante.id",
            "nome": {"$first": "$estudante.nome"},
            "quantidade": {"$sum": 1},
            "protocolos": {"$push": "$protocolo"}
        }},
        {"$match": {"quantidade": {"$gt": 1}}},
        {"$sort": {"quantidade": -1}}
    ]
    return list(solicitacoes.aggregate(pipeline))

if __name__ == "__main__":
    print("Missão 1:", missao_1_fila_critica())
    print("Missão 2:", missao_2_backlog())
    print("Missão 3:", missao_3_carga_setor())
    print("Missão 4:", missao_4_estudantes_recorrentes())