Claro! Aqui está o código completo do **Waku Score com proteção por senha**.

### 📋 **CÓDIGO COMPLETO - WAKU SCORE 2025**

```python
import streamlit as st
import pandas as pd
import time

# =============================================================================
# CONFIGURAÇÃO DA PÁGINA (Estilo App Mobile)
# =============================================================================
st.set_page_config(
    page_title="Waku Score",
    page_icon="⚽",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# =============================================================================
# 🔐 SISTEMA DE LOGIN (Proteção por Senha)
# =============================================================================

# Define a senha correta
SENHA_CORRETA = "112719.Ramira"

# Verifica se o usuário já está autenticado na sessão
if 'autenticado' not in st.session_state:
    st.session_state.autenticado = False

# Se não estiver autenticado, mostra a tela de login
if not st.session_state.autenticado:
    st.markdown("# 🔒 Acesso Restrito")
    st.markdown("Digite a senha para acessar o Waku Score.")

    # Formulário de Login
    with st.form(key='login_form'):
        senha_digitada = st.text_input("Senha", type="password")
        botao_entrar = st.form_submit_button("Entrar")

        if botao_entrar:
            if senha_digitada == SENHA_CORRETA:
                st.session_state.autenticado = True
                st.success("Acesso concedido! Carregando...")
                time.sleep(0.5)
                st.rerun()  # Recarrega a página para mostrar o app
            else:
                st.error("🚨 Senha incorreta. Tente novamente.")
    
    # Importante: Interrompe a execução do restante do código se não estiver autenticado
    st.stop()

# =============================================================================
# SE AUTENTICADO: LÓGICA CENTRAL DO WAKU (Core Engine)
# =============================================================================

class WakuCore:
    def __init__(self):
        # Inicializa dados (Persistência de Sessão no Streamlit Cloud)
        if 'dados_waku' not in st.session_state:
            st.session_state.dados_waku = self.carregar_dados_iniciais()
        if 'banca' not in st.session_state:
            st.session_state.banca = 1000.00
        if 'stake_pct' not in st.session_state:
            st.session_state.stake_pct = 2.5

    def carregar_dados_iniciais(self):
        # Dados base (Simulados - Temporada 2025)
        return {
            'Man City': {'liga': 'ENG', 'fg': 90, 'mom': 1.10, 'form': 'V,V,V,E,V', 'rank': 1},
            'Real Madrid': {'liga': 'ESP', 'fg': 88, 'mom': 1.08, 'form': 'V,E,V,V,V', 'rank': 2},
            'Bayern': {'liga': 'GER', 'fg': 89, 'mom': 1.09, 'form': 'V,V,E,V,V', 'rank': 3},
            'Arsenal': {'liga': 'ENG', 'fg': 87, 'mom': 1.05, 'form': 'V,E,V,V,D', 'rank': 4},
            'Benfica': {'liga': 'POR', 'fg': 85, 'mom': 1.12, 'form': 'V,V,V,V,V', 'rank': 5},
            'PSG': {'liga': 'FRA', 'fg': 86, 'mom': 1.11, 'form': 'V,V,E,V,V', 'rank': 6},
            'Liverpool': {'liga': 'ENG', 'fg': 84, 'mom': 1.03, 'form': 'D,V,E,V,V', 'rank': 7},
            'Inter Milan': {'liga': 'ITA', 'fg': 85, 'mom': 1.06, 'form': 'V,V,E,V,E', 'rank': 8},
        }

    def calcular_indice(self, time):
        """Calcula o Índice Waku (Força Geral * Momentum)"""
        dados = st.session_state.dados_waku[time]
        return dados['fg'] * dados['mom']

    def analisar_confronto(self, time_a, time_b, local):
        """Retorna as probabilidades (Time A, Time B)"""
        idx_a = self.calcular_indice(time_a)
        idx_b = self.calcular_indice(time_b)

        # Bônus de Mando de Campo (15%)
        bonus = 1.15
        if local == "Casa": idx_a *= bonus
        if local == "Fora": idx_b *= bonus

        total = idx_a + idx_b
        return (idx_a / total) * 100, (idx_b / total) * 100

    def get_semaforo_jogo(self, time_a, time_b, local="Casa"):
        """
        Retorna o sinal do semáforo e o nível de dificuldade da aposta.
        """
        p_a, p_b = self.analisar_confronto(time_a, time_b, local)
        diferenca = abs(p_a - p_b)

        if diferenca > 25:
            return "🟢 FÁCIL", diferenca
        elif diferenca > 10:
            return "🟡 NORMAL", diferenca
        else:
            return "🔴 DIFÍCIL", diferenca

# Inicializa o motor APENAS se autenticado
waku = WakuCore()

# =============================================================================
# INTERFACE (Estilo Flashscore)
# =============================================================================

# --- CABEÇALHO FIXO ---
col1, col2 = st.columns([3, 1])
with col1:
    st.title("⚽ Waku Score")
with col2:
    st.metric("Banca", f"€{st.session_state.banca:,.2f}")

# --- ABAS DE NAVEGAÇÃO ---
tab_destaques, tab_analisar, tab_ranking, tab_banca = st.tabs([
    "🔥 Destaques", "⚔️ Simular Jogo", "🏆 Rankings", "💰 Gestão"
])

# -----------------------------------------------------------------------------
# ABA 1: DESTAQUES (Com Semáforo)
# -----------------------------------------------------------------------------
with tab_destaques:
    st.subheader("Análises do Dia")

    jogos_do_dia = [
        ("Benfica", "Inter Milan", "Hoje 20:00"),
        ("Man City", "Arsenal", "Amanhã 16:30"),
        ("Real Madrid", "Liverpool", "Amanhã 21:00"),
    ]

    for t1, t2, hora in jogos_do_dia:
        semaforo, diff = waku.get_semaforo_jogo(t1, t2, "Casa")
        
        with st.container():
            cols = st.columns([1, 3, 3, 3])

            with cols[0]:
                st.markdown(f"<h2 style='text-align: center;'>{semaforo[:2]}</h2>", unsafe_allow_html=True)

            with cols[1]:
                st.markdown(f"**{t1}**")

            with cols[2]:
                st.markdown(f"**{t2}**")

            with cols[3]:
                if st.button("Analisar", key=f"btn_{t1}_{t2}", use_container_width=True):
                    st.session_state.jogo_selecionado = (t1, t2)
                    st.toast(f"Vá para a aba 'Simular Jogo'")

            st.caption(f"{hora} | Dificuldade: {semaforo[3:]} (Dif. {diff:.0f}%)")
        st.markdown("---")

    # Alertas Rápidos
    st.subheader("Alertas do Sistema")
    st.info("💎 **Valor Identificado:** Man City tem consistência 95%.")
    st.error("⚠️ **Risco:** Liverpool (D,V,E...) está inconstante.")


# -----------------------------------------------------------------------------
# ABA 2: SIMULAR JOGO
# -----------------------------------------------------------------------------
with tab_analisar:
    st.subheader("Simulador de Confronto")

    equipes = list(st.session_state.dados_waku.keys())
    
    default_a = st.session_state.get('jogo_selecionado', (equipes[0], equipes[1]))[0]
    default_b = st.session_state.get('jogo_selecionado', (equipes[0], equipes[1]))[1]

    if default_a not in equipes: default_a = equipes[0]
    if default_b not in equipes or default_b == default_a: 
        lista_b = [e for e in equipes if e != default_a]
        default_b = lista_b[0] if lista_b else equipes[0]

    c1, c2 = st.columns(2)
    with c1:
        time_mandante = st.selectbox("Mandante", options=equipes, index=equipes.index(default_a))
    with c2:
        lista_b = [e for e in equipes if e != time_mandante]
        idx_b = lista_b.index(default_b) if default_b in lista_b else 0
        time_visitante = st.selectbox("Visitante", options=lista_b, index=idx_b)

    
    if st.button("⚡ ANALISAR CONFRONTO", use_container_width=True):
        if 'jogo_selecionado' in st.session_state: del st.session_state.jogo_selecionado

        with st.spinner("Calculando..."):
            time.sleep(0.3)
            
            p_a, p_b = waku.analisar_confronto(time_mandante, time_visitante, "Casa")
            semaforo, diff = waku.get_semaforo_jogo(time_mandante, time_visitante, "Casa")

            st.markdown("---")
            st.markdown(f"<h1 style='text-align: center;'>{semaforo[:2]}</h1>", unsafe_allow_html=True)
            st.markdown(f"<p style='text-align: center; font-size: 18px;'>Dificuldade: <b>{semaforo[3:]}</b></p>", unsafe_allow_html=True)

            colA, colVS, colB = st.columns([4, 1, 4])

            with colA:
                st.metric(time_mandante, f"{p_a:.1f}%", "Mandante")
                st.progress(int(p_a))
                st.caption(f"Forma: {st.session_state.dados_waku[time_mandante]['form']}")

            with colVS:
                st.markdown("<h1 style='text-align: center; padding-top: 15px;'>VS</h1>", unsafe_allow_html=True)

            with colB:
                st.metric(time_visitante, f"{p_b:.1f}%", "Visitante")
                st.progress(int(p_b))
                st.caption(f"Forma: {st.session_state.dados_waku[time_visitante]['form']}")

            st.markdown("---")
            favorito = time_mandante if p_a > p_b else time_visitante

            if "FÁCIL" in semaforo:
                st.success(f"✅ **ALTA CONFIANÇA:** {favorito} é o grande favorito. (Diferença: {diff:.1f}%)")
            elif "NORMAL" in semaforo:
                st.warning(f"⚠️ **FAVORITISMO MODERADO:** Ligeira vantagem para {favorito}. (Diferença: {diff:.1f}%)")
            else:
                st.error(f"🔴 **ALTO RISCO:** Jogo extremamente equilibrado. Cautela! (Diferença: {diff:.1f}%)")

# -----------------------------------------------------------------------------
# ABA 3: RANKINGS (Classificação)
# -----------------------------------------------------------------------------
with tab_ranking:
    st.subheader("Ranking Global Waku")
    tabela_data = []
    for time, dados in st.session_state.dados_waku.items():
        tabela_data.append({
            "Time": time,
            "Liga": dados['liga'],
            "Forma (5j)": dados['form'],
            "Índice Waku": waku.calcular_indice(time)
        })
    
    df = pd.DataFrame(tabela_data).sort_values("Índice Waku", ascending=False)
    df = df.reset_index(drop=True)
    df.index += 1 

    st.dataframe(
        df,
        use_container_width=True,
        column_config={
            "Índice Waku": st.column_config.ProgressColumn("Força", format="%d", min_value=0, max_value=110),
        }
    )

# -----------------------------------------------------------------------------
# ABA 4: GESTÃO (Banca)
# -----------------------------------------------------------------------------
with tab_banca:
    st.header("Controle Financeiro")
    
    stake_atual = (st.session_state.banca * st.session_state.stake_pct) / 100
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Banca Total", f"€{st.session_state.banca:,.2f}")
    with col2:
        st.metric("Stake Sugerida", f"€{stake_atual:.2f}", f"{st.session_state.stake_pct}%")

    st.markdown("---")
    st.subheader("Registrar Resultado de Aposta")

    c1, c2 = st.columns(2)
    with c1:
        resultado = st.radio("Resultado", ["Vitória ✅", "Derrota ❌"])
    with c2:
        valor = st.number_input("Valor (€)", min_value=0.01, step=10.0, key="valor_aposta")

    if st.button("Atualizar Banca 💰"):
        if valor <= 0:
            st.error("O valor deve ser maior que zero.")
        else:
            if resultado == "Derrota ❌":
                st.session_state.banca -= valor
            else:
                st.session_state.banca += valor
            
            time.sleep(0.5)
            st.rerun()

    st.markdown("---")
    st.subheader("⚙️ Configurações de Risco")
    novo_pct = st.slider("Stake (% da Banca)", 1.0, 5.0, st.session_state.stake_pct, 0.5, key="slider_stake")
    
    if st.button("Salvar Risco"):
        st.session_state.stake_pct = novo_pct
        st.rerun()
```

---

### 📝 **O que fazer com este código:**

1. **Copie TODO o código acima**
2. **Cole no Bloco de Notas**
3. **Salve como:** `waku_score.py` (lembre-se de mudar o tipo para "Todos os arquivos")
4. **Use este arquivo** para fazer o deploy no Streamlit

Este é o código completo e final do Waku Score com todas as funcionalidades! 🚀
