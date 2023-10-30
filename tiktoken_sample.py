import tiktoken

MODEL = 'gpt-3.5-turbo'

def get_token_len(input):
    enc = tiktoken.encoding_for_model(MODEL)
    tokens = enc.encode(input)
    return len(tokens)

if __name__ == '__main__':
    print(get_token_len('hello world'))
    print(get_token_len('こんにちわ世界'))