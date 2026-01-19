# 🖼️ Image Splitter - Divisor de Imagens 1024x1024

Aplicação Python com interface gráfica para dividir imagens 1024x1024 em 4 partes iguais de 512x512 pixels.

## 📋 Requisitos

- Python 3.7 ou superior
- Biblioteca Pillow (PIL)

## 🚀 Instalação

### 1. Instalar Python
Certifique-se de ter o Python instalado:
```bash
python --version
```

### 2. Instalar Dependências
```bash
pip install -r requirements.txt
```

Ou instalar manualmente:
```bash
pip install Pillow
```

## 💻 Como Usar

### Executar a Aplicação
```bash
python image_splitter.py
```

### Passo a Passo

1. **Selecionar Imagem**
   - Clique em "📁 Selecionar Imagem (1024x1024)"
   - Escolha uma imagem PNG, JPG, JPEG, BMP, TIFF ou WEBP
   - A imagem DEVE ter exatamente 1024x1024 pixels

2. **Selecionar Pasta de Saída**
   - Clique em "📂 Selecionar Pasta de Saída"
   - Escolha onde os 4 arquivos serão salvos

3. **Processar**
   - Clique em "✂️ Recortar Imagem"
   - Aguarde o processamento
   - 4 novos arquivos serão criados

## 📦 Saída

A aplicação gera 4 arquivos com os seguintes nomes:

```
original_nome_parte_1_top_left.png
original_nome_parte_2_top_right.png
original_nome_parte_3_bottom_left.png
original_nome_parte_4_bottom_right.png
```

### Distribuição dos Recortes

```
┌─────────┬─────────┐
│ Parte 1 │ Parte 2 │
│  Top    │  Top    │
│  Left   │  Right  │
├─────────┼─────────┤
│ Parte 3 │ Parte 4 │
│ Bottom  │ Bottom  │
│  Left   │  Right  │
└─────────┴─────────┘
```

Cada parte tem 512x512 pixels.

## 🎨 Recursos

- ✅ Interface gráfica amigável
- ✅ Validação automática de dimensões
- ✅ Suporte para múltiplos formatos (PNG, JPG, JPEG, BMP, TIFF, WEBP)
- ✅ Processamento em thread separada (não trava a interface)
- ✅ Feedback visual com barra de progresso
- ✅ Mensagens de erro detalhadas
- ✅ Nomes de arquivo descritivos

## 🛠️ Tecnologias

- **Python 3.7+**
- **Tkinter** - Interface gráfica (já incluída no Python)
- **Pillow (PIL)** - Manipulação de imagens

## 📝 Notas Técnicas

### Coordenadas de Recorte

```python
Parte 1 (Top-Left):     (0, 0, 512, 512)
Parte 2 (Top-Right):    (512, 0, 1024, 512)
Parte 3 (Bottom-Left):  (0, 512, 512, 1024)
Parte 4 (Bottom-Right): (512, 512, 1024, 1024)
```

### Formatos Suportados

- PNG (recomendado para qualidade)
- JPG/JPEG
- BMP
- TIFF
- WEBP

## ⚠️ Solução de Problemas

### "ModuleNotFoundError: No module named 'PIL'"
```bash
pip install Pillow
```

### "Erro de Dimensão"
Certifique-se de que a imagem tem exatamente 1024x1024 pixels. Você pode verificar no Windows clicando com o botão direito → Propriedades → Detalhes.

### Imagem não abre
Verifique se o arquivo não está corrompido e se é um formato suportado.

## 📄 Licença

MIT License - Livre para uso pessoal e comercial.

## 👨‍💻 Autor

EasyCraft Tools  
Data: 23/10/2025

---

**Versão**: 1.0.0  
**Status**: ✅ Produção
