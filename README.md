# 🖼️ Filtros de Processamento de Imagens

Este repositório contém implementações em Python utilizando a biblioteca OpenCV, organizadas por categorias de filtros de imagem. Para cada categoria, foi utilizado **um filtro específico** aplicado sobre uma imagem de exemplo.

---

## 1. Realce e Ajuste de Intensidade
- **Filtro:** CLAHE (Contrast Limited Adaptive Histogram Equalization)
- **Descrição:** Aumenta o contraste de forma adaptativa por regiões da imagem.
- **Arquivo:** `realce_ajuste_intensidade/realce.py`

---

## 2. Redução de Ruído e Suavização
- **Filtro:** Filtro Bilateral
- **Descrição:** Suaviza a imagem mantendo as bordas nítidas.
- **Arquivo:** `reducao_ruido_suavizacao/suavizacao.py`

---

## 3. Detecção de Bordas
- **Filtro:** Detector de bordas de Canny
- **Descrição:** Detecta contornos com base em gradientes.
- **Arquivo:** `deteccao_bordas/bordas.py`

---

## 4. Detecção de Formas e Texturas
- **Filtro:** Transformada de Hough para círculos
- **Descrição:** Identifica círculos em imagens.
- **Arquivo:** `deteccao_formas_texturas/formas_texturas.py`

---

## 5. Transformações Geométricas
- **Transformações:** Redimensionamento + Rotação
- **Descrição:** A imagem foi redimensionada e rotacionada em 45°.
- **Arquivo:** `transformacoes_geometricas/transformacoes.py`

---

## 6. Filtros Morfológicos
- **Filtro:** Fechamento (Closing)
- **Descrição:** Remove buracos pequenos em objetos brancos.
- **Arquivo:** `filtros_morfologicos/morfologico.py`

---

## 🛠️ Requisitos

- Python 3.x
- OpenCV: `pip install opencv-python`

---

## 📦 Como executar

```bash
cd nome_da_pasta/
python nome_do_script.py
