# 📚 Exemplos de Uso - Image Splitter

## Casos de Uso Práticos

### 1. 🎮 Tiles para Jogos
**Cenário**: Dividir tilesets grandes em tiles menores para engines de jogos.

**Input**: `tileset_terrain.png` (1024x1024)  
**Output**: 4 tiles de 512x512 para usar em mapas

**Benefício**: Facilita organização de assets e carregamento otimizado.

---

### 2. 🎨 Processamento de Imagens IA
**Cenário**: Dividir imagens grandes para processamento em lotes por modelos de IA.

**Input**: `landscape_photo.jpg` (1024x1024)  
**Output**: 4 partes para processar individualmente

**Benefício**: Reduz uso de memória e permite processamento paralelo.

---

### 3. 📱 Otimização Web/Mobile
**Cenário**: Dividir imagens grandes para carregamento progressivo (lazy loading).

**Input**: `hero_banner.png` (1024x1024)  
**Output**: 4 partes para carregar sob demanda

**Benefício**: Melhora performance e tempo de carregamento inicial.

---

### 4. 🖼️ Criação de Mosaicos
**Cenário**: Criar mosaicos de fotos para impressão ou displays.

**Input**: `artwork.png` (1024x1024)  
**Output**: 4 partes para impressão em diferentes materiais

**Benefício**: Facilita impressão em tamanhos variados.

---

### 5. 🎯 Testes de Qualidade
**Cenário**: Analisar diferentes regiões de uma imagem separadamente.

**Input**: `medical_scan.png` (1024x1024)  
**Output**: 4 regiões para análise individual

**Benefício**: Foco em áreas específicas sem processar imagem inteira.

---

## Exemplos de Linha de Comando

### Gerar Imagem de Teste
```bash
python generate_test_image.py
```
**Resultado**: `test_image_1024x1024.png`

### Executar Splitter
```bash
python image_splitter.py
```

### Instalar em Ambiente Virtual
```bash
# Criar ambiente virtual
python -m venv venv

# Ativar (Windows)
venv\Scripts\activate

# Ativar (Linux/Mac)
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Executar
python image_splitter.py
```

---

## Fluxo de Trabalho Típico

### Preparação
```
1. Ter imagem 1024x1024 pronta
2. Criar pasta de saída (ex: "output/")
3. Executar aplicação
```

### Processamento
```
1. Selecionar imagem origem
2. Selecionar pasta destino
3. Clicar em "Recortar Imagem"
4. Aguardar processamento (2-5 segundos)
```

### Resultado
```
output/
├── minha_imagem_parte_1_top_left.png
├── minha_imagem_parte_2_top_right.png
├── minha_imagem_parte_3_bottom_left.png
└── minha_imagem_parte_4_bottom_right.png
```

---

## Estrutura de Nomes de Arquivo

### Padrão
```
[nome_original]_parte_[numero]_[posicao].[extensao]
```

### Exemplos
```
✓ landscape_parte_1_top_left.png
✓ avatar_parte_2_top_right.jpg
✓ texture_parte_3_bottom_left.png
✓ banner_parte_4_bottom_right.webp
```

---

## Mapeamento de Coordenadas

### Imagem Original (1024x1024)
```
        0           512         1024
    0   ┌─────────┬─────────┐
        │         │         │
        │ Parte 1 │ Parte 2 │
        │ (0,0)   │ (512,0) │
  512   ├─────────┼─────────┤
        │         │         │
        │ Parte 3 │ Parte 4 │
        │ (0,512) │(512,512)│
 1024   └─────────┴─────────┘
```

### Coordenadas de Recorte
```python
Parte 1: (0,   0,   512, 512)  # Top-Left
Parte 2: (512, 0,   1024, 512) # Top-Right
Parte 3: (0,   512, 512, 1024) # Bottom-Left
Parte 4: (512, 512, 1024, 1024) # Bottom-Right
```

---

## Dicas e Boas Práticas

### ✅ Fazer
- Usar imagens exatamente 1024x1024
- Organizar saída em pastas separadas
- Manter backup da imagem original
- Usar formatos sem perda (PNG) para qualidade
- Testar com `generate_test_image.py` primeiro

### ❌ Evitar
- Imagens com dimensões diferentes de 1024x1024
- Sobrescrever arquivos originais
- Usar JPG para imagens com texto (perda de qualidade)
- Processar muitas imagens sem organização

---

## Resolução de Problemas

### Problema: "Imagem muito pequena/grande"
**Solução**: Redimensione para 1024x1024 antes usando:
- Photoshop
- GIMP
- Paint.NET
- Online: squoosh.app

### Problema: "Qualidade ruim após recorte"
**Solução**: Use PNG ao invés de JPG para preservar qualidade

### Problema: "Nomes de arquivo muito longos"
**Solução**: Renomeie arquivo original para nome mais curto

---

## Automação (Avançado)

### Processar Várias Imagens (Batch)
```python
# batch_process.py
import os
from PIL import Image

def batch_split(input_folder, output_folder):
    for filename in os.listdir(input_folder):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            filepath = os.path.join(input_folder, filename)
            img = Image.open(filepath)
            
            if img.size == (1024, 1024):
                # Processar imagem
                # (implementar lógica de split aqui)
                pass

# batch_split('input/', 'output/')
```

---

## Performance

### Tempo de Processamento Típico
- Imagem PNG: ~1-2 segundos
- Imagem JPG: ~0.5-1 segundo
- Depende de: CPU, disco, formato

### Uso de Memória
- ~8-16 MB por imagem 1024x1024
- Thread separada previne travamento da UI

---

**Última Atualização**: 23/10/2025  
**Versão**: 1.0.0
