import os
from datetime import datetime
from flask import current_app
from werkzeug.utils import secure_filename

def save_html_file(html_content):
    """
    保存HTML文件并返回访问路径
    
    参数:
        html_content (str): HTML文件内容
        
    返回:
        str: 文件的完整访问URL
    """
    try:
        # 确保static文件夹存在
        if not hasattr(current_app, 'static_folder') or not current_app.static_folder:
            current_app.static_folder = os.path.join(current_app.root_path, 'static')
        
        # 创建存储目录
        upload_folder = os.path.join(current_app.static_folder, 'uploads', 'html')
        os.makedirs(upload_folder, exist_ok=True)
        
        # 生成文件名（使用时间戳确保唯一性）
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'document_{timestamp}.html'
        filename = secure_filename(filename)
        
        # 完整的文件保存路径
        file_path = os.path.join(upload_folder, filename)
        
        # 写入文件
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        # 构建完整的URL
        relative_path = f'/uploads/html/{filename}'
        full_url = f"{current_app.config['BASE_URL']}{current_app.config['STATIC_URL_PATH']}{relative_path}"
        
        return full_url
    
    except Exception as e:
        raise Exception(f"保存HTML文件失败: {str(e)}")