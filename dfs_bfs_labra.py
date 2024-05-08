import pygame
import time

# Ikkunan asetukset:
WINDOW_SIZE = [800, 600]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Graph Traversal")

pygame.init()

# Värien määrittäminen:
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)

# Graafi:
graph = {
    '1': ['2', '3'],
    '2': ['4', '5'],
    '3': ['6', '7'],
    '4': [],
    '5': [],
    '6': ['8', '9'],
    '7': [],
    '8': [],
    '9': [],
}

# Solmujen sijaintien määrittäminen ikkunassa:
node_positions = {
    '1': (200, 100),
    '2': (100, 200),
    '3': (300, 200),
    '4': (50, 300),
    '5': (150, 300),
    '6': (250, 300),
    '7': (350, 300),
    '8': (200, 400),
    '9': (300, 400),
}

# Ikkunan keskikohdan laskeminen:
max_x = max(node_positions.values(), key=lambda x: x[0])[0]
max_y = max(node_positions.values(), key=lambda x: x[1])[1]
min_x = min(node_positions.values(), key=lambda x: x[0])[0]
min_y = min(node_positions.values(), key=lambda x: x[1])[1]

offset_x = (WINDOW_SIZE[0] - (max_x - min_x)) // 2 - min_x
offset_y = (WINDOW_SIZE[1] - (max_y - min_y)) // 2 - min_y

# Solmujen sijoittaminen keskikohtaan nähden:
node_positions = {k: (v[0] + offset_x, v[1] + offset_y) for k, v in node_positions.items()}

# Graafin piirtäminen:
def draw_graph():
    font = pygame.font.Font(None, 24)
    for node, neighbours in graph.items():
        x1, y1 = node_positions[node]
        pygame.draw.circle(screen, BLACK, (x1, y1), 20)
        text = font.render(node, True, BLACK)
        text_rect = text.get_rect(center=(x1, y1))
        screen.blit(text, text_rect)
        for neighbour in neighbours:
            x2, y2 = node_positions[neighbour]
            pygame.draw.line(screen, GRAY, (x1, y1), (x2, y2), 2)

# Syvyyshaku funktio:
def dfs(node):
    visited = set()
    stack = [node]

    while stack:
        current_node = stack.pop()
        if current_node not in visited:
            visited.add(current_node)
            draw_visited(current_node)
            pygame.display.update()
            time.sleep(0.4)
            for neighbour in graph[current_node]:
                stack.append(neighbour)

# Leveyshaku funktio:
def bfs(node):
    visited = set()
    queue = [node]

    while queue:
        current_node = queue.pop(0)
        if current_node not in visited:
            visited.add(current_node)
            draw_visited(current_node)
            pygame.display.update()
            time.sleep(0.4)
            for neighbour in graph[current_node]:
                queue.append(neighbour)

# Funktio vierailtujen solmujen värjäykseen:
def draw_visited(node):
    x, y = node_positions[node]
    pygame.draw.circle(screen, BLUE, (x, y), 20)


def main():
    running = True
    start_node = '3'

    while running:
        screen.fill(WHITE)
        draw_graph()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    dfs(start_node)
                elif event.key == pygame.K_l:
                    bfs(start_node)

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()