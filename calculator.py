import pygame

pygame.init()

dimensions = 650,610

WIN = pygame.display.set_mode(dimensions)

pygame.display.set_caption("Calculator")

BLACK_COLOR = (0,0,0)
WHITE_COLOR = (255,255,255)
RED_COLOR = (255,0,0)

def main():
    clock = pygame.time.Clock()

    fonts = pygame.font.SysFont("comicsans", 70)

    text = fonts.render("Press me!", True, WHITE_COLOR)

    FPS = 60
    running = True
    num1 = ""
    method = ""
    num2 = ""

    num1_mode = "True"
    method_mode = False
    num2_mode = "False"
    num1_method = ""

    def get_w2(object):
        return object.get_width()/2

    def get_h2(object):
        return object.get_height()/2

    def get_x2(x, w):
        return x - w/2
    
    def get_y2(y, h):
        return y - h/2

    def make_buttons(window, color, font_color, x, y, w, h, event, fonts, text):
        pygame.draw.rect(window, color, (x, y, w, h))
        text_ = fonts.render(text, font_color, True) 
        redraw_windows(WIN, text_, x+w/2/2, y-h/2/2)
        mx,my = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (mx >= x) and (mx <= (x + w)) and (my >= y) and (my <= (y + h)):
                return True
        

    def redraw_windows(window, object, x, y):
        window.blit(object, (x,y))
        pygame.display.update()

    while running:
        clock.tick(FPS)
        pygame.display.update()
        

        for event in pygame.event.get():

            if make_buttons(WIN, WHITE_COLOR, RED_COLOR, 0, 400, 70, 70, event, fonts, "1"):
                if num1_mode == "Erase":
                    pygame.draw.rect(WIN, BLACK_COLOR, (0,0,650,400))
                    num1_mode = "True"
                if num1_mode == "True":
                    num1 = num1 + "1"
                    num1_text = fonts.render(num1, True, RED_COLOR)
                    redraw_windows(WIN, num1_text, 0,0)
                if num2_mode == "True":
                    num2 = num2 + "1"
                    num1_method_num2 = num1_method + num2
                    num1_method_num2_text = fonts.render(num1_method_num2, True, RED_COLOR)
                    redraw_windows(WIN, num1_method_num2_text, 0, 0)
            if make_buttons(WIN, WHITE_COLOR, RED_COLOR, 70, 400, 70, 70, event, fonts, "2"):
                if num1_mode == "Erase":
                    pygame.draw.rect(WIN, BLACK_COLOR, (0,0,650,400))
                    num1_mode = "True"
                if num1_mode == "True":
                    num1 = num1 + "2"
                    num1_text = fonts.render(num1, True, RED_COLOR)
                    redraw_windows(WIN, num1_text, 0,0)
                if num2_mode == "True":
                    num2 = num2 + "2"
                    num1_method_num2 = num1_method + num2
                    num1_method_num2_text = fonts.render(num1_method_num2, True, RED_COLOR)
                    redraw_windows(WIN, num1_method_num2_text, 0, 0)
            if make_buttons(WIN, WHITE_COLOR, RED_COLOR, 140, 400, 70, 70, event, fonts, "3"):
                if num1_mode == "Erase":
                    pygame.draw.rect(WIN, BLACK_COLOR, (0,0,650,400))
                    num1_mode = "True"
                if num1_mode == "True":
                    num1 = num1 + "3"
                    num1_text = fonts.render(num1, True, RED_COLOR)
                    redraw_windows(WIN, num1_text, 0,0)
                if num2_mode == "True":
                    num2 = num2 + "3"
                    num1_method_num2 = num1_method + num2
                    num1_method_num2_text = fonts.render(num1_method_num2, True, RED_COLOR)
                    redraw_windows(WIN, num1_method_num2_text, 0, 0)
            if make_buttons(WIN, WHITE_COLOR, RED_COLOR, 210, 400, 70, 70, event, fonts, "4"):
                if num1_mode == "Erase":
                    pygame.draw.rect(WIN, BLACK_COLOR, (0,0,650,400))
                    num1_mode = "True"
                if num1_mode == "True":
                    num1 = num1 + "4"
                    num1_text = fonts.render(num1, True, RED_COLOR)
                    redraw_windows(WIN, num1_text, 0,0)
                if num2_mode == "True":
                    num2 = num2 + "4"
                    num1_method_num2 = num1_method + num2
                    num1_method_num2_text = fonts.render(num1_method_num2, True, RED_COLOR)
                    redraw_windows(WIN, num1_method_num2_text, 0, 0)
            if make_buttons(WIN, WHITE_COLOR, RED_COLOR, 280, 400, 70, 70, event, fonts, "5"):
                if num1_mode == "Erase":
                    pygame.draw.rect(WIN, BLACK_COLOR, (0,0,650,400))
                    num1_mode = "True"
                if num1_mode == "True":
                    num1 = num1 + "5"
                    num1_text = fonts.render(num1, True, RED_COLOR)
                    redraw_windows(WIN, num1_text, 0,0)
                if num2_mode == "True":
                    num2 = num2 + "5"
                    num1_method_num2 = num1_method + num2
                    num1_method_num2_text = fonts.render(num1_method_num2, True, RED_COLOR)
                    redraw_windows(WIN, num1_method_num2_text, 0, 0)
            if make_buttons(WIN, WHITE_COLOR, RED_COLOR, 0, 470, 70, 70, event, fonts, "6"):
                if num1_mode == "Erase":
                    pygame.draw.rect(WIN, BLACK_COLOR, (0,0,650,400))
                    num1_mode = "True"
                if num1_mode == "True":
                    num1 = num1 + "6"
                    num1_text = fonts.render(num1, True, RED_COLOR)
                    redraw_windows(WIN, num1_text, 0,0)
                if num2_mode == "True":
                    num2 = num2 + "6"
                    num1_method_num2 = num1_method + num2
                    num1_method_num2_text = fonts.render(num1_method_num2, True, RED_COLOR)
                    redraw_windows(WIN, num1_method_num2_text, 0, 0)
            if make_buttons(WIN, WHITE_COLOR, RED_COLOR, 70, 470, 70, 70, event, fonts, "7"):
                if num1_mode == "Erase":
                    pygame.draw.rect(WIN, BLACK_COLOR, (0,0,650,400))
                    num1_mode = "True"
                if num1_mode == "True":
                    num1 = num1 + "7"
                    num1_text = fonts.render(num1, True, RED_COLOR)
                    redraw_windows(WIN, num1_text, 0,0)
                if num2_mode == "True":
                    num2 = num2 + "7"
                    num1_method_num2 = num1_method + num2
                    num1_method_num2_text = fonts.render(num1_method_num2, True, RED_COLOR)
                    redraw_windows(WIN, num1_method_num2_text, 0, 0)
            if make_buttons(WIN, WHITE_COLOR, RED_COLOR, 140, 470, 70, 70, event, fonts, "8"):
                if num1_mode == "Erase":
                    pygame.draw.rect(WIN, BLACK_COLOR, (0,0,650,400))
                    num1_mode = "True"
                if num1_mode == "True":
                    num1 = num1 + "8"
                    num1_text = fonts.render(num1, True, RED_COLOR)
                    redraw_windows(WIN, num1_text, 0,0)
                if num2_mode == "True":
                    num2 = num2 + "8"
                    num1_method_num2 = num1_method + num2
                    num1_method_num2_text = fonts.render(num1_method_num2, True, RED_COLOR)
                    redraw_windows(WIN, num1_method_num2_text, 0, 0)
            if make_buttons(WIN, WHITE_COLOR, RED_COLOR, 210, 470, 70, 70, event, fonts, "9"):
                if num1_mode == "Erase":
                    pygame.draw.rect(WIN, BLACK_COLOR, (0,0,650,400))
                    num1_mode = "True"
                if num1_mode == "True":
                    num1 = num1 + "9"
                    num1_text = fonts.render(num1, True, RED_COLOR)
                    redraw_windows(WIN, num1_text, 0,0)
                if num2_mode == "True":
                    num2 = num2 + "9"
                    num1_method_num2 = num1_method + num2
                    num1_method_num2_text = fonts.render(num1_method_num2, True, RED_COLOR)
                    redraw_windows(WIN, num1_method_num2_text, 0, 0)
            if make_buttons(WIN, WHITE_COLOR, BLACK_COLOR, 280, 470, 70, 70, event, fonts, "0"):
                if num1_mode == "Erase":
                    pygame.draw.rect(WIN, BLACK_COLOR, (0,0,650,400))
                    num1_mode = "True"
                if num1_mode == "True":
                    num1 = num1 + "0"
                    num1_text = fonts.render(num1, True, RED_COLOR)
                    redraw_windows(WIN, num1_text, 0,0)
                if num2_mode == "True":
                    num2 = num2 + "0"
                    num1_method_num2 = num1_method + num2
                    num1_method_num2_text = fonts.render(num1_method_num2, True, RED_COLOR)
                    redraw_windows(WIN, num1_method_num2_text, 0, 0)
            if make_buttons(WIN, WHITE_COLOR, RED_COLOR, 0, 540, 70, 70, event, fonts, "X"):
                if not num1 == "" and method == "" and num2 == "":
                    num1_mode = "False"
                    method_mode = True
                    method = "*"
                    method_mode = False 
                    pygame.draw.rect(WIN, BLACK_COLOR, (0,0,650,400))
                    num1_method = num1 + method
                    num1_method_text = fonts.render(num1_method, True, RED_COLOR)
                    redraw_windows(WIN, num1_method_text, 0, 0)
                    num1_mode = "False"
                    num2_mode = "True"

            if make_buttons(WIN, WHITE_COLOR, RED_COLOR, 70, 540, 70, 70, event, fonts, "/"):
                if not num1 == "" and method == "" and num2 == "":
                    num1_mode = "False"
                    method_mode = True
                    method = "/"
                    method_mode = False
                    pygame.draw.rect(WIN, BLACK_COLOR, (0,0,650,400))
                    num1_method = num1 + method
                    num1_method_text = fonts.render(num1_method, True, RED_COLOR)
                    redraw_windows(WIN, num1_method_text, 0, 0)
                    num1_mode = "False"
                    num2_mode = "True"

            if make_buttons(WIN, WHITE_COLOR, RED_COLOR, 140, 540, 70, 70, event, fonts, "+"):
                if not num1 == "" and method == "" and num2 == "":
                    num1_mode = "False"
                    method_mode = True
                    method = "+"
                    method_mode = False
                    pygame.draw.rect(WIN, BLACK_COLOR, (0,0,650,400))
                    num1_method = num1 + method
                    num1_method_text = fonts.render(num1_method, True, RED_COLOR)
                    redraw_windows(WIN, num1_method_text, 0, 0)
                    num1_mode = "False"
                    num2_mode = "True"

            if make_buttons(WIN, WHITE_COLOR, RED_COLOR, 210, 540, 70, 70, event, fonts, "-"):
                if not num1 == "" and method == "" and num2 == "" and num2_mode == "False":
                    num1_mode = "False"
                    method_mode = True
                    method = "-"
                    method_mode = False
                    pygame.draw.rect(WIN, BLACK_COLOR, (0,0,650,400))
                    num1_method = num1 + method
                    num1_method_text = fonts.render(num1_method, True, RED_COLOR)
                    redraw_windows(WIN, num1_method_text, 0, 0)
                    num1_mode = "False"
                    num2_mode = "True"

            if make_buttons(WIN, WHITE_COLOR, RED_COLOR, 280, 540, 70, 70, event, fonts, "="):
                if not num1 == "" and not num2 == "" and not method == "" and num2_mode == "True":
                    if method == "*":
                        pygame.draw.rect(WIN, BLACK_COLOR, (0,0,650,400))
                        answer = str(int(num1) * int(num2))
                        answer_text = fonts.render(answer, True, RED_COLOR)
                        redraw_windows(WIN, answer_text, 0, 0)
                        num1 = ""
                        method = ""
                        num2 = ""
                        num1_mode = "Erase"
                        num2_mode = "False"
                        answer = ""
                    if method == "/":
                        pygame.draw.rect(WIN, BLACK_COLOR, (0,0,650,400))
                        answer = str(round(int(num1) / int(num2), 2))
                        answer_text = fonts.render(answer, True, RED_COLOR)
                        redraw_windows(WIN, answer_text, 0, 0)
                        num1 = ""
                        method = ""
                        num2 = ""
                        num1_mode = "Erase"
                        num2_mode = "False"
                        answer = ""
                    if method == "+":
                        pygame.draw.rect(WIN, BLACK_COLOR, (0,0,650,400))
                        answer = str(int(num1) + int(num2))
                        answer_text = fonts.render(answer, True, RED_COLOR)
                        redraw_windows(WIN, answer_text, 0, 0)
                        num1 = ""
                        method = ""
                        num2 = ""
                        num1_mode = "Erase"
                        num2_mode = "False"
                        answer = ""
                    if method == "-":
                        pygame.draw.rect(WIN, BLACK_COLOR, (0,0,650,400))
                        answer = str(int(num1) - int(num2))
                        answer_text = fonts.render(answer, True, RED_COLOR)
                        redraw_windows(WIN, answer_text, 0, 0)
                        num1 = ""
                        method = ""
                        num2 = ""
                        num1_mode = "Erase"
                        num2_mode = "False"
                        answer = ""
                        
            if event.type == pygame.QUIT:
                running = False
                

main()