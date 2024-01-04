import dotenv
dotenv.load_dotenv(verbose=True)

import pandas as pd
import numpy as np

from openai import OpenAI

df = pd.DataFrame({"x1": [1, 2], "x2": [3, 4]})

df_str = df.to_string()


def chen_ming_algorithm(data):
    """
    chen ming algorithm, return a json string
    :param data: required, xxx
    :return: json string
    """
    import io, json 
    data = io.StringIO(data)
    df_new = pd.read_csv(data, sep="\s+", index_col=0)
    res = np.sum(df_new, axis=1) - 1
    return json.dumps(res.to_string())


available_functions = {
    chen_ming_algorithm.__name__: chen_ming_algorithm,
}

print(available_functions)


chen_ming_function = {
    'name': chen_ming_algorithm.__name__,
    'description': 'chen ming algorithm, defines a way of calculating on dataset.',
    'parameters': 
        {
            'type': 'object', 
            'properties': {
                'data': {
                    'type': 'string',
                    'description': "data set"}
                }, 
            'required': ['data'],
        },
}


functions = [chen_ming_function]


client = OpenAI()

messages = [
    {"role": "system", "content": "数据集df_json: '%s'" % df_str},
    {"role": "user", "content": "帮我在数据集data上执行chenming算法"},
]
response = client.chat.completions.create(
    model = "gpt-4-0613",
    messages = messages,
    functions = functions,
    function_call = "auto",
)

print("======= first response =========")
print(response)


func_name = response.choices[0].message.function_call.name

func_ref = available_functions[func_name]

import json
func_args = json.loads(response.choices[0].message.function_call.arguments)

func_response = func_ref(**func_args)
print("======= after invoke function =========")
print(func_response)


messages.append(response.choices[0].message)

messages.append(
    {
        'role': "function",
        'name': func_name,
        'content': func_response,
    }
)

response = client.chat.completions.create(
    model = "gpt-4-0613",
    messages = messages,
)

print("======= second response =========")
print(response)
