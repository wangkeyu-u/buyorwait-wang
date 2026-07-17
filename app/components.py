from __future__ import annotations

import base64
from pathlib import Path

import streamlit as st


def hero_section() -> None:
    asset = Path(__file__).parent / "assets" / "buyorwait-shopping-orb.png"
    encoded = base64.b64encode(asset.read_bytes()).decode("ascii")
    template = """
    <section id="bow-home-stage" aria-label="BuyOrWait immersive home">
      <div class="crack-layer" aria-hidden="true"></div>
      <div class="field-layer stars" data-depth="-0.06"></div>
      <div class="field-layer glow-a" data-depth="-0.22"></div>
      <div class="field-layer glow-b" data-depth="0.16"></div>
      <div class="field-layer glass-floor" data-depth="0.04"></div>

      <div class="copy-layer" data-depth="-0.08">
        <div class="hero-kicker"><span></span> AI game purchase timing</div>
        <h1>Buy Now or Wait?</h1>
        <p>
          Let AI analyze price timing, review signals, and deal momentum before you spend.
        </p>
      </div>

      <div class="visual-layer" data-depth="0.20">
        <div class="image-halo"></div>
        <img src="data:image/png;base64,__IMAGE__" alt="" />
        <div class="eye-shine left"></div>
        <div class="eye-shine right"></div>
      </div>

      <div class="float-card card-price" data-depth="-0.34">
        <small>Deal momentum</small>
        <strong>+18%</strong>
        <span>discount pressure rising</span>
      </div>
      <div class="float-card card-ai" data-depth="0.28">
        <small>AI recommendation</small>
        <strong>WAIT</strong>
        <span>review trend is unstable</span>
      </div>
      <div class="float-card card-score" data-depth="-0.18">
        <small>Confidence</small>
        <strong>72</strong>
        <span>near buy threshold</span>
      </div>
      <div class="float-card card-input" data-depth="0.12">
        <small>Steam game URL</small>
        <strong>Hades II</strong>
        <span>AI scan ready</span>
      </div>
    </section>

    <style>
      :root {
        --mx: 0;
        --my: 0;
        --ink: oklch(0.98 0.003 84);
        --muted: oklch(0.79 0.028 255);
        --cyan: oklch(0.82 0.13 202);
        --violet: oklch(0.68 0.16 292);
        --amber: oklch(0.78 0.15 73);
      }
      * { box-sizing: border-box; }
      html,
      body {
        width: 100%;
        height: 100%;
        margin: 0;
        overflow: hidden;
        background: transparent;
        font-family: "Avenir Next", "SF Pro Display", "Manrope", ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      }
      #bow-home-stage {
        position: relative;
        width: 100vw;
        height: 100vh;
        overflow: hidden;
        user-select: none;
        -webkit-user-select: none;
        background:
          radial-gradient(circle at 73% 35%, oklch(0.76 0.13 203 / 0.24), transparent 22rem),
          radial-gradient(circle at 88% 8%, oklch(0.70 0.16 292 / 0.28), transparent 20rem),
          radial-gradient(circle at 17% 77%, oklch(0.79 0.15 73 / 0.16), transparent 23rem),
          linear-gradient(135deg, oklch(0.43 0.030 239), oklch(0.305 0.033 263) 46%, oklch(0.355 0.025 225));
        box-shadow: inset 0 1px 0 oklch(1 0 0 / 0.12);
        perspective: 1300px;
        isolation: isolate;
      }
      #bow-home-stage:before {
        content: "";
        position: absolute;
        inset: 0;
        background-image:
          radial-gradient(circle, oklch(1 0 0 / 0.10) 0 1px, transparent 1px),
          linear-gradient(115deg, transparent 0 38%, oklch(1 0 0 / 0.07), transparent 52%);
        background-size: 54px 54px, auto;
        mask-image: linear-gradient(90deg, black, black 48%, transparent 88%);
        pointer-events: none;
        z-index: 1;
      }
      .field-layer {
        position: absolute;
        pointer-events: none;
        transition: transform 180ms ease-out;
      }
      .stars {
        inset: 0;
        z-index: 1;
        background-image: radial-gradient(circle, oklch(1 0 0 / 0.16) 0 1px, transparent 1.3px);
        background-size: 68px 68px;
        opacity: 0.55;
        transform: translate(calc(var(--mx) * -10px), calc(var(--my) * -8px));
      }
      .glow-a,
      .glow-b {
        border-radius: 999px;
        filter: blur(22px);
      }
      .glow-a {
        width: 310px;
        height: 310px;
        left: 6%;
        top: 14%;
        background: oklch(0.68 0.16 292 / 0.28);
        transform: translate(calc(var(--mx) * -18px), calc(var(--my) * -10px));
      }
      .glow-b {
        width: 220px;
        height: 220px;
        right: 5%;
        bottom: 16%;
        background: oklch(0.82 0.13 202 / 0.20);
        transform: translate(calc(var(--mx) * 20px), calc(var(--my) * 14px));
      }
      .glass-floor {
        z-index: 2;
        left: 12%;
        right: 8%;
        bottom: -11%;
        height: 34%;
        border-radius: 50%;
        background:
          radial-gradient(ellipse at center, oklch(0.85 0.08 203 / 0.20), transparent 68%),
          linear-gradient(90deg, transparent, oklch(1 0 0 / 0.10), transparent);
        filter: blur(2px);
        transform: rotateX(64deg) translate(calc(var(--mx) * 10px), calc(var(--my) * 8px));
      }
      .copy-layer {
        position: absolute;
        z-index: 5;
        left: clamp(24px, 5vw, 72px);
        top: 50%;
        width: min(570px, 46vw);
        transform: translate3d(calc(var(--mx) * -7px), calc(var(--my) * -5px), 0);
        transition: transform 150ms ease-out;
        translate: 0 -50%;
      }
      .hero-kicker {
        display: inline-flex;
        align-items: center;
        gap: 9px;
        min-height: 34px;
        padding: 8px 13px;
        border: 1px solid oklch(0.88 0.08 202 / 0.34);
        border-radius: 999px;
        color: oklch(0.88 0.09 202);
        background: oklch(0.44 0.04 246 / 0.34);
        backdrop-filter: blur(16px) saturate(1.35);
        font-size: 13px;
        font-weight: 850;
      }
      .hero-kicker span {
        width: 9px;
        height: 9px;
        border-radius: 999px;
        background: var(--amber);
        box-shadow: 0 0 18px var(--amber);
      }
      h1 {
        margin: 20px 0 14px;
        color: var(--ink);
        font-size: clamp(60px, 7.2vw, 118px);
        max-width: 9ch;
        line-height: 0.88;
        letter-spacing: 0;
        font-weight: 950;
        text-wrap: balance;
        text-shadow:
          0 1px 0 oklch(1 0 0 / 0.20),
          0 16px 36px oklch(0 0 0 / 0.28),
          0 0 32px oklch(0.82 0.13 202 / 0.12);
      }
      h1:after {
        content: "";
        display: block;
        width: 58%;
        height: 2px;
        margin-top: 15px;
        background: linear-gradient(90deg, oklch(0.83 0.13 203 / 0.0), oklch(0.83 0.13 203 / 0.78), oklch(0.78 0.15 73 / 0.58), transparent);
        box-shadow: 0 0 24px oklch(0.83 0.13 203 / 0.30);
      }
      p {
        margin: 0;
        color: var(--muted);
        max-width: 44ch;
        font-size: 19px;
        line-height: 1.58;
      }
      .visual-layer {
        position: absolute;
        z-index: 4;
        inset: 0;
        transform-style: preserve-3d;
        transform:
          translate3d(calc(var(--mx) * 28px), calc(var(--my) * 18px), 0)
          rotateY(calc(var(--mx) * -8deg))
          rotateX(calc(var(--my) * 5deg));
        transition: transform 150ms ease-out;
      }
      .image-halo {
        position: absolute;
        right: 4%;
        top: 7%;
        width: min(760px, 64vw);
        height: min(760px, 72vh);
        border-radius: 999px;
        background:
          radial-gradient(circle, oklch(0.85 0.12 203 / 0.20), transparent 58%),
          radial-gradient(circle at 60% 42%, oklch(0.76 0.16 292 / 0.20), transparent 48%);
        filter: blur(5px);
      }
      .visual-layer img {
        position: absolute;
        right: -1%;
        top: 1%;
        width: min(970px, 74vw);
        height: 96%;
        object-fit: cover;
        object-position: center;
        border-radius: 28px;
        mask-image: linear-gradient(90deg, transparent 0, black 18%, black 100%);
        filter: saturate(1.10) contrast(1.02) drop-shadow(0 32px 44px oklch(0 0 0 / 0.28));
      }
      .eye-shine {
        position: absolute;
        z-index: 6;
        width: 26px;
        height: 26px;
        border-radius: 999px;
        background: radial-gradient(circle, oklch(0.98 0.02 198), oklch(0.80 0.13 202 / 0.44), transparent 70%);
        box-shadow: 0 0 24px oklch(0.82 0.13 202 / 0.74);
        transform: translate(calc(var(--mx) * 8px), calc(var(--my) * 6px));
      }
      .eye-shine.left { right: 31%; top: 37%; }
      .eye-shine.right { right: 25%; top: 36%; }
      .float-card {
        position: absolute;
        z-index: 7;
        min-width: 172px;
        padding: 15px 16px;
        border: 1px solid oklch(0.95 0.02 250 / 0.30);
        border-radius: 20px;
        color: var(--ink);
        background:
          linear-gradient(135deg, oklch(1 0 0 / 0.26), transparent 42%),
          oklch(0.44 0.036 250 / 0.38);
        backdrop-filter: blur(22px) saturate(1.45);
        box-shadow: 0 18px 32px oklch(0 0 0 / 0.18), inset 0 1px 0 oklch(1 0 0 / 0.22);
        transition: transform 170ms ease-out, box-shadow 170ms ease-out;
      }
      .float-card:hover {
        transform: translateY(-7px) scale(1.02);
        box-shadow: 0 22px 34px oklch(0 0 0 / 0.20), inset 0 1px 0 oklch(1 0 0 / 0.24);
      }
      .float-card small {
        display: block;
        color: oklch(0.82 0.028 252);
        font-weight: 800;
        font-size: 12px;
      }
      .float-card strong {
        display: block;
        margin-top: 5px;
        color: var(--ink);
        font-size: 30px;
        line-height: 1;
      }
      .float-card span {
        display: block;
        margin-top: 6px;
        color: oklch(0.78 0.025 250);
        font-size: 12px;
      }
      .card-price {
        left: 48%;
        top: 12%;
        transform: translate(calc(var(--mx) * -28px), calc(var(--my) * -18px));
      }
      .card-ai {
        right: 5%;
        top: 58%;
        transform: translate(calc(var(--mx) * 22px), calc(var(--my) * 14px));
      }
      .card-score {
        left: 46%;
        bottom: 12%;
        transform: translate(calc(var(--mx) * -16px), calc(var(--my) * 20px));
      }
      .card-input {
        left: 56%;
        bottom: 29%;
        transform: translate(calc(var(--mx) * 12px), calc(var(--my) * -20px));
      }
      .crack-layer {
        position: absolute;
        inset: 0;
        z-index: 30;
        pointer-events: none;
      }
      .crack-layer svg {
        position: absolute;
        inset: 0;
        width: 100%;
        height: 100%;
        animation: crackFade 1450ms ease-out forwards;
      }
      .crack-layer path {
        fill: none;
        stroke-linecap: round;
        stroke-linejoin: round;
      }
      @keyframes ripple {
        to {
          opacity: 0;
          transform: translate(-50%, -50%) scale(12);
        }
      }
      @keyframes crackFade {
        0% { opacity: 0; filter: drop-shadow(0 0 0 oklch(1 0 0 / 0)); }
        9% { opacity: 1; filter: drop-shadow(0 0 10px oklch(0.83 0.13 203 / 0.50)); }
        72% { opacity: 0.92; }
        100% { opacity: 0; filter: drop-shadow(0 0 1px oklch(1 0 0 / 0)); }
      }
      @media (max-width: 920px) {
        #bow-home-stage { height: 100vh; }
        .copy-layer {
          left: 22px;
          top: 33px;
          width: calc(100% - 44px);
          translate: 0;
        }
        h1 { font-size: 54px; max-width: 10ch; }
        p { font-size: 16px; }
        .visual-layer img {
          top: 34%;
          right: -45%;
          width: 150%;
          height: 70%;
        }
        .float-card { display: none; }
        .card-ai { display: block; right: 16px; top: auto; bottom: 36px; min-width: 150px; }
        .eye-shine { display: none; }
      }
      @media (max-width: 600px) {
        .card-ai { display: none; }
      }
      @media (prefers-reduced-motion: reduce) {
        .copy-layer, .visual-layer, .float-card, .field-layer, .eye-shine {
          transition: none;
          transform: none;
        }
      }
    </style>
    <script>
      const stage = document.getElementById("bow-home-stage");
      const crackLayer = stage.querySelector(".crack-layer");
      const update = (event) => {
        const rect = stage.getBoundingClientRect();
        const x = ((event.clientX - rect.left) / rect.width - 0.5) * 2;
        const y = ((event.clientY - rect.top) / rect.height - 0.5) * 2;
        stage.style.setProperty("--mx", Math.max(-1, Math.min(1, x)).toFixed(3));
        stage.style.setProperty("--my", Math.max(-1, Math.min(1, y)).toFixed(3));
      };
      stage.addEventListener("mousemove", update);
      stage.addEventListener("mouseleave", () => {
        stage.style.setProperty("--mx", "0");
        stage.style.setProperty("--my", "0");
      });
      stage.addEventListener("dblclick", (event) => crack(event.clientX, event.clientY));
      function crack(clientX, clientY) {
        const rect = stage.getBoundingClientRect();
        const x = clientX - rect.left;
        const y = clientY - rect.top;
        const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        svg.setAttribute("viewBox", `0 0 ${rect.width} ${rect.height}`);
        const defs = document.createElementNS("http://www.w3.org/2000/svg", "defs");
        defs.innerHTML = `
          <filter id="glassGlow" x="-8%" y="-8%" width="116%" height="116%">
            <feDropShadow dx="0" dy="0" stdDeviation="1.8" flood-color="rgba(142,222,255,.58)" />
          </filter>
        `;
        svg.appendChild(defs);
        const axes = 11;
        for (let i = 0; i < axes; i += 1) {
          const angle = (Math.PI * 2 * i) / axes + (Math.random() - 0.5) * 0.35;
          const main = fracturePath(x, y, rect.width, rect.height, angle, 7 + (i % 4), 46 + Math.random() * 34, 0.42);
          main.setAttribute("stroke", "rgba(244, 253, 255, 0.86)");
          main.setAttribute("stroke-width", i % 4 === 0 ? "1.45" : "0.95");
          main.setAttribute("filter", "url(#glassGlow)");
          svg.appendChild(main);
          const branchCount = 2 + (i % 3);
          for (let j = 0; j < branchCount; j += 1) {
            const branchStart = pointOnPath(x, y, angle, 42 + j * 34 + Math.random() * 18);
            const branchAngle = angle + (j % 2 ? 1 : -1) * (0.45 + Math.random() * 0.42);
            const branch = fracturePath(branchStart.x, branchStart.y, rect.width, rect.height, branchAngle, 3 + (j % 3), 18 + Math.random() * 22, 0.62);
            branch.setAttribute("stroke", j % 2 ? "rgba(255,255,255,.56)" : "rgba(126,218,255,.54)");
            branch.setAttribute("stroke-width", "0.62");
            svg.appendChild(branch);
          }
        }
        for (let i = 0; i < 10; i += 1) {
          const shard = document.createElementNS("http://www.w3.org/2000/svg", "polygon");
          const angle = Math.random() * Math.PI * 2;
          const radius = 18 + Math.random() * 68;
          const sx = x + Math.cos(angle) * radius;
          const sy = y + Math.sin(angle) * radius;
          const size = 8 + Math.random() * 18;
          shard.setAttribute("points", `${sx},${sy} ${sx + size},${sy + Math.random() * size} ${sx + Math.random() * size},${sy - size}`);
          shard.setAttribute("fill", "rgba(255,255,255,.055)");
          shard.setAttribute("stroke", "rgba(255,255,255,.24)");
          shard.setAttribute("stroke-width", ".55");
          svg.appendChild(shard);
        }
        crackLayer.innerHTML = "";
        crackLayer.appendChild(svg);
        setTimeout(() => svg.remove(), 1500);
      }
      function pointOnPath(x, y, angle, distance) {
        return { x: x + Math.cos(angle) * distance, y: y + Math.sin(angle) * distance };
      }
      function fracturePath(x, y, width, height, angle, segments, length, spread) {
        const path = document.createElementNS("http://www.w3.org/2000/svg", "path");
        let cx = x;
        let cy = y;
        let d = `M ${cx.toFixed(1)} ${cy.toFixed(1)}`;
        for (let i = 0; i < segments; i += 1) {
          const wobble = (Math.random() - 0.5) * spread;
          const step = length * (0.45 + Math.random() * 0.75);
          cx += Math.cos(angle + wobble) * step;
          cy += Math.sin(angle + wobble) * step;
          cx = Math.max(0, Math.min(width, cx));
          cy = Math.max(0, Math.min(height, cy));
          d += ` L ${cx.toFixed(1)} ${cy.toFixed(1)}`;
        }
        path.setAttribute("d", d);
        return path;
      }
    </script>
    """
    st.iframe(template.replace("__IMAGE__", encoded), height=860)


def page_glass_header(title: str, subtitle: str, active: str) -> None:
    title_class = "compact" if len(title) > 18 else ""
    template = f"""
    <section id="bow-page-head" aria-label="{title}">
      <div class="crack-layer"></div>
      <div class="head-copy">
        <span>BuyOrWait</span>
        <h1 class="{title_class}">{title}</h1>
        <p>{subtitle}</p>
      </div>
    </section>
    <style>
      * {{ box-sizing: border-box; }}
      body {{
        margin: 0;
        background: transparent;
        font-family: "Avenir Next", "SF Pro Display", "Manrope", ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      }}
      #bow-page-head {{
        position: relative;
        overflow: hidden;
        min-height: 178px;
        border: 1px solid oklch(0.84 0.09 203 / 0.35);
        border-radius: 24px;
        padding: 25px;
        color: oklch(0.97 0.004 85);
        background:
          radial-gradient(circle at 82% 18%, oklch(0.70 0.16 292 / 0.24), transparent 18rem),
          radial-gradient(circle at 12% 100%, oklch(0.82 0.13 203 / 0.18), transparent 18rem),
          linear-gradient(135deg, oklch(0.47 0.031 239 / 0.58), oklch(0.31 0.026 252 / 0.62));
        backdrop-filter: blur(24px) saturate(1.42);
        box-shadow: 0 18px 38px oklch(0 0 0 / 0.14), inset 0 1px 0 oklch(1 0 0 / 0.22);
      }}
      #bow-page-head:before {{
        content: "";
        position: absolute;
        inset: 0;
        background: linear-gradient(110deg, transparent, oklch(1 0 0 / 0.10), transparent);
        transform: translateX(-60%);
        animation: sheen 5s ease-in-out infinite;
        pointer-events: none;
      }}
      .head-copy {{
        position: relative;
        z-index: 2;
        width: min(840px, 86%);
      }}
      .head-copy span {{
        color: oklch(0.84 0.13 203);
        font-size: 13px;
        font-weight: 900;
      }}
      .head-copy h1 {{
        margin: 8px 0 8px;
        font-size: clamp(36px, 5.4vw, 64px);
        line-height: 0.95;
        letter-spacing: 0;
        text-shadow: 0 14px 30px oklch(0 0 0 / 0.26);
      }}
      .head-copy h1.compact {{
        font-size: clamp(32px, 4vw, 50px);
        line-height: 1;
        max-width: 100%;
      }}
      .head-copy p {{
        margin: 0;
        color: oklch(0.82 0.030 247);
        font-size: 16px;
        line-height: 1.5;
      }}
      .crack-layer {{
        position: absolute;
        inset: 0;
        z-index: 6;
        pointer-events: none;
      }}
      .crack-layer svg {{
        position: absolute;
        inset: 0;
        width: 100%;
        height: 100%;
        animation: crackFade 1200ms ease-out forwards;
      }}
      .crack-layer path {{
        fill: none;
        stroke-linecap: round;
        stroke-linejoin: round;
      }}
      @keyframes sheen {{
        0%, 58% {{ transform: translateX(-70%); opacity: 0; }}
        72% {{ opacity: 1; }}
        100% {{ transform: translateX(80%); opacity: 0; }}
      }}
      @keyframes crackFade {{
        0% {{ opacity: 0; }}
        10% {{ opacity: 1; filter: drop-shadow(0 0 12px oklch(0.84 0.13 203 / 0.60)); }}
        78% {{ opacity: .9; }}
        100% {{ opacity: 0; }}
      }}
      @media (max-width: 760px) {{
        #bow-page-head {{ padding: 20px; min-height: 190px; }}
        .head-copy {{ width: 100%; }}
      }}
    </style>
    <script>
      const head = document.getElementById("bow-page-head");
      const layer = head.querySelector(".crack-layer");
      head.addEventListener("dblclick", (event) => crack(event.clientX, event.clientY));
      function crack(clientX, clientY) {{
        const rect = head.getBoundingClientRect();
        const x = clientX - rect.left;
        const y = clientY - rect.top;
        const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        svg.setAttribute("viewBox", `0 0 ${{rect.width}} ${{rect.height}}`);
        for (let i = 0; i < 16; i += 1) {{
          const path = document.createElementNS("http://www.w3.org/2000/svg", "path");
          const angle = Math.random() * Math.PI * 2;
          let cx = x;
          let cy = y;
          let d = `M ${{cx.toFixed(1)}} ${{cy.toFixed(1)}}`;
          for (let j = 0; j < 5; j += 1) {{
            const step = 20 + Math.random() * 34;
            cx += Math.cos(angle + (Math.random() - .5) * .9) * step;
            cy += Math.sin(angle + (Math.random() - .5) * .9) * step;
            d += ` L ${{cx.toFixed(1)}} ${{cy.toFixed(1)}}`;
          }}
          path.setAttribute("d", d);
          path.setAttribute("stroke", i % 2 ? "rgba(255,255,255,.68)" : "rgba(137,222,255,.68)");
          path.setAttribute("stroke-width", i % 3 ? ".8" : "1.25");
          svg.appendChild(path);
        }}
        layer.innerHTML = "";
        layer.appendChild(svg);
        setTimeout(() => svg.remove(), 1300);
      }}
    </script>
    """
    st.iframe(template, height=205)


def analyzer_preview(game) -> None:
    status = "BUY" if game.buy_confidence_score >= 75 else "WAIT" if game.buy_confidence_score >= 50 else "SKIP"
    st.markdown(
        f"""
        <div class="analyzer-preview">
          <div>
            <div class="section-label">AI Product Analyzer Preview</div>
            <h2>{game.game_name}</h2>
            <p>
              BuyOrWait checks recent reviews, discount timing, momentum, and anomaly risk before you spend.
            </p>
          </div>
          <div class="preview-result status-{status.lower()}">
            <span>AI recommendation</span>
            <strong>{status}</strong>
            <small>{game.buy_confidence_score:.0f}/100 confidence</small>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def floating_decision_cards(game) -> None:
    st.markdown(
        f"""
        <div class="floating-card-grid">
          <div class="decision-float-card">
            <span>Price timing</span>
            <strong>Watch deal momentum</strong>
            <p>Recent trend suggests the next discount window matters more than the lifetime rating.</p>
          </div>
          <div class="decision-float-card raised">
            <span>Review signal</span>
            <strong>{game.recent_positive_rate:.0%} recent positive</strong>
            <p>Recent sentiment is weighted higher than old reviews, so the answer can change quickly.</p>
          </div>
          <div class="decision-float-card">
            <span>Risk guardrail</span>
            <strong>{game.bombing_signal} anomaly signal</strong>
            <p>Rolling-window detection flags sudden negative-review spikes before they distort the decision.</p>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def game_info_panel(game) -> None:
    st.markdown(
        f"""
        <div class="bow-panel">
          <div class="bow-card-title">Game Info Card</div>
          <div class="bow-card-value">{game.game_name}</div>
          <div class="bow-card-note">appid {game.appid} | {int(game.review_count):,} total reviews</div>
          <div class="game-info-grid">
            <div class="game-info-item">
              <div class="game-info-label">Genre</div>
              <div class="game-info-value">{game.genre}</div>
            </div>
            <div class="game-info-item">
              <div class="game-info-label">Last updated</div>
              <div class="game-info-value">{game.last_updated.strftime("%b %d, %Y")}</div>
            </div>
            <div class="game-info-item">
              <div class="game-info-label">Review count</div>
              <div class="game-info-value">{int(game.review_count):,}</div>
            </div>
            <div class="game-info-item">
              <div class="game-info-label">Anomaly signal</div>
              <div class="game-info-value">{game.bombing_signal}</div>
            </div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def decision_panel(score: float) -> str:
    if score >= 75:
        status = "BUY"
        css = "status-buy"
        caption = "Recent signal is strong enough for a confident buy recommendation."
    elif score >= 50:
        status = "WAIT"
        css = "status-wait"
        caption = "Evidence is mixed. Waiting for a discount, patch, or clearer trend is safer."
    else:
        status = "SKIP"
        css = "status-skip"
        caption = "Negative momentum is elevated enough to flag purchase risk."

    st.markdown(
        f"""
        <div class="decision-shell {css}">
          <div class="decision-label">{status} SIGNAL</div>
          <div class="decision-score">{score:.0f}</div>
          <div class="decision-caption">{caption}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    return status


def alert_card(title: str, value: str, note: str, severity: str = "medium") -> None:
    css = {
        "critical": "alert-critical",
        "high": "alert-high",
        "medium": "alert-medium",
    }.get(severity.lower(), "alert-medium")
    st.markdown(
        f"""
        <div class="{css}">
          <div class="bow-card-title">{title}</div>
          <div class="bow-card-value">{value}</div>
          <div class="bow-card-note">{note}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def architecture_flow() -> None:
    steps = [
        "Game review dataset",
        "Cloud Storage",
        "GPU Batch Processing",
        "Aggregated Tables",
        "Streamlit Product Demo",
    ]
    nodes = "".join([f'<div class="arch-node">{step}</div>' for step in steps])
    st.markdown(f'<div class="arch-flow">{nodes}</div>', unsafe_allow_html=True)
