"""
Image Splitter - Divide uma imagem 1024x1024 em 4 partes iguais
Autor: EasyCraft Tools
Data: 23/10/2025
"""

import os
from tkinter import Tk, Label, Button, filedialog, messagebox, StringVar, Frame
from tkinter.ttk import Progressbar
from PIL import Image
import threading


class ImageSplitter:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Splitter - 1024x1024 → 4 Partes")
        self.root.geometry("600x400")
        self.root.resizable(False, False)
        
        # Variáveis
        self.selected_image_path = None
        self.output_folder = None
        self.status_var = StringVar(value="Aguardando seleção de imagem...")
        
        # Interface
        self.setup_ui()
    
    def setup_ui(self):
        """Configura a interface gráfica"""
        # Frame principal
        main_frame = Frame(self.root, padx=20, pady=20)
        main_frame.pack(fill="both", expand=True)
        
        # Título
        title = Label(
            main_frame,
            text="🖼️ Image Splitter",
            font=("Arial", 18, "bold"),
            fg="#2563eb"
        )
        title.pack(pady=(0, 10))
        
        subtitle = Label(
            main_frame,
            text="Recorte imagens 1024x1024 em 4 partes iguais (512x512)",
            font=("Arial", 10),
            fg="#6b7280"
        )
        subtitle.pack(pady=(0, 20))
        
        # Botão: Selecionar Imagem
        self.btn_select_image = Button(
            main_frame,
            text="📁 Selecionar Imagem (1024x1024)",
            command=self.select_image,
            font=("Arial", 12),
            bg="#3b82f6",
            fg="white",
            activebackground="#2563eb",
            activeforeground="white",
            cursor="hand2",
            padx=20,
            pady=10
        )
        self.btn_select_image.pack(pady=10, fill="x")
        
        # Label: Imagem selecionada
        self.label_selected = Label(
            main_frame,
            text="Nenhuma imagem selecionada",
            font=("Arial", 9),
            fg="#6b7280",
            wraplength=550,
            justify="left"
        )
        self.label_selected.pack(pady=(0, 10))
        
        # Botão: Selecionar Pasta de Saída
        self.btn_select_output = Button(
            main_frame,
            text="📂 Selecionar Pasta de Saída",
            command=self.select_output_folder,
            font=("Arial", 12),
            bg="#8b5cf6",
            fg="white",
            activebackground="#7c3aed",
            activeforeground="white",
            cursor="hand2",
            padx=20,
            pady=10,
            state="disabled"
        )
        self.btn_select_output.pack(pady=10, fill="x")
        
        # Label: Pasta de saída
        self.label_output = Label(
            main_frame,
            text="Nenhuma pasta selecionada",
            font=("Arial", 9),
            fg="#6b7280",
            wraplength=550,
            justify="left"
        )
        self.label_output.pack(pady=(0, 10))
        
        # Botão: Processar
        self.btn_process = Button(
            main_frame,
            text="✂️ Recortar Imagem",
            command=self.process_image,
            font=("Arial", 14, "bold"),
            bg="#10b981",
            fg="white",
            activebackground="#059669",
            activeforeground="white",
            cursor="hand2",
            padx=20,
            pady=15,
            state="disabled"
        )
        self.btn_process.pack(pady=20, fill="x")
        
        # Barra de progresso
        self.progress = Progressbar(
            main_frame,
            mode="indeterminate",
            length=550
        )
        
        # Status
        self.label_status = Label(
            main_frame,
            textvariable=self.status_var,
            font=("Arial", 10),
            fg="#10b981"
        )
        self.label_status.pack(pady=(10, 0))
    
    def select_image(self):
        """Seleciona a imagem para processar"""
        file_path = filedialog.askopenfilename(
            title="Selecione uma imagem 1024x1024",
            filetypes=[
                ("Imagens", "*.png *.jpg *.jpeg *.bmp *.tiff *.webp"),
                ("Todos os arquivos", "*.*")
            ]
        )
        
        if not file_path:
            return
        
        # Validar dimensões
        try:
            with Image.open(file_path) as img:
                width, height = img.size
                
                if width != 1024 or height != 1024:
                    messagebox.showerror(
                        "Erro de Dimensão",
                        f"A imagem deve ter exatamente 1024x1024 pixels!\n\n"
                        f"Dimensões da imagem selecionada: {width}x{height}"
                    )
                    return
            
            self.selected_image_path = file_path
            filename = os.path.basename(file_path)
            self.label_selected.config(
                text=f"✓ Imagem selecionada: {filename}",
                fg="#10b981"
            )
            self.btn_select_output.config(state="normal")
            self.status_var.set("Imagem validada! Selecione a pasta de saída.")
            
        except Exception as e:
            messagebox.showerror(
                "Erro ao Abrir Imagem",
                f"Não foi possível abrir a imagem:\n{str(e)}"
            )
    
    def select_output_folder(self):
        """Seleciona a pasta de saída"""
        folder = filedialog.askdirectory(
            title="Selecione a pasta para salvar os recortes"
        )
        
        if not folder:
            return
        
        self.output_folder = folder
        self.label_output.config(
            text=f"✓ Pasta de saída: {folder}",
            fg="#10b981"
        )
        self.btn_process.config(state="normal")
        self.status_var.set("Pronto para processar!")
    
    def process_image(self):
        """Processa a imagem em thread separada"""
        self.btn_process.config(state="disabled")
        self.btn_select_image.config(state="disabled")
        self.btn_select_output.config(state="disabled")
        self.progress.pack(pady=10)
        self.progress.start(10)
        self.status_var.set("Processando imagem...")
        
        # Executar em thread para não travar a UI
        thread = threading.Thread(target=self._split_image)
        thread.start()
    
    def _split_image(self):
        """Divide a imagem em 4 partes iguais"""
        try:
            # Abrir imagem
            img = Image.open(self.selected_image_path)
            
            # Nome base do arquivo
            filename = os.path.splitext(os.path.basename(self.selected_image_path))[0]
            extension = os.path.splitext(self.selected_image_path)[1]
            
            # Coordenadas de recorte (512x512 cada)
            crops = [
                (0, 0, 512, 512),       # Top-Left
                (512, 0, 1024, 512),    # Top-Right
                (0, 512, 512, 1024),    # Bottom-Left
                (512, 512, 1024, 1024)  # Bottom-Right
            ]
            
            positions = ["top_left", "top_right", "bottom_left", "bottom_right"]
            
            saved_files = []
            
            # Recortar e salvar cada parte
            for i, (crop_box, position) in enumerate(zip(crops, positions), 1):
                cropped = img.crop(crop_box)
                output_filename = f"{filename}_parte_{i}_{position}{extension}"
                output_path = os.path.join(self.output_folder, output_filename)
                cropped.save(output_path)
                saved_files.append(output_filename)
            
            img.close()
            
            # Atualizar UI (thread-safe)
            self.root.after(0, self._process_complete, saved_files)
            
        except Exception as e:
            self.root.after(0, self._process_error, str(e))
    
    def _process_complete(self, saved_files):
        """Callback quando processamento é concluído"""
        self.progress.stop()
        self.progress.pack_forget()
        self.status_var.set("✓ Imagem processada com sucesso!")
        
        files_list = "\n".join([f"• {f}" for f in saved_files])
        messagebox.showinfo(
            "Sucesso!",
            f"Imagem recortada em 4 partes:\n\n{files_list}\n\n"
            f"Local: {self.output_folder}"
        )
        
        # Resetar interface
        self.reset_ui()
    
    def _process_error(self, error_msg):
        """Callback quando há erro no processamento"""
        self.progress.stop()
        self.progress.pack_forget()
        self.status_var.set("✗ Erro ao processar imagem")
        
        messagebox.showerror(
            "Erro no Processamento",
            f"Ocorreu um erro ao processar a imagem:\n\n{error_msg}"
        )
        
        # Reabilitar botões
        self.btn_process.config(state="normal")
        self.btn_select_image.config(state="normal")
        self.btn_select_output.config(state="normal")
    
    def reset_ui(self):
        """Reseta a interface para processar outra imagem"""
        self.selected_image_path = None
        self.output_folder = None
        self.label_selected.config(
            text="Nenhuma imagem selecionada",
            fg="#6b7280"
        )
        self.label_output.config(
            text="Nenhuma pasta selecionada",
            fg="#6b7280"
        )
        self.btn_select_image.config(state="normal")
        self.btn_select_output.config(state="disabled")
        self.btn_process.config(state="disabled")
        self.status_var.set("Aguardando seleção de imagem...")


def main():
    """Função principal"""
    root = Tk()
    app = ImageSplitter(root)
    root.mainloop()


if __name__ == "__main__":
    main()
