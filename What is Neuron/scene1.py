from manim import * 

class InitialScene(Scene):
    def construct(self):
        title = Text("Neurons in Deep Learning", font_size=48, color=YELLOW)
        subtitle = Text("How Machines Think", font_size=32, color=WHITE).next_to(title, DOWN)

        underline = Line(
            start = title.get_left() + DOWN * 0.4,
            end = title.get_right() + DOWN * 0.4,
            color = YELLOW
        )

        self.play(Write(title), run_time=1.5)
        self.play(Create(underline), FadeIn(subtitle), run_time=1)
        self.wait(2)
        self.play(
            title.animate.scale(1.1).set_color(BLUE_B),
            subtitle.animate.shift(DOWN * 0.5).set_color(GRAY_B),
            run_time=1 
        )
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle), FadeOut(underline), run_time=1)


class Intro(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        num_layers = 4
        nodes_per_layer = [3, 5, 4, 2]
        layer_distance = 2.5
        node_distance = 0.7

        layers = VGroup()
        node_positions = []

        # Create layers and nodes
        for i, num_nodes in enumerate(nodes_per_layer):
            layer = VGroup()
            positions = []
            for j in range(num_nodes):
                node = Sphere(radius=0.18, color=YELLOW)
                y = (j - (num_nodes - 1) / 2) * node_distance
                pos = np.array([i * layer_distance, y, 0])
                node.move_to(pos)
                layer.add(node)
                positions.append(pos)
            layers.add(layer)
            node_positions.append(positions)

        self.add(layers)

        # Draw connections between layers
        for i in range(len(node_positions) - 1):
            for start in node_positions[i]:
                for end in node_positions[i + 1]:
                    edge = Line3D(start, end, color=GREY)
                    self.add(edge)

        self.wait(1)

        # Animate data passing through nodes
        for i, layer in enumerate(layers):
            for node in layer:
                self.play(node.animate.set_color(RED), run_time=0.3)
            self.wait(0.5)
            for node in layer:
                self.play(node.animate.set_color(YELLOW), run_time=0.2)

        # Show result at the last layer
        result_text = Text("Result", color=GREEN, size=0.5)
        result_text.move_to(node_positions[-1][0] + RIGHT * 1.2)
        self.play(FadeIn(result_text))
        self.wait(2)