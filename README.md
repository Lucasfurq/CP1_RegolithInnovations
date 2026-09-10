# CP1_Regolith Innovations

**Mission Control | Dados, Decisões e Soluções para a Lua**

Sistema em Python para monitorar os estoques críticos de **água e energia** de uma base lunar, gerar diagnósticos automatizados e simular cenários de risco (poeira nos painéis solares, corte de consumo) para apoiar a tomada de decisão da equipe de Mission Control.

##  Equipe

| Integrante | RM |
|---|---|
| Lucas Furquim Lima | 568690 |
| Diogo Chiaradia | 570246 |
| Gustavo Torres | 572952 |
| Eduardo Braziliano | 573274 |
| Lucas Bomfim | 570420 |
| Julia Johanson | 572220 |

**Turma:** 1CCPJ
**Tema:** Água e Energia — Autonomia, Geração e Distribuição na Base Lunar

##  Estrutura do repositório

```
CP1_Regolith_Innovations/
├── dados_lunar.py      # Base de dados (reservatórios, consumo, geração solar, baterias etc.)
├── Programa_1.py        # Monitoramento e diagnóstico automático
├── Programa_2.py        # Simulação interativa de cenários
├── Ficha_da_Missao.pdf  # Documento com objetivo, dados, indicadores e decisão esperada
└── README.md
```

##  Objetivo

Processar os dados operacionais da base lunar para:
- Calcular indicadores de **autonomia** de água e energia;
- Emitir **alertas automáticos** quando um recurso estiver em risco;
- Permitir que o operador **simule cenários** (acúmulo de poeira, cortes de consumo) e veja o impacto no balanço energético antes de agir.

##  Dados utilizados (`dados_lunar.py`)

| Base | Conteúdo |
|---|---|
| `reservatorios` | Capacidade, nível atual e qualidade da água de 6 reservatórios |
| `consumo_recursos` | Consumo diário de água e energia por módulo (Habitat, Laboratório, Mineração, Médico, Comunicação, Depósito) e prioridade |
| `geracao_solar` | Geração/consumo por ciclo, poeira acumulada e temperatura do painel |
| `baterias` | Capacidade, carga atual e saúde de 6 baterias |
| `pontos_distribuicao` / `mapa_prioridades` / `referencias_lunares` | Dados complementares para evoluções futuras |

##  Como executar

Pré-requisito: Python 3 instalado.

Clone o repositório e execute os programas na raiz do projeto (os três arquivos `.py` precisam estar na mesma pasta):

```bash
git clone <link-do-repositorio>
cd CP1_Regolith_Innovations
```

### Programa 1 — Monitoramento e Diagnóstico

Executa automaticamente, sem interação do usuário:

```bash
python3 Programa_1.py
```

Exibe capacidade e autonomia de água, alertas de reservatórios abaixo de 70% ou com qualidade < 97%, além do balanço de energia e status das baterias.

### Programa 2 — Simulação com Interação

Executa de forma interativa: pede dois valores ao operador.

```bash
python3 Programa_2.py
```

- **Acréscimo % de poeira** nos painéis solares (ex.: `10`)
- **% de corte de energia** em módulos não essenciais (ex.: `5`)

O programa recalcula a geração solar e o consumo, mostra o novo balanço energético e, em caso de déficit, estima **quantos dias faltam até as baterias se esgotarem**.

##  Indicadores calculados

- **Volume e Capacidade Hídrica** — capacidade total vs. volume disponível (%)
- **Autonomia de Água** — dias de operação com o consumo atual
- **Balanço Energético** — carga das baterias vs. consumo diário
- **Sistema de Alertas** — reservatório crítico (< 70% cheio ou qualidade < 97%)
- **Simulação de Déficit** — tempo estimado até o esgotamento das baterias em cenários adversos

##  Ficha da Missão

O documento [`Ficha_da_Missao.pdf`](./Ficha_da_Missao.pdf) traz o objetivo completo do projeto, os dados selecionados, os indicadores do Programa 1 e a lógica de decisão do Programa 2, com exemplos reais de execução.
