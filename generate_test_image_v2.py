"""
Gerador de Imagem de Teste 1024x1024 (Versão 2)
Cria uma imagem colorida com grade e números PERFEITAMENTE CENTRALIZADOS
"""

from PIL import Image, ImageDraw, ImageFont
import os


def generate_test_image(filename="test_image_1024x1024.png"):
    """Gera uma imagem de teste 1024x1024 com conteúdo centralizado"""
    
    # Criar imagem 1024x1024
    img = Image.new('RGB', (1024, 1024), color='white')
    draw = ImageDraw.Draw(img)
    
    # Configurações de fonte (tamanhos otimizados)
    try:
        font_large = ImageFont.truetype("arial.ttf", 140)  # Número grande
        font_small = ImageFont.truetype("arial.ttf", 32)   # Texto pequeno
        font_title = ImageFont.truetype("arial.ttf", 36)   # Título
    except:
        font_large = ImageFont.load_default()
        font_small = ImageFont.load_default()
        font_title = ImageFont.load_default()
    
    # Cores e textos para cada quadrante
    quadrants = [
        {
            "coords": (0, 0, 512, 512),
            "color": "#3b82f6",
            "number": "1",
            "text": "Top-Left"
        },
        {
            "coords": (512, 0, 1024, 512),
            "color": "#10b981",
            "number": "2",
            "text": "Top-Right"
        },
        {
            "coords": (0, 512, 512, 1024),
            "color": "#f59e0b",
            "number": "3",
            "text": "Bottom-Left"
        },
        {
            "coords": (512, 512, 1024, 1024),
            "color": "#ef4444",
            "number": "4",
            "text": "Bottom-Right"
        }
    ]
    
    # Desenhar cada quadrante
    for quad in quadrants:
        x1, y1, x2, y2 = quad["coords"]
        
        # Fundo colorido
        draw.rectangle([x1, y1, x2, y2], fill=quad["color"])
        
        # Borda branca
        draw.rectangle([x1, y1, x2, y2], outline="white", width=8)
        
        # Centro absoluto do quadrante
        center_x = x1 + (x2 - x1) // 2
        center_y = y1 + (y2 - y1) // 2
        
        # Desenhar número (centralizado verticalmente)
        bbox = draw.textbbox((0, 0), quad["number"], font=font_large)
        num_width = bbox[2] - bbox[0]
        num_height = bbox[3] - bbox[1]
        
        draw.text(
            (center_x - num_width//2, center_y - num_height//2 - 20),  # Ajuste fino
            quad["number"],
            fill="white",
            font=font_large,
            stroke_width=3,
            stroke_fill="#00000040"
        )
        
        # Desenhar texto (centralizado abaixo do número)
        bbox = draw.textbbox((0, 0), quad["text"], font=font_small)
        text_width = bbox[2] - bbox[0]
        
        draw.text(
            (center_x - text_width//2, center_y + num_height//2 + 10),
            quad["text"],
            fill="white",
            font=font_small,
            stroke_width=2,
            stroke_fill="#00000030"
        )
        
        # Marcadores de centro (cruz)
        draw.line([(center_x-15, center_y), (center_x+15, center_y)], fill="white", width=3)
        draw.line([(center_x, center_y-15), (center_x, center_y+15)], fill="white", width=3)
    
    # Linhas centrais (mais espessas)
    draw.line([(512, 0), (512, 1024)], fill="white", width=12)
    draw.line([(0, 512), (1024, 512)], fill="white", width=12)
    
    # Cabeçalho/título
    title = "TEST IMAGE 1024x1024 - CENTRALIZED CONTENT"
    bbox = draw.textbbox((0, 0), title, font=font_title)
    title_width = bbox[2] - bbox[0]
    
    draw.rectangle([0, 0, 1024, 60], fill="black")
    draw.text(
        ((1024 - title_width) // 2, 15),
        title,
        fill="white",
        font=font_title,
        stroke_width=2,
        stroke_fill="#ffffff30"
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
    print("  GERADOR DE IMAGEM DE TESTE - Conteúdo Centralizado")
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
