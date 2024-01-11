from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
import base64
import email
from email import policy
from email.parser import BytesParser


# 从本地文件中加载凭据
creds = Credentials.from_authorized_user_file('token.json')

# 创建 Gmail API 客户端
service = build('gmail', 'v1', credentials=creds)

# 列出用户的一封最新邮件
results = service.users().messages().list(userId='me', maxResults=1).execute()
messages = results.get('messages', [])

# 遍历邮件
for message in messages:
    # 获取邮件的详细信息
    msg = service.users().messages().get(userId='me', id=message['id']).execute()

    # 获取邮件头部信息
    headers = msg['payload']['headers']

    # 提取发件人、发件时间
    From, Date = "", ""
    for h in headers:
        name = h['name']
        if name.lower() == 'from':
            From = h['value']
        if name.lower() == 'date':
            Date = h['value']

    # 提取邮件正文
    if 'parts' in msg['payload']:
        part = msg['payload']['parts'][0]
        if part['mimeType'] == 'text/plain':
            data = part['body']["data"]
        else:
            data = msg['payload']['body']["data"]
    else:
        data = msg['payload']['body']["data"]
        
    data = data.replace("-","+").replace("_","/")
    decoded_data = base64.b64decode(data)
    str_text = str(decoded_data, "utf-8")
    msg_str = email.message_from_string(str_text)

    if msg_str.is_multipart():
        text = msg_str.get_payload()[0]  
    else:
        text = msg_str.get_payload()
    
    print('From: {}'.format(From[:8]))
    print('Date: {}'.format(Date))
    print('Content: {}'.format(text))

    