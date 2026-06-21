/**
 * hero-chart.js — 首屏 Hero 区复利曲线图表演示
 * 嵌入 index.html 使用
 * 两条曲线：金色8%复利 vs 白色3%单利（无风险基准）
 */
(function () {
  'use strict';

  /* ============================================================
     Constants & Design Tokens
     ============================================================ */
  const W = 380, H = 280;
  const MARGIN = { top: 28, right: 28, bottom: 36, left: 40 };
  const COLORS = {
    bg:           '#0B0D10',
    curveA:       '#D4AF37',
    curveB:       'rgba(255,255,255,0.25)',
    baseline:     'rgba(212,175,55,0.3)',
    axisText:     'rgba(255,255,255,0.4)',
    labelBg:      'rgba(22,26,34,0.9)',
    labelText:    '#FFFFFF',
    labelGoldText:'#D4AF37',
    grid:         'rgba(255,255,255,0.04)',
  };

  /* ============================================================
     Data
     ============================================================ */
  const YEARS = 20;
  const START_VAL = 100;

  // Curve A: 8% compound
  const RATE_A = 0.08;
  const dataA = [];
  for (let y = 1; y <= YEARS; y++) {
    dataA.push({
      year:  y,
      value: Math.round(START_VAL * Math.pow(1 + RATE_A, y) * 10) / 10
    });
  }

  // Curve B: 3% linear
  const RATE_B = 0.03;
  const dataB = [];
  for (let y = 1; y <= YEARS; y++) {
    dataB.push({
      year:  y,
      value: Math.round((START_VAL * (1 + RATE_B * y)) * 10) / 10
    });
  }

  const BASELINE_YEAR = 10;
  const BASELINE_VAL = dataA[BASELINE_YEAR - 1].value;

  /* ============================================================
     Layout helpers
     ============================================================ */
  const plotW = W - MARGIN.left - MARGIN.right;
  const plotH = H - MARGIN.top - MARGIN.bottom;
  const xMin = 1, xMax = YEARS;
  const yMax = 500;
  const yMin = 0;

  function xPos(year) {
    return MARGIN.left + (year - xMin) / (xMax - xMin) * plotW;
  }
  function yPos(value) {
    return MARGIN.top + plotH - (value - yMin) / (yMax - yMin) * plotH;
  }

  /* ============================================================
     Canvas rendering
     ============================================================ */
  const canvas = document.getElementById('compoundChart');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  if (!ctx) {
    clearTimeout(fallbackTimer);
    fallbackEl.classList.add('active');
    return;
  }

  const dpr = window.devicePixelRatio || 1;
  if (dpr > 1) {
    canvas.width = W * dpr;
    canvas.height = H * dpr;
    canvas.style.width = W + 'px';
    canvas.style.height = H + 'px';
    ctx.scale(dpr, dpr);
  }

  let animProgress = 0;
  let animationDone = false;
  let hoveredIndex = -1;
  let hoveredCurve = null;
  let cachedSnapshot = null;

  function roundRect(ctx, x, y, w, h, r) {
    ctx.beginPath();
    ctx.moveTo(x + r, y);
    ctx.lineTo(x + w - r, y);
    ctx.quadraticCurveTo(x + w, y, x + w, y + r);
    ctx.lineTo(x + w, y + h - r);
    ctx.quadraticCurveTo(x + w, y + h, x + w - r, y + h);
    ctx.lineTo(x + r, y + h);
    ctx.quadraticCurveTo(x, y + h, x + r, y + h - r);
    ctx.lineTo(x, y + r);
    ctx.quadraticCurveTo(x, y, x + r, y);
    ctx.closePath();
  }

  function drawCurve(data, color, lineWidth, dash, progress) {
    const visibleCount = Math.floor(progress * (data.length - 1));
    const frac = progress * (data.length - 1) - visibleCount;

    ctx.save();
    if (dash) { ctx.setLineDash(dash); }
    ctx.strokeStyle = color;
    ctx.lineWidth = lineWidth;
    ctx.lineJoin = 'round';
    ctx.lineCap = 'round';
    ctx.beginPath();

    for (let i = 0; i <= visibleCount && i < data.length; i++) {
      const x = xPos(data[i].year);
      const y = yPos(data[i].value);
      if (i === 0) {
        ctx.moveTo(x, y);
      } else {
        const prev = data[i - 1];
        const cpX = (xPos(prev.year) + x) / 2;
        ctx.quadraticCurveTo(cpX, yPos(prev.value), x, y);
      }
    }

    if (frac > 0 && visibleCount + 1 < data.length) {
      const i = visibleCount;
      const p1 = data[i], p2 = data[i + 1];
      const p1x = xPos(p1.year), p1y = yPos(p1.value);
      const p2x = xPos(p2.year), p2y = yPos(p2.value);
      const mx = p1x + (p2x - p1x) * frac;
      const my = p1y + (p2y - p1y) * frac;
      const cpX = (p1x + p2x) / 2;
      ctx.quadraticCurveTo(cpX, p1y, mx, my);
    }

    ctx.stroke();
    ctx.restore();
  }

  function drawChart(progress, hoverIdx, hoverCurve) {
    ctx.clearRect(0, 0, W, H);

    // Background
    ctx.fillStyle = COLORS.bg;
    ctx.fillRect(0, 0, W, H);

    // Grid
    ctx.strokeStyle = COLORS.grid;
    ctx.lineWidth = 1;
    for (let v = 0; v <= yMax; v += 100) {
      const y = yPos(v);
      ctx.beginPath();
      ctx.moveTo(MARGIN.left, y);
      ctx.lineTo(W - MARGIN.right, y);
      ctx.stroke();
    }

    // Y-axis labels
    ctx.fillStyle = COLORS.axisText;
    ctx.font = '10px "Inter", "Noto Sans SC", sans-serif';
    ctx.textAlign = 'right';
    ctx.textBaseline = 'middle';
    for (let v = 0; v <= yMax; v += 100) {
      ctx.fillText(v + '万', MARGIN.left - 8, yPos(v));
    }

    // X-axis labels
    ctx.textAlign = 'center';
    ctx.textBaseline = 'top';
    for (let y = 1; y <= YEARS; y += 5) {
      ctx.fillText('第' + y + '年', xPos(y), MARGIN.top + plotH + 8);
    }

    // Baseline
    const blX1 = xPos(1);
    const blX2 = xPos(YEARS);
    const blY = yPos(BASELINE_VAL);
    ctx.save();
    ctx.setLineDash([5, 5]);
    ctx.strokeStyle = COLORS.baseline;
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(blX1, blY);
    ctx.lineTo(blX2, blY);
    ctx.stroke();
    ctx.restore();

    ctx.fillStyle = COLORS.axisText;
    ctx.font = '10px "Inter", "Noto Sans SC", sans-serif';
    ctx.textAlign = 'right';
    ctx.textBaseline = 'bottom';
    ctx.fillText('守夜人底线', blX2 + 4, blY - 2);

    // Curve B (white dashed)
    drawCurve(dataB, COLORS.curveB, 1.2, [8, 4], progress);

    // Curve A (gold solid)
    drawCurve(dataA, COLORS.curveA, 2, null, progress);

    // Data dots
    const visibleCount = Math.floor(progress * (dataA.length - 1));
    for (let i = 0; i <= visibleCount && i < dataA.length; i++) {
      const ax = xPos(dataA[i].year), ay = yPos(dataA[i].value);
      ctx.fillStyle = COLORS.curveA;
      ctx.globalAlpha = 0.2;
      ctx.beginPath();
      ctx.arc(ax, ay, 2.5, 0, Math.PI * 2);
      ctx.fill();

      const bx = xPos(dataB[i].year), by = yPos(dataB[i].value);
      ctx.fillStyle = 'rgba(255,255,255,0.12)';
      ctx.globalAlpha = 0.4;
      ctx.beginPath();
      ctx.arc(bx, by, 2, 0, Math.PI * 2);
      ctx.fill();

      ctx.globalAlpha = 1;
    }

    // Hover label
    if (hoverIdx >= 0 && hoverCurve) {
      const dataset = hoverCurve === 'A' ? dataA : dataB;
      const pt = dataset[hoverIdx];
      const px = xPos(pt.year);
      const py = yPos(pt.value);
      const isCurveA = hoverCurve === 'A';

      const labelW = 136;
      const labelH = 44;
      let labelX = px - labelW / 2;
      let labelY = py - labelH - 14;

      if (labelX < MARGIN.left) labelX = MARGIN.left;
      if (labelX + labelW > W - MARGIN.right) labelX = W - MARGIN.right - labelW;
      if (labelY < MARGIN.top) labelY = py + 10;

      ctx.fillStyle = COLORS.labelBg;
      roundRect(ctx, labelX, labelY, labelW, labelH, 4);
      ctx.fill();

      ctx.fillStyle = isCurveA ? COLORS.labelGoldText : 'rgba(255,255,255,0.7)';
      ctx.font = '10px "Inter", "Noto Sans SC", sans-serif';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      const midX = labelX + labelW / 2;
      const prefix = isCurveA ? '守夜人 · 第 ' : '基准 · 第 ';
      ctx.fillText(prefix + pt.year + ' 年', midX, labelY + 14);
      ctx.fillStyle = isCurveA ? COLORS.labelGoldText : '#FFFFFF';
      ctx.font = '600 13px "Inter", "Noto Sans SC", sans-serif';
      ctx.fillText(pt.value + ' 万', midX, labelY + 33);
    }
  }

  /* ============================================================
     Animation
     ============================================================ */
  let animStartTime = null;
  const ANIM_DELAY = 800;
  const ANIM_DURATION = 1200;

  function startAnimation() {
    clearTimeout(fallbackTimer);
    fallbackEl.classList.remove('active');
    canvas.style.display = '';

    animStartTime = performance.now() + ANIM_DELAY;
    requestAnimationFrame(animate);
  }

  function animate(timestamp) {
    if (!animStartTime) {
      animStartTime = timestamp + ANIM_DELAY;
    }
    const elapsed = timestamp - animStartTime;
    if (elapsed < 0) {
      drawChart(0, hoveredIndex, hoveredCurve);
      requestAnimationFrame(animate);
      return;
    }
    animProgress = Math.min(1, elapsed / ANIM_DURATION);
    drawChart(animProgress, hoveredIndex, hoveredCurve);

    if (animProgress < 1) {
      requestAnimationFrame(animate);
    } else {
      animationDone = true;
      drawChart(1, hoveredIndex, hoveredCurve);
      cacheSnapshot();
    }
  }

  function cacheSnapshot() {
    try { cachedSnapshot = canvas.toDataURL('image/png'); } catch (e) { }
  }

  /* ============================================================
     Hover detection
     ============================================================ */
  let lastHoverTime = 0;
  const HOVER_THROTTLE = 100;

  function getHoverInfo(event) {
    const rect = canvas.getBoundingClientRect();
    const scaleX = W / rect.width;
    const scaleY = H / rect.height;
    const mx = (event.clientX - rect.left) * scaleX;
    const my = (event.clientY - rect.top) * scaleY;

    let bestIdx = -1;
    let bestCurve = null;
    let bestDist = 10;

    for (let i = 0; i < dataA.length; i++) {
      const px = xPos(dataA[i].year), py = yPos(dataA[i].value);
      const dist = Math.sqrt((mx - px) ** 2 + (my - py) ** 2);
      if (dist < bestDist) {
        bestDist = dist;
        bestIdx = i;
        bestCurve = 'A';
      }
    }

    for (let i = 0; i < dataB.length; i++) {
      const px = xPos(dataB[i].year), py = yPos(dataB[i].value);
      const dist = Math.sqrt((mx - px) ** 2 + (my - py) ** 2);
      if (dist < bestDist) {
        bestDist = dist;
        bestIdx = i;
        bestCurve = 'B';
      }
    }

    return { idx: bestIdx, curve: bestCurve };
  }

  function onMouseMove(event) {
    const now = performance.now();
    if (now - lastHoverTime < HOVER_THROTTLE) return;
    lastHoverTime = now;

    const info = getHoverInfo(event);
    if (info.idx !== hoveredIndex || info.curve !== hoveredCurve) {
      hoveredIndex = info.idx;
      hoveredCurve = info.curve;
      if (animationDone) {
        drawChart(1, hoveredIndex, hoveredCurve);
      }
    }
  }

  function onMouseLeave() {
    if (hoveredIndex !== -1) {
      hoveredIndex = -1;
      hoveredCurve = null;
      if (animationDone) {
        drawChart(1, hoveredIndex, hoveredCurve);
      }
    }
  }

  function onVisibilityChange() {
    if (animationDone && cachedSnapshot) {
      const img = new Image();
      img.onload = function () {
        ctx.clearRect(0, 0, W, H);
        ctx.drawImage(img, 0, 0, W, H);
        if (hoveredIndex >= 0) {
          drawChart(1, hoveredIndex, hoveredCurve);
        }
      };
      img.src = cachedSnapshot;
    }
  }

  /* ============================================================
     2-second fallback
     ============================================================ */
  const fallbackEl = document.getElementById('chartFallback');
  const fallbackTimer = setTimeout(function () {
    if (!animStartTime) {
      fallbackEl.classList.add('active');
      canvas.style.display = 'none';
    }
  }, 2000);

  /* ============================================================
     Init
     ============================================================ */
  drawChart(0, -1, null);
  setTimeout(startAnimation, 50);

  console.log('[hero-chart] canvas =', canvas, '| ctx =', ctx);

  canvas.addEventListener('mousemove', onMouseMove);
  canvas.addEventListener('mouseleave', onMouseLeave);
  window.addEventListener('scroll', onVisibilityChange, { passive: true });
  window.addEventListener('resize', onVisibilityChange, { passive: true });

  console.log('[hero-chart] 图表已初始化。守夜人机制（金色8%复利）vs 无风险基准（白色3%单利）');
})();
