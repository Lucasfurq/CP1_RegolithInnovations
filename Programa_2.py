# ==========================================
# PROGRAMA 2: SIMULAÇÃO COM INTERAÇÃO
# ==========================================

from dados_lunar import geracao_solar, consumo_recursos, baterias

def simular_cenario():
    print("=== SIMULADOR DE SUPRIMENTOS - MISSION CONTROL ===")
    
    # Exibir estado base
    consumo_base = sum(c["energia_kwh_dia"] for c in consumo_recursos)
    carga_total = sum((b["capacidade_kwh"] * b["carga_pct"]) / 100 for b in baterias)
    
    print(f"Consumo base atual: {consumo_base} kWh/dia")
    print(f"Carga atual nas baterias: {carga_total:.1f} kWh\n")
    
    try:
        fator_poeira = float(input("Digite o acréscimo percentual de poeira nos painéis solares (ex: 5 para +5%): "))
        reducao_consumo = float(input("Digite a porcentagem de corte de energia em módulos não essenciais (ex: 10 para -10%): "))
    except ValueError:
        print("Erro: Digite apenas números válidos.")
        return

    # Simulação de impacto
    ultimo_ciclo = geracao_solar[-1]
    nova_geracao = ultimo_ciclo["geracao_kw"] * (1 - (fator_poeira / 100))
    novo_consumo = consumo_base * (1 - (reducao_consumo / 100))
    
    balanco = nova_geracao - novo_consumo

    print("\n" + "="*40)
    print("RESULTADO DA SIMULAÇÃO")
    print(f"Nova Geração Solar estimada: {nova_geracao:.2f} kW")
    print(f"Novo Consumo ajustado: {novo_consumo:.2f} kWh/dia")
    print(f"Balanço Energético: {balanco:.2f} kW/dia")
    
    if balanco >= 0:
        print("STATUS: SITUAÇÃO ESTÁVEL 🟢 Geração cobre o consumo.")
    else:
        print("STATUS: ALERTA CRÍTICO 🔴 Déficit energético! As baterias serão descarregadas.")
        dias_ate_colapso = carga_total / abs(balanco)
        print(f"Tempo estimado até esgotar as baterias: {dias_ate_colapso:.1f} dias.")
    print("="*40)

if __name__ == "__main__":
    simular_cenario()