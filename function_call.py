import openai

df_str = '    x1    x2\n0   1    3\n1   2    4'

openai.ChatCompletion.create(
    model = "gpt-4-0613",
    messages = [
        {"role": "system", "content": "数据集df_str: '%s'" % df_str},
        {"role": "user", "content": "帮我解释一下df_str数据集"},
    ]
)