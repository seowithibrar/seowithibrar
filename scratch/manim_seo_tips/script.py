from manim import *

# Color Palette Constants
BG_COLOR = "#0F172A"       # Dark Slate
EMERALD = "#059669"        # Academic / Growth Emerald
GOLD = "#F59E0B"           # Warm Gold
CYAN = "#38BDF8"           # Tech Cyan
WHITE = "#FFFFFF"
MUTED = "#94A3B8"

MONO_FONT = "Consolas"

class Scene1_Hook(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_subcaption("3 Golden Tips to Dominate Google Search!", duration=2.5)

        # Title Group
        badge = Text("2026 SEO GUIDE", font_size=20, color=GOLD, font=MONO_FONT, weight=BOLD)
        badge_box = SurroundingRectangle(badge, color=GOLD, buff=0.2, corner_radius=0.1)
        badge_group = VGroup(badge, badge_box).to_edge(UP, buff=0.8)

        title = Text("3 GOLDEN TIPS FOR SEO", font_size=42, color=WHITE, font=MONO_FONT, weight=BOLD)
        title.next_to(badge_group, DOWN, buff=0.4)

        # Simulated Search Bar
        search_box = Rectangle(width=7.5, height=1.0, color=CYAN, fill_color="#1E293B", fill_opacity=0.9, corner_radius=0.2)
        search_text = Text("Google Search: How to Rank #1", font_size=22, color=CYAN, font=MONO_FONT)
        search_group = VGroup(search_box, search_text).center().shift(DOWN * 0.8)

        # Animations
        self.play(FadeIn(badge_group, shift=DOWN * 0.3), run_time=0.6)
        self.play(Write(title), run_time=0.9)
        self.play(Create(search_box), Write(search_text), run_time=1.0)
        self.wait(0.5)

        # Clean Exit
        self.play(FadeOut(Group(*self.mobjects)), run_time=0.4)


class Scene2_ThreeTips(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_subcaption("1. Search Intent. 2. Page Speed. 3. E-E-A-T Trust.", duration=5.0)

        header = Text("3 ACTIONABLE SEO PILLARS", font_size=32, color=CYAN, font=MONO_FONT, weight=BOLD)
        header.to_edge(UP, buff=0.6)
        self.play(FadeIn(header, shift=DOWN * 0.2), run_time=0.5)

        # Tip 1: Search Intent
        tip1_bg = RoundedRectangle(corner_radius=0.2, width=8.5, height=1.1, color=EMERALD, fill_color="#1E293B", fill_opacity=0.8)
        tip1_title = Text("1. MATCH SEARCH INTENT", font_size=22, color=EMERALD, font=MONO_FONT, weight=BOLD)
        tip1_desc = Text("Solve user query with top clarity", font_size=16, color=MUTED, font=MONO_FONT)
        tip1_text = VGroup(tip1_title, tip1_desc).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        tip1_group = VGroup(tip1_bg, tip1_text).shift(UP * 1.2)
        tip1_text.move_to(tip1_bg.get_center()).shift(RIGHT * 0.3)

        # Tip 2: Technical Speed
        tip2_bg = RoundedRectangle(corner_radius=0.2, width=8.5, height=1.1, color=CYAN, fill_color="#1E293B", fill_opacity=0.8)
        tip2_title = Text("2. ULTRA-FAST PAGE SPEED", font_size=22, color=CYAN, font=MONO_FONT, weight=BOLD)
        tip2_desc = Text("Core Web Vitals load < 1.5 seconds", font_size=16, color=MUTED, font=MONO_FONT)
        tip2_text = VGroup(tip2_title, tip2_desc).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        tip2_group = VGroup(tip2_bg, tip2_text).next_to(tip1_group, DOWN, buff=0.35)
        tip2_text.move_to(tip2_bg.get_center()).shift(RIGHT * 0.3)

        # Tip 3: E-E-A-T & Authority
        tip3_bg = RoundedRectangle(corner_radius=0.2, width=8.5, height=1.1, color=GOLD, fill_color="#1E293B", fill_opacity=0.8)
        tip3_title = Text("3. HIGH E-E-A-T TRUST", font_size=22, color=GOLD, font=MONO_FONT, weight=BOLD)
        tip3_desc = Text("Expertise, Authority & Whitehat Links", font_size=16, color=MUTED, font=MONO_FONT)
        tip3_text = VGroup(tip3_title, tip3_desc).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        tip3_group = VGroup(tip3_bg, tip3_text).next_to(tip2_group, DOWN, buff=0.35)
        tip3_text.move_to(tip3_bg.get_center()).shift(RIGHT * 0.3)

        # Sequenced Entrance
        self.play(Create(tip1_bg), Write(tip1_text), run_time=1.2)
        self.play(Create(tip2_bg), Write(tip2_text), run_time=1.2)
        self.play(Create(tip3_bg), Write(tip3_text), run_time=1.2)
        self.wait(1.0)

        # Clean Exit
        self.play(FadeOut(Group(*self.mobjects)), run_time=0.4)


class Scene3_Outro(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_subcaption("Dominate Google Search with SEO With Ibrar!", duration=2.5)

        rank_badge = Text("#1 RANKING", font_size=24, color=GOLD, font=MONO_FONT, weight=BOLD)
        main_title = Text("DOMINATE GOOGLE SEARCH!", font_size=38, color=EMERALD, font=MONO_FONT, weight=BOLD)
        subtitle = Text("SEO With Ibrar | seowithibrar.com", font_size=22, color=CYAN, font=MONO_FONT)

        group = VGroup(rank_badge, main_title, subtitle).arrange(DOWN, buff=0.4).center()

        box = SurroundingRectangle(group, color=EMERALD, buff=0.4, corner_radius=0.2)

        self.play(Create(box), Write(group), run_time=1.4)
        self.play(group.animate.scale(1.05), run_time=0.6)
        self.wait(0.5)

        self.play(FadeOut(Group(*self.mobjects)), run_time=0.3)
