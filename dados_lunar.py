reservatorios = [
    {"id": "AG-01", "capacidade_l": 1200, "nivel_l": 1010, "qualidade_pct": 98},
    {"id": "AG-02", "capacidade_l": 900, "nivel_l": 720, "qualidade_pct": 97},
    {"id": "AG-03", "capacidade_l": 650, "nivel_l": 515, "qualidade_pct": 99},
    {"id": "AG-04", "capacidade_l": 500, "nivel_l": 340, "qualidade_pct": 96},
    {"id": "AG-05", "capacidade_l": 400, "nivel_l": 275, "qualidade_pct": 98},
    {"id": "AG-06", "capacidade_l": 300, "nivel_l": 198, "qualidade_pct": 95}
]

consumo_recursos = [
    {"modulo": "Habitat", "agua_l_dia": 58, "energia_kwh_dia": 420, "prioridade": 1},
    {"modulo": "Laboratorio", "agua_l_dia": 27, "energia_kwh_dia": 360, "prioridade": 2},
    {"modulo": "Mineracao", "agua_l_dia": 18, "energia_kwh_dia": 610, "prioridade": 3},
    {"modulo": "Medico", "agua_l_dia": 16, "energia_kwh_dia": 285, "prioridade": 1},
    {"modulo": "Comunicacao", "agua_l_dia": 4, "energia_kwh_dia": 190, "prioridade": 1},
    {"modulo": "Deposito", "agua_l_dia": 6, "energia_kwh_dia": 120, "prioridade": 3}
]

geracao_solar = [
    {"ciclo": 1, "geracao_kw": 96, "consumo_kw": 82, "poeira_pct": 4, "temp_painel_c": 31},
    {"ciclo": 2, "geracao_kw": 93, "consumo_kw": 84, "poeira_pct": 6, "temp_painel_c": 33},
    {"ciclo": 3, "geracao_kw": 89, "consumo_kw": 86, "poeira_pct": 9, "temp_painel_c": 35},
    {"ciclo": 4, "geracao_kw": 84, "consumo_kw": 88, "poeira_pct": 13, "temp_painel_c": 37},
    {"ciclo": 5, "geracao_kw": 79, "consumo_kw": 91, "poeira_pct": 17, "temp_painel_c": 39},
    {"ciclo": 6, "geracao_kw": 75, "consumo_kw": 93, "poeira_pct": 21, "temp_painel_c": 41}
]

baterias = [
    {"id": "BT-01", "capacidade_kwh": 520, "carga_pct": 88, "saude_pct": 96},
    {"id": "BT-02", "capacidade_kwh": 480, "carga_pct": 81, "saude_pct": 94},
    {"id": "BT-03", "capacidade_kwh": 350, "carga_pct": 74, "saude_pct": 98},
    {"id": "BT-04", "capacidade_kwh": 300, "carga_pct": 67, "saude_pct": 91},
    {"id": "BT-05", "capacidade_kwh": 240, "carga_pct": 79, "saude_pct": 95},
    {"id": "BT-06", "capacidade_kwh": 180, "carga_pct": 58, "saude_pct": 89}
]

pontos_distribuicao = [
    {"nome": "Habitat", "coordenada": (10, 10)},
    {"nome": "Laboratorio", "coordenada": (12, 14)},
    {"nome": "Mineracao", "coordenada": (21, 18)},
    {"nome": "Medico", "coordenada": (8, 11)},
    {"nome": "Comunicacao", "coordenada": (7, 16)},
    {"nome": "Deposito", "coordenada": (15, 9)}
]

mapa_prioridades = [
    [2, 2, 1, 1, 0, 0],
    [2, 2, 2, 1, 1, 0],
    [1, 2, 2, 2, 1, 1],
    [1, 1, 2, 2, 2, 1],
    [0, 1, 1, 2, 2, 2],
    [0, 0, 1, 1, 2, 2]
]

referencias_lunares = [
    {"grandeza": "irradiancia_solar", "valor": 1361.0, "unidade": "W/m2"},
    {"grandeza": "gelo_agua_cabeus", "valor": 5.6, "unidade": "% em massa"},
    {"grandeza": "incerteza_gelo_cabeus", "valor": 2.9, "unidade": "pontos percentuais"},
    {"grandeza": "temperatura_superficie_sol", "valor": 127, "unidade": "C"},
    {"grandeza": "temperatura_superficie_escuridao", "valor": -173, "unidade": "C"}
]