FROM python:alpine3.19

WORKDIR /app

#COPIO DEL DIRECTORIO DONDE ESTOY AL QUE SE CREARÁ EN EL CONTENEDOR
COPY /convers.py /app/      

CMD [ "python","/app/convers.py" ]