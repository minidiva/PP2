import pygame
import math

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Advanced Drawing Tool")
    clock = pygame.time.Clock()
    
    # Tool variables
    radius = 15
    current_color = (0, 0, 255)  # Start with blue
    tool = 'pen'  # Tools: 'pen', 'rectangle', 'circle', 'eraser', 'square', 
                  # 'right_triangle', 'equilateral_triangle', 'rhombus'
    
    # Drawing state
    drawing = False
    start_pos = None
    current_pos = None
    
    # Canvas
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
                
                # Color selection
                if event.key == pygame.K_r:
                    current_color = (255, 0, 0)  # Red
                elif event.key == pygame.K_g:
                    current_color = (0, 255, 0)  # Green
                elif event.key == pygame.K_b:
                    current_color = (0, 0, 255)  # Blue
                elif event.key == pygame.K_y:
                    current_color = (255, 255, 0)  # Yellow
                elif event.key == pygame.K_c:
                    current_color = (0, 255, 255)  # Cyan
                elif event.key == pygame.K_m:
                    current_color = (255, 0, 255)  # Magenta
                elif event.key == pygame.K_w:
                    current_color = (255, 255, 255)  # White
                elif event.key == pygame.K_k:
                    current_color = (0, 0, 0)  # Black
                
                # Tool selection
                # UPD: Added new shape tools with keys 5-8
                if event.key == pygame.K_1:
                    tool = 'pen'
                elif event.key == pygame.K_2:
                    tool = 'rectangle'
                elif event.key == pygame.K_3:
                    tool = 'circle'
                elif event.key == pygame.K_4:
                    tool = 'eraser'
                elif event.key == pygame.K_5:  # UPD: Square tool
                    tool = 'square'
                elif event.key == pygame.K_6:  # UPD: Right triangle tool
                    tool = 'right_triangle'
                elif event.key == pygame.K_7:  # UPD: Equilateral triangle tool
                    tool = 'equilateral_triangle'
                elif event.key == pygame.K_8:  # UPD: Rhombus tool
                    tool = 'rhombus'
            
            # Mouse controls
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    if tool in ['pen', 'eraser']:
                        drawing = True
                    # UPD: Added new tools to the drawing trigger
                    elif tool in ['rectangle', 'circle', 'square', 'right_triangle', 
                                'equilateral_triangle', 'rhombus']:
                        start_pos = event.pos
                        drawing = True
                elif event.button == 3:  # Right click
                    if tool in ['pen', 'eraser']:
                        radius = max(1, radius - 1)  # Decrease radius
                
            if event.type == pygame.KEYDOWN:    
                if event.key == pygame.K_UP:
                    radius += 3
                    print(radius)
                if event.key == pygame.K_DOWN:
                    radius -= 3
                    print(radius)
            
            if event.type == pygame.MOUSEMOTION:
                if drawing and tool in ['pen', 'eraser']:
                    color = current_color if tool == 'pen' else (0, 0, 0)
                    pos = event.pos
                    pygame.draw.circle(canvas, color, pos, radius)
                # UPD: Added motion tracking for new tools
                elif drawing and tool in ['rectangle', 'circle', 'square', 'right_triangle', 
                                        'equilateral_triangle', 'rhombus']:
                    current_pos = event.pos
            
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and drawing:
                    end_pos = event.pos
                    if tool == 'rectangle':
                        # Draw rectangle
                        rect = pygame.Rect(
                            min(start_pos[0], end_pos[0]),
                            min(start_pos[1], end_pos[1]),
                            abs(end_pos[0] - start_pos[0]),
                            abs(end_pos[1] - start_pos[1])
                        )
                        pygame.draw.rect(canvas, current_color, rect, 0)
                    elif tool == 'circle':
                        # Draw circle
                        dx = end_pos[0] - start_pos[0]
                        dy = end_pos[1] - start_pos[1]
                        radius_shape = int(math.hypot(dx, dy))
                        pygame.draw.circle(canvas, current_color, start_pos, radius_shape, 0)
                    # UPD: Square tool implementation
                    elif tool == 'square':
                        # Draw square (equal width and height)
                        size = max(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
                        rect = pygame.Rect(
                            start_pos[0] if end_pos[0] > start_pos[0] else start_pos[0] - size,
                            start_pos[1] if end_pos[1] > start_pos[1] else start_pos[1] - size,
                            size, size
                        )
                        pygame.draw.rect(canvas, current_color, rect, 0)
                    # UPD: Right triangle tool implementation
                    elif tool == 'right_triangle':
                        # Draw right triangle (90° angle at start_pos)
                        points = [
                            start_pos,
                            (start_pos[0], end_pos[1]),
                            end_pos
                        ]
                        pygame.draw.polygon(canvas, current_color, points)
                    # UPD: Equilateral triangle tool implementation
                    elif tool == 'equilateral_triangle':
                        # Draw equilateral triangle
                        width = end_pos[0] - start_pos[0]
                        height = int(abs(width) * math.sqrt(3) / 2)
                        if width < 0:
                            height = -height
                        
                        points = [
                            start_pos,
                            (start_pos[0] + width, start_pos[1]),
                            (start_pos[0] + width//2, start_pos[1] - height)
                        ]
                        pygame.draw.polygon(canvas, current_color, points)
                    # UPD: Rhombus tool implementation
                    elif tool == 'rhombus':
                        # Draw rhombus (diamond shape)
                        center_x = (start_pos[0] + end_pos[0]) // 2
                        center_y = (start_pos[1] + end_pos[1]) // 2
                        width = abs(end_pos[0] - start_pos[0]) // 2
                        height = abs(end_pos[1] - start_pos[1]) // 2
                        
                        points = [
                            (center_x, center_y - height),  # Top
                            (center_x + width, center_y),   # Right
                            (center_x, center_y + height),  # Bottom
                            (center_x - width, center_y)    # Left
                        ]
                        pygame.draw.polygon(canvas, current_color, points)
                    
                    drawing = False
                    current_pos = None
        
        # Draw the canvas
        screen.blit(canvas, (0, 0))
        
        # Draw preview for shape tools
        if drawing and tool in ['rectangle', 'circle', 'square', 'right_triangle', 
                              'equilateral_triangle', 'rhombus'] and current_pos:
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
            # UPD: Square preview implementation
            elif tool == 'square':
                size = max(abs(current_pos[0] - start_pos[0]), abs(current_pos[1] - start_pos[1]))
                rect = pygame.Rect(
                    start_pos[0] if current_pos[0] > start_pos[0] else start_pos[0] - size,
                    start_pos[1] if current_pos[1] > start_pos[1] else start_pos[1] - size,
                    size, size
                )
                pygame.draw.rect(screen, preview_color, rect, 1)
            # UPD: Right triangle preview implementation
            elif tool == 'right_triangle':
                points = [
                    start_pos,
                    (start_pos[0], current_pos[1]),
                    current_pos
                ]
                pygame.draw.polygon(screen, preview_color, points, 1)
            # UPD: Equilateral triangle preview implementation
            elif tool == 'equilateral_triangle':
                width = current_pos[0] - start_pos[0]
                height = int(abs(width) * math.sqrt(3) / 2)
                if width < 0:
                    height = -height
                
                points = [
                    start_pos,
                    (start_pos[0] + width, start_pos[1]),
                    (start_pos[0] + width//2, start_pos[1] - height)
                ]
                pygame.draw.polygon(screen, preview_color, points, 1)
            # UPD: Rhombus preview implementation
            elif tool == 'rhombus':
                center_x = (start_pos[0] + current_pos[0]) // 2
                center_y = (start_pos[1] + current_pos[1]) // 2
                width = abs(current_pos[0] - start_pos[0]) // 2
                height = abs(current_pos[1] - start_pos[1]) // 2
                
                points = [
                    (center_x, center_y - height),
                    (center_x + width, center_y),
                    (center_x, center_y + height),
                    (center_x - width, center_y)
                ]
                pygame.draw.polygon(screen, preview_color, points, 1)
        
        # Display tool info and controls
        font = pygame.font.Font(None, 24)
        color_text = font.render(f"Color: {current_color}", True, (255, 255, 255))
        tool_text = font.render(f"Tool: {tool}", True, (255, 255, 255))
        # UPD: Extended controls text to include new tools
        controls_text = font.render("1:Pen 2:Rect 3:Circle 4:Eraser 5:Square 6:R Triangle 7:Eq Triangle 8:Rhombus", 
                                  True, (255, 255, 255))
        screen.blit(color_text, (10, 10))
        screen.blit(tool_text, (10, 30))
        screen.blit(controls_text, (10, 50))
        
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()