from manim import *

class InsertingTextExample(Scene):
    def construct(self):
        intro = 'I'm Rustam Ali, a\n passionate Data Science student\n from NIT Jamshedpur. My academic\n journey has equipped me with a\n strong foundation in Machine\n Learning, Deep Learning, data\n analysis, software development,\n and many more.'
        
        # Create the full text object
        text = Text("", color=PURPLE).scale(1.5).to_edge(LEFT)
        cursor = Rectangle(
            color=GREY_A,
            fill_color=GREY_A,
            fill_opacity=1.0,
            height=0.8,
            width=0.1,
        )
        
        # Position cursor at starting position
        cursor.move_to(text.get_left())
        self.add(text, cursor)
        
        # Build text character by character
        current_text = ""
        
        for i, char in enumerate(intro):
            current_text += char
            new_text = Text(current_text, color=PURPLE).scale(1.5).to_edge(LEFT)
            
            # Update cursor position based on the current text
            if char == '\n':
                # For newlines, position cursor at start of new line
                lines_so_far = current_text.count('\n')
                cursor_pos = new_text.get_left() + DOWN * lines_so_far * 0.8
            else:
                # For regular characters, position cursor at end of text
                cursor_pos = new_text.get_right() + RIGHT * 0.05
            
            # Animate the text change and cursor movement
            self.play(
                Transform(text, new_text),
                cursor.animate.move_to(cursor_pos),
                run_time=0.05
            )
        
        # Final cursor blinks
        self.play(FadeOut(cursor), run_time=0.3)
        self.play(FadeIn(cursor), run_time=0.3)
        self.play(FadeOut(cursor), run_time=0.3)
        self.play(FadeIn(cursor), run_time=0.3)