import cv2

# Caminho absoluto com barras invertidas duplas
caminho_img = "C:\\Users\\Luís\\Documents\\Faculdade\\image-processing-filters\\realce_ajuste_intensidade\\original.jpg"

# Carregar a imagem
img = cv2.imread(caminho_img)

# Verificação se a imagem foi carregada corretamente
if img is None:
    print("Erro ao carregar a imagem.")
    exit()

# Realce de contraste com CLAHE
img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
img_yuv[:, :, 0] = clahe.apply(img_yuv[:, :, 0])
img_clahe = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

# Salvar a imagem processada
cv2.imwrite("C:\\Users\\Luís\\Documents\\Faculdade\\image-processing-filters\\realce_ajuste_intensidade\\filtrada.jpg", img_clahe)

print("Imagem realçada salva com sucesso!")
