# Пример для видео. Если одиночные картинки - вместо капчуринга использовать cv2.imread

NORM = 32 # свойство модели - размер кадра должен делиться на 32 нацело
cap = cv2.VideoCapture(full_file_path)
FPS = cap.get(cv2.CAP_PROP_FPS)
FRAME_H = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
FRAME_W = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
FRAME_SIZE = (FRAME_W // NORM * NORM, FRAME_H // NORM * NORM)

app = FaceAnalysis(name=model_name) # 'buffalo_l'
app.prepare(ctx_id=0, det_thresh=threshold, det_size=FRAME_SIZE) # threshold по-умолчанию 0,5, лучше ставить 0,75
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Преобразование изображения из BGR в RGB один раз
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    face_locations = app.get(rgb_frame)
