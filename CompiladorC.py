with open("arquivo.c", "r") as f:
    conteudo = f.read()

limpo = remove_comentarios_c(conteudo)

with open("saida.c", "w") as f:
    f.write(limpo)

def remove_comentarios_c(codigo):
    i = 0
    resultado = []
    dentro_comentario_bloco = False
    while i < len(codigo):
        if not dentro_comentario_bloco and codigo[i:i+2] == '//':
            # Comentário de linha
            while i < len(codigo) and codigo[i] != '\n':
                resultado.append(' ')
                i += 1
        elif not dentro_comentario_bloco and codigo[i:i+2] == '/*':
            # Início de comentário de bloco
            dentro_comentario_bloco = True
            resultado.append(' ')
            resultado.append(' ')
            i += 2
        elif dentro_comentario_bloco:
            if codigo[i:i+2] == '*/':
                dentro_comentario_bloco = False
                resultado.append(' ')
                resultado.append(' ')
                i += 2
            else:
                if codigo[i] == '\n':
                    resultado.append('\n')
                else:
                    resultado.append(' ')
                i += 1
        else:
            resultado.append(codigo[i])
            i += 1
    return ''.join(resultado)
