from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel

tokenizer = RegexTokenizer()
model = FastTextSocialNetworkModel(tokenizer=tokenizer)

message = input('Type your text here')

result = model.predict(message, k=2)
print(message, '-&gt;', result)