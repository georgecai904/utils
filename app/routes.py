from flask import Blueprint, request, jsonify
from app.email_service import send_email
from app.file_service import save_html_file

bp = Blueprint('main', __name__)

@bp.route('/send-email', methods=['POST'])
def email_endpoint():
    data = request.get_json()
    
    if not data or 'to' not in data or 'subject' not in data or 'body' not in data:
        return jsonify({'error': '缺少必要参数'}), 400
        
    try:
        send_email(
            to=data['to'],
            subject=data['subject'],
            body=data['body']
        )
        return jsonify({'message': '邮件发送成功'}), 200
    except Exception as e:
        return jsonify({'error': f'发送邮件时出错: {str(e)}'}), 500 
    
    
@bp.route('/upload-html', methods=['POST'])
def upload_html():
    if not request.files:
        # 尝试直接从请求体获取数据
        try:
            html_content = request.data.decode('utf-8')
            file_url = save_html_file(html_content)
            return jsonify({'url': file_url}), 200
        except Exception as e:
            return jsonify({'error': f'处理文件时出错: {str(e)}'}), 400
    
    # 如果是通过multipart/form-data发送的文件
    file = list(request.files.values())[0]  # 获取第一个文件
    if file.filename == '':
        return jsonify({'error': '没有选择文件'}), 400
        
    if not file.filename.endswith('.html'):
        return jsonify({'error': '只支持HTML文件'}), 400
    
    try:
        html_content = file.read().decode('utf-8')
        file_url = save_html_file(html_content)
        return jsonify({'url': file_url}), 200
    except Exception as e:
        return jsonify({'error': f'处理文件时出错: {str(e)}'}), 500