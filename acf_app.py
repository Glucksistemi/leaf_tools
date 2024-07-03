import gradio as gr
import zipfile
from pathlib import Path
from acf import transform_acf
from typing import List


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
    inputs=gr.File(file_count='multiple', label='upload one or more .acf files', file_types=['.acf', '.ACF']),
    outputs=gr.File()
)

app.launch(server_port=7860, server_name="127.0.0.1")