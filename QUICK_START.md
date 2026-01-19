# 🚀 Quick Start - Image Splitter

## Início Rápido (3 passos)

### 1️⃣ Instalar Dependências
```bash
pip install Pillow
```

### 2️⃣ Executar Aplicação

**Opção A - Duplo Clique (Windows)**
```
Clique duas vezes em: run.bat
```

**Opção B - Linha de Comando**
```bash
python image_splitter.py
```

### 3️⃣ Usar a Interface

1. Clique em **"📁 Selecionar Imagem (1024x1024)"**
2. Clique em **"📂 Selecionar Pasta de Saída"**
3. Clique em **"✂️ Recortar Imagem"**
4. ✅ Pronto! 4 arquivos criados!

---

## 🧪 Gerar Imagem de Teste

Se você não tem uma imagem 1024x1024 para testar:

```bash
python generate_test_image.py
```

Isso vai criar `test_image_1024x1024.png` com uma grade colorida.

---

## 📦 Resultado

Entrada:
```
minha_foto.png (1024x1024)
```

Saída:
```
minha_foto_parte_1_top_left.png (512x512)
minha_foto_parte_2_top_right.png (512x512)
minha_foto_parte_3_bottom_left.png (512x512)
minha_foto_parte_4_bottom_right.png (512x512)
```

---

## ❓ Problemas Comuns

### Erro: "Python não encontrado"
- Instale Python 3.7+ de [python.org](https://www.python.org/downloads/)
- Marque a opção "Add Python to PATH" durante instalação

### Erro: "ModuleNotFoundError: No module named 'PIL'"
```bash
pip install Pillow
```

### Erro: "Dimensão incorreta"
- A imagem DEVE ter exatamente 1024x1024 pixels
- Verifique as dimensões: Clique direito → Propriedades → Detalhes

---

## 📞 Suporte

Dúvidas? Verifique o `README.md` para documentação completa.

---

**Versão**: 1.0.0  
**Atualizado**: 23/10/2025
