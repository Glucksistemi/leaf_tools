import gradio as gr
import zipfile
from pathlib import Path
from acf import transform_acf
from typing import List
import os


title = "Инструмент для конвертации ACF в XLSX"
description = """
Инструкция:
1. Загрузите один или более файлов в левую часть экрана (перетаскиванием или кликнув и далее выбрав на ПК)
2. Нажмите Submit
3. Скачайте результат из правой половины окна (при загрузке нескольких файлов, результаты будут скачиваться в виде zip-архива)
4. Для загрузки следующей порции файлов, нажмите Clear

Видео-версия инструкции [по ссылке](https://vk.com/video9302191_456239220?list=ln-JuJGnX1lICuKrrmPGz)

Исходный код: [https://github.com/Glucksistemi/leaf_tools](https://github.com/Glucksistemi/leaf_tools)
"""

def multiple_conv(acf_files: List[str]) -> str:
    result_files = []
    print(acf_files)
    for file in acf_files:
        file_path = Path(file)
        df = transform_acf(file)
        res_file = file_path.parent / (str(file_path.name)[:-4]+'_conv.xlsx')
        df.to_excel(res_file, index=False)
        result_files.append(res_file)
    if len(result_files) == 1:
        return str(result_files[0])
    elif len(result_files) == 0:
        raise Exception('no files got processed:(')
    else:
        zip_path = Path(acf_files[0]).parent / 'all_files.zip'
        with zipfile.ZipFile(zip_path, 'w') as out_zip:
            for file in result_files:
                out_zip.write(
                    file,
                    file.name
                )
        return str(zip_path)


app = gr.Interface(
    fn=multiple_conv,
    inputs=[
        gr.File(file_count='multiple', label='upload one or more .acf files', file_types=['.acf', '.ACF']),
    ],
    outputs=gr.File(),
    title=title,
    description=description
)

app.launch(server_port=7860, server_name="127.0.0.1", root_path=os.environ.get('ROOT_PATH', ''))