def draw_centered_text_in_rect(surface, text, font, color, rect, padding=10):
  words = text.split(" ")
  lines = []
  current_line = ""
  max_width = rect.width - padding * 2

  for word in words:
    test_line = f"{current_line} {word}".strip()
    if font.size(test_line)[0] <= max_width:
      current_line = test_line
    else:
      if current_line:
        lines.append(current_line)
      current_line = word
  if current_line:
    lines.append(current_line)

  line_height = font.get_linesize()
  max_lines = (rect.height - padding * 2) // line_height
  lines = lines[:max_lines]  # Оставляем только те строки, что влезут по высоте

  # Начальная координата Y для вертикального центрирования всего блока
  total_height = len(lines) * line_height
  y = rect.centery - total_height // 2

  for line in lines:
    text_surf = font.render(line, True, color)
    # Центрируем каждую строку по горизонтали
    text_rect = text_surf.get_rect(centerx=rect.centerx, top=y)
    surface.blit(text_surf, text_rect)
    y += line_height