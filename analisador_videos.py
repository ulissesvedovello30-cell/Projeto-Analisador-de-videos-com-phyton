# IA para analisar vídeos
from groq import Groq
from yt_dlp import YoutubeDL
import whisper
import os

# Configurar FFmpeg para todos os componentes
ffmpeg_path = r"C:\ffmpeg\ffmpeg-8.0-full_build\bin"
os.environ["PATH"] = ffmpeg_path + os.pathsep + os.environ["PATH"]

# Inicializa o client da Groq
client = Groq(api_key="Coloque sua Chave Api da Groq aqui/
Enter your Groq API key here.")

# Recebendo a URL do vídeo
url = input("Digite a URL do vídeo: ")

# Configurar opções de download
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'audio.%(ext)s',  # nome do arquivo baixado
    'ffmpeg_location': r'C:\ffmpeg\ffmpeg-8.0-full_build\bin',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

# Baixar o áudio
with YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

# Transcrever com Whisper
modelo = whisper.load_model("medium")
resultado = modelo.transcribe("audio.mp3")  
transcricao = resultado["text"]  
# Dividir transcrição em chunks
palavras = transcricao.split()
chunks = []
chunk_size = 500

for i in range(0, len(palavras), chunk_size):
    chunk_texto = " ".join(palavras[i:i+chunk_size])
    chunks.append(chunk_texto)

# Enviar cada chunk para OpenAI e armazenar respostas
responses = []

for chunk_text in chunks:
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "Você é um analista de vídeos. Analise o vídeo e dê uma resposta detalhada."},
            {"role": "user", "content": chunk_text}
        ]
    )
    responses.append(response.choices[0].message.content)

# Combinar os resultados
analise_final = "\n\n".join(responses)

# Mostrar análise final
print("=== Análise final do vídeo ===")
print(analise_final)
