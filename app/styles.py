import streamlit as st


def inject_global_styles() -> None:
    st.markdown(
        """
        <style>
        :root {
            --bow-bg: oklch(0.285 0.022 246);
            --bow-panel: oklch(0.340 0.027 246);
            --bow-panel-2: oklch(0.385 0.034 242);
            --bow-ink: oklch(0.965 0.004 85);
            --bow-muted: oklch(0.805 0.027 247);
            --bow-line: oklch(0.58 0.045 239);
            --bow-primary: oklch(0.69 0.146 74.6);
            --bow-cyan: oklch(0.78 0.132 203);
            --bow-green: oklch(0.72 0.162 148);
            --bow-red: oklch(0.66 0.205 29);
            --bow-orange: oklch(0.74 0.16 62);
            --bow-glass: oklch(0.42 0.030 244 / 0.45);
            --bow-glass-strong: oklch(0.48 0.036 242 / 0.62);
            --bow-glass-border: oklch(0.84 0.09 203 / 0.38);
            --bow-glass-highlight: oklch(1 0 0 / 0.24);
        }

        .stApp {
            background:
                radial-gradient(circle at 18% 8%, oklch(0.50 0.070 222 / 0.34), transparent 34rem),
                radial-gradient(circle at 86% 18%, oklch(0.56 0.090 74 / 0.19), transparent 30rem),
                linear-gradient(180deg, oklch(0.315 0.020 246), oklch(0.270 0.019 248) 54%, oklch(0.235 0.017 250));
            color: var(--bow-ink);
        }

        header[data-testid="stHeader"] {
            background: oklch(0.22 0.018 248 / 0.68);
            backdrop-filter: blur(18px) saturate(1.25);
        }

        [data-testid="stSidebar"] {
            background:
                linear-gradient(180deg, oklch(0.310 0.022 246 / 0.96), oklch(0.255 0.019 250 / 0.96));
            border-right: 1px solid var(--bow-line);
        }

        [data-testid="stSidebar"] * {
            color: var(--bow-ink);
        }

        [data-testid="stRadio"] div[role="radiogroup"] {
            gap: 7px;
        }

        [data-testid="stRadio"] label {
            position: relative;
            min-height: 38px;
            margin: 0;
            padding: 8px 12px;
            border: 1px solid oklch(0.62 0.10 214 / 0.18);
            border-radius: 999px;
            background:
                linear-gradient(135deg, var(--bow-glass-highlight), transparent 38%),
                linear-gradient(180deg, var(--bow-glass), oklch(0.285 0.020 248 / 0.48));
            backdrop-filter: blur(18px) saturate(1.35);
            box-shadow:
                inset 0 1px 0 oklch(1 0 0 / 0.12),
                inset 0 -1px 0 oklch(0 0 0 / 0.18);
            transition: transform 160ms ease-out, border-color 160ms ease-out, background 160ms ease-out, box-shadow 160ms ease-out;
            overflow: hidden;
        }

        [data-testid="stRadio"] label:before {
            content: "";
            position: absolute;
            inset: 1px auto 1px -45%;
            width: 42%;
            border-radius: inherit;
            background: linear-gradient(90deg, transparent, oklch(1 0 0 / 0.22), transparent);
            transform: skewX(-18deg);
            opacity: 0;
            pointer-events: none;
            transition: transform 260ms ease-out, opacity 180ms ease-out;
        }

        [data-testid="stRadio"] label:hover {
            border-color: oklch(0.82 0.13 203 / 0.42);
            background:
                linear-gradient(135deg, oklch(1 0 0 / 0.22), transparent 38%),
                linear-gradient(180deg, var(--bow-glass-strong), oklch(0.315 0.024 248 / 0.58));
        }

        [data-testid="stRadio"] label:hover:before {
            opacity: 1;
            transform: translateX(320%) skewX(-18deg);
        }

        [data-testid="stRadio"] label:active {
            transform: scale(0.975);
        }

        [data-testid="stRadio"] label:has(input:checked) {
            border-color: oklch(0.78 0.132 203 / 0.76);
            background:
                linear-gradient(135deg, oklch(1 0 0 / 0.24), transparent 40%),
                linear-gradient(180deg, oklch(0.48 0.070 220 / 0.66), oklch(0.335 0.032 248 / 0.70));
            box-shadow:
                inset 0 1px 0 oklch(1 0 0 / 0.22),
                0 0 0 1px oklch(0.78 0.132 203 / 0.18),
                0 0 18px oklch(0.78 0.132 203 / 0.16);
        }

        [data-testid="stRadio"] label:has(input:focus-visible),
        div[data-baseweb="select"]:focus-within > div,
        div[data-baseweb="input"]:focus-within {
            outline: 2px solid oklch(0.78 0.132 203 / 0.78);
            outline-offset: 2px;
        }

        .block-container {
            max-width: 1280px;
            padding-top: 1.4rem;
            padding-bottom: 3rem;
        }

        .block-container,
        [data-testid="stSidebar"],
        [data-testid="stHeader"] {
            font-family: "Avenir Next", "SF Pro Display", "Manrope", ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        }

        .section-label {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            margin: 12px 0 10px;
            color: var(--bow-cyan);
            font-size: 0.84rem;
            font-weight: 850;
        }

        .section-label:before {
            content: "";
            width: 8px;
            height: 8px;
            border-radius: 999px;
            background: var(--bow-primary);
            box-shadow: 0 0 16px var(--bow-primary);
        }

        h1, h2, h3 {
            color: var(--bow-ink);
            letter-spacing: 0;
            font-family: "Avenir Next", "SF Pro Display", "Manrope", ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
            font-weight: 900;
            text-shadow:
                0 1px 0 oklch(1 0 0 / 0.12),
                0 14px 30px oklch(0 0 0 / 0.16);
        }

        p, li, label, span, div {
            font-family: ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        }

        div[data-testid="stMetric"] {
            background:
                linear-gradient(135deg, oklch(1 0 0 / 0.09), transparent 42%),
                linear-gradient(180deg, oklch(0.44 0.034 246 / 0.72), oklch(0.34 0.026 248 / 0.78));
            border: 1px solid var(--bow-line);
            border-radius: 20px;
            padding: 1rem;
            backdrop-filter: blur(18px) saturate(1.25);
            box-shadow:
                0 16px 30px oklch(0 0 0 / 0.11),
                inset 0 1px 0 oklch(1 0 0 / 0.15);
            transform: translateZ(0);
            transition: transform 180ms cubic-bezier(.2,.9,.2,1.35), box-shadow 180ms ease-out, border-color 180ms ease-out;
        }

        div[data-testid="stMetric"]:hover {
            transform: translateY(-4px);
            border-color: oklch(0.78 0.132 203 / 0.52);
            box-shadow:
                0 22px 36px oklch(0 0 0 / 0.14),
                inset 0 1px 0 oklch(1 0 0 / 0.20);
        }

        div[data-testid="stMetric"] label {
            color: var(--bow-muted);
        }

        div[data-testid="stMetricValue"] {
            color: var(--bow-ink);
        }

        div[data-baseweb="select"] > div,
        div[data-baseweb="input"],
        div[data-baseweb="datepicker"] input {
            border: 1px solid var(--bow-glass-border);
            border-radius: 12px;
            background:
                linear-gradient(135deg, oklch(1 0 0 / 0.17), transparent 42%),
                linear-gradient(180deg, oklch(0.44 0.030 246 / 0.58), oklch(0.315 0.021 248 / 0.60));
            backdrop-filter: blur(18px) saturate(1.35);
            box-shadow:
                inset 0 1px 0 oklch(1 0 0 / 0.16),
                inset 0 -1px 0 oklch(0 0 0 / 0.24);
            transition: transform 160ms ease-out, border-color 160ms ease-out, background 160ms ease-out, box-shadow 160ms ease-out;
        }

        div[data-baseweb="select"] > div:hover,
        div[data-baseweb="input"]:hover,
        div[data-baseweb="datepicker"] input:hover {
            border-color: oklch(0.78 0.132 203 / 0.58);
            background:
                linear-gradient(135deg, oklch(1 0 0 / 0.22), transparent 42%),
                linear-gradient(180deg, oklch(0.49 0.036 245 / 0.68), oklch(0.350 0.024 248 / 0.62));
        }

        div[data-baseweb="select"] > div:active,
        div[data-baseweb="input"]:active {
            transform: scale(0.992);
        }

        [data-baseweb="popover"] [role="listbox"],
        [data-baseweb="popover"] [role="dialog"] {
            border: 1px solid var(--bow-glass-border);
            border-radius: 12px;
            background: oklch(0.325 0.022 248 / 0.94);
            backdrop-filter: blur(22px) saturate(1.45);
            box-shadow: 0 12px 28px oklch(0 0 0 / 0.34);
            overflow: hidden;
        }

        [data-baseweb="tag"] {
            border: 1px solid oklch(0.78 0.132 203 / 0.38);
            border-radius: 999px;
            background:
                linear-gradient(135deg, oklch(1 0 0 / 0.18), transparent 45%),
                oklch(0.40 0.04 222 / 0.70);
            color: var(--bow-ink);
        }

        .st-key-page_nav {
            margin: 12px 0 18px;
        }

        .st-key-page_nav [data-testid="stHorizontalBlock"] {
            gap: 10px;
            flex-wrap: wrap;
        }

        .st-key-page_nav .stButton {
            width: auto !important;
        }

        .st-key-page_nav .stButton > button {
            min-height: 42px;
            padding: 0 15px;
            border-radius: 16px;
            font-weight: 850;
            background:
                linear-gradient(145deg, oklch(1 0 0 / 0.24), transparent 36%),
                linear-gradient(180deg, oklch(0.50 0.036 240 / 0.52), oklch(0.30 0.020 248 / 0.56));
            backdrop-filter: blur(22px) saturate(1.44);
            box-shadow:
                inset 0 1px 0 oklch(1 0 0 / 0.24),
                inset 0 -1px 0 oklch(0 0 0 / 0.18);
        }

        .st-key-page_nav .stButton > button[kind="primary"] {
            border-color: oklch(0.78 0.15 73 / 0.72);
            background:
                linear-gradient(135deg, oklch(1 0 0 / 0.28), transparent 38%),
                linear-gradient(180deg, oklch(0.70 0.13 73 / 0.54), oklch(0.36 0.05 70 / 0.60));
            box-shadow:
                inset 0 1px 0 oklch(1 0 0 / 0.28),
                0 0 20px oklch(0.78 0.15 73 / 0.16);
        }

        [data-testid="stPlotlyChart"] {
            position: relative;
            border: 1px solid oklch(0.84 0.09 203 / 0.30);
            border-radius: 24px;
            padding: 10px;
            background:
                radial-gradient(circle at 16% 8%, oklch(0.74 0.14 203 / 0.12), transparent 16rem),
                linear-gradient(145deg, oklch(1 0 0 / 0.16), transparent 36%),
                linear-gradient(180deg, oklch(0.46 0.030 246 / 0.46), oklch(0.31 0.022 250 / 0.58));
            backdrop-filter: blur(24px) saturate(1.38);
            box-shadow:
                0 22px 42px oklch(0 0 0 / 0.14),
                inset 0 1px 0 oklch(1 0 0 / 0.18),
                inset 0 -1px 0 oklch(0 0 0 / 0.18);
            transform: perspective(900px) rotateX(0deg) translateZ(0);
            transition: transform 180ms cubic-bezier(.2,.9,.2,1.28), box-shadow 180ms ease-out, border-color 180ms ease-out;
            overflow: hidden;
        }

        [data-testid="stPlotlyChart"]:before {
            content: "";
            position: absolute;
            inset: 1px auto 1px -42%;
            width: 36%;
            border-radius: inherit;
            background: linear-gradient(90deg, transparent, oklch(1 0 0 / 0.18), transparent);
            transform: skewX(-18deg);
            pointer-events: none;
            opacity: 0;
            transition: transform 280ms ease-out, opacity 160ms ease-out;
            z-index: 2;
        }

        [data-testid="stPlotlyChart"]:hover {
            border-color: oklch(0.84 0.09 203 / 0.52);
            transform: perspective(900px) rotateX(1.2deg) translateY(-4px);
            box-shadow:
                0 28px 48px oklch(0 0 0 / 0.16),
                inset 0 1px 0 oklch(1 0 0 / 0.22),
                0 0 24px oklch(0.78 0.132 203 / 0.10);
        }

        [data-testid="stPlotlyChart"]:hover:before {
            opacity: 1;
            transform: translateX(360%) skewX(-18deg);
        }

        [data-testid="stPlotlyChart"]:active {
            animation: bow-jelly-chart 430ms cubic-bezier(.18, .89, .32, 1.28);
        }

        @keyframes bow-jelly-chart {
            0% { transform: perspective(900px) scale(1) rotateX(1deg); }
            28% { transform: perspective(900px) scale(0.986, 1.018) rotateX(0deg); }
            62% { transform: perspective(900px) scale(1.012, 0.992) rotateX(1.4deg); }
            100% { transform: perspective(900px) scale(1) rotateX(1.2deg); }
        }

        .stButton > button,
        .stDownloadButton > button,
        button[data-testid="baseButton-secondary"],
        button[data-testid="baseButton-primary"] {
            position: relative;
            min-height: 40px;
            border: 1px solid var(--bow-glass-border);
            border-radius: 999px;
            color: var(--bow-ink);
            background:
                linear-gradient(135deg, oklch(1 0 0 / 0.20), transparent 42%),
                linear-gradient(180deg, oklch(0.46 0.036 246 / 0.62), oklch(0.32 0.018 248 / 0.64));
            backdrop-filter: blur(18px) saturate(1.35);
            box-shadow:
                inset 0 1px 0 oklch(1 0 0 / 0.18),
                inset 0 -1px 0 oklch(0 0 0 / 0.22);
            transition: transform 150ms ease-out, border-color 150ms ease-out, background 150ms ease-out, box-shadow 150ms ease-out;
            overflow: hidden;
        }

        .stButton > button:hover,
        .stDownloadButton > button:hover,
        button[data-testid="baseButton-secondary"]:hover,
        button[data-testid="baseButton-primary"]:hover {
            border-color: oklch(0.78 0.132 203 / 0.70);
            box-shadow:
                inset 0 1px 0 oklch(1 0 0 / 0.24),
                0 0 0 1px oklch(0.78 0.132 203 / 0.16),
                0 0 18px oklch(0.78 0.132 203 / 0.14);
        }

        .stButton > button:active,
        .stDownloadButton > button:active,
        button[data-testid="baseButton-secondary"]:active,
        button[data-testid="baseButton-primary"]:active {
            transform: scale(0.97);
            background:
                linear-gradient(135deg, oklch(1 0 0 / 0.14), transparent 42%),
                linear-gradient(180deg, oklch(0.36 0.026 248 / 0.72), oklch(0.27 0.014 248 / 0.74));
        }

        .bow-hero {
            position: relative;
            overflow: hidden;
            min-height: 315px;
            border: 1px solid oklch(0.38 0.06 230);
            border-radius: 14px;
            padding: 28px;
            background:
                linear-gradient(115deg, oklch(0.16 0.04 249 / 0.96), oklch(0.11 0.012 260 / 0.96) 56%, oklch(0.23 0.07 71 / 0.82)),
                linear-gradient(90deg, transparent 0 48%, oklch(0.78 0.132 203 / 0.18) 48% 49%, transparent 49% 100%);
            box-shadow: 0 8px 28px oklch(0 0 0 / 0.22);
        }

        .bow-hero:before {
            content: "";
            position: absolute;
            inset: 0;
            background-image:
                linear-gradient(oklch(1 0 0 / 0.035) 1px, transparent 1px),
                linear-gradient(90deg, oklch(1 0 0 / 0.03) 1px, transparent 1px);
            background-size: 34px 34px;
            mask-image: linear-gradient(90deg, black, transparent 78%);
            pointer-events: none;
        }

        .bow-kicker {
            position: relative;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            color: var(--bow-cyan);
            font-size: 0.82rem;
            font-weight: 700;
        }

        .bow-kicker:before {
            content: "";
            width: 9px;
            height: 9px;
            border-radius: 999px;
            background: var(--bow-green);
            box-shadow: 0 0 12px var(--bow-green);
        }

        .bow-title {
            position: relative;
            margin: 12px 0 8px;
            color: var(--bow-ink);
            font-size: 4.7rem;
            line-height: 0.93;
            font-weight: 900;
            letter-spacing: -0.025em;
            text-wrap: balance;
        }

        .bow-subtitle {
            position: relative;
            max-width: 62ch;
            color: var(--bow-muted);
            font-size: 1.05rem;
            line-height: 1.65;
            margin-bottom: 18px;
        }

        .bow-pill-row {
            position: relative;
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
        }

        .bow-pill {
            border: 1px solid oklch(0.44 0.055 246);
            background: oklch(0.18 0.03 248 / 0.72);
            color: var(--bow-ink);
            border-radius: 999px;
            padding: 8px 12px;
            font-size: 0.84rem;
        }

        .bow-panel {
            border: 1px solid var(--bow-line);
            border-radius: 18px;
            background:
                linear-gradient(135deg, oklch(1 0 0 / 0.14), transparent 42%),
                linear-gradient(180deg, oklch(0.44 0.030 246 / 0.62), oklch(0.33 0.023 248 / 0.72));
            padding: 20px;
            backdrop-filter: blur(22px) saturate(1.35);
            box-shadow: 0 18px 34px oklch(0 0 0 / 0.12), inset 0 1px 0 oklch(1 0 0 / 0.16);
        }

        .bow-card-title {
            color: var(--bow-muted);
            font-size: 0.78rem;
            font-weight: 700;
            margin-bottom: 8px;
        }

        .bow-card-value {
            color: var(--bow-ink);
            font-size: 1.35rem;
            font-weight: 800;
            margin-bottom: 4px;
        }

        .bow-card-note {
            color: var(--bow-muted);
            font-size: 0.9rem;
            line-height: 1.45;
        }

        .game-info-grid {
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 12px;
            margin-top: 10px;
        }

        .game-info-item {
            min-width: 0;
            border: 1px solid oklch(0.72 0.06 225 / 0.28);
            border-radius: 14px;
            padding: 12px;
            background: oklch(0.42 0.027 248 / 0.34);
        }

        .game-info-label {
            color: var(--bow-muted);
            font-size: 0.78rem;
            font-weight: 750;
            margin-bottom: 5px;
        }

        .game-info-value {
            color: var(--bow-ink);
            font-size: 1rem;
            font-weight: 800;
            overflow-wrap: anywhere;
        }

        .decision-shell {
            border-radius: 18px;
            padding: 22px;
            border: 1px solid var(--decision-line);
            background:
                linear-gradient(135deg, oklch(1 0 0 / 0.12), transparent 40%),
                linear-gradient(135deg, var(--decision-bg), oklch(0.32 0.026 250 / 0.72));
            backdrop-filter: blur(22px) saturate(1.34);
            box-shadow: 0 18px 34px oklch(0 0 0 / 0.13), inset 0 1px 0 oklch(1 0 0 / 0.14);
        }

        .decision-label {
            color: var(--decision-color);
            font-size: 0.95rem;
            font-weight: 900;
        }

        .decision-score {
            color: var(--bow-ink);
            font-size: 4.25rem;
            line-height: 0.98;
            font-weight: 900;
            letter-spacing: -0.035em;
        }

        .decision-caption {
            color: var(--bow-muted);
            margin-top: 8px;
        }

        .status-buy {
            --decision-color: var(--bow-green);
            --decision-bg: oklch(0.33 0.078 151 / 0.64);
            --decision-line: oklch(0.59 0.14 151);
        }

        .status-wait {
            --decision-color: var(--bow-orange);
            --decision-bg: oklch(0.36 0.075 67 / 0.58);
            --decision-line: oklch(0.64 0.12 67);
        }

        .status-skip {
            --decision-color: var(--bow-red);
            --decision-bg: oklch(0.34 0.09 28 / 0.62);
            --decision-line: oklch(0.58 0.16 29);
        }

        .alert-critical, .alert-high, .alert-medium {
            border-radius: 18px;
            padding: 16px;
            border: 1px solid;
            background:
                linear-gradient(135deg, oklch(1 0 0 / 0.10), transparent 42%),
                linear-gradient(180deg, var(--alert-bg), oklch(0.31 0.020 248 / 0.64));
            backdrop-filter: blur(18px) saturate(1.30);
        }

        .alert-critical {
            --alert-bg: oklch(0.34 0.09 29 / 0.72);
            border-color: oklch(0.62 0.18 29);
            box-shadow: 0 0 18px oklch(0.62 0.18 29 / 0.22);
        }

        .alert-high {
            --alert-bg: oklch(0.36 0.095 55 / 0.66);
            border-color: oklch(0.68 0.15 55);
            box-shadow: 0 0 18px oklch(0.68 0.15 55 / 0.18);
        }

        .alert-medium {
            --alert-bg: oklch(0.35 0.07 82 / 0.58);
            border-color: oklch(0.72 0.13 82);
        }

        .arch-flow {
            display: grid;
            grid-template-columns: repeat(5, minmax(120px, 1fr));
            gap: 10px;
            align-items: stretch;
        }

        .arch-node {
            min-height: 88px;
            border: 1px solid var(--bow-line);
            border-radius: 10px;
            background: oklch(0.37 0.028 248 / 0.80);
            padding: 12px;
            color: var(--bow-ink);
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            font-weight: 750;
        }

        .arch-arrow {
            display: none;
        }

        .todo-badge {
            display: inline-block;
            color: oklch(0.16 0.035 70);
            background: var(--bow-primary);
            border-radius: 999px;
            padding: 5px 10px;
            font-weight: 800;
            font-size: 0.8rem;
        }

        [data-testid="stDataFrame"] {
            border: 1px solid var(--bow-line);
            border-radius: 16px;
            overflow: hidden;
        }

        .analyzer-preview {
            margin: 8px 0 18px;
            display: grid;
            grid-template-columns: minmax(0, 1fr) minmax(230px, 0.36fr);
            gap: 18px;
            align-items: stretch;
            border: 1px solid oklch(0.84 0.09 203 / 0.32);
            border-radius: 24px;
            padding: 22px;
            background:
                radial-gradient(circle at 10% 10%, oklch(0.72 0.16 292 / 0.18), transparent 18rem),
                linear-gradient(135deg, oklch(1 0 0 / 0.16), transparent 38%),
                oklch(0.38 0.030 246 / 0.50);
            backdrop-filter: blur(24px) saturate(1.35);
            box-shadow: 0 18px 40px oklch(0 0 0 / 0.14), inset 0 1px 0 oklch(1 0 0 / 0.18);
        }

        .analyzer-preview h2 {
            margin: 4px 0 8px;
            font-size: 2.1rem;
            line-height: 1.04;
            text-wrap: balance;
        }

        .analyzer-preview p {
            margin: 0;
            color: var(--bow-muted);
            max-width: 64ch;
            line-height: 1.55;
        }

        .preview-result {
            border: 1px solid var(--preview-line);
            border-radius: 20px;
            padding: 18px;
            background:
                linear-gradient(135deg, oklch(1 0 0 / 0.18), transparent 40%),
                var(--preview-bg);
            box-shadow: inset 0 1px 0 oklch(1 0 0 / 0.16);
        }

        .preview-result span,
        .preview-result small {
            display: block;
            color: var(--bow-muted);
            font-weight: 750;
        }

        .preview-result strong {
            display: block;
            margin: 8px 0;
            color: var(--preview-ink);
            font-size: 2.8rem;
            line-height: 0.92;
            font-weight: 950;
        }

        .preview-result.status-buy {
            --preview-line: oklch(0.72 0.16 148 / 0.58);
            --preview-bg: oklch(0.42 0.08 148 / 0.42);
            --preview-ink: var(--bow-green);
        }

        .preview-result.status-wait {
            --preview-line: oklch(0.78 0.15 73 / 0.58);
            --preview-bg: oklch(0.45 0.08 73 / 0.42);
            --preview-ink: var(--bow-primary);
        }

        .preview-result.status-skip {
            --preview-line: oklch(0.66 0.20 29 / 0.58);
            --preview-bg: oklch(0.42 0.09 29 / 0.42);
            --preview-ink: var(--bow-red);
        }

        .floating-card-grid {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 16px;
            margin: 18px 0 22px;
            perspective: 900px;
        }

        .decision-float-card {
            min-height: 166px;
            border: 1px solid oklch(0.84 0.08 203 / 0.27);
            border-radius: 22px;
            padding: 20px;
            background:
                linear-gradient(135deg, oklch(1 0 0 / 0.13), transparent 42%),
                oklch(0.37 0.030 248 / 0.48);
            backdrop-filter: blur(20px) saturate(1.32);
            box-shadow: 0 18px 32px oklch(0 0 0 / 0.12), inset 0 1px 0 oklch(1 0 0 / 0.16);
            transform: translateZ(0);
            transition: transform 180ms ease-out, box-shadow 180ms ease-out, border-color 180ms ease-out;
        }

        .decision-float-card.raised {
            transform: translateY(-10px) rotateX(2deg);
        }

        .decision-float-card:hover {
            transform: translateY(-12px) rotateX(2deg);
            border-color: oklch(0.84 0.09 203 / 0.48);
            box-shadow: 0 24px 40px oklch(0 0 0 / 0.16), inset 0 1px 0 oklch(1 0 0 / 0.20);
        }

        .decision-float-card span {
            color: var(--bow-cyan);
            font-size: 0.82rem;
            font-weight: 850;
        }

        .decision-float-card strong {
            display: block;
            margin: 10px 0 8px;
            color: var(--bow-ink);
            font-size: 1.2rem;
        }

        .decision-float-card p {
            color: var(--bow-muted);
            margin: 0;
            line-height: 1.5;
        }

        .dashboard-divider {
            height: 1px;
            margin: 34px 0 22px;
            background: linear-gradient(90deg, transparent, oklch(0.84 0.09 203 / 0.52), transparent);
        }

        @media (max-width: 900px) {
            .bow-title {
                font-size: 3.15rem;
            }
            .bow-hero {
                min-height: 260px;
                padding: 22px;
            }
            .game-info-grid {
                grid-template-columns: 1fr;
            }
            .analyzer-preview,
            .floating-card-grid {
                grid-template-columns: 1fr;
            }
            .decision-float-card.raised {
                transform: none;
            }
            .arch-flow {
                grid-template-columns: 1fr;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
