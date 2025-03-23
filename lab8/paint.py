import pygame
import math

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Drawing Tool")
    clock = pygame.time.Clock()
    
    # переменные инструмента
    radius = 15
    current_color = (0, 0, 255)  # Start with blue
    tool = 'pen'  # Tools: 'pen', 'rectangle', 'circle', 'eraser'
    
    # состояние кисти
    drawing = False
    start_pos = None
    current_pos = None
    
    # холст
    canvas = pygame.Surface((640, 480))
    canvas.fill((0, 0, 0))
    
    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                
                # выбор цвета
                if event.key == pygame.K_r:
                    current_color = (255, 0, 0)
                elif event.key == pygame.K_g:
                    current_color = (0, 255, 0)
                elif event.key == pygame.K_b:
                    current_color = (0, 0, 255)
                elif event.key == pygame.K_y:
                    current_color = (255, 255, 0)
                elif event.key == pygame.K_c:
                    current_color = (0, 255, 255)
                elif event.key == pygame.K_m:
                    current_color = (255, 0, 255)
                elif event.key == pygame.K_w:
                    current_color = (255, 255, 255)
                elif event.key == pygame.K_k:
                    current_color = (0, 0, 0)
                
                # выбор инструмента
                if event.key == pygame.K_1:
                    tool = 'pen'
                elif event.key == pygame.K_2:
                    tool = 'rectangle'
                elif event.key == pygame.K_3:
                    tool = 'circle'
                elif event.key == pygame.K_4:
                    tool = 'eraser'
            
            # управление мышью
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # лкм
                    if tool in ['pen', 'eraser']:
                        drawing = True
                    elif tool in ['rectangle', 'circle']:
                        start_pos = event.pos
                        drawing = True
                elif event.button == 3:  # пкм
                    if tool in ['pen', 'eraser']:
                        radius = max(1, radius - 1)  # уменьшить радиус
            
            if event.type == pygame.MOUSEMOTION:
                if drawing and tool in ['pen', 'eraser']:
                    color = current_color if tool == 'pen' else (0, 0, 0)
                    pos = event.pos
                    pygame.draw.circle(canvas, color, pos, radius)
                elif drawing and tool in ['rectangle', 'circle']:
                    current_pos = event.pos
            
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and drawing:
                    if tool in ['rectangle', 'circle']:
                        end_pos = event.pos
                        if tool == 'rectangle':
                            rect = pygame.Rect(
                                min(start_pos[0], end_pos[0]),
                                min(start_pos[1], end_pos[1]),
                                abs(end_pos[0] - start_pos[0]),
                                abs(end_pos[1] - start_pos[1])
                            )
                            pygame.draw.rect(canvas, current_color, rect, 0)
                        elif tool == 'circle':
                            dx = end_pos[0] - start_pos[0]
                            dy = end_pos[1] - start_pos[1]
                            radius_shape = int(math.hypot(dx, dy))
                            pygame.draw.circle(canvas, current_color, start_pos, radius_shape, 0)
                    drawing = False
                    current_pos = None
        
        screen.blit(canvas, (0, 0))
        
        if drawing and tool in ['rectangle', 'circle'] and current_pos:
            preview_color = current_color
            if tool == 'rectangle':
                x1, y1 = start_pos
                x2, y2 = current_pos
                rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))
                pygame.draw.rect(screen, preview_color, rect, 1)
            elif tool == 'circle':
                dx = current_pos[0] - start_pos[0]
                dy = current_pos[1] - start_pos[1]
                radius_preview = int(math.hypot(dx, dy))
                pygame.draw.circle(screen, preview_color, start_pos, radius_preview, 1)
        
        # инфо о инструменте и цвете
        font = pygame.font.Font(None, 24)
        color_text = font.render(f"Color: {current_color}", True, (255, 255, 255))
        tool_text = font.render(f"Tool: {tool}", True, (255, 255, 255))
        screen.blit(color_text, (10, 10))
        screen.blit(tool_text, (10, 30))
        
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()