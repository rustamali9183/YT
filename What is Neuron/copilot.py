from manim import *

# 🧠 What Are Neurons?
class WhatAreNeurons(Scene):
    def construct(self):
        neuron = Circle(radius=1, color=BLUE)
        inputs = [Arrow(LEFT, RIGHT).shift(UP*i*0.5) for i in range(-2, 3)]
        labels = [Text(f"x{i+1}", font_size=24).next_to(inputs[i], LEFT) for i in range(len(inputs))]

        self.play(Create(neuron))
        for i in range(len(inputs)):
            self.play(GrowArrow(inputs[i]), Write(labels[i]))
        self.wait(1)

        output = Arrow(neuron.get_right(), RIGHT*3, buff=0.1)
        self.play(GrowArrow(output))
        self.wait(1)

# 🧱 Building Blocks
class BuildingBlocks(Scene):
    def construct(self):
        pixel = Square(color=WHITE).scale(0.5)
        cell = Circle(color=GREEN).scale(0.5)
        atom = Dot(color=YELLOW).scale(2)
        neuron = Circle(color=BLUE).scale(1)

        self.play(FadeIn(pixel))
        self.wait(1)
        self.play(Transform(pixel, cell))
        self.wait(1)
        self.play(Transform(cell, atom))
        self.wait(1)
        self.play(Transform(atom, neuron))
        self.wait(2)

# 🧬 Biological vs Artificial Neurons
class BioVsArtificial(Scene):
    def construct(self):
        bio = Text("Biological Neuron", font_size=24).to_edge(LEFT)
        artificial = Text("Artificial Neuron", font_size=24).to_edge(RIGHT)
        self.play(Write(bio), Write(artificial))

        bio_flow = Arrow(LEFT*3, LEFT, color=GREEN)
        art_flow = Arrow(RIGHT*3, RIGHT, color=BLUE)
        self.play(GrowArrow(bio_flow), GrowArrow(art_flow))
        self.wait(2)

# 📐 Mathematics Behind a Neuron
class NeuronMath(Scene):
    def construct(self):
        eq = MathTex("z = w_1x_1 + w_2x_2 + \\dots + w_nx_n + b")
        self.play(Write(eq))
        self.wait(2)

        # Highlight terms
        for term in ["w_1x_1", "w_2x_2", "b"]:
            highlight = MathTex(term).set_color(YELLOW)
            self.play(Transform(eq, highlight))
            self.wait(1)
            self.play(Transform(highlight, eq))

# 🔄 How Neurons Work Together
class NetworkFlow(Scene):
    def construct(self):
        input_layer = VGroup(*[Circle(radius=0.3, color=WHITE).shift(UP*i) for i in range(-1, 2)]).shift(LEFT*3)
        hidden_layer = VGroup(*[Circle(radius=0.3, color=BLUE).shift(UP*i) for i in range(-1, 2)])
        output_layer = VGroup(*[Circle(radius=0.3, color=GREEN).shift(UP*i) for i in range(-1, 2)]).shift(RIGHT*3)

        self.play(Create(input_layer), Create(hidden_layer), Create(output_layer))
        for i in input_layer:
            for j in hidden_layer:
                self.play(GrowArrow(Arrow(i.get_right(), j.get_left(), buff=0.1)))
        self.wait(2)

# 🧠 Real-Life Example
class DigitExample(Scene):
    def construct(self):
        digit = Text("7", font_size=72).set_color(YELLOW)
        self.play(FadeIn(digit))
        self.wait(1)

        network = VGroup(*[Circle(radius=0.3, color=BLUE).shift(RIGHT*i) for i in range(1, 4)])
        self.play(Transform(digit, network[0]))
        self.wait(1)
        self.play(Transform(network[0], network[1]), Transform(network[1], network[2]))
        self.wait(2)

# 🎯 Final Thoughts
class RecapScene(Scene):
    def construct(self):
        points = BulletedList(
            "Neurons are the smallest units",
            "Inspired by biology",
            "Process data mathematically",
            "Organized into layers",
            font_size=28
        )
        self.play(Write(points))
        self.wait(3)

        outro = Text("One neuron at a time 💡", font_size=36).to_edge(DOWN)
        self.play(FadeIn(outro))
        self.wait(2)