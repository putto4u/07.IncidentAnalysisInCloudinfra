from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_AUTO_SHAPE_TYPE
from pptx.enum.text import MSO_ANCHOR
from pptx.util import Inches, Pt


@dataclass(frozen=True)
class Theme:
    bg: RGBColor = RGBColor(12, 18, 28)  # deep navy
    panel: RGBColor = RGBColor(20, 31, 47)
    panel_soft: RGBColor = RGBColor(26, 39, 58)
    text: RGBColor = RGBColor(233, 239, 245)
    muted: RGBColor = RGBColor(170, 184, 199)
    accent: RGBColor = RGBColor(0, 196, 255)  # cyan
    accent_soft: RGBColor = RGBColor(76, 222, 255)
    accent2: RGBColor = RGBColor(255, 92, 124)  # alert red
    ok: RGBColor = RGBColor(0, 220, 160)


THEME = Theme()


def _set_slide_bg(slide, color: RGBColor) -> None:
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = color


def _add_visual_motif(slide) -> None:
    # Right-top translucent ring motif
    ring_outer = slide.shapes.add_shape(MSO_AUTO_SHAPE_TYPE.DONUT, Inches(11.2), Inches(-0.1), Inches(2.8), Inches(2.8))
    ring_outer.fill.solid()
    ring_outer.fill.fore_color.rgb = THEME.panel_soft
    ring_outer.line.fill.background()

    ring_inner = slide.shapes.add_shape(MSO_AUTO_SHAPE_TYPE.DONUT, Inches(11.65), Inches(0.35), Inches(1.9), Inches(1.9))
    ring_inner.fill.solid()
    ring_inner.fill.fore_color.rgb = THEME.accent_soft
    ring_inner.line.fill.background()

    # Left-side vertical ribbon for stronger brand identity
    ribbon = slide.shapes.add_shape(MSO_AUTO_SHAPE_TYPE.RECTANGLE, Inches(0), Inches(0), Inches(0.14), Inches(7.5))
    ribbon.fill.solid()
    ribbon.fill.fore_color.rgb = THEME.accent
    ribbon.line.fill.background()


def _add_header_bar(slide, title: str, subtitle: str | None = None) -> None:
    _add_visual_motif(slide)

    left = Inches(0)
    top = Inches(0)
    width = Inches(13.333)
    height = Inches(0.85)
    shape = slide.shapes.add_shape(MSO_AUTO_SHAPE_TYPE.RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = THEME.panel
    shape.line.fill.background()

    tx = shape.text_frame
    tx.clear()
    tx.margin_left = Inches(0.55)
    tx.margin_right = Inches(0.4)
    tx.vertical_anchor = MSO_ANCHOR.MIDDLE

    p = tx.paragraphs[0]
    r = p.add_run()
    r.text = title
    r.font.name = "Malgun Gothic"
    r.font.size = Pt(26)
    r.font.bold = True
    r.font.color.rgb = THEME.text

    if subtitle:
        p2 = tx.add_paragraph()
        p2.space_before = Pt(2)
        r2 = p2.add_run()
        r2.text = subtitle
        r2.font.name = "Malgun Gothic"
        r2.font.size = Pt(14)
        r2.font.color.rgb = THEME.muted

    accent = slide.shapes.add_shape(
        MSO_AUTO_SHAPE_TYPE.RECTANGLE, Inches(0), Inches(0.84), Inches(13.333), Inches(0.06)
    )
    accent.fill.solid()
    accent.fill.fore_color.rgb = THEME.accent
    accent.line.fill.background()


def _add_footer(slide, left_text: str = "모의해킹 · 분석 · 탐지/방어 프로젝트 강의", right_text: str = "© Template") -> None:
    y = Inches(7.05)
    h = Inches(0.45)
    bar = slide.shapes.add_shape(MSO_AUTO_SHAPE_TYPE.RECTANGLE, Inches(0), y, Inches(13.333), h)
    bar.fill.solid()
    bar.fill.fore_color.rgb = THEME.panel
    bar.line.fill.background()

    tf = bar.text_frame
    tf.clear()
    tf.margin_left = Inches(0.5)
    tf.margin_right = Inches(0.5)
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE

    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = left_text
    r.font.name = "Malgun Gothic"
    r.font.size = Pt(11)
    r.font.color.rgb = THEME.muted

    # right aligned small tag
    tag = slide.shapes.add_shape(MSO_AUTO_SHAPE_TYPE.ROUNDED_RECTANGLE, Inches(11.0), y + Inches(0.08), Inches(2.2), Inches(0.29))
    tag.fill.solid()
    tag.fill.fore_color.rgb = THEME.bg
    tag.line.color.rgb = THEME.accent
    tag.line.width = Pt(1)
    ttf = tag.text_frame
    ttf.clear()
    ttf.vertical_anchor = MSO_ANCHOR.MIDDLE
    tp = ttf.paragraphs[0]
    tr = tp.add_run()
    tr.text = right_text
    tr.font.name = "Malgun Gothic"
    tr.font.size = Pt(10)
    tr.font.color.rgb = THEME.text


def _add_title_and_bullets(slide, title: str, bullets: list[str]) -> None:
    _add_header_bar(slide, title)
    body = slide.shapes.add_shape(
        MSO_AUTO_SHAPE_TYPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(1.25), Inches(12.15), Inches(5.65)
    )
    body.fill.solid()
    body.fill.fore_color.rgb = THEME.panel_soft
    body.line.color.rgb = THEME.bg
    body.line.width = Pt(1)
    tf = body.text_frame
    tf.clear()
    tf.margin_left = Inches(0.55)
    tf.margin_right = Inches(0.45)
    tf.margin_top = Inches(0.25)
    tf.word_wrap = True
    tf.vertical_anchor = MSO_ANCHOR.TOP

    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = "핵심 포인트"
    r.font.name = "Malgun Gothic"
    r.font.size = Pt(18)
    r.font.bold = True
    r.font.color.rgb = THEME.accent

    for b in bullets:
        bp = tf.add_paragraph()
        bp.level = 0
        bp.space_before = Pt(8)
        rr = bp.add_run()
        rr.text = f"• {b}"
        rr.font.name = "Malgun Gothic"
        rr.font.size = Pt(16)
        rr.font.color.rgb = THEME.text

    _add_footer(slide)


def _add_section_slide(slide, section: str, tagline: str) -> None:
    _set_slide_bg(slide, THEME.bg)
    _add_visual_motif(slide)

    panel = slide.shapes.add_shape(MSO_AUTO_SHAPE_TYPE.RECTANGLE, Inches(0.8), Inches(2.2), Inches(11.7), Inches(3.1))
    panel.fill.solid()
    panel.fill.fore_color.rgb = THEME.panel_soft
    panel.line.color.rgb = THEME.accent
    panel.line.width = Pt(1.2)

    accent = slide.shapes.add_shape(MSO_AUTO_SHAPE_TYPE.RECTANGLE, Inches(0.8), Inches(2.2), Inches(0.12), Inches(3.1))
    accent.fill.solid()
    accent.fill.fore_color.rgb = THEME.accent
    accent.line.fill.background()

    tf = panel.text_frame
    tf.clear()
    tf.margin_left = Inches(0.7)
    tf.margin_right = Inches(0.5)
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf.word_wrap = True

    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = section
    r.font.name = "Malgun Gothic"
    r.font.size = Pt(44)
    r.font.bold = True
    r.font.color.rgb = THEME.text

    p2 = tf.add_paragraph()
    p2.space_before = Pt(10)
    r2 = p2.add_run()
    r2.text = tagline
    r2.font.name = "Malgun Gothic"
    r2.font.size = Pt(18)
    r2.font.color.rgb = THEME.muted

    _add_footer(slide, right_text=section)


def _add_two_column(slide, title: str, left_title: str, right_title: str) -> None:
    _add_header_bar(slide, title)

    box_w = Inches(6.0)
    box_h = Inches(5.3)
    left_box = slide.shapes.add_shape(MSO_AUTO_SHAPE_TYPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(1.25), box_w, box_h)
    right_box = slide.shapes.add_shape(MSO_AUTO_SHAPE_TYPE.ROUNDED_RECTANGLE, Inches(6.75), Inches(1.25), box_w, box_h)
    for box in (left_box, right_box):
        box.fill.solid()
        box.fill.fore_color.rgb = THEME.panel_soft
        box.line.color.rgb = THEME.accent
        box.line.width = Pt(1)

    def _fill_box(box, heading: str) -> None:
        tf = box.text_frame
        tf.clear()
        tf.margin_left = Inches(0.5)
        tf.margin_right = Inches(0.45)
        tf.margin_top = Inches(0.25)
        tf.word_wrap = True
        tf.vertical_anchor = MSO_ANCHOR.TOP
        p = tf.paragraphs[0]
        r = p.add_run()
        r.text = heading
        r.font.name = "Malgun Gothic"
        r.font.size = Pt(18)
        r.font.bold = True
        r.font.color.rgb = THEME.accent
        # placeholders
        for t in ["- 포인트 1", "- 포인트 2", "- 포인트 3"]:
            pp = tf.add_paragraph()
            pp.space_before = Pt(8)
            rr = pp.add_run()
            rr.text = t
            rr.font.name = "Malgun Gothic"
            rr.font.size = Pt(15)
            rr.font.color.rgb = THEME.text

    _fill_box(left_box, left_title)
    _fill_box(right_box, right_title)
    _add_footer(slide)


def _add_code_slide(slide, title: str, language: str = "Sigma / YARA / Python") -> None:
    _add_header_bar(slide, title, subtitle=f"예시 코드 ({language})")

    code = slide.shapes.add_shape(MSO_AUTO_SHAPE_TYPE.ROUNDED_RECTANGLE, Inches(0.75), Inches(1.35), Inches(11.85), Inches(5.7))
    code.fill.solid()
    code.fill.fore_color.rgb = RGBColor(6, 10, 16)
    code.line.color.rgb = THEME.accent
    code.line.width = Pt(1)

    tf = code.text_frame
    tf.clear()
    tf.margin_left = Inches(0.4)
    tf.margin_right = Inches(0.4)
    tf.margin_top = Inches(0.25)
    tf.word_wrap = True
    tf.vertical_anchor = MSO_ANCHOR.TOP

    p = tf.paragraphs[0]
    run = p.add_run()
    run.text = (
        "# TODO: 탐지 규칙/분석 스크립트를 여기에 붙여넣으세요\n"
        "title: Suspicious PowerShell EncodedCommand\n"
        "logsource:\n"
        "  product: windows\n"
        "  service: powershell\n"
        "detection:\n"
        "  selection:\n"
        "    CommandLine|contains: '-enc'\n"
        "  condition: selection\n"
    )
    run.font.name = "Consolas"
    run.font.size = Pt(14)
    run.font.color.rgb = RGBColor(230, 236, 245)

    _add_footer(slide)


def _add_timeline_slide(slide, title: str) -> None:
    _add_header_bar(slide, title, subtitle="사고 분석 타임라인 (예시)")

    area = slide.shapes.add_shape(MSO_AUTO_SHAPE_TYPE.ROUNDED_RECTANGLE, Inches(0.7), Inches(1.35), Inches(12.0), Inches(5.7))
    area.fill.solid()
    area.fill.fore_color.rgb = THEME.panel_soft
    area.line.color.rgb = THEME.accent
    area.line.width = Pt(1)

    # timeline line
    line = slide.shapes.add_shape(MSO_AUTO_SHAPE_TYPE.RECTANGLE, Inches(1.2), Inches(4.0), Inches(10.9), Inches(0.08))
    line.fill.solid()
    line.fill.fore_color.rgb = THEME.muted
    line.line.fill.background()

    events = [
        ("T0", "피싱/취약점\n초기 침투", THEME.accent2),
        ("T+5m", "다운로더\n실행", THEME.accent),
        ("T+20m", "권한 상승/\n지속성", THEME.accent2),
        ("T+40m", "C2 통신/\n내부 이동", THEME.accent),
        ("T+2h", "탐지/격리/\n포렌식", THEME.ok),
    ]

    x0 = 1.35
    dx = 2.15
    for i, (t, label, color) in enumerate(events):
        x = Inches(x0 + i * dx)
        dot = slide.shapes.add_shape(MSO_AUTO_SHAPE_TYPE.OVAL, x, Inches(3.77), Inches(0.45), Inches(0.45))
        dot.fill.solid()
        dot.fill.fore_color.rgb = color
        dot.line.fill.background()

        box = slide.shapes.add_shape(MSO_AUTO_SHAPE_TYPE.ROUNDED_RECTANGLE, x - Inches(0.45), Inches(4.25), Inches(1.35), Inches(1.05))
        box.fill.solid()
        box.fill.fore_color.rgb = RGBColor(10, 15, 24)
        box.line.color.rgb = color
        box.line.width = Pt(1)

        tf = box.text_frame
        tf.clear()
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        tf.word_wrap = True
        p = tf.paragraphs[0]
        r = p.add_run()
        r.text = f"{t}\n{label}"
        r.font.name = "Malgun Gothic"
        r.font.size = Pt(12)
        r.font.color.rgb = THEME.text

    _add_footer(slide)


def _add_checklist_slide(slide, title: str, items: list[str]) -> None:
    _add_header_bar(slide, title, subtitle="실습/운영 체크리스트")

    box = slide.shapes.add_shape(MSO_AUTO_SHAPE_TYPE.ROUNDED_RECTANGLE, Inches(0.7), Inches(1.35), Inches(12.0), Inches(5.7))
    box.fill.solid()
    box.fill.fore_color.rgb = THEME.panel_soft
    box.line.color.rgb = THEME.accent
    box.line.width = Pt(1)
    tf = box.text_frame
    tf.clear()
    tf.margin_left = Inches(0.6)
    tf.margin_right = Inches(0.5)
    tf.margin_top = Inches(0.3)
    tf.word_wrap = True

    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = "체크 항목"
    r.font.name = "Malgun Gothic"
    r.font.size = Pt(18)
    r.font.bold = True
    r.font.color.rgb = THEME.accent

    for it in items:
        pp = tf.add_paragraph()
        pp.space_before = Pt(9)
        rr = pp.add_run()
        rr.text = f"☐ {it}"
        rr.font.name = "Malgun Gothic"
        rr.font.size = Pt(16)
        rr.font.color.rgb = THEME.text

    _add_footer(slide)


def _add_process_diagram_slide(slide, title: str) -> None:
    _add_header_bar(slide, title, subtitle="3단계 학습 플로우")

    base = slide.shapes.add_shape(MSO_AUTO_SHAPE_TYPE.ROUNDED_RECTANGLE, Inches(0.65), Inches(1.35), Inches(12.05), Inches(5.6))
    base.fill.solid()
    base.fill.fore_color.rgb = THEME.panel_soft
    base.line.color.rgb = THEME.accent
    base.line.width = Pt(1)

    nodes = [
        (Inches(1.2), "1. 침투 재현", "공격 경로 이해"),
        (Inches(5.15), "2. 증거 분석", "로그/패킷/메모리"),
        (Inches(9.1), "3. 탐지/방어", "룰/플레이북 반영"),
    ]
    colors = [THEME.accent2, THEME.accent, THEME.ok]

    for i, (x, t1, t2) in enumerate(nodes):
        box = slide.shapes.add_shape(MSO_AUTO_SHAPE_TYPE.ROUNDED_RECTANGLE, x, Inches(2.45), Inches(2.9), Inches(2.2))
        box.fill.solid()
        box.fill.fore_color.rgb = RGBColor(10, 15, 24)
        box.line.color.rgb = colors[i]
        box.line.width = Pt(1.5)
        tf = box.text_frame
        tf.clear()
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        p = tf.paragraphs[0]
        r = p.add_run()
        r.text = f"{t1}\n{t2}"
        r.font.name = "Malgun Gothic"
        r.font.size = Pt(17)
        r.font.bold = True
        r.font.color.rgb = THEME.text

    arrows = [
        (Inches(4.15), Inches(3.4)),
        (Inches(8.1), Inches(3.4)),
    ]
    for x, y in arrows:
        ar = slide.shapes.add_shape(MSO_AUTO_SHAPE_TYPE.CHEVRON, x, y, Inches(0.75), Inches(0.35))
        ar.fill.solid()
        ar.fill.fore_color.rgb = THEME.muted
        ar.line.fill.background()

    _add_footer(slide)


def _add_architecture_slide(slide, title: str) -> None:
    _add_header_bar(slide, title, subtitle="공격/방어 아키텍처 다이어그램")

    panel = slide.shapes.add_shape(MSO_AUTO_SHAPE_TYPE.ROUNDED_RECTANGLE, Inches(0.65), Inches(1.35), Inches(12.05), Inches(5.6))
    panel.fill.solid()
    panel.fill.fore_color.rgb = THEME.panel_soft
    panel.line.color.rgb = THEME.accent
    panel.line.width = Pt(1)

    cols = [
        ("외부 위협", Inches(1.0), THEME.accent2),
        ("경계 방어", Inches(4.1), THEME.accent),
        ("내부 자산", Inches(7.2), THEME.ok),
        ("SOC 대응", Inches(10.2), THEME.accent),
    ]

    for name, x, col in cols:
        node = slide.shapes.add_shape(MSO_AUTO_SHAPE_TYPE.ROUNDED_RECTANGLE, x, Inches(2.4), Inches(2.0), Inches(2.1))
        node.fill.solid()
        node.fill.fore_color.rgb = RGBColor(10, 15, 24)
        node.line.color.rgb = col
        node.line.width = Pt(1.4)
        tf = node.text_frame
        tf.clear()
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        p = tf.paragraphs[0]
        r = p.add_run()
        r.text = name
        r.font.name = "Malgun Gothic"
        r.font.size = Pt(16)
        r.font.bold = True
        r.font.color.rgb = THEME.text

    for x in [Inches(3.1), Inches(6.2), Inches(9.25)]:
        line = slide.shapes.add_shape(MSO_AUTO_SHAPE_TYPE.CHEVRON, x, Inches(3.2), Inches(0.7), Inches(0.35))
        line.fill.solid()
        line.fill.fore_color.rgb = THEME.muted
        line.line.fill.background()

    _add_footer(slide)


def _add_image_grid_slide(slide, title: str) -> None:
    _add_header_bar(slide, title, subtitle="이미지/스크린샷 삽입 템플릿")

    bg = slide.shapes.add_shape(MSO_AUTO_SHAPE_TYPE.ROUNDED_RECTANGLE, Inches(0.65), Inches(1.35), Inches(12.05), Inches(5.6))
    bg.fill.solid()
    bg.fill.fore_color.rgb = THEME.panel_soft
    bg.line.color.rgb = THEME.accent
    bg.line.width = Pt(1)

    slots = [
        (Inches(1.05), Inches(1.85), "이미지 A\n(실습 화면)"),
        (Inches(4.55), Inches(1.85), "이미지 B\n(패킷 분석)"),
        (Inches(8.05), Inches(1.85), "이미지 C\n(EDR 콘솔)"),
        (Inches(1.05), Inches(4.05), "이미지 D\n(ATT&CK 매핑)"),
        (Inches(4.55), Inches(4.05), "이미지 E\n(로그 대시보드)"),
        (Inches(8.05), Inches(4.05), "이미지 F\n(리포트 그래프)"),
    ]
    for x, y, label in slots:
        ph = slide.shapes.add_shape(MSO_AUTO_SHAPE_TYPE.RECTANGLE, x, y, Inches(3.1), Inches(1.75))
        ph.fill.solid()
        ph.fill.fore_color.rgb = RGBColor(8, 12, 18)
        ph.line.color.rgb = THEME.muted
        tf = ph.text_frame
        tf.clear()
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        p = tf.paragraphs[0]
        r = p.add_run()
        r.text = label
        r.font.name = "Malgun Gothic"
        r.font.size = Pt(13)
        r.font.color.rgb = THEME.muted

    _add_footer(slide)


def _add_big_image_slide(slide, title: str) -> None:
    _add_header_bar(slide, title, subtitle="큰 이미지 + 해설 박스")
    left = slide.shapes.add_shape(MSO_AUTO_SHAPE_TYPE.RECTANGLE, Inches(0.75), Inches(1.35), Inches(8.35), Inches(5.6))
    left.fill.solid()
    left.fill.fore_color.rgb = RGBColor(8, 12, 18)
    left.line.color.rgb = THEME.muted
    tf = left.text_frame
    tf.clear()
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = "메인 이미지 삽입 영역\n(사고 흐름도 / 대시보드 캡처)"
    r.font.name = "Malgun Gothic"
    r.font.size = Pt(20)
    r.font.color.rgb = THEME.muted

    notes = [("주석 1", Inches(9.35), Inches(1.55)), ("주석 2", Inches(9.35), Inches(3.0)), ("주석 3", Inches(9.35), Inches(4.45))]
    for t, x, y in notes:
        box = slide.shapes.add_shape(MSO_AUTO_SHAPE_TYPE.ROUNDED_RECTANGLE, x, y, Inches(3.2), Inches(1.05))
        box.fill.solid()
        box.fill.fore_color.rgb = THEME.panel_soft
        box.line.color.rgb = THEME.accent
        tf2 = box.text_frame
        tf2.clear()
        tf2.vertical_anchor = MSO_ANCHOR.MIDDLE
        p2 = tf2.paragraphs[0]
        rr = p2.add_run()
        rr.text = f"{t}\n핵심 해설 입력"
        rr.font.name = "Malgun Gothic"
        rr.font.size = Pt(12)
        rr.font.color.rgb = THEME.text

    _add_footer(slide)


def build_presentation(out_path: Path) -> None:
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    # 1) Cover
    cover = prs.slides.add_slide(prs.slide_layouts[6])
    _set_slide_bg(cover, THEME.bg)
    _add_visual_motif(cover)
    hero = cover.shapes.add_shape(MSO_AUTO_SHAPE_TYPE.ROUNDED_RECTANGLE, Inches(0.9), Inches(1.6), Inches(11.55), Inches(3.2))
    hero.fill.solid()
    hero.fill.fore_color.rgb = THEME.panel_soft
    hero.line.color.rgb = THEME.accent
    hero.line.width = Pt(1.3)
    tf = hero.text_frame
    tf.clear()
    tf.margin_left = Inches(0.8)
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = "모의해킹 · 분석 · 탐지/방어\n프로젝트 강의 템플릿"
    r.font.name = "Malgun Gothic"
    r.font.size = Pt(44)
    r.font.bold = True
    r.font.color.rgb = THEME.text
    p2 = tf.add_paragraph()
    p2.space_before = Pt(10)
    r2 = p2.add_run()
    r2.text = "실습 중심 · 인시던트 기반 스토리텔링 · 운영 가능한 산출물"
    r2.font.name = "Malgun Gothic"
    r2.font.size = Pt(18)
    r2.font.color.rgb = THEME.muted

    strip = cover.shapes.add_shape(MSO_AUTO_SHAPE_TYPE.RECTANGLE, Inches(0), Inches(6.7), Inches(13.333), Inches(0.8))
    strip.fill.solid()
    strip.fill.fore_color.rgb = THEME.panel
    strip.line.fill.background()
    stf = strip.text_frame
    stf.clear()
    stf.margin_left = Inches(0.9)
    stf.vertical_anchor = MSO_ANCHOR.MIDDLE
    sp = stf.paragraphs[0]
    sr = sp.add_run()
    sr.text = "강사명 / 과정명 / 날짜  |  버전 v1.0"
    sr.font.name = "Malgun Gothic"
    sr.font.size = Pt(16)
    sr.font.color.rgb = THEME.muted

    badge = cover.shapes.add_shape(MSO_AUTO_SHAPE_TYPE.ROUNDED_RECTANGLE, Inches(10.3), Inches(0.6), Inches(2.5), Inches(0.6))
    badge.fill.solid()
    badge.fill.fore_color.rgb = THEME.bg
    badge.line.color.rgb = THEME.accent
    badge.line.width = Pt(1.2)
    btf = badge.text_frame
    btf.clear()
    btf.vertical_anchor = MSO_ANCHOR.MIDDLE
    bp = btf.paragraphs[0]
    br = bp.add_run()
    br.text = "Hands-on"
    br.font.name = "Malgun Gothic"
    br.font.size = Pt(16)
    br.font.bold = True
    br.font.color.rgb = THEME.accent

    # 2) Agenda
    agenda = prs.slides.add_slide(prs.slide_layouts[6])
    _set_slide_bg(agenda, THEME.bg)
    _add_title_and_bullets(
        agenda,
        "목차 (Agenda)",
        [
            "1. 프로젝트 개요 및 공격 시나리오",
            "2. 침투(모의해킹) 단계: 초기 접근·권한·지속성",
            "3. 분석 단계: 정적·동적·네트워크·메모리",
            "4. 탐지·방어 단계: 규칙(Sigma/YARA)·EDR·SOAR",
            "5. 인시던트 리포트 & 운영 이관(체크리스트)",
        ],
    )

    # 3) Section divider: Pentest
    s1 = prs.slides.add_slide(prs.slide_layouts[6])
    _add_section_slide(s1, "PART 1", "모의해킹(침투) 설계와 재현")

    # 4) Content: Scenario
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    _set_slide_bg(slide, THEME.bg)
    _add_title_and_bullets(
        slide,
        "공격 시나리오 정의",
        [
            "목표 자산/범위(네트워크·계정·클라우드 리소스) 정의",
            "공격 체인(MITRE ATT&CK) 매핑: Initial Access → Execution → Persistence",
            "성공 기준: 탐지 로그 확보, IOC 도출, 대응 플레이북 검증",
            "윤리/법적 준수: 승인 범위·데이터 취급·증적(Chain of Custody)",
        ],
    )

    # 5) Two-column: Offensive vs Defensive artifacts
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    _set_slide_bg(slide, THEME.bg)
    _add_two_column(slide, "산출물(Artifacts) 설계", "공격(레드팀) 산출물", "방어(블루팀) 산출물")

    # 5-1) Process diagram
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    _set_slide_bg(slide, THEME.bg)
    _add_process_diagram_slide(slide, "강의 진행 프로세스 도식")

    # 5-2) Image-rich slide
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    _set_slide_bg(slide, THEME.bg)
    _add_big_image_slide(slide, "핵심 사례 이미지 분석")

    # 6) Section divider: Analysis
    s2 = prs.slides.add_slide(prs.slide_layouts[6])
    _add_section_slide(s2, "PART 2", "악성코드/행위 분석으로 근거 만들기")

    # 7) Content: Analysis workflow
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    _set_slide_bg(slide, THEME.bg)
    _add_title_and_bullets(
        slide,
        "분석 워크플로우 (정적 → 동적 → 네트워크)",
        [
            "정적: 해시/PE 메타/문자열/임포트/패커·난독화 여부",
            "동적: 프로세스 트리·파일/레지스트리·스케줄러·서비스 변경",
            "네트워크: DNS/HTTP(S)/TLS 지문·C2 패턴·도메인 생성(DGA)",
            "증거 정리: IOC, TTP, 타임라인, 재현 가능한 스텝",
        ],
    )

    # 8) Code: detection rule
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    _set_slide_bg(slide, THEME.bg)
    _add_code_slide(slide, "탐지 규칙 예시 (Sigma/YARA)")

    slide = prs.slides.add_slide(prs.slide_layouts[6])
    _set_slide_bg(slide, THEME.bg)
    _add_image_grid_slide(slide, "분석 근거 이미지 보드")

    # 9) Section divider: Detection & Defense
    s3 = prs.slides.add_slide(prs.slide_layouts[6])
    _add_section_slide(s3, "PART 3", "탐지·방어: 운영 가능한 룰과 자동화")

    slide = prs.slides.add_slide(prs.slide_layouts[6])
    _set_slide_bg(slide, THEME.bg)
    _add_architecture_slide(slide, "탐지/방어 아키텍처 도식")

    # 10) Timeline (incident)
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    _set_slide_bg(slide, THEME.bg)
    _add_timeline_slide(slide, "인시던트 타임라인")

    # 11) Checklist
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    _set_slide_bg(slide, THEME.bg)
    _add_checklist_slide(
        slide,
        "운영 이관 체크리스트",
        [
            "탐지 룰(시그마/EDR 쿼리)과 테스트 케이스 포함",
            "오탐/정탐 기준과 예외 처리(화이트리스트) 문서화",
            "대응 플레이북(격리/차단/계정 잠금) 승인 라인 정의",
            "대시보드/경보 우선순위(Severity) 튜닝 근거 남기기",
            "사후 보고서(요약·영향·원인·재발방지) 템플릿 제공",
        ],
    )

    # 12) Q&A
    qa = prs.slides.add_slide(prs.slide_layouts[6])
    _set_slide_bg(qa, THEME.bg)
    _add_section_slide(qa, "Q&A", "질문과 토론")

    # 13) Thank you
    end = prs.slides.add_slide(prs.slide_layouts[6])
    _set_slide_bg(end, THEME.bg)
    _add_visual_motif(end)
    panel = end.shapes.add_shape(MSO_AUTO_SHAPE_TYPE.ROUNDED_RECTANGLE, Inches(1.2), Inches(2.25), Inches(10.95), Inches(3.0))
    panel.fill.solid()
    panel.fill.fore_color.rgb = THEME.panel_soft
    panel.line.color.rgb = THEME.accent
    panel.line.width = Pt(1.2)
    tf = panel.text_frame
    tf.clear()
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = "감사합니다"
    r.font.name = "Malgun Gothic"
    r.font.size = Pt(56)
    r.font.bold = True
    r.font.color.rgb = THEME.text
    p2 = tf.add_paragraph()
    p2.space_before = Pt(10)
    r2 = p2.add_run()
    r2.text = "연락처 / 자료 링크 / 실습 저장소"
    r2.font.name = "Malgun Gothic"
    r2.font.size = Pt(18)
    r2.font.color.rgb = THEME.muted
    _add_footer(end, right_text="END")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    prs.save(str(out_path))


if __name__ == "__main__":
    build_presentation(Path(__file__).resolve().parent / "templet.pptx")
