"""
Gerador de Imagem de Teste 1024x1024
Cria uma imagem colorida com grade e números para testar o Image Splitter
"""

from PIL import Image, ImageDraw, ImageFont
import os


def generate_test_image(filename="test_image_1024x1024.png"):
    """Gera uma imagem de teste 1024x1024 com grade colorida"""
    
    # Criar imagem 1024x1024
    img = Image.new('RGB', (1024, 1024), color='white')
    draw = ImageDraw.Draw(img)
    
    # Cores para cada quadrante
    colors = [
        ('#3b82f6', 'Parte 1\nTop-Left'),      # Azul
        ('#10b981', 'Parte 2\nTop-Right'),     # Verde
        ('#f59e0b', 'Parte 3\nBottom-Left'),   # Laranja
        ('#ef4444', 'Parte 4\nBottom-Right')   # Vermelho
    ]
    
    # Posições dos quadrantes
    positions = [
        (0, 0, 512, 512),       # Top-Left
        (512, 0, 1024, 512),    # Top-Right
        (0, 512, 512, 1024),    # Bottom-Left
        (512, 512, 1024, 1024)  # Bottom-Right
    ]
    
    try:
        # Fontes com tamanhos ajustados
        font_large = ImageFont.truetype("arial.ttf", 120) if os.name == 'nt' else ImageFont.load_default()
        font_small = ImageFont.truetype("arial.ttf", 30) if os.name == 'nt' else ImageFont.load_default()
    except:
        font_large = ImageFont.load_default()
        font_small = ImageFont.load_default()
    
    # Desenhar cada quadrante
    for i, ((x1, y1, x2, y2), (color, text)) in enumerate(zip(positions, colors), 1):
        # Fundo colorido
        draw.rectangle([x1, y1, x2, y2], fill=color)
        
        # Borda branca
        draw.rectangle([x1, y1, x2, y2], outline='white', width=5)
        
        # Centro do quadrante
        center_x = (x1 + x2) // 2
        center_y = (y1 + y2) // 2
        
        # Desenhar número (centralizado verticalmente)
        number_text = str(i)
        bbox = draw.textbbox((0, 0), number_text, font=font_large)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        draw.text(
            (center_x - text_width//2, center_y - text_height//2 - 30),
            number_text,
            fill='white',
            font=font_large
        )
        
        # Desenhar texto (centralizado abaixo do número)
        lines = text.split('\n')
        for j, line in enumerate(lines):
            bbox = draw.textbbox((0, 0), line, font=font_small)
            line_width = bbox[2] - bbox[0]
            draw.text(
                (center_x - line_width//2, center_y + text_height//2 + j*35),
                line,
                fill='white',
                font=font_small
            )
        
        # Marcador de centro
        draw.line([(center_x-15, center_y), (center_x+15, center_y)], fill='white', width=2)
        draw.line([(center_x, center_y-15), (center_x, center_y+15)], fill='white', width=2)
    
    # Linhas centrais
    draw.line([(512, 0), (512, 1024)], fill='white', width=8)
    draw.line([(0, 512), (1024, 512)], fill='white', width=8)
    
    # Título
    try:
        font_title = ImageFont.truetype("arial.ttf", 24) if os.name == 'nt' else ImageFont.load_default()
    except:
        font_title = ImageFont.load_default()
    
    title = "TEST IMAGE 1024x1024 - Image Splitter"
    bbox = draw.textbbox((0, 0), title, font=font_title)
    title_width = bbox[2] - bbox[0]
    
    draw.rectangle([0, 0, 1024, 40], fill='black')
    draw.text(
        ((1024 - title_width) // 2, 10),
        title,
        fill='white',
        font=font_title
    )
    
    # Salvar imagem
    output_path = os.path.join(os.path.dirname(__file__), filename)
    img.save(output_path)
    print(f"✓ Imagem de teste criada: {output_path}")
    print(f"  Dimensões: {img.size[0]}x{img.size[1]} pixels")
    print(f"  Formato: {img.format if img.format else 'PNG'}")
    print(f"\nAgora você pode usar esta imagem no Image Splitter!")
    
    return output_path


if __name__ == "__main__":
    print("=" * 60)
    print("  GERADOR DE IMAGEM DE TESTE - Image Splitter")
    print("=" * 60)
    print()
    
    try:
        generate_test_image()
        print("\n[SUCESSO] Imagem de teste gerada com sucesso!")
    except Exception as e:
        print(f"\n[ERRO] Falha ao gerar imagem: {str(e)}")
        import traceback
        traceback.print_exc()
    
    print()
    input("Pressione ENTER para sair...")
