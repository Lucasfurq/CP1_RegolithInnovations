# ==========================================
# PROGRAMA 1: MONITORAMENTO E DIAGNÓSTICO
# ==========================================

from dados_lunar import reservatorios, consumo_recursos, geracao_solar, baterias

def diagnostico_agua():
    print("=== DIAGNÓSTICO DE ÁGUA ===")
    total_capacidade = sum(r["capacidade_l"] for r in reservatorios)
    total_nivel = sum(r["nivel_l"] for r in reservatorios)
    pct_total = (total_nivel / total_capacidade) * 100
    
    consumo_total_agua = sum(c["agua_l_dia"] for c in consumo_recursos)
    autonomia_dias = total_nivel / consumo_total_agua

    print(f"Capacidade Total: {total_capacidade} L")
    print(f"Volume Atual: {total_nivel} L ({pct_total:.1f}%)")
    print(f"Consumo Diário Total: {consumo_total_agua} L/dia")
    print(f"Autonomia estimada: {autonomia_dias:.1f} dias\n")

    print("Alertas de Reservatórios:")
    for r in reservatorios:
        taxa = (r["nivel_l"] / r["capacidade_l"]) * 100
        if taxa < 70 or r["qualidade_pct"] < 97:
            print(f"  [ALERTA] Reservatório {r['id']}: {taxa:.1f}% cheio | Qualidade: {r['qualidade_pct']}%")
    print("-" * 40)

def diagnostico_energia():
    print("\n=== DIAGNÓSTICO DE ENERGIA ===")
    total_capacidade_baterias = sum(b["capacidade_kwh"] for b in baterias)
    carga_total_kwh = sum((b["capacidade_kwh"] * b["carga_pct"]) / 100 for b in baterias)
    consumo_total_energia = sum(c["energia_kwh_dia"] for c in consumo_recursos)
    
    # Ciclo atual (último ciclo registrado)
    ultimo_ciclo = geracao_solar[-1]
    
    print(f"Capacidade de Armazenamento: {total_capacidade_baterias} kWh")
    print(f"Carga Atual nas Baterias: {carga_total_kwh:.1f} kWh")
    print(f"Consumo Total Diário: {consumo_total_energia} kWh/dia")
    print(f"Geração Solar Atual (Ciclo {ultimo_ciclo['ciclo']}): {ultimo_ciclo['geracao_kw']} kW")
    print(f"Temperatura do Painel: {ultimo_ciclo['temp_painel_c']}°C | Poeira: {ultimo_ciclo['poeira_pct']}%")
    print("-" * 40)

if __name__ == "__main__":
    print("🚀 INICIANDO SISTEMA DE MONITORAMENTO LUNAR\n")
    diagnostico_agua()
    diagnostico_energia()