from manim import *

class Count(Animation):
    def __init__(self, number: DecimalNumber, start: float, end: float, **kwargs) -> None:
        # Pass number as the mobject of the animation
        super().__init__(number,  **kwargs)
        # Set start and end
        self.start = start
        self.end = end

    def interpolate_mobject(self, alpha: float) -> None:
        # Set value of DecimalNumber according to alpha
        value = self.start + (alpha * (self.end - self.start))
        self.mobject.set_value(value)

class Scene1(Scene):
    def construct(self):
        bgcolor = '#121633'
        self.camera.background_color = bgcolor
        square1 = Square()
        square1.set_stroke(color = BLUE, width = 5)
        square1.set_fill(color = BLUE_E, opacity = 0.5)
        HIS = Text("HIS")
        self.play(Create(square1),Write(HIS), run_time = 4)
        Text1 = Text("Hospital Information System")
        rectangle1 = Rectangle()
        rectangle1.set_stroke(color = BLUE, width = 5)
        rectangle1.set_fill(color = BLUE_E, opacity = 0.5)
        rectangle1.stretch(factor = 2.25, dim = 0)
        self.play(Transform(HIS, Text1),Transform(square1, rectangle1) ,run_time = 4)
        self.wait(1)
        HIS2 = Text("HIS")
        circle1 = Circle()
        circle1.set_stroke(color = BLUE, width = 5)
        circle1.set_fill(color = BLUE_E, opacity = 0.5)
        self.play(Transform(HIS, HIS2), Transform(square1, circle1))

class Scene2(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()
        bgcolor = '#121633'
        c1color = '#bf80ff'
        c1color_2 = '#e6ccff'
        c2color    = '#ff80aa'
        c2color_2 = '#ffccdd'
        c3color = '#ffff80'
        c3color_2 = '#ffffcc'
        c4color = '#df9fbf'
        c4color_2 = '#f2d9e6'
        c5color = '#bfff80'
        c5color_2 = '#e6ffcc'
        c6color = '#ffbf80'
        c6color_2 = '#ffe6cc'
        c7color = '#bfbfbf'
        c7color_2 = '#e6e6e6'
        self.camera.background_color = bgcolor
        circle1 = Circle()
        circle1.set_stroke(color = BLUE, width = 5)
        circle1.set_fill(color = BLUE_E, opacity = 0.5)
        HIS = Text("HIS")
        self.add(circle1, HIS)
        self.play(circle1.animate.scale(0.5), HIS.animate.scale(0.5))
        c1 = Circle()
        c1.set_stroke(color = c1color, width = 5)
        c1.set_fill(color = c1color_2, opacity = 0.5)
        c1.scale(0.5)
        c2 = Circle()
        c2.set_stroke(color = c2color, width = 5)
        c2.set_fill(color = c2color_2, opacity = 0.5)
        c2.scale(0.5)
        c3 = Circle()
        c3.set_stroke(color = c3color, width = 5)
        c3.set_fill(color = c3color_2, opacity = 0.5)
        c3.scale(0.5)
        c4 = Circle()
        c4.set_stroke(color = c4color, width = 5)
        c4.set_fill(color = c4color_2, opacity = 0.5)
        c4.scale(0.5)
        c5 = Circle()
        c5.set_stroke(color = c5color, width = 5)
        c5.set_fill(color = c5color_2, opacity = 0.5)
        c5.scale(0.5)
        c6 = Circle()
        c6.set_stroke(color = c6color, width = 5)
        c6.set_fill(color = c6color_2, opacity = 0.5)
        c6.scale(0.5)
        c7 = Circle()
        c7.set_stroke(color = c7color, width = 5)
        c7.set_fill(color = c7color_2, opacity = 0.5)
        c7.scale(0.5)
        c1text = Text("CIS")
        c1text.scale(0.5)
        c2text = Text("FIS")
        c2text.scale(0.5)
        c3text = Text("LIS")
        c3text.scale(0.5)
        c4text = Text("NIS")
        c4text.scale(0.5)
        c5text = Text("PIS")
        c5text.scale(0.5)
        c6text = Text("PACS")
        c6text.scale(0.5)
        c7text = Text("RIS")
        c7text.scale(0.5)
        new_locations = [3 * LEFT + 2 * UP, 1 * LEFT + 3 * UP, 1 * RIGHT + 3 * UP, 3 * RIGHT + 2 * UP, 3 * RIGHT + 2 * DOWN, 3 * DOWN, 3 * LEFT + 2 * DOWN]
        mobjects = [c1,c2,c3,c4,c5,c6,c7]
        texts = [c1text, c2text, c3text, c4text, c5text, c6text, c7text]
        for loc, mob, textz in zip(new_locations, mobjects, texts):
            self.play(Create(mob),mob.animate.shift(loc), Write(textz),textz.animate.shift(loc))
        self.play(self.camera.frame.animate.scale(0.5).move_to(c1), FadeOut(circle1,c2,c3,c4,c5,c6,c7,c2text,c3text,c4text,c5text,c6text,c7text, HIS), run_time = 2)

class Scene3(Scene):
    def construct(self):
        bgcolor = '#121633'
        c1color = '#bf80ff'
        c1color_2 = '#e6ccff'
        self.camera.background_color = bgcolor
        c1 = Circle()
        c1.set_stroke(color = c1color, width = 10)
        c1.set_fill(color = c1color_2, opacity = 0.5)
        c1text = Text("CIS")
        self.add(c1, c1text)
        self.wait(1)
        rectangle1 = Rectangle()
        rectangle1.set_stroke(color = c1color, width = 5)
        rectangle1.set_fill(color = c1color_2, opacity = 0.5)
        rectangle1.stretch(factor = 2.25, dim = 0)
        c1text_full = Text("Clinical Information System")
        self.play(Transform(c1, rectangle1), Transform(c1text, c1text_full), run_time = 2)
        self.play(c1.animate.scale(0.25),c1text.animate.scale(0.25))
        self.play(c1.animate.shift(UP*3.5),c1text.animate.shift(UP*3.5))
        cf1 = Text("Organization")
        cf2 = Text("Storage")
        cf3 = Text("Verification")
        self.play(Write(cf1), run_time = 2)
        self.play(Transform(cf1, cf2),run_time = 2)
        self.play(Transform(cf1, cf3),run_time = 2)
        self.play(FadeOut(cf1))
        firsttext = Text("How does it provide better care?")
        firsttext.shift(UP * 2.5)
        firsttext.scale(0.25)
        self.play(Write(firsttext))
        framebox = SurroundingRectangle(firsttext)
        self.play(Create(framebox))
        MH = Text("Medical History")
        MH.scale(0.5)
        MH.shift(DOWN*1.5)
        self.play(Write(MH))
        self.play(FadeOut(MH))
        newsquare = Square()
        newsquare.set_stroke(color = WHITE, width = 5)
        newsquare.shift(LEFT*3.5)
        newsquare.scale(0.5)
        self.play(Create(newsquare))
        line1 = Line(LEFT,RIGHT)
        line1.scale(0.3)
        line1.shift(LEFT*3.5)
        line1.shift(UP*0.25)
        line2 = Line(LEFT,RIGHT)
        line2.scale(0.3)
        line2.shift(LEFT*3.5)
        line3 = Line(LEFT,RIGHT)
        line3.scale(0.3)
        line3.shift(LEFT*3.5)
        line3.shift(DOWN*0.25)
        self.play(Create(line1), Create(line2), Create(line3))
        prescription_text = Text("Prescriptions")
        prescription_text.scale(0.5)
        prescription_text.shift(LEFT*3.5)
        prescription_text.shift(DOWN*1.25)
        pharmacy_text = Text("Pharmacy")
        pharmacy_text.scale(0.5)
        pharmacy_text.shift(RIGHT*2)
        pharmacy_text.shift(DOWN*1.25)
        self.play(Write(prescription_text), Write(pharmacy_text))
        prescription = VGroup(newsquare, line1, line2, line3)
        self.play(FadeOut(prescription_text))
        self.play(Rotating(prescription, radians=PI, about_point=LEFT, run_time=2))
        self.play(FadeOut(prescription), FadeOut(pharmacy_text))
        rotation_center = ORIGIN
        theta_tracker = ValueTracker(0.1)
        line1 = Line(ORIGIN, RIGHT*0.75)
        line1.set_stroke(color = YELLOW)
        line_moving = Line(ORIGIN, RIGHT)
        line_moving.set_stroke(color = YELLOW)
        line_ref = line_moving.copy()
        line_ref.set_stroke(color = YELLOW)
        line_moving.rotate(
            theta_tracker.get_value() * DEGREES, about_point=rotation_center
        )
        a = Angle(line1, line_moving, radius=0.5, other_angle=False)
        self.wait()
        line_moving.add_updater(
            lambda x: x.become(line_ref.copy()).rotate(
                theta_tracker.get_value() * DEGREES, about_point=rotation_center
            )
        )

        a.add_updater(
            lambda x: x.become(Angle(line1, line_moving, radius=0.5, other_angle=False))
        )
        number = DecimalNumber().set_color(WHITE).scale(0.5)
        number.shift(DOWN*0.75)
        number.add_updater(lambda number: number.move_to(DOWN*1.5))
        circle_new = Circle()
        circle_new.scale(1.25)
        circle_new.set_stroke(color = WHITE, width = 5)
        self.play(FadeIn(circle_new))
        self.wait(0.2)
        self.play(FadeIn(line1), FadeIn(line_moving), FadeIn(theta_tracker))
        self.play(theta_tracker.animate.set_value(360), Count(number, 0, 60), run_time = 3, rate_func = linear)

class Scene4(Scene):
    def construct(self):
        bgcolor = '#121633'
        c2color = '#ff80aa'
        c2color_2 = '#ffccdd'
        self.camera.background_color = bgcolor
        c2 = Circle()
        c2.set_stroke(color = c2color, width = 10)
        c2.set_fill(color = c2color_2, opacity = 0.5)
        c2text = Text("FIS")
        self.add(c2, c2text)
        self.wait(1)
        rectangle2 = Rectangle()
        rectangle2.set_stroke(color = c2color, width = 5)
        rectangle2.set_fill(color = c2color_2, opacity = 0.5)
        rectangle2.stretch(factor = 2.25, dim = 0)
        c2text_full = Text("Financial Information System")
        self.play(Transform(c2, rectangle2), Transform(c2text, c2text_full), run_time = 2)
        self.play(c2.animate.scale(0.25),c2text.animate.scale(0.25))
        self.play(c2.animate.shift(UP*3.5),c2text.animate.shift(UP*3.5))
        definition = Text("An organised approach to connecting and interpreting financial information.")
        definition.scale(0.5)
        self.play(Write(definition))
        self.wait(1)
        self.play(FadeOut(definition))
        uses_of_fis = Text("Uses")
        self.play(Write(uses_of_fis))
        self.play(uses_of_fis.animate.shift(UP*2.5))
        use1 = Text("Ensures that there are sufficient funds on hand to pay for obligations as they come due for payment.")
        use2 = Text("Put excess funds to use in appropriate and liquid investments.")
        use3 = Text("Determine which customers, products, product lines and subsidiaries are the most and least profitable.")
        use1.scale(0.35)
        use2.scale(0.35)
        use3.scale(0.35)
        use2.shift(DOWN*0.75)
        use3.shift(DOWN*1.5)
        self.play(Write(use1))
        self.play(Write(use2))
        self.play(Write(use3))
        self.wait(3)
        self.play(FadeOut(use1), FadeOut(use2), FadeOut(use3))
            

class Scene5(Scene):
    def construct(self):
        bgcolor = '#121633'
        self.camera.background_color = bgcolor
        c3color = '#ffff80'
        c3color_3 = '#ffffcc'
        self.camera.background_color = bgcolor
        c3 = Circle()
        c3.set_stroke(color = c3color, width = 10)
        c3.set_fill(color = c3color_3, opacity = 0.5)
        c3text = Text("LIS")
        self.add(c3, c3text)
        self.wait(1)
        rectangle3 = Rectangle()
        rectangle3.set_stroke(color = c3color, width = 5)
        rectangle3.set_fill(color = c3color_3, opacity = 0.5)
        rectangle3.stretch(factor = 2.5, dim = 0)
        c3text_full = Text("Laboratory Information System")
        self.play(Transform(c3, rectangle3), Transform(c3text, c3text_full), run_time = 2)
        self.play(c3.animate.scale(0.25),c3text.animate.scale(0.25))
        self.play(c3.animate.shift(UP*3.5),c3text.animate.shift(UP*3.5))
        definition = Text("Software system that records, manages, and stores data for clinical laboratories.")
        definition.scale(0.5)
        self.play(Write(definition))
        self.wait(1)
        self.play(FadeOut(definition))
        uses_of_fis = Text("Uses")
        self.play(Write(uses_of_fis))
        self.play(uses_of_fis.animate.shift(UP*2.5))
        firsttext = Text("Sending test orders to lab instruments.")
        secondtext = Text("Tracking orders.")
        firsttext.scale(0.35)
        secondtext.scale(0.35)
        secondtext.shift(DOWN*0.75)
        self.play(Write(firsttext))
        self.play(Write(secondtext))
        self.wait(3)
        self.play(FadeOut(firsttext), FadeOut(secondtext))



class Scene6(Scene):
    def construct(self):
        bgcolor = '#121633'
        self.camera.background_color = bgcolor
        c4color = '#df9fbf'
        c4color_2 = '#f2d9e6'
        self.camera.background_color = bgcolor
        c4 = Circle()
        c4.set_stroke(color = c4color, width = 10)
        c4.set_fill(color = c4color_2, opacity = 0.5)
        c4text = Text("NIS")
        self.add(c4, c4text)
        self.wait(1)
        rectangle4 = Rectangle()
        rectangle4.set_stroke(color = c4color, width = 5)
        rectangle4.set_fill(color = c4color_2, opacity = 0.5)
        rectangle4.stretch(factor = 2.5, dim = 0)
        c4text_full = Text("Nursing Information System")
        self.play(Transform(c4, rectangle4), Transform(c4text, c4text_full), run_time = 2)
        self.play(c4.animate.scale(0.25),c4text.animate.scale(0.25))
        self.play(c4.animate.shift(UP*3.5),c4text.animate.shift(UP*3.5))
        definition = Text("It refers to the application of computer science and information science to manage operations involved in the nursing profession.")
        definition.scale(0.25)
        self.play(Write(definition))
        self.wait(2.5)
        self.play(FadeOut(definition))
        uses_of_fis = Text("Uses")
        self.play(Write(uses_of_fis))
        self.play(uses_of_fis.animate.shift(UP*2.5))
        use1 = Text("It helps improved nurses’ documentation.")
        use2 = Text("It helps in overall better staff management.")
        use3 = Text("It helps in having an efficient decision-making process.")
        use1.scale(0.35)
        use2.scale(0.35)
        use3.scale(0.35)
        use2.shift(DOWN*0.75)
        use3.shift(DOWN*1.5)
        self.play(Write(use1))
        self.play(Write(use2))
        self.play(Write(use3))
        self.wait(3)
        self.play(FadeOut(use1), FadeOut(use2), FadeOut(use3))

class Scene7(Scene):
    def construct(self):
        bgcolor = '#121633'
        self.camera.background_color = bgcolor
        c3color = '#bfff80'
        c3color_3 = '#e6ffcc'
        self.camera.background_color = bgcolor
        c3 = Circle()
        c3.set_stroke(color = c3color, width = 10)
        c3.set_fill(color = c3color_3, opacity = 0.5)
        c3text = Text("PIS")
        self.add(c3, c3text)
        self.wait(1)
        rectangle3 = Rectangle()
        rectangle3.set_stroke(color = c3color, width = 5)
        rectangle3.set_fill(color = c3color_3, opacity = 0.5)
        rectangle3.stretch(factor = 3, dim = 0)
        c3text_full = Text("Pharmaceutical Information System")
        self.play(Transform(c3, rectangle3), Transform(c3text, c3text_full), run_time = 2)
        self.play(c3.animate.scale(0.25),c3text.animate.scale(0.25))
        self.play(c3.animate.shift(UP*3.5),c3text.animate.shift(UP*3.5))
        definition = Text("The pharmacy information system (PIS) is a multi-functional system that allows pharmacists to maintain the supply and organization of prescription drugs.")
        definition.scale(0.25)
        self.play(Write(definition))
        self.wait(2.75)
        self.play(FadeOut(definition))
        uses_of_fis = Text("Uses")
        self.play(Write(uses_of_fis))
        self.play(uses_of_fis.animate.shift(UP*2.5))
        use1 = Text("Supports the distribution and management of drugs.")
        use2 = Text("Shows drug and medical device inventory.")
        use3 = Text("Facilitates the needed reports.")
        use1.scale(0.35)
        use2.scale(0.35)
        use3.scale(0.35)
        use2.shift(DOWN*0.75)
        use3.shift(DOWN*1.5)
        self.play(Write(use1))
        self.play(Write(use2))
        self.play(Write(use3))
        self.wait(3)
        self.play(FadeOut(use1), FadeOut(use2), FadeOut(use3))

class Scene8(Scene):
    def construct(self):
        bgcolor = '#121633'
        c3color = '#ffbf80'
        c3color_2 = '#ffe6cc'
        self.camera.background_color = bgcolor
        c3 = Circle()
        c3.set_stroke(color = c3color, width = 10)
        c3.set_fill(color = c3color_2, opacity = 0.5)
        c3text = Text("PACS")
        self.add(c3, c3text)
        self.wait(1)
        rectangle3 = Rectangle()
        rectangle3.set_stroke(color = c3color, width = 5)
        rectangle3.set_fill(color = c3color_2, opacity = 0.5)
        rectangle3.stretch(factor = 3.5, dim = 0)
        c3text_full = Text("Picture Archiving and Communication System")
        self.play(Transform(c3, rectangle3), Transform(c3text, c3text_full), run_time = 2)
        self.play(c3.animate.scale(0.25),c3text.animate.scale(0.25))
        self.play(c3.animate.shift(UP*3.5),c3text.animate.shift(UP*3.5))
        definition = Text("It is a medical imaging technology which provides economical storage and convenient access to images from multiple source machine types.")
        definition.scale(0.25)
        self.play(Write(definition))
        self.wait(3.5)
        self.play(FadeOut(definition))
        uses_of_fis = Text("Uses")
        self.play(Write(uses_of_fis))
        self.play(uses_of_fis.animate.shift(UP*2.5))
        use1 = Text("Replaces the hard-copy means of managing medical images. Hence it helps save time and costs and previous images can be accessed instantly.")
        use2 = Text("Allows off-site practicioners to view and report the medical images.")
        use3 = Text("It acts as a platform for radiology images interfacing.")
        use4 = Text("It is used by radiology staff to manage the workflow of patient exams.")
        use1.scale(0.3)
        use2.scale(0.3)
        use3.scale(0.3)
        use4.scale(0.3)
        use2.shift(DOWN*0.75)
        use3.shift(DOWN*1.5)
        use4.shift(DOWN*2.5)
        self.play(Write(use1))
        self.play(Write(use2))
        self.play(Write(use3))
        self.play(Write(use4))
        self.wait(10)
        self.play(FadeOut(use1), FadeOut(use2), FadeOut(use3), FadeOut(use4))

class Scene9(Scene):
    def construct(self):
        bgcolor = '#121633'
        c3color = '#bfbfbf'
        c3color_2 = '#e6e6e6'
        self.camera.background_color = bgcolor
        c3 = Circle()
        c3.set_stroke(color = c3color, width = 10)
        c3.set_fill(color = c3color_2, opacity = 0.5)
        c3text = Text("RIS")
        self.add(c3, c3text)
        self.wait(1)
        rectangle3 = Rectangle()
        rectangle3.set_stroke(color = c3color, width = 5)
        rectangle3.set_fill(color = c3color_2, opacity = 0.5)
        rectangle3.stretch(factor = 3.5, dim = 0)
        c3text_full = Text("Radiological Information System")
        self.play(Transform(c3, rectangle3), Transform(c3text, c3text_full), run_time = 2)
        self.play(c3.animate.scale(0.25),c3text.animate.scale(0.25))
        self.play(c3.animate.shift(UP*3.5),c3text.animate.shift(UP*3.5))
        definition = Text("It is the core system for the electronic management of the imaging departments.")
        definition.scale(0.25)
        self.play(Write(definition))
        self.wait(3.5)
        self.play(FadeOut(definition))
        uses_of_fis = Text("Uses")
        self.play(Write(uses_of_fis))
        self.play(uses_of_fis.animate.shift(UP*2.5))
        use1 = Text("The RIS allows staff to make appointments for both inpatients and outpatients.")
        use2 = Text("A RIS can generate statistical reports for a single patient, group of patients or particular procedures. ")
        use3 = Text("Using a RIS system, providers can track a patient's entire radiology history from admission to discharge.")
        use1.scale(0.35)
        use2.scale(0.35)
        use3.scale(0.35)
        use2.shift(DOWN*0.75)
        use3.shift(DOWN*1.5)
        self.play(Write(use1))
        self.play(Write(use2))
        self.play(Write(use3))
        self.wait(3)
        self.play(FadeOut(use1), FadeOut(use2), FadeOut(use3))