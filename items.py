import os

# Путь к папке с изображениями
image_folder_path = 'G:\\relax_ox\\useful\\imgs\\redm'

# Получаем список имен файлов в папке
image_names = os.listdir(image_folder_path)

# Преобразуем список в множество, чтобы удалить дубликаты
image_names = set(image_names)

# Открываем файл для записи
with open('dis.txt', 'w') as f:
    # Генерируем код для каждого изображения
    for image_name in image_names:
        # Удаляем расширение файла из имени
        item_name = os.path.splitext(image_name)[0]
        
        # Генерируем код для элемента ox_inventory
        f.write(f"""
        ['{item_name}'] = {{
            label = '{item_name}',
            weight = 1,
            stack = true,
            close = true,
        }},
        """)

# Файл output.txt будет создан в той же папке, где находится этот скрипт.
# Если вы хотите сохранить файл в другом месте, вы можете изменить 'output.txt' на полный путь к файлу.