import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.set_page_config(
    page_title="Emotional Supply Chains",
    page_icon="🫙",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Palette ────────────────────────────────────────────────────────────────────
CORAL         = "#ff6b6b"
CORAL_DARK    = "#c0392b"
CORAL_LIGHT   = "#ffd6cc"
BG            = "#0e0e0e"
BG_CARD       = "#161616"
BG_CARD2      = "#1c1c1c"
GRAY          = "#888888"
BOUNDED       = "#2ecc71"
LINEAR        = "#f39c12"
EXPONENTIAL   = CORAL

# ── CSS ────────────────────────────────────────────────────────────────────────
st.markdown(f"""
<style>
  .stApp {{ background:{BG}; color:#e0e0e0; }}
  .main .block-container {{ padding-top:2rem; max-width:1400px; }}
  section[data-testid="stSidebar"] {{ display:none; }}

  .card {{
    background:{BG_CARD};
    border-radius:12px;
    padding:1.5rem 1.8rem;
    margin-bottom:0.8rem;
  }}
  .card-accent-coral  {{ border-left:4px solid {CORAL}; }}
  .card-accent-green  {{ border-left:4px solid {BOUNDED}; }}
  .card-accent-yellow {{ border-left:4px solid {LINEAR}; }}

  .ws-big {{
    font-size:4.5rem;
    font-weight:700;
    line-height:1;
    font-family:Georgia,serif;
  }}
  .label-sm {{
    font-size:0.75rem;
    letter-spacing:0.12em;
    text-transform:uppercase;
    font-family:monospace;
    color:{GRAY};
  }}
  .regime-pill {{
    display:inline-block;
    padding:0.35em 1.1em;
    border-radius:999px;
    font-size:0.82rem;
    font-weight:700;
    font-family:monospace;
    letter-spacing:0.08em;
    margin-top:0.6rem;
  }}
  .note {{
    font-family:Georgia,serif;
    font-style:italic;
    font-size:0.9rem;
    color:{GRAY};
    margin-top:0.4rem;
  }}
  .tier-block {{
    background:{BG_CARD2};
    border-radius:8px;
    padding:0.9rem 1rem;
    text-align:center;
  }}
  .tier-val {{
    font-size:1.6rem;
    font-weight:600;
    font-family:Georgia,serif;
    line-height:1.2;
  }}
  [data-testid="stSlider"] label {{
    color:#ccc !important;
    font-family:monospace !important;
    font-size:0.85rem !important;
  }}
  .stButton > button {{
    background:{BG_CARD};
    color:#999;
    border:1px solid #2a2a2a;
    font-family:monospace;
    font-size:0.78rem;
    width:100%;
  }}
  .stButton > button:hover {{
    border-color:{CORAL};
    color:{CORAL};
    background:{BG_CARD};
  }}
  hr {{ border-color:#1e1e1e; }}
</style>
""", unsafe_allow_html=True)


# ── Model ──────────────────────────────────────────────────────────────────────
def compute_tiers(beta: float, gamma: float, m: int, K: int):
    """Per-node investment C at each tier (key = tier index, 1 = direct admirer of Sink)."""
    if K < 2:
        return {1: float(beta)}, float(beta) * m
    C = {K - 1: float(beta)}
    for k in range(K - 2, 0, -1):
        C[k] = beta + gamma * m * C[k + 1]
    W_S = m * C[1]
    return C, W_S


def ws_closed(beta: float, gamma: float, m: int, K: int) -> float:
    """W(S) = β·m·[(γm)^(K−1) − 1] / (γm − 1), linear case when γm = 1."""
    if K < 2:
        return 0.0
    gm = gamma * m
    if abs(gm - 1.0) < 1e-9:
        return beta * m * (K - 1)
    return beta * m * (gm ** (K - 1) - 1) / (gm - 1)


def regime(gamma: float, m: int):
    gm = gamma * m
    if abs(gm - 1.0) < 0.015:
        return "LINEAR", LINEAR, f"γm ≈ 1"
    elif gm < 1.0:
        return "BOUNDED", BOUNDED, f"γm = {gm:.2f}"
    else:
        return "EXPONENTIAL", EXPONENTIAL, f"γm = {gm:.2f}"


# ── Session defaults ───────────────────────────────────────────────────────────
if "beta"  not in st.session_state: st.session_state.beta  = 10
if "gamma" not in st.session_state: st.session_state.gamma = 0.50
if "m"     not in st.session_state: st.session_state.m     = 3
if "K"     not in st.session_state: st.session_state.K     = 3


# ── Header ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center;padding:0.5rem 0 0.2rem;">
  <h1 style="font-size:1.9rem;color:#e0e0e0;margin-bottom:0.15rem;font-family:Georgia,serif;">
    Emotional Supply Chains
  </h1>
  <p style="color:#555;font-style:italic;font-size:0.9rem;font-family:Georgia,serif;">
    "You cannot win a game you did not know you were playing."
  </p>
</div>
""", unsafe_allow_html=True)
st.divider()


# ── Layout ─────────────────────────────────────────────────────────────────────
col_ctrl, col_right = st.columns([1, 3], gap="large")

with col_ctrl:
    st.markdown('<div class="label-sm" style="margin-bottom:0.6rem;">Parameters</div>',
                unsafe_allow_html=True)

    beta  = st.slider("β — baseline energy",  1,  50, st.session_state.beta,  1)
    gamma = st.slider("γ — pass-through rate", 0.0, 1.0, st.session_state.gamma, 0.01, format="%.2f")
    m     = st.slider("m — branching factor",  1,   6, st.session_state.m,     1)
    K     = st.slider("K — total tiers",       2,   8, st.session_state.K,     1)

    if st.button("↩  Reset to paper example  (β=10, γ=0.5, m=3, K=3)"):
        st.session_state.beta  = 10
        st.session_state.gamma = 0.50
        st.session_state.m     = 3
        st.session_state.K     = 3
        st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    reg_name, reg_color, reg_label = regime(gamma, m)
    st.markdown(f"""
    <div class="card" style="border-left:4px solid {reg_color};">
      <div class="label-sm">Regime</div>
      <div class="regime-pill" style="background:{reg_color}20;color:{reg_color};border:1px solid {reg_color}44;">
        {reg_name}
      </div>
      <div class="note" style="margin-top:0.5rem;">{reg_label}</div>
      <div class="note" style="margin-top:0.2rem; font-size:0.78rem;">
        {'Sink ego grows exponentially with depth' if reg_name == 'EXPONENTIAL'
         else 'Sink ego grows linearly with depth' if reg_name == 'LINEAR'
         else 'Sink ego is bounded — there is hope'}
      </div>
    </div>
    """, unsafe_allow_html=True)


# ── Compute ────────────────────────────────────────────────────────────────────
C_tiers, W_S = compute_tiers(beta, gamma, m, K)
leverage = W_S / beta if beta > 0 else 0
reg_name, reg_color, reg_label = regime(gamma, m)

with col_right:
    top_left, top_center, top_right = st.columns([2, 1, 2], gap="medium")

    # ── Arborescence ──────────────────────────────────────────────────────────
    with top_left:
        fig_tree = go.Figure()
        fig_tree.update_layout(
            paper_bgcolor=BG_CARD, plot_bgcolor=BG_CARD,
            margin=dict(l=5, r=5, t=5, b=5), height=290,
            showlegend=False,
            xaxis=dict(visible=False, range=[-0.05, 1.05]),
            yaxis=dict(visible=False, range=[-0.1, 1.1]),
        )

        # Positions: tier k → y = 1 - k/(K-1), x spread
        def x_positions(count):
            return [0.5] if count == 1 else [i / (count - 1) for i in range(count)]

        pos = {}  # (tier, idx) → (x, y)
        for tk in range(K):
            cnt = 1 if tk == 0 else m ** tk
            ys  = 1.0 - tk / max(K - 1, 1)
            for i, x in enumerate(x_positions(cnt)):
                pos[(tk, i)] = (x, ys)

        # Edges
        ex, ey = [], []
        for tk in range(1, K):
            cnt = 1 if tk == 0 else m ** tk
            for idx in range(cnt):
                pidx = idx // m
                cx, cy = pos[(tk, idx)]
                px, py = pos[(tk - 1, pidx)]
                ex += [cx, px, None]
                ey += [cy, py, None]

        fig_tree.add_trace(go.Scatter(x=ex, y=ey, mode="lines",
            line=dict(color="#2a2a2a", width=1.5), hoverinfo="none"))

        # Nodes
        for tk in range(K):
            cnt = 1 if tk == 0 else m ** tk
            for idx in range(cnt):
                x, y = pos[(tk, idx)]
                if tk == 0:
                    col, sz, txt = reg_color, 26, "S"
                elif tk == K - 1:
                    col, sz, txt = "#252525", 10, ""
                else:
                    c_val = C_tiers.get(tk, beta)
                    sz  = max(12, min(22, int(c_val / beta * 9)))
                    col = "#3a1a1a"
                    txt = ""

                fig_tree.add_trace(go.Scatter(
                    x=[x], y=[y], mode="markers+text",
                    marker=dict(size=sz, color=col,
                                line=dict(color="#444", width=1)),
                    text=[txt],
                    textposition="middle center",
                    textfont=dict(color="white", size=10, family="Georgia"),
                    hoverinfo="none",
                ))

        # W(S) annotation on Sink
        sink_x, sink_y = pos[(0, 0)]
        fig_tree.add_annotation(
            x=sink_x, y=sink_y + 0.12, text=f"W={W_S:.0f}",
            showarrow=False, font=dict(size=9, color=reg_color, family="monospace"),
        )
        st.plotly_chart(fig_tree, use_container_width=True,
                        config={"displayModeBar": False})

    # ── W(S) Big Number ───────────────────────────────────────────────────────
    with top_center:
        st.markdown(f"""
        <div class="card card-accent-coral" style="border-left-color:{reg_color};
             text-align:center; padding:1.8rem 1rem; min-height:260px;
             display:flex; flex-direction:column; justify-content:center;">
          <div class="label-sm">W(S) — Sink's wealth</div>
          <div class="ws-big" style="color:{reg_color}; margin:0.5rem 0;">
            {W_S:.0f}
          </div>
          <div style="color:#555;font-family:monospace;font-size:0.8rem;">units</div>
          <div class="note" style="margin-top:1rem;">
            {leverage:.1f}× a single person's effort
          </div>
          <div class="note" style="font-size:0.78rem; margin-top:0.3rem;">
            deficit: –{beta} per node, always
          </div>
        </div>
        """, unsafe_allow_html=True)

    # ── W(S) vs K Chart ───────────────────────────────────────────────────────
    with top_right:
        K_range = list(range(2, 13))
        W_vals  = [ws_closed(beta, gamma, m, k) for k in K_range]

        fig_k = go.Figure()
        fig_k.add_trace(go.Scatter(
            x=K_range, y=W_vals,
            mode="lines", line=dict(color=reg_color, width=2.5),
            fill="tozeroy", fillcolor=f"{reg_color}12",
            hovertemplate="K=%{x}<br>W(S)=%{y:.1f}<extra></extra>",
        ))
        fig_k.add_trace(go.Scatter(
            x=[K], y=[ws_closed(beta, gamma, m, K)],
            mode="markers",
            marker=dict(size=11, color=reg_color,
                        line=dict(color="white", width=2)),
            hovertemplate=f"Current: K={K}, W(S)={W_S:.1f}<extra></extra>",
        ))
        fig_k.add_hline(y=beta, line_dash="dot", line_color="#2a2a2a",
                        annotation_text=f"  β={beta}",
                        annotation_font=dict(color="#444", size=10))

        fig_k.update_layout(
            paper_bgcolor=BG_CARD, plot_bgcolor=BG_CARD,
            margin=dict(l=10, r=10, t=10, b=40), height=290,
            showlegend=False,
            xaxis=dict(title="K (tiers)", color="#444", gridcolor="#1a1a1a",
                       tickfont=dict(color="#555"), title_font=dict(color="#555")),
            yaxis=dict(title="W(S)", color="#444", gridcolor="#1a1a1a",
                       tickfont=dict(color="#555"), title_font=dict(color="#555")),
            font=dict(family="monospace", color="#555"),
        )
        st.plotly_chart(fig_k, use_container_width=True,
                        config={"displayModeBar": False})

    # ── Per-tier Breakdown ────────────────────────────────────────────────────
    st.divider()
    st.markdown('<div class="label-sm" style="margin-bottom:0.7rem;">Per-tier breakdown — what each tier keeps vs. passes upward</div>',
                unsafe_allow_html=True)

    tier_cols = st.columns(K)
    for tk in range(K):
        with tier_cols[tk]:
            if tk == 0:
                label   = "The Sink"
                value   = f"+{W_S:.0f}"
                deficit = "accumulates all"
                color   = reg_color
            elif tk == K - 1:
                c_val   = C_tiers.get(tk, beta)
                label   = f"Tier {tk}  (base)"
                value   = f"→ {c_val:.0f}"
                deficit = f"deficit: –{beta}"
                color   = "#333"
            else:
                c_val   = C_tiers.get(tk, beta)
                label   = f"Tier {tk}"
                value   = f"→ {c_val:.0f}"
                deficit = f"deficit: –{beta}"
                color   = "#5a2a2a"

            st.markdown(f"""
            <div class="tier-block" style="border-top:3px solid {color};">
              <div class="label-sm">{label}</div>
              <div class="tier-val" style="color:{color};">{value}</div>
              <div class="note" style="font-size:0.78rem;">{deficit}</div>
            </div>
            """, unsafe_allow_html=True)

# ── Footer ─────────────────────────────────────────────────────────────────────
st.divider()
st.markdown(f"""
<div style="text-align:center;padding:0.5rem 0 1rem;">
  <span style="font-family:Georgia,serif;font-style:italic;font-size:0.82rem;color:#333;">
    Emotional Supply Chains · Farid Nahadi · 2026 ·
    <a href="https://github.com/siamsadmanazad/emotional_supply_chain"
       style="color:#444;text-decoration:none;">github</a>
  </span>
</div>
""", unsafe_allow_html=True)
